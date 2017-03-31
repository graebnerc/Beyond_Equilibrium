from __future__ import print_function
import numpy
import random
import scipy.stats
"""
This is the source code for the paper entitled
"Beyond Equilibrium: Revisiting Two-Sided Markets from an Agent-Based Modeling Perspective"
published in the International Journal of Computational Economics and Econometrics.
Authors: Torsten Heinrich and Claudius Graebner
Emails: torsten.heinrich@maths.ox.ac.uk and claudius@claudius-graebner.com

We suggest to call the file using the associated callscript via a terminal using the following command (requires a 
shellscript environment such as bash):
./callscript_all.sh

If you wish to start a single run, the script should be used in the following way:
1. call "python src-tsm.py [filename=<output file name>] [strategy=<RIL/RILS/RO>] [providernum=<number of providers>] \
                           [fixedentryfee=<entryfee>] [pcc=<per customer fixed costs>] [runid=<run id>]"

The model defines 3 types of agents
1. sellers
2. buyers (sellers and buyers, also collectively called customers, represent the two sides of the 'market')
3. providers - those who controll the customers' access to the tsm ... the real actors in this model

This model consists of:
1. simple decision mechanism for customers (the only real agency is to subscribe and unsubscribe to providers)
2. strategic decision making for providers, driven by reinforcement learning
3. simple exchange mechanism

It is recommended to run the model with the associated bash script. Otherwise, the files can be called directly.
It requires a directory "data" to store the results.
Then you may call the file figures.py that generates the figures of the paper in a directory figures/.

This script is organized as follows:
1. Definition of the control variables.
2. Defintion of the recording variables that are used to store the results of the simulation.
3. The actual ABM.
The different parts are preceeded by a heading as block comment.
"""

"""
Control variables
"""

output_filename = 'results'    # Default name for time series and figures
provider_strategy = 'RO'       # Default strategy (may be 'RO', 'RIL', or 'RILS')
graphical_output = False       # Do not create figures by default
t_max = 500			    # number of iterations
no_providers = 1		# number of access providers to the tsm service
no_sellers = 2000		# number of the first tsm side ('sellers')
no_buyers = 10000		# number of the second tsm side ('buyers')
no_transactions_per_iteration = 30000		# maximum number of transactions per iteration
operatingcost = 10000		        # cost of tsm service for provider per period
provider_fixed_cost_ps = 25        # cost occurring to the provider per seller
provider_fixed_cost_pb = 25        # cost occurring to the provider per buyer
provider_transaction_cost_b = 50    # cost occurring to the provider per transaction through the buyer
provider_transaction_cost_s = 50    # cost occurring to the provider per transaction through the seller
max_providers = 5			# maximum number of providers a customer may have subscribed at any given time
threshold_level = 400		# monetary threshold of customer revenue below which she will not try to subscribe networks of further providers (given she already has one)
price_average = 1000		# average price for transactions between buyers (who have a uniform-distributed reservation price above) and sellers (who have a uniform-distributed reservation price below)
init_buyer_subscription_fee = 0   # initial subscription fee for buyers to providers
init_trans_cost_b = 0.0     # initial per transaction cost for the buyers
init_seller_subscription_fee = 0  # initial subscription fee for sellers to providers
init_trans_cost_s = 0.0     # initial per transaction cost for the sellers
init_roaming_cost = 100		# initial 'roaming' access cost for transactions with customers of other providers

# boundary variables
min_cost = 100			    # minimum boundary 'roaming' access cost
max_cost = 100			    # maximum boundary 'roaming' access cost
min_entryfee_s = -3000      # minimum boundary seller entrance fee
max_entryfee_s = 5000       # maximum boundary seller entrance fee
min_entryfee_b = -3000      # minimum boundary buyer entrance fee
max_entryfee_b = 5000       # maximum boundary buyer entrance fee
min_trans_cost_s = -1000    # min transaction cost for seller
max_trans_cost_s = 1010	    # max transaction cost for seller
min_trans_cost_b = -1000    # min transaction cost for buyer
max_trans_cost_b = 1010	    # max transaction cost for buyer
ema_factor = 0.01           # exponential moving average factor
past_discounting_root_expon = 0.99  # exponent for root function for discounting old reinforcement learning imbalances

# auxiliary global variables
provider_id = 0     # provider id counter
seller_id = 0       # 'seller' id counter
buyer_id = 0        # 'buyer' id counter
transaction_counter = 0     # counter variable for transactions in period
t = -1                      # time
figure = -1                 # figure objects

# object list variables
providerlist = []   # global list of provider objects
customerlist = []   # global list of customer objects
sellerlist = []     # global list of seller objects
buyerlist = []      # global list of buyer objects

# global network externality provider choice functions
s_providerweights = []  # global seller network externality function (weights for providers according to sellers' preferences, used in sellers' provider choices), has weight entries for all providers, thus the same length as providerlist
b_providerweights = []  # global buyer network externality function (weights for providers according to buyers' preferences, used in buyers' provider choices), has weight entries for all providers, thus the same length as providerlist


"""
Recording variables.
They are used to store the results of the simulations.
"""

rec_t = []				# time from 0 through t_max-1 (required for drawing)
rec_transactions = []   # number of transactions per period
rec_prov_min = []       # providers' minimum period revenue
rec_prov_max = []       # providers' maximum period revenue
rec_prov_av = []        # providers' average period revenue
rec_cn_max = []			# providers' maximum number of customers (by period)
rec_cn_min = []			# providers' minimum number of customers (by period)
rec_cn_av = []			# providers' average number of customers (by period)
rec_efb_min = []		# minimum buyer subscription fee
rec_efb_max = []		# maximum buyer subscription fee
rec_efb_av = []			# average buyer subscription fee (average weighted by number of customers)
rec_efs_min = []		# minimum seller subscription fee
rec_efs_max = []		# maximum seller subscription fee
rec_efs_av = []			# average seller subscription fee (average weighted by number of customers)
rec_tfb_min = []        # minimum transaction fee charged from the buyers
rec_tfb_max = []        # maximum transaction fee charged from the buyers
rec_tfb_av = []         # average transaction fee charged from the buyers
rec_tfs_min = []        # minimum transaction fee charged from the sellers
rec_tfs_max = []        # maximum transaction fee charged from the sellers
rec_tfs_av = []         # average transaction fee charged from the sellers
rec_cost_min = []		# minimum 'roaming' access cost for customers of other providers
rec_cost_max = []		# maximum 'roaming' access cost for customers of other providers
rec_cost_av = []		# average 'roaming' access cost for customers of other providers
rec_customer_min = []   # customers' minimum period 'revenue'
rec_customer_max = []   # customers' maximum period 'revenue'
rec_customer_av = []    # customers' average period 'revenue'
rec_seller_min = []		# sellers' minimum period 'revenue'
rec_seller_max = []		# sellers' maximum period 'revenue'
rec_seller_av = []		# sellers' average period 'revenue'
rec_buyer_min = []		# buyers' minimum period 'revenue'
rec_buyer_max = []		# buyers' maximum period 'revenue'
rec_buyer_av = []		# buyers' average period 'revenue'


"""
The agent based model

1st part (lines  149 -  916): Class definitions.
2nd part (lines  922 - 1486): Definition of auxiliary functions.
3rd part (lines 1493 - 1645): Defintion of the main function, i.e. what is called if the model is run.
4th part (lines 1669 - 1744): The conditional block for the __main__ environment, executed if the script gets called externally.
"""


class Customer:
    """
    This is the basic customer class.
    Buyer and seller classes inherit from this class.

    When a customer gets instantiated it gets recorded into the global list of customers.
    It is instantiated with zero initial money.
    It has a subscripion list that contains the providers the customer has currently subscribed to.
    It also stores the revenue generated by the subscription to a provider in the previous rourd (prevenue).
    Initially, a customer is subscriped to a random provider.
    """

    def __init__(self):
        customerlist.append(self)
        self.buyer = True
        self.money = 0
        self.providers = []
        self.prevenue = []
        newprovider = random.choice(providerlist)
        self.providers.append(newprovider)
        self.prevenue.append(0)
        newprovider.customer_no += 1


class Seller(Customer):
    """
    The seller class inherits from the customer class.
    It gets assigned a unique seller id.
    The reservation price of the seller is chose randomly each round.
    The mean of the distribution is set as a global parameter.
    After complete instantiation, the agent is recorded in the global sellerlist.

    """

    def __init__(self):
        Customer.__init__(self)
        global seller_id
        self.id = seller_id
        seller_id += 1
        self.buyer = False
        self.providers[0].seller_no += 1
        self.reservation_price = random.uniform(price_average * 0.5, price_average)
        sellerlist.append(self)

    def update_reservation_price(self):
        self.reservation_price = random.uniform(price_average * 0.5, price_average)


class Buyer(Customer):
    """
    The buyer class. It inherits from the customer class.
    It is almost identical to the sellerclass, only the distribution of reservation prices is different.
    """

    def __init__(self):
        Customer.__init__(self)
        global buyer_id
        self.id = buyer_id
        buyer_id += 1
        self.providers[0].buyer_no += 1
        self.reservation_price = random.uniform(price_average, price_average * 1.5)
        buyerlist.append(self)

    def update_reservation_price(self):
        self.reservation_price = random.uniform(price_average, price_average * 1.5)


class Provider:
    """
    Provider (tsm service provider) class.
    It consists of
    1. An initialization function
    2. Two iteration functions that are called every round.
       Other dependencies (interaction with the evaluate function) require that the provider's actions are 
       separated into two functions.
    """

    def __init__(self):
        """
        After being instantiated, the provider gets assigned an id and recorded into the global providerlist.

        Then, initial values for the strategy parameters (entryfee and transaction fee) are set.

        The status variables of the provider are the following:
            1. Current revenue
            2. Revenue in the previous period (lastrevenue)
            3. Current number of customers
            4. Number of customers in the previous period (lastcustomers_no)
            5. The number of buyer and sellers among current customers
        They are needed for the provider decision making.

        Finally, the provider gets assigned a decision algorithm.
            SoReinforcement learning:
            SoReinforcemtn learningS
            SoRationalChoice
        Only one of the strategies can be chosen for a single provider. The others must be commented out.
        Note that reinforcement learning requires a call
        of the strategy object before the first iteration (happens as default).
        """
        providerlist.append(self)
        global provider_id
        self.id = provider_id
        provider_id += 1

        self.entryfee_b = init_buyer_subscription_fee
        self.entryfee_s = init_seller_subscription_fee
        self.roaming_cost = init_roaming_cost  # Note that roaming costs are not used in this version of the model.
        self.trans_cost_b = init_trans_cost_b
        self.trans_cost_s = init_trans_cost_s
        
        self.revenue = 0
        self.lastrevenue = -1
        self.customer_no = 0
        self.lastcustomer_no = 0
        self.buyer_no = 0
        self.seller_no = 0
        
        if provider_strategy == 'RIL':
            self.so_function = SoReinforcementLearning()
        elif provider_strategy == 'RILS':
            self.so_function = SoReinforcementLearningS(1000000, 2000)
        elif provider_strategy == 'RO':
            self.so_function = SoRationalChoice(provider_transaction_cost_b, provider_transaction_cost_s,
                                            provider_fixed_cost_pb, provider_fixed_cost_ps)
        self.strategy = []
        self.so_function(self, self.roaming_cost, self.entryfee_s, self.entryfee_b,
                         self.trans_cost_b, self.trans_cost_s, self.revenue, self.lastrevenue,
                         self.customer_no, self.lastcustomer_no, True)

    def iterate1(self):
        """
        This function, called every round, contains the first stage of iterating the provider.
        It applies fixed costs and per-customer costs to the provider's revenue count.
        It must be called before the evaluate function, which must be called before the iterate2 method.
        """

        self.revenue -= operatingcost
        self.revenue -= self.buyer_no * provider_fixed_cost_pb
        self.revenue -= self.seller_no * provider_fixed_cost_ps
        
    def iterate2(self):
        """
        This function, called every round, contains the second stage of iterating the provider
        It sets entryfees  and transactions fees for buyers and sellers according
        to the decision making algorithm used by the provider.

        After this has been done, the status variables of the provider are updated.
        """
        self.roaming_cost, self.entryfee_b, self.entryfee_s, self.trans_cost_b, self.trans_cost_s = self.so_function(
            self, self.roaming_cost, self.entryfee_s, self.entryfee_b, self.trans_cost_b, self.trans_cost_s,
            self.revenue, self.lastrevenue, self.customer_no, self.lastcustomer_no, False)

        self.lastrevenue = self.revenue
        self.lastcustomer_no = self.customer_no
        self.lastbuyer_no = self.buyer_no
        self.lastseller_no = self.seller_no
        self.revenue = 0


class StrategyObject():
    """
    The parent class for strategy objects.
    It works through the proper strategy object function (so_function) that is particular to each strategy class.
    """

    def __init__(self, so_function):
        self.__so_function = so_function

    def __call__(self, **s_args):
        return self.__so_function(**s_args)


class SoReinforcementLearning(StrategyObject):
    """
    Strategy object for reinforcement learning. Usually it tries to maximize the profit of the provider.
    It may also consider the number of customers (change line 331 fro that), but this had been found to have
    no effect on the results.
    """

    def __init__(self):
        self.include_customer_no = False

    def __call__(self, prov, prov_roaming_cost, prov_efs, prov_efb, prov_tcb, prov_tcs, prov_rev, prov_lrev, prov_cno,
                 prov_lcno, firsttime):
        """
        :param prov:            The provider associated with the call
        :param prov_roaming_cost:    The roaming costs charged by the provider (not used in the current version))
        :param prov_efs:        Current entry fee for the sellers
        :param prov_efb:        Current entry fee for the buyers
        :param prov_rev:        Current revenue of the provider
        :param prov_lrev:       Revenue of the provider in the previous round
        :param prov_cno:        Number of current customers
        :param prov_lcno:       Number of customers in the previous round
        :param firsttime:       Should be True if the object gets called the first time.
        :return: tuple (provider cost, entry cost for seller, entry cost for buyer)

        The procedure is as follows:
            0. In the very first round, the strategy weights are initialized.
            1. Check whether provider can match her operating cost
            2. Calculate revenue of the previous round
            3. Choose a new strategy
            4. Apply the strategy

        ad. 0:
        The provider gets a list of strategies. A strategy consists of 5 pointers: one for each quantity to be set.
        These are the roaming costs and the entry and transaction fees, for buyers and sellers respectively.
        For each of the quantities the buyer either decrease,  keep, or increase the current value. This gets
        encoded with integers 0, 1, and 2 respectively.
        For each of the strategies, there is a probibility weight that gets adjusted during the learning process.
        The probability weights for each strategy are instantiated as one, and will be normalized each round.

        ad 1:
        If the provider is not able to match her operating costs with the current strategy profile, the strategies
        for all five dimensions are strongly discouraged (i.e. their probability weight gets divided by 10),
        and all negative fees and costs get reset to zero.

        ad 2:
        From the second period on, the provider uses a relative success measure to compare his current revenues
        to past revenues (in case the provider also considers the customer number for his success, the two
        measures are related multiplicatively).
        The learning is then applied proportionally to the relative success measure by multiplying the strategy values
        with the relative success measure (which is between 0 and +infty, good if >1, bad if <1).
        A root function ensures that the impact of older successes are weights off and newer successes are valued more
        strongly.
        In the end, the strategy weights are renormalized.

        ad 3:
        The new strategy is chosen from the distribution of probability weights.

        ad 4:
        The new strategy gets applied and new entry and transaction fees are set. A geometric moving average function
        ensures slow adjustment.
        """

        # Step 0: Initialization
        if firsttime:
            prov.strategy.append([])
            for i in range(5):
                prov.strategy[0].append(random.randint(0, 2))
            prov.strategy.append([])
            for i in range(5):
                prov.strategy[1].append(numpy.ones(3))
            return

        debug = False
        if debug:
            print(prov.id, ' SO-RIL: current/last revenue ', prov_rev,prov_lrev)
            if prov.id == 0:
                print('  ', prov.id, ' current/last user no ', prov_cno,prov_lcno)
                print('  ', prov.id, ' strategy ', prov.strategy)
                print('  ', prov.id, ' rc efb efs tcb tcs ', prov_roaming_cost, prov_efs, prov_efb, prov_tcb, prov_tcs)

        # Step 1: Disourage strategies if provider cannot match operating costs.
        if prov.revenue < 0:
            prov.strategy[1][0][prov.strategy[0][0]] /= 10.
            prov.strategy[1][1][prov.strategy[0][1]] /= 10.
            prov.strategy[1][2][prov.strategy[0][2]] /= 10.
            prov.strategy[1][3][prov.strategy[0][3]] /= 10.
            prov.strategy[1][4][prov.strategy[0][4]] /= 10.
            prov_roaming_cost = 100 if prov_roaming_cost < 100 else prov_roaming_cost
            prov_efs = 100 if prov_efs < 100 else prov_efs
            prov_efb = 100 if prov_efb < 100 else prov_efb
            prov_tcs = 100 if prov_tcs < 100 else prov_tcs
            prov_tcb = 100 if prov_tcb < 100 else prov_tcb
            return prov_roaming_cost, prov_efb, prov_efs, prov_tcb, prov_tcs

        # Step 2: obtain a relative success measure:

        if prov_lrev <= 0:  # In the first found, the relative success measure is set to unity
            relative_success = 1.0
        else:
            relative_success = prov_rev * 1. / prov_lrev

        if self.include_customer_no:
            relative_success *= (prov_cno+1)/(prov_lcno+1)  # Addition of one to avoid division by zero
        for dim in range(5):                                # slowly level out old imbalances
            for i in range(len(prov.strategy[1][dim])):     # for all 5 dimensions and all components of all dimensions
                prov.strategy[1][dim][i] **= past_discounting_root_expon	 # apply a slight root function

        for dim in range(5):
            prov.strategy[1][dim][prov.strategy[0][dim]] *= relative_success

        for dim in range(5):  # re-normalize strategy weight vectors before choosing a new strategy.
            sumweight = sum(prov.strategy[1][dim])
            for i in range(len(prov.strategy[1][dim])):
                prov.strategy[1][dim][i] /= sumweight

        # Step 3. Choose a new strategy
        for dim in range(5):            # for all 5 dimensions
            s = random.uniform(0, 1)    # draw from Uniform(0,1), assign appropriate strategy from strategy vector
            prov.strategy[0][dim] = -1
            while s > 0:
                prov.strategy[0][dim] += 1
                s -= prov.strategy[1][dim][prov.strategy[0][dim]]

        # Step 4. Apply the strategy

        #   'roaming' access cost
        vector = [min_cost, prov_roaming_cost, max_cost]
        prov_roaming_cost = (1 - ema_factor) * prov_roaming_cost + ema_factor * vector[prov.strategy[0][0]]
        assert isinstance(prov_roaming_cost, float), \
            'New provider cost not given as float but as %s' % str(type(prov_roaming_cost))

        #   entry fee sellers
        vector = [min_entryfee_s, prov_efs, max_entryfee_s]
        prov_efs = (1 - ema_factor) * prov_efs + ema_factor * vector[prov.strategy[0][1]]
        assert isinstance(prov_efs, float), \
            'New entry fee_seller not given as float but as %s' % str(type(prov_efs))

        #   entry fee buyers
        vector = [min_entryfee_b, prov_efb, max_entryfee_b]
        prov_efb = (1 - ema_factor) * prov_efb + ema_factor * vector[prov.strategy[0][2]]
        assert isinstance(prov_efb, float), \
            'New entry fee_buyer not given as float but as %s' % str(type(prov_efb))

        #   transaction fee buyers
        vector = [min_trans_cost_b, prov_tcb, max_trans_cost_b]
        prov_tcb = (1 - ema_factor) * prov_tcb + ema_factor * vector[prov.strategy[0][3]]
        assert isinstance(prov_efb, float), \
            'New transaction fee_buyer not given as float but as %s' % str(type(prov_tcb))

        #   transaction fee buyers
        vector = [min_trans_cost_s, prov_tcs, max_trans_cost_s]
        prov_tcs = (1 - ema_factor) * prov_tcs + ema_factor * vector[prov.strategy[0][4]]
        assert isinstance(prov_tcs, float), \
            'New transaction fee_seller not given as float but as %s' % str(type(prov_tcs))
        
        return prov_roaming_cost, prov_efb, prov_efs, prov_tcb, prov_tcs


class SoReinforcementLearningS(StrategyObject):
    """
    The strategy object for reinforcement learning with satisficing.
    The same description as for the normal reinforcement learning applies. The only difference is the satisficing
    condition added in step 2:
    The probability weights get adjusted only if the satisficing level is not reached. Also, the
    strategy only gets chosen anew and applied, if the satisficing level is not reached.
    """

    def __init__(self, satisficing_level_revenue, satisficing_level_cn):
        self.include_customer_no = False
        self.satisficing_level_revenue = satisficing_level_revenue
        self.satisficing_level_cn = satisficing_level_cn

    def __call__(self, prov, prov_roaming_cost, prov_efs, prov_efb, prov_tcb, prov_tcs, prov_rev, prov_lrev, prov_cno,
                 prov_lcno, firsttime):
        """
        This call method is the old choose_strat function.
        :param prov:            The provider associated with the call (given through "self"
        :param prov_roaming_cost:    The roaming costs charged by the provider
        :param prov_efs:        The entry fee for the sellers
        :param prov_efb:        The entry fee for the buyers
        :param prov_rev:        Current revenue of the provider
        :param prov_lrev:       Revenue of the provider in the previous round
        :param prov_cno:        Number of current customers
        :param prov_lcno:       Number of customers in the previous round
        :param firsttime:       Should be True if the object gets called the first time
        :return: tuple (provider cost, entry cost for seller, entry cost for buyer
        The process is as follows:
            1. Check whether provider can match her operating cost
            2. Calculate revenue of the previous round
            3. Check whether saticying level is reached. If yes, stop. If not, continue with next step.
            4. Choose a new strategy
            5. Apply the strategy
        """

        if firsttime:
            prov.strategy.append([])
            for i in range(5):
                prov.strategy[0].append(random.randint(0,2))
            prov.strategy.append([])
            for i in range(5):
                prov.strategy[1].append(numpy.ones(3))
            return

        
        debug = False

        if debug:
            print(prov.id, ' SO-RIL: current/last revenue ', prov_rev, prov_lrev)
            if prov.id == 0:
                print('  ', prov.id, ' current/last user no ', prov_cno, prov_lcno)
                print('  ', prov.id, ' strategy ', prov.strategy)
                print('  ', prov.id, ' rc efb efs tcb tcs ', prov_roaming_cost, prov_efs, prov_efb, prov_tcb, prov_tcs)
        
        
        # Step 1: Disourage strategies if provider cannot match operating costs.
        if prov.revenue < 0:
            prov.strategy[1][0][prov.strategy[0][0]] /= 10.
            prov.strategy[1][1][prov.strategy[0][1]] /= 10.
            prov.strategy[1][2][prov.strategy[0][2]] /= 10.
            prov.strategy[1][3][prov.strategy[0][3]] /= 10.
            prov.strategy[1][4][prov.strategy[0][4]] /= 10.
            prov_roaming_cost = 100 if prov_roaming_cost < 100 else prov_roaming_cost
            prov_efs = 100 if prov_efs < 100 else prov_efs
            prov_efb = 100 if prov_efb < 100 else prov_efb
            prov_tcs = 100 if prov_tcs < 100 else prov_tcs
            prov_tcb = 100 if prov_tcb < 100 else prov_tcb
            return prov_roaming_cost, prov_efb, prov_efs, prov_tcb, prov_tcs

        # 2. Obtain a relative success measure and check if satisfying level is reached:

        if prov_lrev <= 0:          # In the first found, the relative success measure is set to unity
            relative_success = 1.0
        else:
            relative_success = prov_rev * 1. / prov_lrev

        if self.include_customer_no:
            relative_success *= (prov_cno+1) / (prov_lcno+1)

        if prov_rev < self.satisficing_level_revenue or prov_cno < self.satisficing_level_cn:
            
            for dim in range(5):
                for i in range(len(prov.strategy[1][dim])):
                    prov.strategy[1][dim][i] **= past_discounting_root_expon
    
            for dim in range(5):
                prov.strategy[1][dim][prov.strategy[0][dim]] *= relative_success

            for dim in range(5):  # re-normalize strategy weight vectors
                sumweight = sum(prov.strategy[1][dim])
                for i in range(len(prov.strategy[1][dim])):
                    prov.strategy[1][dim][i] /= sumweight
    
        # 3. Choose new strategy (only if satisficing level is not reached)

            for dim in range(5):
                s = random.uniform(0, 1)
                prov.strategy[0][dim] = -1
                while s > 0:
                    prov.strategy[0][dim] += 1
                    s -= prov.strategy[1][dim][prov.strategy[0][dim]]
    
        # 4. Apply the strategy (only if satisficing level is not reached)

            #   'roaming' access cost
            vector = [min_cost, prov_roaming_cost, max_cost]
            prov_roaming_cost = (1 - ema_factor) * prov_roaming_cost + ema_factor * vector[prov.strategy[0][0]]
            assert isinstance(prov_roaming_cost, float), \
                'New provider cost not given as float but as %s' % str(type(prov_roaming_cost))

            #   entry fee sellers
            vector = [min_entryfee_s, prov_efs, max_entryfee_s]
            prov_efs = (1 - ema_factor) * prov_efs + ema_factor * vector[prov.strategy[0][1]]
            assert isinstance(prov_efs, float), \
                'New entry fee_seller not given as float but as %s' % str(type(prov_efs))
            #   entry fee buyers
            vector = [min_entryfee_b, prov_efb, max_entryfee_b]
            prov_efb = (1 - ema_factor) * prov_efb + ema_factor * vector[prov.strategy[0][2]]
            assert isinstance(prov_efb, float), \
                'New entry fee_buyer not given as float but as %s' % str(type(prov_efb))
            #   transaction fee buyers
            vector = [min_trans_cost_b, prov_tcb, max_trans_cost_b]
            prov_tcb = (1 - ema_factor) * prov_tcb + ema_factor * vector[prov.strategy[0][3]]
            assert isinstance(prov_efb, float), \
                'New transaction fee_buyer not given as float but as %s' % str(type(prov_tcb))
            #   transaction fee buyers
            vector = [min_trans_cost_s, prov_tcs, max_trans_cost_s]
            prov_tcs = (1 - ema_factor) * prov_tcs + ema_factor * vector[prov.strategy[0][4]]
            assert isinstance(prov_tcs, float), \
                'New transaction fee_seller not given as float but as %s' % str(type(prov_tcs))
        
        return prov_roaming_cost, prov_efb, prov_efs, prov_tcb, prov_tcs


class SoRationalChoice(StrategyObject):
    """
    The strategy object used to replicate the Rochet-Tirole results.
    For the optimization we are using an evolutionary optimization algorithm due to Storn/Price (1997).
    The provider chooses the entry fees and roaming costs such that revenue gets maximized.
    The procedure does not work when both entry and transaction costs should be set.

    The procedure is as follows:
        1. The provider sets certain hypothetical price structures (roaming, entryfees, per_transactfees)
            In the replication case we assume the entryfees to be zero, but consider cost per transaction)
        2. The provider checks how many transaction costs would take place if the respective price structures were set.
        3. The provider chooses the structure that gives her the highest revenue.
    """

    def __init__(self, provider_transaction_cost_b, provider_transaction_cost_s, provider_fixed_cost_pb,
                 provider_fixed_cost_ps):
        """
        For initialization. The following values are needed for the calculations:
            1. The current transactions costs for buyer
            2. The current transactions costs for seller
            3. The fixed costs incurred to the provider for each buyer
            4. The fixed costs incurred to the provider for each seller
        """
        print("Initialize RO class...")
        self.provider_transaction_cost_b = provider_transaction_cost_b
        self.provider_transaction_cost_s = provider_transaction_cost_s
        self.provider_fixed_cost_pb = provider_fixed_cost_pb
        self.provider_fixed_cost_ps = provider_fixed_cost_ps
        pass

    def __call__(self, prov, *args):
        """
        1. Initializes a revenue function that replicates the one of Rochet-Tirole.
        2. Initializes the DifferentialEvolution class with the standard parameters (chosen according to literature).
        3. Applies the DifferentialEvolution algorithm.
        4. Returns the computed optima and together with the fixed parameters.

        Note: *args is not used, but it assures compatibility with unified call syntax because it is used
        by the other strategy objects.
        """
        print("Called RO function...")
        # Step 1
        revenue = RevenueFunction(prov.buyer_no, prov.seller_no, self.provider_transaction_cost_b,
                                  self.provider_transaction_cost_s, self.provider_fixed_cost_pb,
                                  self.provider_fixed_cost_ps, prov.entryfee_b, prov.entryfee_s, prov.roaming_cost)

        # Step 2
        diff_evo_instance = DifferentialEvolution(2, 0.9, 0.9, 200, revenue)  # optimize only transaction fees
        # diff_evo_instance = DifferentialEvolution(4, 0.9, 0.9, 200, revenue)  # optimize transaction and entry fees

        # Step 3
        optimum = revenue.expand_DE_vars(diff_evo_instance.optimize())

        # Step 4
        print('Computed optimum ', optimum)
        if len(optimum) <= 3:
            return prov.roaming_cost, prov.entryfee_b, prov.entryfee_s, optimum[0], optimum[1]
        elif len(optimum) <= 4:
            return prov.roaming_cost, optimum[2], optimum[3], optimum[0], optimum[1]
        else:
            return optimum[4], optimum[2], optimum[3], optimum[0], optimum[1]


class RevenueFunction:
    """
    The function is used to calculate the revenue. It mimics the function of Rochet-Tirole.

    We introduce a transaction number factor ("tnf") to ensure that providers do not imagine an
    unrealistically high number of transactions as it is suggested in the Rochet-Tirole paper,
    who simply say that total transactions are D_s*D_b.

    When the function gets called, it automatically updates the variables that have been updated by
    the provider (entryfees, and/or transaction fees).
    """

    def __init__(self, number_buyer_last_round, number_seller_last_round, provider_transaction_cost_b,
                 provider_transaction_cost_s, provider_fixed_cost_pb, provider_fixed_cost_ps, old_entryfee_b,
                 old_entryfee_s, old_roaming_cost):
        self.number_buyer_last_round = number_buyer_last_round
        self.number_seller_last_round = number_seller_last_round
        self.c_b = provider_transaction_cost_b
        self.c_s = provider_transaction_cost_s
        self.C_b = provider_fixed_cost_pb
        self.C_s = provider_fixed_cost_ps
        self.old_entryfee_b = old_entryfee_b
        self.old_entryfee_s = old_entryfee_s
        self.old_roaming_cost = old_roaming_cost
        self.trans_inst_nRT = Transaction()

        self.tnf = float(no_transactions_per_iteration)/max(1, (len(sellerlist)*len(buyerlist)))
        self.no_sellers = len(sellerlist)
        self.no_buyers = len(buyerlist)

    def __call__(self, sv):
        """
        Takes the results of the differential evolution algorithm as an input and uses acutual costs.
        If len(sv) == 1: only transaction costs get updated
        If len(sv) == 2: also the entryfees for the buyers get updated
        If len(sv) == 3: also the entryfees for the sellers get updated
        """

        rv = self.expand_DE_vars(sv)
        transaction_cost_b = rv[0]
        transaction_cost_s = rv[1]
        entryfee_b = self.old_entryfee_b
        entryfee_s = self.old_entryfee_s
        if len(rv) > 2:
            entryfee_b = rv[2]
            if len(rv) > 3:
                entryfee_s = rv[3]

        D_b, D_s, exp_trans_n = self.trans_inst_nRT.get_demand(entryfee_b, entryfee_s, self.number_buyer_last_round,
                                                               self.number_seller_last_round, transaction_cost_b,
                                                               transaction_cost_s, self.tnf, self.no_sellers,
                                                               self.no_buyers)
        balance_T = (transaction_cost_b + transaction_cost_s - self.c_b - self.c_s) * self.tnf*exp_trans_n
        balance_AB = (entryfee_b - self.C_b) * D_b
        balance_AS = (entryfee_s - self.C_s) * D_s

        debug = False
        if debug:
            print('return function: entryfees:', entryfee_b, entryfee_s, ' transact fees: ', transaction_cost_b,
                  transaction_cost_s, ' revenue=', balance_T+balance_AB + balance_AS,
                  '=sum of:', balance_T, balance_AB, balance_AS, )

        return balance_T + balance_AB + balance_AS


    @staticmethod
    def expand_DE_vars(sv):
        """
        This function is used to expand the variables beyond the 0,1 interval that is allowed for in the DE algorithm.
        """
        rv = list(sv) # avoid python interfering with sv in wherever this method was called
        rv[0] = rv[0]*(max_trans_cost_b - min_trans_cost_b) + min_trans_cost_b
        rv[1] = rv[1]*(max_trans_cost_s - min_trans_cost_s) + min_trans_cost_s
        if len(rv) > 2:
            rv[2] = rv[2]*(max_entryfee_b - min_entryfee_b) + min_entryfee_b
            if len(rv) > 3:
                rv[3] = rv[3]*(max_entryfee_s - min_entryfee_s) + min_entryfee_s
                if len(rv) > 4:
                    rv[4] = rv[4]*(max_cost - min_cost) + min_cost
        return rv


class DifferentialEvolution:
    """
    Object for differential evolution optimization. This is our python implementation of the differential evolution
    algorithm of Storn and Price (1997).
    The algorithm requires the following parameters:
        F = amplification of variation
        D = dimensionality (number of parameters to be optimized)
        CR = "crossover operator", mutation probability for any point in the genome after the first mutation
        G = number of mutation/selection generations
        tf = target function for optimization; may be any function that accepts
            ndarray object with D elements and returns a single numeric target value.
        Quasi-parameter NP: Population size.
    For an in depth-description of the algorithm see the paper of Storn/Price (1997).
    The parameters are set in accordance with what is suggested in Liu/Lampinen 2005.

    The target value is then maximized over a vector of D dimensions between 0 and 1.
    The target function may stretch these values to whichever value range it would like them to be. We use the
    function "expand_DE_vars" in the RevenueFunction class for this purpose.

    Original references:

    Liu, J. & Lampinen, J. (2005). A fuzzy adaptive differential evolution algorithm. Soft Computing, 9 (6), 448-462.
    doi:10.1007/s00500-004-0363-x
    Storn, R. & Price, K. (1997). Differential evolution - a simple and efficient heuristic for global optimization
    over continuous spaces. Journal of Global Optimization, 11 (4), 341-359. doi:10. 1023/A:1008202821328
    """

    def __init__(self, D, F, CR, G, tf):
        self._D = D
        assert isinstance(self._D, int)
        assert D > 0, 'Dimensionality of parameters to be optimized must be at least one.'
        self._NP = 10 * D
        self._F = F
        assert 0 <= self._F <= 2
        self._CR = CR
        assert self._CR <= 1
        assert self._CR >= 0
        self._G = G
        assert isinstance(self._G, int)
        assert self._G >= 0
        self._tf = tf
        self.test_target(self._tf)
        self._members = []
        for i in range(self._NP):
            self._members.append(generate_sv(self._D))

    def test_target(self, tf):
        """
        Tests the given target function. Called by init.
        True if target function works properly.
        Otherwise exits the whole process.
        """
        testarray = numpy.zeros(self._D)
        testval = tf(testarray)
        try:
            testarray = numpy.zeros(self._D)
            isinstance(tf(testarray), (int, float, complex))
        except ImportError:
            print('Target function does not work or does not work with specified dimensionality ', self._D)
            print('Output of target function not a proper number: %s' % str(type(tf(testarray))))
            print('Differential evolution algorithm cannot continue')
            exit(43)
        pass

    def iterate(self):
        """
        A singe iteration of the algorithm. Consists of the following steps for each element of the population:
            1. Mutation (generate mutation candidate for each genome point)
            2. Crossover operation (choose some of the mutations, retain the original for other points)
            3. Selection operation (select mutant or retain original)
        """

        for i in range(self._NP):
            # 1. Mutation
            r1 = r2 = r3 = i
            while r1 == i:
                r1 = random.randint(0, self._NP-1)
            while r2 == i:
                r2 = random.randint(0,self._NP-1)
            while r3 == i:
                r3 = random.randint(0,self._NP-1)
            mutant_v = self._members[r1] + self._F*(self._members[r2] - self._members[r3])
            mutant_v = renormalize_sv(mutant_v)

            # 2. Crossover
            target_v = 1 * self._members[i]
            rnbr = random.randint(0, self._D-1)
            for j in range(self._D):
                if random.uniform(0, 1) <= self._CR or j == rnbr:
                    target_v[j] = mutant_v[j]

            # 3. Selection
            if self._tf(target_v) > self._tf(self._members[i]):
                self._members[i] = target_v

    def optimize(self):
        """
        Runs the differential evolution algorithm over self._G generations.
        """
        for i in range(self._G):
            print("Optimizing round %s\r" % str(i), end=' ')
            self.iterate()
        best_v = self._members[0]
        bvr = self._tf(best_v)
        for i in range(1, self._NP):
            if self._tf(self._members[i]) > bvr:
                best_v = self._members[i]
                bvr = self._tf(best_v)
        return best_v


class Transaction:
    """
    The transaction class. Through the method get_demand it gives the actual demand of buyers and sellers.
    """

    def __init__(self):
        pass

    def get_demand(self, access_fee_b, access_fee_s, number_buyer_last_round, number_seller_last_round,
                   transaction_price_b, transaction_price_s, tnf, no_sellers, no_buyers):
        """
        Uses all relevant costs for transactions as inputs and returns the actual demand of buyers and sellers.
        While the rational optimizing providers knows about this function, it is unknown to the providers using
        reinforcement learning.

        To be more efficient it does not check all actual reservation prices, but uses a sample of size 100 of the
        distribution of reservation. This procedure has been verified and gives the same results as if the
        actual reservation prices had been used.

        The function returns both the actual demand and the hypothetical demand if only the transaction prices for
        the respective side had been used.
        """

        reservation_prices_b = scipy.stats.uniform.rvs(size=100, loc=price_average*0.5, scale=price_average*0.5)
        reservation_prices_s = scipy.stats.uniform.rvs(size=100, loc=price_average, scale=price_average*0.5)
        cost_per_trans_b = transaction_price_b + access_fee_b / max(0.0001, number_seller_last_round*tnf)
        demand_b = sum(i >= cost_per_trans_b for i in price_average-reservation_prices_b)
        cost_per_trans_s = transaction_price_s + access_fee_s / max(0.0001, number_buyer_last_round*tnf)
        demand_s = sum(i >= cost_per_trans_s for i in reservation_prices_s-price_average)
        debug=False
        if debug:
            print(cost_per_trans_b,' = ',transaction_price_b, ' + ',
                  access_fee_b / max(0.0001, number_seller_last_round*tnf))
            print('Resulting in (for buyer (0)):',cost_per_trans_b, ' < ',
                  price_average,' - ',reservation_prices_b[0])
            print(cost_per_trans_s,' = ',transaction_price_s, ' + ',
                  access_fee_s / max(0.0001, number_buyer_last_round*tnf))
            print('Resulting in (for seller (0)):',cost_per_trans_s, ' < ',
                  reservation_prices_s[0],' - ',price_average)

        demand_ex_post_b = min(demand_b, sum(i >= transaction_price_b for i in price_average-reservation_prices_b))
        demand_ex_post_s = min(demand_s, sum(i >= transaction_price_s for i in reservation_prices_s-price_average))
        if debug:
            print('Ex post demands: ', demand_b, demand_s)

        return demand_b*no_buyers/100., demand_s*no_sellers/100., \
               demand_ex_post_b*demand_ex_post_s/10000.*no_buyers*no_sellers

"""
Definitions of auxiliary functions
"""

def transaction():
    """
    Function for a transaction between sellers and buyers, mediated through a provider.
    It is called from within the main function so many times as is specified in parameter no_transactions_per_iteration.
    Before the function gets called, the reservation prices were set randomly via the buyer/seller method

    The timing is as follows:

    1. Seller and buyer are randomly chosen
    2. Compare the reservation prices. Continue only if the buyer rprice is above the seller rprice.
    3. Find the cheapest available channel of transmission between buyer and seller (depending on their subscriptions).
    4. Check if this channel allows a positive 'revenue' for seller and buyer from the transaction. If this is the
    case, the transaction is conducted. Buyer and seller are awarded half of the remaining 'revenue' each
    and  and providers are awarded the transaction costs they charge.
    5. In the end, the transaction counter gets augmented if the transaction took place.
    """

    debug = False   # switch on for more output

    # 1. Step: Choose buyers and sellers
    seller = random.choice(sellerlist)
    buyer = random.choice(buyerlist)
    assert isinstance(seller, Seller)
    assert isinstance(buyer, Buyer)

    # 2. Step: Determine whether a transaction in principally feasible
    if seller.reservation_price < buyer.reservation_price:		# only if reservation price is not exceeded
        bprice = buyer.reservation_price
        sprice = seller.reservation_price
        if debug:
            print('DEBUG ta: ', sprice, bprice)

    # 3. Step: Find cheapest channel of transmission
        transmission_cost = bprice - sprice
        sprov = -1
        bprov = -1
        for sp in seller.providers:
            assert isinstance(sp, Provider)
            for bp in buyer.providers:
                assert isinstance(bp, Provider)
                if debug:
                    print('DEBUG ta: provider found')
                cost = 0
                if sp != bp:
                    cost += sp.roaming_cost + bp.roaming_cost
                cost += sp.trans_cost_s + bp.trans_cost_b

                if debug:
                    print('DEBUG ta: cost=', cost,
                          '= CS (', sp.trans_cost_s, ') + BS (', bp.trans_cost_b, '), surplus=', transmission_cost)
                if cost < transmission_cost:
                    sprov = sp				# ... reset sellers optimal provider
                    bprov = bp				# ... and buyers optimal provider
                    transmission_cost = cost	# ... and cheapest transmission cost
                    if debug:
                        print('DEBUG ta: ... success')
        
    # 4. Step: Check if the channel is feasible and eventually effect the transactions
        if sprov != -1 and bprov != -1:
            crevenue = (bprice - sprice - transmission_cost) / 2.0  # customers split 'revenue' evenly,
            brevenue = ((bprice - sprice) / 2.0) - bprov.trans_cost_b
            if bprov != sprov:
                brevenue -= bprov.roaming_cost
            srevenue = ((bprice - sprice) / 2.0) - sprov.trans_cost_s
            if bprov != sprov:
                srevenue -= sprov.roaming_cost
            seller.money += srevenue
            buyer.money += brevenue
            seller.prevenue[seller.providers.index(sprov)] += srevenue
            buyer.prevenue[buyer.providers.index(bprov)] += brevenue

            if sprov != bprov:
                sprov.revenue += sprov.roaming_cost
                bprov.revenue += bprov.roaming_cost
            sprov.revenue += sprov.trans_cost_s - provider_transaction_cost_s
            bprov.revenue += bprov.trans_cost_b - provider_transaction_cost_b

    # 5. Increase transaction counter
            global transaction_counter
            transaction_counter += 1


def chooseprovider(buyer, network_ext):
    """
    Customers choose their new provider according to this function. It is called in the main function
    :param buyer:           True if the customer who has to decide is a buyer.
    :param network_ext:     Weight for the decision mechanism (see below).
    :return: One provider the customer subscribes to

    The decision mechanism is specified as follows:
        If network_ext == 0:
            The choice is made randomly amongst all providers
        If network_ext == 1:
            The choice is made exclusively made on the base of the provider weights which depend on the nb of
            customers already subscribed to the provider.
        If network_ext is in between 0 and 1:
            A random variable determine which one of the two gets used

    For the network-externality based choice, the agents access the provider weights defined in the main function.
    These weights give providers with a larger number of customers a higher probability of being chosen. 
    """

    assert 0 <= network_ext <= 1, 'network_ext outside viable range'

    if network_ext == 0:  # Decision is made randomly
        suggestion_no_ne = random.choice(providerlist)
        return suggestion_no_ne

    else:   # Decision is based on network externalities
        r = random.uniform(0, 1)    # draw a random variable
        i = -1                      # define index variable
        if buyer:                       # if customer is buyer, we must use b_providerweights
            while r > 0:                    # select the provider corresponding to r using the b_providerweights 
                                            # (weights for every provider, sum=1), as follows:
                i += 1						# increment index by one
                r -= b_providerweights[i]   # decrease r by weight of provider number i
                                            # if r so becomes <=0, the loop will ends and number i is selected
        else:                           # if customer is no buyer (i.e. a seller), we must use s_providerweights
            while r > 0:					# select the provider corresponding to r using the s_providerweights 
                                            # (weights for every provider, sum=1), as follows:
                i += 1 						# increment index by one
                r -= s_providerweights[i]   # decrease r by weight of provider number i
                                            # if r so becomes <=0, the loop will ends and number i is selected
        suggestion_network_ext = providerlist[i]    # save selected provider

    if network_ext == 1:
        return suggestion_network_ext

    else:  # network_ext < 1
        suggestion_no_ne = random.choice(providerlist)  # Same as above with ne==0

    r = random.uniform(0, 1)			# Get new random value (0,1)
    if r < network_ext:					# If smaller network_ext the network externality based choice is used
        return suggestion_network_ext
    else:                               # Otherwise the uniform random choice has been selected
        return suggestion_no_ne


def evaluate(time):
    """
    Collects all relevant data from agents, i.e. costumers and providers, and records everything in lists.
    The output gets printed every 20 rounds and at the end of the simulation.
    """

    # Auxiliary variables
    rev_sum = 0	    # auxiliary variable (sum of revenue of all providers), for averages
    cus_sum = 0	    # auxiliary variable (sum of customer numbers of all providers), for averages
    buyer_sum = 0   # auxiliary variable (sum of buyer numbers of all providers), for averages
    seller_sum = 0  # auxiliary variable (sum of seller numbers of all providers), for averages
    prov_no = len(providerlist)	    # auxiliary variable (number of providers), for averages

    # initial values of variables to be collected, initialized with the entry fee buyers of first provider
    efb_min = providerlist[0].entryfee_b		# minimum entry fee for buyers,
    efb_max = providerlist[0].entryfee_b		# maximum entry fee for buyers
    efb_av = 0								    # average entry fee for buyers
    efs_min = providerlist[0].entryfee_s		# minimum entry fee for sellers
    efs_max = providerlist[0].entryfee_s		# maximum entry fee for sellers
    efs_av = 0								    # average entry fee for sellers
    tfb_min = providerlist[0].trans_cost_b		# minimum transaction fee for buyers
    tfb_max = providerlist[0].trans_cost_b		# maximum transaction fee for buyers
    tfb_av = 0
    tfs_min = providerlist[0].trans_cost_s  	# minimum transaction fee for sellers
    tfs_max = providerlist[0].trans_cost_s		# maximum transaction fee for sellers
    tfs_av = 0
    cost_min = providerlist[0].roaming_cost	    # minimum 'roaming' access cost
    cost_max = providerlist[0].roaming_cost	    # maximum 'roaming' access cost
    cost_av = 0								    # average 'roaming' access cost
    rev_min = providerlist[0].revenue		    # minimum revenue of providers
    rev_max = providerlist[0].revenue		    # maximum revenue of providers
    rev_av = 0								    # average revenue of providers
    cus_max = providerlist[0].customer_no		# minimum number of customers by providers
    cus_min = providerlist[0].customer_no		# maximum number of customers by providers
    cus_av = 0								    # average number of customers by providers

    # collect data
    for prov in providerlist:
        assert isinstance(prov, Provider), 'This object should be a provider instance!'
        efb_min = prov.entryfee_b if efb_min > prov.entryfee_b else efb_min
        efb_max = prov.entryfee_b if efb_max < prov.entryfee_b else efb_max
        efb_av += prov.entryfee_b * prov.buyer_no

        efs_min = prov.entryfee_s if efs_min > prov.entryfee_s else efs_min
        efs_max = prov.entryfee_s if efs_max < prov.entryfee_s else efs_max
        efs_av += prov.entryfee_s * prov.seller_no

        cost_min = prov.roaming_cost if cost_min > prov.roaming_cost else cost_min
        cost_max = prov.roaming_cost if cost_max < prov.roaming_cost else cost_max
        cost_av += prov.roaming_cost * prov.customer_no

        tfb_min = prov.trans_cost_b if tfb_min > prov.trans_cost_b else tfb_min
        tfb_max = prov.trans_cost_b if tfb_max < prov.trans_cost_b else tfb_max
        tfb_av += prov.trans_cost_b * prov.buyer_no

        tfs_min = prov.trans_cost_s if tfs_min > prov.trans_cost_s else tfs_min
        tfs_max = prov.trans_cost_s if tfs_max < prov.trans_cost_s else tfs_max
        tfs_av += prov.trans_cost_s * prov.seller_no

        rev_min = prov.revenue if rev_min > prov.revenue else rev_min
        rev_max = prov.revenue if rev_max < prov.revenue else rev_max
        rev_av += prov.revenue

        cus_min = prov.customer_no if cus_min > prov.customer_no else cus_min
        cus_max = prov.customer_no if cus_max < prov.customer_no else cus_max
        cus_av += prov.customer_no

        rev_sum += prov.revenue
        cus_sum += prov.customer_no
        buyer_sum += prov.buyer_no
        seller_sum += prov.seller_no

    # finalize computation of averages by dividing by respective sum of weights
    efb_av /= buyer_sum
    efs_av /= seller_sum
    cost_av /= cus_sum
    rev_av /= prov_no
    cus_av /= prov_no
    tfb_av /= buyer_sum
    tfs_av /= seller_sum

    money_min = customerlist[0].money		# customer minimum revenue, initialized as revenue of first customer
    money_max = customerlist[0].money		# customer minimum revenue, initialized as revenue of first customer
    money_av = 0							# customer average revenue, initialized as 0
    for cus in customerlist:
        assert isinstance(cus, Buyer) or isinstance(cus, Seller), 'Object should be instance of Buyer or Seller!'
        m = cus.money
        money_max = m if m > money_max else money_max
        money_min = m if m < money_min else money_min
        money_av += m
    money_av /= len(customerlist)

    # seller average, maximum, minimum revenue:
    money_min_s = sellerlist[0].money
    money_max_s = sellerlist[0].money
    money_av_s = 0
    for cus in sellerlist:
        m = cus.money
        money_max_s = m if m > money_max_s else money_max_s
        money_min_s = m if m < money_min_s else money_min_s
        money_av_s += m
    money_av_s /= len(sellerlist)

    # buyer average, maximum, minimum revenue:
    money_min_b = buyerlist[0].money
    money_max_b = buyerlist[0].money
    money_av_b = 0
    for cus in buyerlist:
        m = cus.money
        money_max_b = m if m > money_max_b else money_max_b
        money_min_b = m if m < money_min_b else money_min_b
        money_av_b += m
    money_av_b /= len(buyerlist)

    # print output every 20 turns and at the end of the simulation (t==t_max-1)
    if t % 20 == 0 or t == t_max-1:
        printstring='Period {0:0d}: \nCustomers: Money Average: {1:4f} \nSellers: Money Average: {2:4f} \n' \
                    'Buyers: Money Average: {3:4f} \nProviders: EntryFee for Buyers ' \
                    '(min average max): {4:4f} {5:4f} {6:4f} \n' \
                    'Providers: EntryFee for Sellers (min average max): {7:4f} {8:4f} {9:4f} \n' \
                    'Providers: Compatibility Penalty (min average max): {10:4f} {11:4f} {12:4f} \n' \
                    'Providers: Revenue (min average max): {13:4f} {14:4f} {15:4f} \n' \
                    'Providers: CustomerNumber (min average max): {16:4f} {17:4f} ' \
                    '{18:4f} \n'.format(time, money_av, money_av_s, money_av_b, efb_min, efb_av,
                                        efb_max, efs_min, efs_av, efs_max, cost_min, cost_av, cost_max, rev_min,
                                        rev_av, rev_max, cus_min, cus_av, cus_max)
        print(printstring)
    
    debug = True # Turn on for more printed output
    if debug:
        tsp = providerlist[0]
        printstring = 'Period {0:0d}: \nProvider ' \
                    'EntryFee for Sellers: {1:4f} ' \
                    'EntryFee for Buyers: {2:4f} ' \
                    'Revenue: {3:4f} ' \
                    'CustomerNumber: {4:4d} ' \
                    'SellerNumber: {5:4d} ' \
                    'BuyerNumber: {6:4d} ' \
                    'TransactionNumber: {7:4d} ' \
                    'Transaction Price S: {8:4f} ' \
                    'Transaction Price B: {9:4f} ' \
                    .format(time, tsp.entryfee_s, tsp.entryfee_b, tsp.revenue, tsp.customer_no, tsp.seller_no,
                            tsp.buyer_no, transaction_counter, tsp.trans_cost_s, tsp.trans_cost_b)
        print(printstring)

    # record variables into historical records
    rec_t.append(time)
    rec_transactions.append(transaction_counter)
    rec_prov_min.append(rev_min)
    rec_prov_max.append(rev_max)
    rec_prov_av.append(rev_av)
    rec_cn_min.append(cus_min)
    rec_cn_max.append(cus_max)
    rec_cn_av.append(cus_av)
    rec_efb_min.append(efb_min)
    rec_efb_max.append(efb_max)
    rec_efb_av.append(efb_av)
    rec_efs_min.append(efs_min)
    rec_efs_max.append(efs_max)
    rec_efs_av.append(efs_av)
    rec_tfb_min.append(tfb_min)
    rec_tfb_max.append(tfb_max)
    rec_tfb_av.append(tfb_av)
    rec_tfs_min.append(tfs_min)
    rec_tfs_max.append(tfs_max)
    rec_tfs_av.append(tfs_av)
    rec_cost_min.append(cost_min)
    rec_cost_max.append(cost_max)
    rec_cost_av.append(cost_av)
    rec_customer_av.append(money_av)
    rec_customer_min.append(money_min)
    rec_customer_max.append(money_max)
    rec_seller_av.append(money_av_s)
    rec_seller_min.append(money_min_s)
    rec_seller_max.append(money_max_s)
    rec_buyer_av.append(money_av_b)
    rec_buyer_min.append(money_min_b)
    rec_buyer_max.append(money_max_b)


def generate_sv(D):
    """
    Gives a random vector of size D, with random numbers in (0,1)
    """
    elements = [random.uniform(0, 1) for i in range(D)]
    elements = numpy.asarray(elements)
    return elements


def renormalize_sv(elements):
    """
    Accepts a vector or array and removes the integer part of all elements, reducing them floats in the interval (0,1).

    Example:
        x = [1.2, 4.5, 5, 3.1]
        renormalize(x)
        print(x)
        [0.2, 0.5, 0, 0.1]
    """

    D = len(elements)
    elements_new = [elements[i] % 1 for i in range(D)]
    return elements_new


def write_output(outputfilename):
    """
    This function writes the output into a .py file.
    """

    outputfile = 'output/' + outputfilename + '.py'
    print('Writing output to file ', outputfile, '...')
    f = open(outputfile, 'w')
    f.write('transactions = ' + str(rec_transactions) + '\n' +
            'prov_rev_min = ' + str(rec_prov_min) + '\n' +
            'prov_rev_max = ' + str(rec_prov_max) + '\n' +
            'prov_rev_av = ' + str(rec_prov_av) + '\n' +
            'prov_cn_min = ' + str(rec_cn_min) + '\n' +
            'prov_cn_max = ' + str(rec_cn_max) + '\n' +
            'prov_cn_av = ' + str(rec_cn_av) + '\n' +
            'sub_fee_buyer_min = ' + str(rec_efb_min) + '\n' +
            'sub_fee_buyer_max = ' + str(rec_efb_max) + '\n' +
            'sub_fee_buyer_av =' + str(rec_efb_av) + '\n' +
            'sub_fee_seller_min =' + str(rec_efs_min) + '\n' +
            'sub_fee_seller_max = ' + str(rec_efs_max) + '\n' +
            'sub_fee_seller_av = ' + str(rec_efs_av) + '\n' +
            'trans_fee_b_min = ' + str(rec_tfb_min) + '\n' +
            'trans_fee_b_max = ' + str(rec_tfb_max) + '\n' +
            'trans_fee_b_av = ' + str(rec_tfb_av) + '\n' +
            'trans_fee_s_min = ' + str(rec_tfs_min) + '\n' +
            'trans_fee_s_max = ' + str(rec_tfs_max) + '\n' +
            'trans_fee_s_av = ' + str(rec_tfs_av) + '\n' +
            'roaming_min = ' + str(rec_cost_min) + '\n' +
            'roaming_max = ' + str(rec_cost_max) + '\n' +
            'roaming_av = ' + str(rec_cost_av) + '\n' +
            'cus_rev_min = ' + str(rec_customer_min) + '\n' +
            'cus_rev_max = ' + str(rec_customer_max) + '\n' +
            'cus_rev_av = ' + str(rec_customer_av) + '\n' +
            'seller_rev_min = ' + str(rec_seller_min) + '\n' +
            'seller_rev_max = ' + str(rec_seller_max) + '\n' +
            'seller_rev_av = ' + str(rec_seller_av) + '\n' +
            'buyer_rev_min = ' + str(rec_buyer_min) + '\n' +
            'buyer_rev_max = ' + str(rec_buyer_max) + '\n' +
            'buyer_rev_av = ' + str(rec_buyer_av))
    f.close()
    print('...writing completed.')


def reset_simulation():
    """
    Resets all global variables. Can be used to clear any remains of a running simulation and its history.
    """

    provider_id = 0
    seller_id = 0
    buyer_id = 0
    figure = - 1
    global providerlist, customerlist, sellerlist, buyerlist
    providerlist = []
    customerlist = []
    sellerlist = []
    buyerlist = []
    global s_providerweights, b_providerweights
    s_providerweights = []
    b_providerweights = []
    global transaction_counter, t
    transaction_counter = 0
    t = -1
    global rec_t, rec_transactions, rec_prov_min, rec_prov_av, rec_prov_max, rec_cn_min, rec_cn_av, rec_cn_max, \
        rec_efb_min, rec_efb_av, rec_efb_max
    global rec_efs_min, rec_efs_av, rec_efs_max, rec_cost_min, rec_cost_av, rec_cost_max, rec_customer_min, \
        rec_customer_av, rec_customer_max
    global rec_seller_min, rec_seller_av, rec_seller_max, rec_buyer_min, rec_buyer_av, rec_buyer_max
    rec_t = []
    rec_transactions = []
    rec_prov_min = []
    rec_prov_max = []
    rec_prov_av = []
    rec_cn_max = []
    rec_cn_min = []
    rec_cn_av = []
    rec_efb_min = []
    rec_efb_max = []
    rec_efb_av = []
    rec_efs_min = []
    rec_efs_max = []
    rec_efs_av = []
    rec_tfb_min = []
    rec_tfb_max = []
    rec_tfb_av = []
    rec_tfs_min = []
    rec_tfs_max = []
    rec_tfs_av = []
    rec_cost_min = []
    rec_cost_max = []
    rec_cost_av = []
    rec_customer_min = []
    rec_customer_max = []
    rec_customer_av = []
    rec_seller_min = []
    rec_seller_max = []
    rec_seller_av = []
    rec_buyer_min = []
    rec_buyer_max = []
    rec_buyer_av = []


def draw(isLast, draw_delay=1):
    """
    This function is responsible for the graphical output.
    It uses pylab and is called from within the main function.
    :param isLast: if true, the figure gets saved as pdf
    :param draw_delay: number of periods beween updates of the figure 
    :return: nothing, it just draws and saves the figure after t_max.
    """
    global figure
    import pylab
    
    """catch the first call of the function to prepare the figures"""
    if figure == -1:
        figure = []
        figure.append(pylab.figure())
        figure.append(pylab.figure())
        figure.append(pylab.figure())
        figure.append(pylab.figure())
    
    pylab.ion()				# set interactive (so that the simulation continues after drawing)
    
    """	first figure: provider data and total transaction count"""
    pylab.figure(figure[0].number)
    pylab.suptitle('v02 Provider Data')
    pylab.subplot(311)
    pylab.ylabel('Provider Revenue')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_prov_av[-1*draw_delay-1:], 'b')			# provider revenue
    pylab.plot(rec_t[-1*draw_delay-1:], rec_prov_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_prov_max[-1*draw_delay-1:], 'k')
    pylab.subplot(312)
    pylab.ylabel('Provider Customers')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cn_av[-1*draw_delay-1:], 'b')			# number of customers
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cn_max[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cn_min[-1*draw_delay-1:], 'k')
    pylab.subplot(313)
    pylab.ylabel('Transactions')
    pylab.xlabel('Time')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_transactions[-1*draw_delay-1:], 'b')	# total number of transactions
    pylab.show()
    pylab.pause(0.001)
    
    """second figure: customer data"""
    pylab.figure(figure[1].number)
    pylab.suptitle('v02 Customer Data')
    pylab.subplot(311)
    pylab.ylabel('Customer Revenue')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_customer_av[-1*draw_delay-1:], 'b')		#customer revenue
    pylab.plot(rec_t[-1*draw_delay-1:], rec_customer_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_customer_max[-1*draw_delay-1:], 'k')
    pylab.subplot(312)
    pylab.ylabel('Seller Revenue')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_seller_av[-1*draw_delay-1:], 'b')		#seller revenue
    pylab.plot(rec_t[-1*draw_delay-1:], rec_seller_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_seller_max[-1*draw_delay-1:], 'k')
    pylab.subplot(313)
    pylab.ylabel('Buyer Revenue')
    pylab.xlabel('Time')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_buyer_av[-1*draw_delay-1:], 'b')		# buyer revenue
    pylab.plot(rec_t[-1*draw_delay-1:], rec_buyer_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_buyer_max[-1*draw_delay-1:], 'k')
    pylab.show()
    pylab.pause(0.001)
    
    """third figure: pricing data (1)"""
    pylab.figure(figure[2].number)
    pylab.suptitle('v02 Pricing Data')
    pylab.subplot(311)
    pylab.ylabel('Buyer Subscription Fee')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efb_av[-1*draw_delay-1:], 'b')			#buyer subscription fee
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efb_min[-1*draw_delay-1:] , 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efb_max[-1*draw_delay-1:], 'k')
    pylab.subplot(312)
    pylab.ylabel('Seller Subscription Fee')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efs_av[-1*draw_delay-1:], 'b')			#seller subscription fee
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efs_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_efs_max[-1*draw_delay-1:], 'k')
    pylab.subplot(313)
    pylab.ylabel("'Roaming' Access Cost")
    pylab.xlabel('Time')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_av[-1*draw_delay-1:], 'b')			#roaming access cost
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_max[-1*draw_delay-1:], 'k')
    pylab.show()
    pylab.pause(0.001)
    
    """fourth figure: pricing data (2)"""
    pylab.figure(figure[3].number)
    pylab.suptitle('v02 Pricing Data')
    pylab.subplot(311)
    pylab.ylabel('Buyer Transaction Fee')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfb_av[-1*draw_delay-1:], 'b')			#buyer transaction fee
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfb_min[-1*draw_delay-1:] , 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfb_max[-1*draw_delay-1:], 'k')
    pylab.subplot(312)
    pylab.ylabel('Seller Transaction Fee')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfs_av[-1*draw_delay-1:], 'b')			#seller transaction fee
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfs_min[-1*draw_delay-1:], 'k')
    pylab.plot(rec_t[-1*draw_delay-1:], rec_tfs_max[-1*draw_delay-1:], 'k')
    #pylab.subplot(313)
    #pylab.ylabel("")
    pylab.xlabel('Time')
    #pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_av[-1*draw_delay-1:], 'b')		#not used
    #pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_min[-1*draw_delay-1:], 'k')
    #pylab.plot(rec_t[-1*draw_delay-1:], rec_cost_max[-1*draw_delay-1:], 'k')
    pylab.show()
    pylab.pause(0.001)
    
    pylab.ioff()
    
    """catch the last iteration, save the figures and show non-interactive"""
    if isLast:
        pylab.figure(figure[0].number)
        pylab.savefig('output/' + output_filename + '_fig_00' + '.pdf', dpi=600, format='pdf')
        pylab.figure(figure[1].number)
        pylab.savefig('output/' + output_filename + '_fig_01' + '.pdf', dpi=600, format='pdf')
        pylab.figure(figure[2].number)
        pylab.savefig('output/' + output_filename + '_fig_02' + '.pdf', dpi=600, format='pdf')
        pylab.figure(figure[3].number)
        pylab.savefig('output/' + output_filename + '_fig_03' + '.pdf', dpi=600, format='pdf')
        for i in range(3):
            pylab.figure(figure[i].number)
            pylab.show()


"""
The main function of the simulation model
"""

def main():
    """
    This function actually runs the simulation and is called if the script is called externally.
    The timing is the following:
        1. Create the agents

        2. Setup global network externality provider choice functions.
        These functions have as many elements as there are providers and contain probability weights for the choice of
        providers by customers. They may be accessed by the function 'chooseprovider' defined above and give providers
        with a larger customerbase a higher probability of being chosen.

        3. Iteration for the specified time steps. Each iteration contains 6 stages:
            1. Stage: Realization of the transactions.
                1.1. Reset the transaction counter
                1.2. Choose new reservation prices for all buyers and sellers.
                1.3. Conduct the specified number of transactions using the transaction function specified above

            2. Stage: The customer pay the fees to the provider

            3. Stage: The provider get iterated (first part) using their method "iterate"

            4. Stage: Data gets collected and evaluated via the evaluate function.
                Data is also written to outputfile (optional).

            5. Stage: Unsubscription decisions by the customers and adjustment of the providers' network weights
                They unsubscribe if revenue is either less than half the maximum revenue they obtained from
                any subscription or of it is negative.
                Then the network externality weights of the providers get adjusted: if a provider it among the most
                LUKRATIVE ones, then her weight gets increased.
                Finally the unsubscriptions get executed and the providerweights get renormalized.

            6. Stage: Subscription decisions of the customers.
                A customer subscribes to provider if either of the following is true:
                    - If she has more revenue left than the threshold value
                    - If the customer currently has no provider she has to subscribe to a provider
                        with probability of 0.1. This is necessary to ensure that customers do not immediately join
                        the same unfavorable provider.
                The new provider is chosen according to the function "chooseprovider" defined above.

            7. Stage: Reset providerweights and customer's period variables (money, income, revenue, prevenue,...)

            8. Stage: The provider get iterated (second part) using their method "iterate2"
    """

    # 1. Step: Create the agents
    for i in range(no_providers):
        Provider()
    for i in range(no_buyers):
        Buyer()
    for i in range(no_sellers):
        Seller()

    # 2. Step: setup global network externality provider choice functions
    global s_providerweights, b_providerweights
    s_providerweights = numpy.ones(len(providerlist))
    b_providerweights = numpy.ones(len(providerlist))

    # 3. Step: iteration through time
    global t
    for t in range(t_max):
        
        # stage 1: Transactions
        global transaction_counter
        transaction_counter = 0
        for cus in customerlist:
            cus.update_reservation_price()
        for i in range(no_transactions_per_iteration):
            transaction()
        
        # Stage 2: Customers pay their fees
        for cus in customerlist:
            for pindex in range(len(cus.providers)):
                if cus.buyer:
                    cus.money -= cus.providers[pindex].entryfee_b
                    cus.prevenue[pindex] -= cus.providers[pindex].entryfee_b
                    cus.providers[pindex].revenue += cus.providers[pindex].entryfee_b
                else:
                    cus.money -= cus.providers[pindex].entryfee_s
                    cus.providers[pindex].revenue += cus.providers[pindex].entryfee_s
                    cus.prevenue[pindex] -= cus.providers[pindex].entryfee_s
        
        # Stage 3: The provicers get iterated (first part)
        for i in range(len(providerlist)):
            providerlist[i].iterate1()
        
        # Stage 4: Evaluation and data collection
        evaluate(t)
        write_output(output_filename)
        
        # Stage 0 + 4.5j: Graphical output
        if graphical_output and (t % 20 == 0 or t == t_max-1):	#only if graphical_output == True and only every few periods
            isLast = False
            if t == t_max - 1:
                isLast = True
            draw(isLast, 20)
        
        # Stage 5: Unsubscription decisions of the customers and adjustment of providers' network weights
        for cus in customerlist:
            if not cus.prevenue == []:
                maxprev = max(max(cus.prevenue), 0.0)
            cusremovelist = []

            for i in range(len(cus.prevenue)):
                if cus.prevenue[i] < maxprev/2:
                    cusremovelist.append(cus.providers[i])

            for i in range(len(cus.prevenue)):
                if cus.prevenue[i] == maxprev:  # if this subscription is among the ones with maximum revenue
                    if cus.buyer:               # increase the weight of this provider
                        b_providerweights[providerlist.index(cus.providers[i])] += 1
                    else:
                        s_providerweights[providerlist.index(cus.providers[i])] += 1

            # Final unsubscription from providers in cusremovelist
            for removep in cusremovelist:
                cus.providers.remove(removep)
                removep.customer_no -= 1
                if cus.buyer:
                    removep.buyer_no -= 1
                else:
                    removep.seller_no -= 1

        # Renormalize providerweights for both network externality functions
        providerweightsum = sum(b_providerweights)
        b_providerweights /= providerweightsum
        providerweightsum = sum(s_providerweights)
        s_providerweights /= providerweightsum

        # Stage 6: Subsciption decisions of the customers
        for cus in customerlist:
            if (cus.providers == [] and random.randint(0, 9) == 0) or (cus.money > threshold_level and
                                                                               len(cus.providers) < max_providers):
                newprovider = chooseprovider(cus.buyer, 1)
                if not newprovider in cus.providers:
                    cus.providers.append(newprovider)
                    newprovider.customer_no += 1
                    if cus.buyer:
                        newprovider.buyer_no += 1
                    else:
                        newprovider.seller_no += 1

        # Stage 7: Reset providerweights and customer's period variables (money, income, revenue, prevenue,...)
        b_providerweights = numpy.ones(len(providerlist))
        s_providerweights = numpy.ones(len(providerlist))
        for cus in customerlist:
            cus.money = 0
            cus.prevenue = []
            for i in range(len(cus.providers)):
                cus.prevenue.append(0)

        # Stage 8: Iterate the providers (second part)
        for i in range(len(providerlist)):
            providerlist[i].iterate2()

"""
The conditional block for the __main__ environment.
If the script is run externally then the function main() must be called directly.

This code block will handle all optional arguments:
    1. output filename
    2. provider strategy
    3. setting a fixed entry fee
    4. number of providers
    5. per customer fixed costs
    6. the number of buyers
    7. the number of iterations (defaults to 500 for RIL, 40 for RO if not present)
    7. if graphical output should be given (1 or 0 for True or False)
    8. run id
Agruments 2-7 overwrite global defaults. If a filename argument is present, this filename will be
used, otherwise, a filename is be compiled to reflect the arguments, and thus the setting of the 
simulation. It follows the pattern
  <RIL/RILS/RO> _p <Number of providers> [ _ef <fixed entry fee> ] [ _pcc <per customer costs>] _ run id
where the run id must is either empty or the one supplied in argument 8.

The code block will further handle the creation of the output directory if necessary. 
It then commences the simulation by calling main.
"""

if __name__ == "__main__":
    
    # handling optional arguments
    import sys
    output_filename_set = False
    fixed_entry_fee_set = False
    per_cust_f_cost_set = False
    run_id = '_'
    for arg in sys.argv[1:]:
        arg2 = arg.split("=")
        if arg2[0] == "filename":
            output_filename = arg2[1]
            output_filename_set = True
        elif arg2[0] == "strategy":
            provider_strategy = arg2[1]
            t_max = 500 if provider_strategy in ["RIL", "RILS"] else 40
            assert provider_strategy in ["RIL", "RILS", "RO"], "Wrong parameter format: strategy"
        elif arg2[0] == "fixedentryfee":
            try:
                init_buyer_subscription_fee = float(arg2[1])
                init_seller_subscription_fee = float(arg2[1])
                min_entryfee_s = float(arg2[1])
                min_entryfee_b = float(arg2[1])
                max_entryfee_s = float(arg2[1])
                max_entryfee_b = float(arg2[1])
                fixed_entry_fee_set = True
            except:
                assert False, "Wrong parameter format: initentryfee"
        elif arg2[0] == "providernum":
            try:
                no_providers = int(arg2[1])
                assert no_providers > 0, "Wrong parameter format: providernum"
            except:
                assert False, "Wrong parameter format: providernum"
        elif arg2[0] == "pcc":
            try:
                provider_fixed_cost_ps = float(arg2[1])
                provider_fixed_cost_pb = float(arg2[1])
                per_cust_f_cost_set = True
            except:
                assert False, "Wrong parameter format: pcc"
        elif arg2[0] == "nbuyers":
            try:
                no_buyers = int(arg2[1])
                no_transactions_per_iteration=int(30./12.*(no_buyers+no_sellers))
                assert no_buyers > 0
            except:
                assert False, "Wrong parameter format: nbuyers"
        elif arg2[0] == "tmax":
            try:
                t_max = int(arg2[1])
                assert t_max > 0
            except:
                assert False, "Wrong parameter format: tmax"
        elif arg2[0] == "runid":
                run_id += arg2[1]
        elif arg2[0] == "draw":
                if arg2[1] in ['1', 'True']:
                    graphical_output = True
                assert arg2[1] in ['0', '1', 'True', 'False']
        else: 
            print("Unrecognized argument: {0:s}".format(arg2[0]))
            exit(1)
    
    # compiling filename to reflect arguments
    if not output_filename_set:
        no_providers_str = str(no_providers)
        if len(no_providers_str) < 2:
            no_providers_str = '0' + no_providers_str
        output_filename = provider_strategy + '_p' + no_providers_str
        if fixed_entry_fee_set:
            if not init_buyer_subscription_fee < 0:
                output_filename += '_ef' + str(int(init_buyer_subscription_fee))
            else:
                output_filename += '_efm' + str(-1*int(init_buyer_subscription_fee))
        if per_cust_f_cost_set:
            if not provider_fixed_cost_ps < 0:
                output_filename += '_pcc' + str(int(provider_fixed_cost_ps))
            else:
                output_filename += '_pccm' + str(-1*int(provider_fixed_cost_ps))
        output_filename += run_id
    print("Output file will be output/" + output_filename + ".py")
    
    # create output directory if necessary
    import os
    if not os.path.isdir('output'):
        assert not os.path.exists('output'), "Cannot create output directory, a non-directory file of that name exists."
        os.system('mkdir output')
    
    # run
    main()
