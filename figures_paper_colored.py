"""
This file creates all the figures for the manuscript:
"Beyond Equilibrium: Revisiting Two-Sided Markets from an Agent-Based Modeling Perspective"
submitted to the International Journal of Computational Economics and Econometrics.

Authors: Torsten Heinrich and Claudius Graebner
Emails: torsten.heinrich@uni-bremen.de and graebnerc@uni-bremen.de

This script should be called after the simulation was run and the results were stored in a directory called "output".
The directory must be marked as a python package to allow the importing of the results. To this end, on must add an
init file into the directory.

One must also adjust the names of the output files according to the own choice. This can easily be done via the
"search and replace" command. In case you followed the suggested naming convention of the source file, you just need
to adjust the number of runs conducted.
"""
print('Start importing modules')
import numpy as np
import itertools


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('seaborn-white')             # 'viridis'   'grayscale'
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['image.cmap'] = 'viridis'
mpl.rcParams['image.interpolation'] = 'none'

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['figure.facecolor'] = 'white'

mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False

fig_dir = "../figures-colored/"
# mpl.rcParams.keys()


from output import RIL_p01_000 as RIL_p01_00
from output import RIL_p01_001 as RIL_p01_01
from output import RIL_p01_002 as RIL_p01_02
from output import RIL_p01_003 as RIL_p01_03
from output import RIL_p01_004 as RIL_p01_04
from output import RIL_p01_005 as RIL_p01_05
from output import RIL_p01_006 as RIL_p01_06
from output import RIL_p01_007 as RIL_p01_07
from output import RIL_p01_008 as RIL_p01_08
from output import RIL_p01_009 as RIL_p01_09
from output import RIL_p01_010 as RIL_p01_10
from output import RIL_p01_011 as RIL_p01_11
from output import RIL_p01_012 as RIL_p01_12
from output import RIL_p01_013 as RIL_p01_13
from output import RIL_p01_014 as RIL_p01_14
from output import RIL_p01_015 as RIL_p01_15
from output import RIL_p01_016 as RIL_p01_16
from output import RIL_p01_017 as RIL_p01_17
from output import RIL_p01_018 as RIL_p01_18
from output import RIL_p01_019 as RIL_p01_19
from output import RIL_p01_020 as RIL_p01_20
from output import RIL_p01_021 as RIL_p01_21
from output import RIL_p01_022 as RIL_p01_22
from output import RIL_p01_023 as RIL_p01_23
from output import RIL_p01_024 as RIL_p01_24
from output import RIL_p01_025 as RIL_p01_25
from output import RIL_p01_026 as RIL_p01_26
from output import RIL_p01_027 as RIL_p01_27
from output import RIL_p01_028 as RIL_p01_28
from output import RIL_p01_029 as RIL_p01_29
from output import RIL_p01_030 as RIL_p01_30
from output import RIL_p01_031 as RIL_p01_31
from output import RIL_p01_032 as RIL_p01_32
from output import RIL_p01_033 as RIL_p01_33
from output import RIL_p01_034 as RIL_p01_34
from output import RIL_p01_035 as RIL_p01_35
from output import RIL_p01_036 as RIL_p01_36
from output import RIL_p01_037 as RIL_p01_37
from output import RIL_p01_038 as RIL_p01_38
from output import RIL_p01_039 as RIL_p01_39
from output import RIL_p01_040 as RIL_p01_40
from output import RIL_p01_041 as RIL_p01_41
from output import RIL_p01_042 as RIL_p01_42
from output import RIL_p01_043 as RIL_p01_43
from output import RIL_p01_044 as RIL_p01_44
from output import RIL_p01_045 as RIL_p01_45
from output import RIL_p01_046 as RIL_p01_46
from output import RIL_p01_047 as RIL_p01_47
from output import RIL_p01_048 as RIL_p01_48
from output import RIL_p01_049 as RIL_p01_49
from output import RIL_p01_050 as RIL_p01_50
from output import RIL_p01_051 as RIL_p01_51
from output import RIL_p01_052 as RIL_p01_52
from output import RIL_p01_053 as RIL_p01_53
from output import RIL_p01_054 as RIL_p01_54
from output import RIL_p01_055 as RIL_p01_55
from output import RIL_p01_056 as RIL_p01_56
from output import RIL_p01_057 as RIL_p01_57
from output import RIL_p01_058 as RIL_p01_58
from output import RIL_p01_059 as RIL_p01_59
from output import RIL_p01_060 as RIL_p01_60
from output import RIL_p01_061 as RIL_p01_61
from output import RIL_p01_062 as RIL_p01_62
from output import RIL_p01_063 as RIL_p01_63
from output import RIL_p01_064 as RIL_p01_64
from output import RIL_p01_065 as RIL_p01_65
from output import RIL_p01_066 as RIL_p01_66
from output import RIL_p01_067 as RIL_p01_67
from output import RIL_p01_068 as RIL_p01_68
from output import RIL_p01_069 as RIL_p01_69
from output import RIL_p01_070 as RIL_p01_70
from output import RIL_p01_071 as RIL_p01_71
from output import RIL_p01_072 as RIL_p01_72
from output import RIL_p01_073 as RIL_p01_73
from output import RIL_p01_074 as RIL_p01_74
from output import RIL_p01_075 as RIL_p01_75
from output import RIL_p01_076 as RIL_p01_76
from output import RIL_p01_077 as RIL_p01_77
from output import RIL_p01_078 as RIL_p01_78
from output import RIL_p01_079 as RIL_p01_79
from output import RIL_p01_080 as RIL_p01_80
from output import RIL_p01_081 as RIL_p01_81
from output import RIL_p01_082 as RIL_p01_82
from output import RIL_p01_083 as RIL_p01_83
from output import RIL_p01_084 as RIL_p01_84
from output import RIL_p01_085 as RIL_p01_85
from output import RIL_p01_086 as RIL_p01_86
from output import RIL_p01_087 as RIL_p01_87
from output import RIL_p01_088 as RIL_p01_88
from output import RIL_p01_089 as RIL_p01_89
from output import RIL_p01_090 as RIL_p01_90
from output import RIL_p01_091 as RIL_p01_91
from output import RIL_p01_092 as RIL_p01_92
from output import RIL_p01_093 as RIL_p01_93
from output import RIL_p01_094 as RIL_p01_94
from output import RIL_p01_095 as RIL_p01_95
from output import RIL_p01_096 as RIL_p01_96
from output import RIL_p01_097 as RIL_p01_97
from output import RIL_p01_098 as RIL_p01_98
from output import RIL_p01_099 as RIL_p01_99
from output import RIL_p01_100 as RIL_p01_100
from output import RIL_p01_101 as RIL_p01_101
from output import RIL_p01_102 as RIL_p01_102
from output import RIL_p01_103 as RIL_p01_103
from output import RIL_p01_104 as RIL_p01_104
from output import RIL_p01_105 as RIL_p01_105
from output import RIL_p01_106 as RIL_p01_106
from output import RIL_p01_107 as RIL_p01_107
from output import RIL_p01_108 as RIL_p01_108
from output import RIL_p01_109 as RIL_p01_109
from output import RIL_p01_110 as RIL_p01_110
from output import RIL_p01_111 as RIL_p01_111
from output import RIL_p01_112 as RIL_p01_112
from output import RIL_p01_113 as RIL_p01_113
from output import RIL_p01_114 as RIL_p01_114
from output import RIL_p01_115 as RIL_p01_115
from output import RIL_p01_116 as RIL_p01_116
from output import RIL_p01_117 as RIL_p01_117
from output import RIL_p01_118 as RIL_p01_118
from output import RIL_p01_119 as RIL_p01_119
from output import RIL_p01_120 as RIL_p01_120
from output import RIL_p01_121 as RIL_p01_121
from output import RIL_p01_122 as RIL_p01_122
from output import RIL_p01_123 as RIL_p01_123
from output import RIL_p01_124 as RIL_p01_124
from output import RIL_p01_125 as RIL_p01_125
from output import RIL_p01_126 as RIL_p01_126
from output import RIL_p01_127 as RIL_p01_127
from output import RIL_p01_128 as RIL_p01_128
from output import RIL_p01_129 as RIL_p01_129
from output import RIL_p01_130 as RIL_p01_130
from output import RIL_p01_131 as RIL_p01_131
from output import RIL_p01_132 as RIL_p01_132
from output import RIL_p01_133 as RIL_p01_133
from output import RIL_p01_134 as RIL_p01_134
from output import RIL_p01_135 as RIL_p01_135
from output import RIL_p01_136 as RIL_p01_136
from output import RIL_p01_137 as RIL_p01_137
from output import RIL_p01_138 as RIL_p01_138
from output import RIL_p01_139 as RIL_p01_139
from output import RIL_p01_140 as RIL_p01_140
from output import RIL_p01_141 as RIL_p01_141
from output import RIL_p01_142 as RIL_p01_142
from output import RIL_p01_143 as RIL_p01_143
from output import RIL_p01_144 as RIL_p01_144
from output import RIL_p01_145 as RIL_p01_145
from output import RIL_p01_146 as RIL_p01_146
from output import RIL_p01_147 as RIL_p01_147
from output import RIL_p01_148 as RIL_p01_148
from output import RIL_p01_149 as RIL_p01_149
from output import RIL_p01_150 as RIL_p01_150
from output import RIL_p01_151 as RIL_p01_151
from output import RIL_p01_152 as RIL_p01_152
from output import RIL_p01_153 as RIL_p01_153
from output import RIL_p01_154 as RIL_p01_154
from output import RIL_p01_155 as RIL_p01_155
from output import RIL_p01_156 as RIL_p01_156
from output import RIL_p01_157 as RIL_p01_157
from output import RIL_p01_158 as RIL_p01_158
from output import RIL_p01_159 as RIL_p01_159
from output import RIL_p01_160 as RIL_p01_160
from output import RIL_p01_161 as RIL_p01_161
from output import RIL_p01_162 as RIL_p01_162
from output import RIL_p01_163 as RIL_p01_163
from output import RIL_p01_164 as RIL_p01_164
from output import RIL_p01_165 as RIL_p01_165
from output import RIL_p01_166 as RIL_p01_166
from output import RIL_p01_167 as RIL_p01_167
from output import RIL_p01_168 as RIL_p01_168
from output import RIL_p01_169 as RIL_p01_169
from output import RIL_p01_170 as RIL_p01_170
from output import RIL_p01_171 as RIL_p01_171
from output import RIL_p01_172 as RIL_p01_172
from output import RIL_p01_173 as RIL_p01_173
from output import RIL_p01_174 as RIL_p01_174
from output import RIL_p01_175 as RIL_p01_175
from output import RIL_p01_176 as RIL_p01_176
from output import RIL_p01_177 as RIL_p01_177
from output import RIL_p01_178 as RIL_p01_178
from output import RIL_p01_179 as RIL_p01_179
from output import RIL_p01_180 as RIL_p01_180
from output import RIL_p01_181 as RIL_p01_181
from output import RIL_p01_182 as RIL_p01_182
from output import RIL_p01_183 as RIL_p01_183
from output import RIL_p01_184 as RIL_p01_184
from output import RIL_p01_185 as RIL_p01_185
from output import RIL_p01_186 as RIL_p01_186
from output import RIL_p01_187 as RIL_p01_187
from output import RIL_p01_188 as RIL_p01_188
from output import RIL_p01_189 as RIL_p01_189
from output import RIL_p01_190 as RIL_p01_190
from output import RIL_p01_191 as RIL_p01_191
from output import RIL_p01_192 as RIL_p01_192
from output import RIL_p01_193 as RIL_p01_193
from output import RIL_p01_194 as RIL_p01_194
from output import RIL_p01_195 as RIL_p01_195
from output import RIL_p01_196 as RIL_p01_196
from output import RIL_p01_197 as RIL_p01_197
from output import RIL_p01_198 as RIL_p01_198
from output import RIL_p01_199 as RIL_p01_199
from output import RIL_p10_000 as RIL_p10_00
from output import RIL_p10_001 as RIL_p10_01
from output import RIL_p10_002 as RIL_p10_02
from output import RIL_p10_003 as RIL_p10_03
from output import RIL_p10_004 as RIL_p10_04
from output import RIL_p10_005 as RIL_p10_05
from output import RIL_p10_006 as RIL_p10_06
from output import RIL_p10_007 as RIL_p10_07
from output import RIL_p10_008 as RIL_p10_08
from output import RIL_p10_009 as RIL_p10_09
from output import RIL_p10_010 as RIL_p10_10
from output import RIL_p10_011 as RIL_p10_11
from output import RIL_p10_012 as RIL_p10_12
from output import RIL_p10_013 as RIL_p10_13
from output import RIL_p10_014 as RIL_p10_14
from output import RIL_p10_015 as RIL_p10_15
from output import RIL_p10_016 as RIL_p10_16
from output import RIL_p10_017 as RIL_p10_17
from output import RIL_p10_018 as RIL_p10_18
from output import RIL_p10_019 as RIL_p10_19
from output import RIL_p10_020 as RIL_p10_20
from output import RIL_p10_021 as RIL_p10_21
from output import RIL_p10_022 as RIL_p10_22
from output import RIL_p10_023 as RIL_p10_23
from output import RIL_p10_024 as RIL_p10_24
from output import RIL_p10_025 as RIL_p10_25
from output import RIL_p10_026 as RIL_p10_26
from output import RIL_p10_027 as RIL_p10_27
from output import RIL_p10_028 as RIL_p10_28
from output import RIL_p10_029 as RIL_p10_29
from output import RIL_p10_030 as RIL_p10_30
from output import RIL_p10_031 as RIL_p10_31
from output import RIL_p10_032 as RIL_p10_32
from output import RIL_p10_033 as RIL_p10_33
from output import RIL_p10_034 as RIL_p10_34
from output import RIL_p10_035 as RIL_p10_35
from output import RIL_p10_036 as RIL_p10_36
from output import RIL_p10_037 as RIL_p10_37
from output import RIL_p10_038 as RIL_p10_38
from output import RIL_p10_039 as RIL_p10_39
from output import RIL_p10_040 as RIL_p10_40
from output import RIL_p10_041 as RIL_p10_41
from output import RIL_p10_042 as RIL_p10_42
from output import RIL_p10_043 as RIL_p10_43
from output import RIL_p10_044 as RIL_p10_44
from output import RIL_p10_045 as RIL_p10_45
from output import RIL_p10_046 as RIL_p10_46
from output import RIL_p10_047 as RIL_p10_47
from output import RIL_p10_048 as RIL_p10_48
from output import RIL_p10_049 as RIL_p10_49
from output import RIL_p10_050 as RIL_p10_50
from output import RIL_p10_051 as RIL_p10_51
from output import RIL_p10_052 as RIL_p10_52
from output import RIL_p10_053 as RIL_p10_53
from output import RIL_p10_054 as RIL_p10_54
from output import RIL_p10_055 as RIL_p10_55
from output import RIL_p10_056 as RIL_p10_56
from output import RIL_p10_057 as RIL_p10_57
from output import RIL_p10_058 as RIL_p10_58
from output import RIL_p10_059 as RIL_p10_59
from output import RIL_p10_060 as RIL_p10_60
from output import RIL_p10_061 as RIL_p10_61
from output import RIL_p10_062 as RIL_p10_62
from output import RIL_p10_063 as RIL_p10_63
from output import RIL_p10_064 as RIL_p10_64
from output import RIL_p10_065 as RIL_p10_65
from output import RIL_p10_066 as RIL_p10_66
from output import RIL_p10_067 as RIL_p10_67
from output import RIL_p10_068 as RIL_p10_68
from output import RIL_p10_069 as RIL_p10_69
from output import RIL_p10_070 as RIL_p10_70
from output import RIL_p10_071 as RIL_p10_71
from output import RIL_p10_072 as RIL_p10_72
from output import RIL_p10_073 as RIL_p10_73
from output import RIL_p10_074 as RIL_p10_74
from output import RIL_p10_075 as RIL_p10_75
from output import RIL_p10_076 as RIL_p10_76
from output import RIL_p10_077 as RIL_p10_77
from output import RIL_p10_078 as RIL_p10_78
from output import RIL_p10_079 as RIL_p10_79
from output import RIL_p10_080 as RIL_p10_80
from output import RIL_p10_081 as RIL_p10_81
from output import RIL_p10_082 as RIL_p10_82
from output import RIL_p10_083 as RIL_p10_83
from output import RIL_p10_084 as RIL_p10_84
from output import RIL_p10_085 as RIL_p10_85
from output import RIL_p10_086 as RIL_p10_86
from output import RIL_p10_087 as RIL_p10_87
from output import RIL_p10_088 as RIL_p10_88
from output import RIL_p10_089 as RIL_p10_89
from output import RIL_p10_090 as RIL_p10_90
from output import RIL_p10_091 as RIL_p10_91
from output import RIL_p10_092 as RIL_p10_92
from output import RIL_p10_093 as RIL_p10_93
from output import RIL_p10_094 as RIL_p10_94
from output import RIL_p10_095 as RIL_p10_95
from output import RIL_p10_096 as RIL_p10_96
from output import RIL_p10_097 as RIL_p10_97
from output import RIL_p10_098 as RIL_p10_98
from output import RIL_p10_099 as RIL_p10_99
from output import RIL_p10_100 as RIL_p10_100
from output import RIL_p10_101 as RIL_p10_101
from output import RIL_p10_102 as RIL_p10_102
from output import RIL_p10_103 as RIL_p10_103
from output import RIL_p10_104 as RIL_p10_104
from output import RIL_p10_105 as RIL_p10_105
from output import RIL_p10_106 as RIL_p10_106
from output import RIL_p10_107 as RIL_p10_107
from output import RIL_p10_108 as RIL_p10_108
from output import RIL_p10_109 as RIL_p10_109
from output import RIL_p10_110 as RIL_p10_110
from output import RIL_p10_111 as RIL_p10_111
from output import RIL_p10_112 as RIL_p10_112
from output import RIL_p10_113 as RIL_p10_113
from output import RIL_p10_114 as RIL_p10_114
from output import RIL_p10_115 as RIL_p10_115
from output import RIL_p10_116 as RIL_p10_116
from output import RIL_p10_117 as RIL_p10_117
from output import RIL_p10_118 as RIL_p10_118
from output import RIL_p10_119 as RIL_p10_119
from output import RIL_p10_120 as RIL_p10_120
from output import RIL_p10_121 as RIL_p10_121
from output import RIL_p10_122 as RIL_p10_122
from output import RIL_p10_123 as RIL_p10_123
from output import RIL_p10_124 as RIL_p10_124
from output import RIL_p10_125 as RIL_p10_125
from output import RIL_p10_126 as RIL_p10_126
from output import RIL_p10_127 as RIL_p10_127
from output import RIL_p10_128 as RIL_p10_128
from output import RIL_p10_129 as RIL_p10_129
from output import RIL_p10_130 as RIL_p10_130
from output import RIL_p10_131 as RIL_p10_131
from output import RIL_p10_132 as RIL_p10_132
from output import RIL_p10_133 as RIL_p10_133
from output import RIL_p10_134 as RIL_p10_134
from output import RIL_p10_135 as RIL_p10_135
from output import RIL_p10_136 as RIL_p10_136
from output import RIL_p10_137 as RIL_p10_137
from output import RIL_p10_138 as RIL_p10_138
from output import RIL_p10_139 as RIL_p10_139
from output import RIL_p10_140 as RIL_p10_140
from output import RIL_p10_141 as RIL_p10_141
from output import RIL_p10_142 as RIL_p10_142
from output import RIL_p10_143 as RIL_p10_143
from output import RIL_p10_144 as RIL_p10_144
from output import RIL_p10_145 as RIL_p10_145
from output import RIL_p10_146 as RIL_p10_146
from output import RIL_p10_147 as RIL_p10_147
from output import RIL_p10_148 as RIL_p10_148
from output import RIL_p10_149 as RIL_p10_149
from output import RIL_p10_150 as RIL_p10_150
from output import RIL_p10_151 as RIL_p10_151
from output import RIL_p10_152 as RIL_p10_152
from output import RIL_p10_153 as RIL_p10_153
from output import RIL_p10_154 as RIL_p10_154
from output import RIL_p10_155 as RIL_p10_155
from output import RIL_p10_156 as RIL_p10_156
from output import RIL_p10_157 as RIL_p10_157
from output import RIL_p10_158 as RIL_p10_158
from output import RIL_p10_159 as RIL_p10_159
from output import RIL_p10_160 as RIL_p10_160
from output import RIL_p10_161 as RIL_p10_161
from output import RIL_p10_162 as RIL_p10_162
from output import RIL_p10_163 as RIL_p10_163
from output import RIL_p10_164 as RIL_p10_164
from output import RIL_p10_165 as RIL_p10_165
from output import RIL_p10_166 as RIL_p10_166
from output import RIL_p10_167 as RIL_p10_167
from output import RIL_p10_168 as RIL_p10_168
from output import RIL_p10_169 as RIL_p10_169
from output import RIL_p10_170 as RIL_p10_170
from output import RIL_p10_171 as RIL_p10_171
from output import RIL_p10_172 as RIL_p10_172
from output import RIL_p10_173 as RIL_p10_173
from output import RIL_p10_174 as RIL_p10_174
from output import RIL_p10_175 as RIL_p10_175
from output import RIL_p10_176 as RIL_p10_176
from output import RIL_p10_177 as RIL_p10_177
from output import RIL_p10_178 as RIL_p10_178
from output import RIL_p10_179 as RIL_p10_179
from output import RIL_p10_180 as RIL_p10_180
from output import RIL_p10_181 as RIL_p10_181
from output import RIL_p10_182 as RIL_p10_182
from output import RIL_p10_183 as RIL_p10_183
from output import RIL_p10_184 as RIL_p10_184
from output import RIL_p10_185 as RIL_p10_185
from output import RIL_p10_186 as RIL_p10_186
from output import RIL_p10_187 as RIL_p10_187
from output import RIL_p10_188 as RIL_p10_188
from output import RIL_p10_189 as RIL_p10_189
from output import RIL_p10_190 as RIL_p10_190
from output import RIL_p10_191 as RIL_p10_191
from output import RIL_p10_192 as RIL_p10_192
from output import RIL_p10_193 as RIL_p10_193
from output import RIL_p10_194 as RIL_p10_194
from output import RIL_p10_195 as RIL_p10_195
from output import RIL_p10_196 as RIL_p10_196
from output import RIL_p10_197 as RIL_p10_197
from output import RIL_p10_198 as RIL_p10_198
from output import RIL_p10_199 as RIL_p10_199
from output import RILS_p01_000 as RILS_p01_00
from output import RILS_p01_001 as RILS_p01_01
from output import RILS_p01_002 as RILS_p01_02
from output import RILS_p01_003 as RILS_p01_03
from output import RILS_p01_004 as RILS_p01_04
from output import RILS_p01_005 as RILS_p01_05
from output import RILS_p01_006 as RILS_p01_06
from output import RILS_p01_007 as RILS_p01_07
from output import RILS_p01_008 as RILS_p01_08
from output import RILS_p01_009 as RILS_p01_09
from output import RILS_p01_010 as RILS_p01_10
from output import RILS_p01_011 as RILS_p01_11
from output import RILS_p01_012 as RILS_p01_12
from output import RILS_p01_013 as RILS_p01_13
from output import RILS_p01_014 as RILS_p01_14
from output import RILS_p01_015 as RILS_p01_15
from output import RILS_p01_016 as RILS_p01_16
from output import RILS_p01_017 as RILS_p01_17
from output import RILS_p01_018 as RILS_p01_18
from output import RILS_p01_019 as RILS_p01_19
from output import RILS_p01_020 as RILS_p01_20
from output import RILS_p01_021 as RILS_p01_21
from output import RILS_p01_022 as RILS_p01_22
from output import RILS_p01_023 as RILS_p01_23
from output import RILS_p01_024 as RILS_p01_24
from output import RILS_p01_025 as RILS_p01_25
from output import RILS_p01_026 as RILS_p01_26
from output import RILS_p01_027 as RILS_p01_27
from output import RILS_p01_028 as RILS_p01_28
from output import RILS_p01_029 as RILS_p01_29
from output import RILS_p01_030 as RILS_p01_30
from output import RILS_p01_031 as RILS_p01_31
from output import RILS_p01_032 as RILS_p01_32
from output import RILS_p01_033 as RILS_p01_33
from output import RILS_p01_034 as RILS_p01_34
from output import RILS_p01_035 as RILS_p01_35
from output import RILS_p01_036 as RILS_p01_36
from output import RILS_p01_037 as RILS_p01_37
from output import RILS_p01_038 as RILS_p01_38
from output import RILS_p01_039 as RILS_p01_39
from output import RILS_p01_040 as RILS_p01_40
from output import RILS_p01_041 as RILS_p01_41
from output import RILS_p01_042 as RILS_p01_42
from output import RILS_p01_043 as RILS_p01_43
from output import RILS_p01_044 as RILS_p01_44
from output import RILS_p01_045 as RILS_p01_45
from output import RILS_p01_046 as RILS_p01_46
from output import RILS_p01_047 as RILS_p01_47
from output import RILS_p01_048 as RILS_p01_48
from output import RILS_p01_049 as RILS_p01_49
from output import RILS_p01_050 as RILS_p01_50
from output import RILS_p01_051 as RILS_p01_51
from output import RILS_p01_052 as RILS_p01_52
from output import RILS_p01_053 as RILS_p01_53
from output import RILS_p01_054 as RILS_p01_54
from output import RILS_p01_055 as RILS_p01_55
from output import RILS_p01_056 as RILS_p01_56
from output import RILS_p01_057 as RILS_p01_57
from output import RILS_p01_058 as RILS_p01_58
from output import RILS_p01_059 as RILS_p01_59
from output import RILS_p01_060 as RILS_p01_60
from output import RILS_p01_061 as RILS_p01_61
from output import RILS_p01_062 as RILS_p01_62
from output import RILS_p01_063 as RILS_p01_63
from output import RILS_p01_064 as RILS_p01_64
from output import RILS_p01_065 as RILS_p01_65
from output import RILS_p01_066 as RILS_p01_66
from output import RILS_p01_067 as RILS_p01_67
from output import RILS_p01_068 as RILS_p01_68
from output import RILS_p01_069 as RILS_p01_69
from output import RILS_p01_070 as RILS_p01_70
from output import RILS_p01_071 as RILS_p01_71
from output import RILS_p01_072 as RILS_p01_72
from output import RILS_p01_073 as RILS_p01_73
from output import RILS_p01_074 as RILS_p01_74
from output import RILS_p01_075 as RILS_p01_75
from output import RILS_p01_076 as RILS_p01_76
from output import RILS_p01_077 as RILS_p01_77
from output import RILS_p01_078 as RILS_p01_78
from output import RILS_p01_079 as RILS_p01_79
from output import RILS_p01_080 as RILS_p01_80
from output import RILS_p01_081 as RILS_p01_81
from output import RILS_p01_082 as RILS_p01_82
from output import RILS_p01_083 as RILS_p01_83
from output import RILS_p01_084 as RILS_p01_84
from output import RILS_p01_085 as RILS_p01_85
from output import RILS_p01_086 as RILS_p01_86
from output import RILS_p01_087 as RILS_p01_87
from output import RILS_p01_088 as RILS_p01_88
from output import RILS_p01_089 as RILS_p01_89
from output import RILS_p01_090 as RILS_p01_90
from output import RILS_p01_091 as RILS_p01_91
from output import RILS_p01_092 as RILS_p01_92
from output import RILS_p01_093 as RILS_p01_93
from output import RILS_p01_094 as RILS_p01_94
from output import RILS_p01_095 as RILS_p01_95
from output import RILS_p01_096 as RILS_p01_96
from output import RILS_p01_097 as RILS_p01_97
from output import RILS_p01_098 as RILS_p01_98
from output import RILS_p01_099 as RILS_p01_99
from output import RILS_p01_100 as RILS_p01_100
from output import RILS_p01_101 as RILS_p01_101
from output import RILS_p01_102 as RILS_p01_102
from output import RILS_p01_103 as RILS_p01_103
from output import RILS_p01_104 as RILS_p01_104
from output import RILS_p01_105 as RILS_p01_105
from output import RILS_p01_106 as RILS_p01_106
from output import RILS_p01_107 as RILS_p01_107
from output import RILS_p01_108 as RILS_p01_108
from output import RILS_p01_109 as RILS_p01_109
from output import RILS_p01_110 as RILS_p01_110
from output import RILS_p01_111 as RILS_p01_111
from output import RILS_p01_112 as RILS_p01_112
from output import RILS_p01_113 as RILS_p01_113
from output import RILS_p01_114 as RILS_p01_114
from output import RILS_p01_115 as RILS_p01_115
from output import RILS_p01_116 as RILS_p01_116
from output import RILS_p01_117 as RILS_p01_117
from output import RILS_p01_118 as RILS_p01_118
from output import RILS_p01_119 as RILS_p01_119
from output import RILS_p01_120 as RILS_p01_120
from output import RILS_p01_121 as RILS_p01_121
from output import RILS_p01_122 as RILS_p01_122
from output import RILS_p01_123 as RILS_p01_123
from output import RILS_p01_124 as RILS_p01_124
from output import RILS_p01_125 as RILS_p01_125
from output import RILS_p01_126 as RILS_p01_126
from output import RILS_p01_127 as RILS_p01_127
from output import RILS_p01_128 as RILS_p01_128
from output import RILS_p01_129 as RILS_p01_129
from output import RILS_p01_130 as RILS_p01_130
from output import RILS_p01_131 as RILS_p01_131
from output import RILS_p01_132 as RILS_p01_132
from output import RILS_p01_133 as RILS_p01_133
from output import RILS_p01_134 as RILS_p01_134
from output import RILS_p01_135 as RILS_p01_135
from output import RILS_p01_136 as RILS_p01_136
from output import RILS_p01_137 as RILS_p01_137
from output import RILS_p01_138 as RILS_p01_138
from output import RILS_p01_139 as RILS_p01_139
from output import RILS_p01_140 as RILS_p01_140
from output import RILS_p01_141 as RILS_p01_141
from output import RILS_p01_142 as RILS_p01_142
from output import RILS_p01_143 as RILS_p01_143
from output import RILS_p01_144 as RILS_p01_144
from output import RILS_p01_145 as RILS_p01_145
from output import RILS_p01_146 as RILS_p01_146
from output import RILS_p01_147 as RILS_p01_147
from output import RILS_p01_148 as RILS_p01_148
from output import RILS_p01_149 as RILS_p01_149
from output import RILS_p01_150 as RILS_p01_150
from output import RILS_p01_151 as RILS_p01_151
from output import RILS_p01_152 as RILS_p01_152
from output import RILS_p01_153 as RILS_p01_153
from output import RILS_p01_154 as RILS_p01_154
from output import RILS_p01_155 as RILS_p01_155
from output import RILS_p01_156 as RILS_p01_156
from output import RILS_p01_157 as RILS_p01_157
from output import RILS_p01_158 as RILS_p01_158
from output import RILS_p01_159 as RILS_p01_159
from output import RILS_p01_160 as RILS_p01_160
from output import RILS_p01_161 as RILS_p01_161
from output import RILS_p01_162 as RILS_p01_162
from output import RILS_p01_163 as RILS_p01_163
from output import RILS_p01_164 as RILS_p01_164
from output import RILS_p01_165 as RILS_p01_165
from output import RILS_p01_166 as RILS_p01_166
from output import RILS_p01_167 as RILS_p01_167
from output import RILS_p01_168 as RILS_p01_168
from output import RILS_p01_169 as RILS_p01_169
from output import RILS_p01_170 as RILS_p01_170
from output import RILS_p01_171 as RILS_p01_171
from output import RILS_p01_172 as RILS_p01_172
from output import RILS_p01_173 as RILS_p01_173
from output import RILS_p01_174 as RILS_p01_174
from output import RILS_p01_175 as RILS_p01_175
from output import RILS_p01_176 as RILS_p01_176
from output import RILS_p01_177 as RILS_p01_177
from output import RILS_p01_178 as RILS_p01_178
from output import RILS_p01_179 as RILS_p01_179
from output import RILS_p01_180 as RILS_p01_180
from output import RILS_p01_181 as RILS_p01_181
from output import RILS_p01_182 as RILS_p01_182
from output import RILS_p01_183 as RILS_p01_183
from output import RILS_p01_184 as RILS_p01_184
from output import RILS_p01_185 as RILS_p01_185
from output import RILS_p01_186 as RILS_p01_186
from output import RILS_p01_187 as RILS_p01_187
from output import RILS_p01_188 as RILS_p01_188
from output import RILS_p01_189 as RILS_p01_189
from output import RILS_p01_190 as RILS_p01_190
from output import RILS_p01_191 as RILS_p01_191
from output import RILS_p01_192 as RILS_p01_192
from output import RILS_p01_193 as RILS_p01_193
from output import RILS_p01_194 as RILS_p01_194
from output import RILS_p01_195 as RILS_p01_195
from output import RILS_p01_196 as RILS_p01_196
from output import RILS_p01_197 as RILS_p01_197
from output import RILS_p01_198 as RILS_p01_198
from output import RILS_p01_199 as RILS_p01_199
from output import RILS_p10_000 as RILS_p10_00
from output import RILS_p10_001 as RILS_p10_01
from output import RILS_p10_002 as RILS_p10_02
from output import RILS_p10_003 as RILS_p10_03
from output import RILS_p10_004 as RILS_p10_04
from output import RILS_p10_005 as RILS_p10_05
from output import RILS_p10_006 as RILS_p10_06
from output import RILS_p10_007 as RILS_p10_07
from output import RILS_p10_008 as RILS_p10_08
from output import RILS_p10_009 as RILS_p10_09
from output import RILS_p10_010 as RILS_p10_10
from output import RILS_p10_011 as RILS_p10_11
from output import RILS_p10_012 as RILS_p10_12
from output import RILS_p10_013 as RILS_p10_13
from output import RILS_p10_014 as RILS_p10_14
from output import RILS_p10_015 as RILS_p10_15
from output import RILS_p10_016 as RILS_p10_16
from output import RILS_p10_017 as RILS_p10_17
from output import RILS_p10_018 as RILS_p10_18
from output import RILS_p10_019 as RILS_p10_19
from output import RILS_p10_020 as RILS_p10_20
from output import RILS_p10_021 as RILS_p10_21
from output import RILS_p10_022 as RILS_p10_22
from output import RILS_p10_023 as RILS_p10_23
from output import RILS_p10_024 as RILS_p10_24
from output import RILS_p10_025 as RILS_p10_25
from output import RILS_p10_026 as RILS_p10_26
from output import RILS_p10_027 as RILS_p10_27
from output import RILS_p10_028 as RILS_p10_28
from output import RILS_p10_029 as RILS_p10_29
from output import RILS_p10_030 as RILS_p10_30
from output import RILS_p10_031 as RILS_p10_31
from output import RILS_p10_032 as RILS_p10_32
from output import RILS_p10_033 as RILS_p10_33
from output import RILS_p10_034 as RILS_p10_34
from output import RILS_p10_035 as RILS_p10_35
from output import RILS_p10_036 as RILS_p10_36
from output import RILS_p10_037 as RILS_p10_37
from output import RILS_p10_038 as RILS_p10_38
from output import RILS_p10_039 as RILS_p10_39
from output import RILS_p10_040 as RILS_p10_40
from output import RILS_p10_041 as RILS_p10_41
from output import RILS_p10_042 as RILS_p10_42
from output import RILS_p10_043 as RILS_p10_43
from output import RILS_p10_044 as RILS_p10_44
from output import RILS_p10_045 as RILS_p10_45
from output import RILS_p10_046 as RILS_p10_46
from output import RILS_p10_047 as RILS_p10_47
from output import RILS_p10_048 as RILS_p10_48
from output import RILS_p10_049 as RILS_p10_49
from output import RILS_p10_050 as RILS_p10_50
from output import RILS_p10_051 as RILS_p10_51
from output import RILS_p10_052 as RILS_p10_52
from output import RILS_p10_053 as RILS_p10_53
from output import RILS_p10_054 as RILS_p10_54
from output import RILS_p10_055 as RILS_p10_55
from output import RILS_p10_056 as RILS_p10_56
from output import RILS_p10_057 as RILS_p10_57
from output import RILS_p10_058 as RILS_p10_58
from output import RILS_p10_059 as RILS_p10_59
from output import RILS_p10_060 as RILS_p10_60
from output import RILS_p10_061 as RILS_p10_61
from output import RILS_p10_062 as RILS_p10_62
from output import RILS_p10_063 as RILS_p10_63
from output import RILS_p10_064 as RILS_p10_64
from output import RILS_p10_065 as RILS_p10_65
from output import RILS_p10_066 as RILS_p10_66
from output import RILS_p10_067 as RILS_p10_67
from output import RILS_p10_068 as RILS_p10_68
from output import RILS_p10_069 as RILS_p10_69
from output import RILS_p10_070 as RILS_p10_70
from output import RILS_p10_071 as RILS_p10_71
from output import RILS_p10_072 as RILS_p10_72
from output import RILS_p10_073 as RILS_p10_73
from output import RILS_p10_074 as RILS_p10_74
from output import RILS_p10_075 as RILS_p10_75
from output import RILS_p10_076 as RILS_p10_76
from output import RILS_p10_077 as RILS_p10_77
from output import RILS_p10_078 as RILS_p10_78
from output import RILS_p10_079 as RILS_p10_79
from output import RILS_p10_080 as RILS_p10_80
from output import RILS_p10_081 as RILS_p10_81
from output import RILS_p10_082 as RILS_p10_82
from output import RILS_p10_083 as RILS_p10_83
from output import RILS_p10_084 as RILS_p10_84
from output import RILS_p10_085 as RILS_p10_85
from output import RILS_p10_086 as RILS_p10_86
from output import RILS_p10_087 as RILS_p10_87
from output import RILS_p10_088 as RILS_p10_88
from output import RILS_p10_089 as RILS_p10_89
from output import RILS_p10_090 as RILS_p10_90
from output import RILS_p10_091 as RILS_p10_91
from output import RILS_p10_092 as RILS_p10_92
from output import RILS_p10_093 as RILS_p10_93
from output import RILS_p10_094 as RILS_p10_94
from output import RILS_p10_095 as RILS_p10_95
from output import RILS_p10_096 as RILS_p10_96
from output import RILS_p10_097 as RILS_p10_97
from output import RILS_p10_098 as RILS_p10_98
from output import RILS_p10_099 as RILS_p10_99
from output import RILS_p10_100 as RILS_p10_100
from output import RILS_p10_101 as RILS_p10_101
from output import RILS_p10_102 as RILS_p10_102
from output import RILS_p10_103 as RILS_p10_103
from output import RILS_p10_104 as RILS_p10_104
from output import RILS_p10_105 as RILS_p10_105
from output import RILS_p10_106 as RILS_p10_106
from output import RILS_p10_107 as RILS_p10_107
from output import RILS_p10_108 as RILS_p10_108
from output import RILS_p10_109 as RILS_p10_109
from output import RILS_p10_110 as RILS_p10_110
from output import RILS_p10_111 as RILS_p10_111
from output import RILS_p10_112 as RILS_p10_112
from output import RILS_p10_113 as RILS_p10_113
from output import RILS_p10_114 as RILS_p10_114
from output import RILS_p10_115 as RILS_p10_115
from output import RILS_p10_116 as RILS_p10_116
from output import RILS_p10_117 as RILS_p10_117
from output import RILS_p10_118 as RILS_p10_118
from output import RILS_p10_119 as RILS_p10_119
from output import RILS_p10_120 as RILS_p10_120
from output import RILS_p10_121 as RILS_p10_121
from output import RILS_p10_122 as RILS_p10_122
from output import RILS_p10_123 as RILS_p10_123
from output import RILS_p10_124 as RILS_p10_124
from output import RILS_p10_125 as RILS_p10_125
from output import RILS_p10_126 as RILS_p10_126
from output import RILS_p10_127 as RILS_p10_127
from output import RILS_p10_128 as RILS_p10_128
from output import RILS_p10_129 as RILS_p10_129
from output import RILS_p10_130 as RILS_p10_130
from output import RILS_p10_131 as RILS_p10_131
from output import RILS_p10_132 as RILS_p10_132
from output import RILS_p10_133 as RILS_p10_133
from output import RILS_p10_134 as RILS_p10_134
from output import RILS_p10_135 as RILS_p10_135
from output import RILS_p10_136 as RILS_p10_136
from output import RILS_p10_137 as RILS_p10_137
from output import RILS_p10_138 as RILS_p10_138
from output import RILS_p10_139 as RILS_p10_139
from output import RILS_p10_140 as RILS_p10_140
from output import RILS_p10_141 as RILS_p10_141
from output import RILS_p10_142 as RILS_p10_142
from output import RILS_p10_143 as RILS_p10_143
from output import RILS_p10_144 as RILS_p10_144
from output import RILS_p10_145 as RILS_p10_145
from output import RILS_p10_146 as RILS_p10_146
from output import RILS_p10_147 as RILS_p10_147
from output import RILS_p10_148 as RILS_p10_148
from output import RILS_p10_149 as RILS_p10_149
from output import RILS_p10_150 as RILS_p10_150
from output import RILS_p10_151 as RILS_p10_151
from output import RILS_p10_152 as RILS_p10_152
from output import RILS_p10_153 as RILS_p10_153
from output import RILS_p10_154 as RILS_p10_154
from output import RILS_p10_155 as RILS_p10_155
from output import RILS_p10_156 as RILS_p10_156
from output import RILS_p10_157 as RILS_p10_157
from output import RILS_p10_158 as RILS_p10_158
from output import RILS_p10_159 as RILS_p10_159
from output import RILS_p10_160 as RILS_p10_160
from output import RILS_p10_161 as RILS_p10_161
from output import RILS_p10_162 as RILS_p10_162
from output import RILS_p10_163 as RILS_p10_163
from output import RILS_p10_164 as RILS_p10_164
from output import RILS_p10_165 as RILS_p10_165
from output import RILS_p10_166 as RILS_p10_166
from output import RILS_p10_167 as RILS_p10_167
from output import RILS_p10_168 as RILS_p10_168
from output import RILS_p10_169 as RILS_p10_169
from output import RILS_p10_170 as RILS_p10_170
from output import RILS_p10_171 as RILS_p10_171
from output import RILS_p10_172 as RILS_p10_172
from output import RILS_p10_173 as RILS_p10_173
from output import RILS_p10_174 as RILS_p10_174
from output import RILS_p10_175 as RILS_p10_175
from output import RILS_p10_176 as RILS_p10_176
from output import RILS_p10_177 as RILS_p10_177
from output import RILS_p10_178 as RILS_p10_178
from output import RILS_p10_179 as RILS_p10_179
from output import RILS_p10_180 as RILS_p10_180
from output import RILS_p10_181 as RILS_p10_181
from output import RILS_p10_182 as RILS_p10_182
from output import RILS_p10_183 as RILS_p10_183
from output import RILS_p10_184 as RILS_p10_184
from output import RILS_p10_185 as RILS_p10_185
from output import RILS_p10_186 as RILS_p10_186
from output import RILS_p10_187 as RILS_p10_187
from output import RILS_p10_188 as RILS_p10_188
from output import RILS_p10_189 as RILS_p10_189
from output import RILS_p10_190 as RILS_p10_190
from output import RILS_p10_191 as RILS_p10_191
from output import RILS_p10_192 as RILS_p10_192
from output import RILS_p10_193 as RILS_p10_193
from output import RILS_p10_194 as RILS_p10_194
from output import RILS_p10_195 as RILS_p10_195
from output import RILS_p10_196 as RILS_p10_196
from output import RILS_p10_197 as RILS_p10_197
from output import RILS_p10_198 as RILS_p10_198
from output import RILS_p10_199 as RILS_p10_199
from output import RILS_p10_pcc10_000 as RILS_p10_pcc10_00
from output import RILS_p10_pcc10_001 as RILS_p10_pcc10_01
from output import RILS_p10_pcc10_002 as RILS_p10_pcc10_02
from output import RILS_p10_pcc10_003 as RILS_p10_pcc10_03
from output import RILS_p10_pcc10_004 as RILS_p10_pcc10_04
from output import RILS_p10_pcc10_005 as RILS_p10_pcc10_05
from output import RILS_p10_pcc10_006 as RILS_p10_pcc10_06
from output import RILS_p10_pcc10_007 as RILS_p10_pcc10_07
from output import RILS_p10_pcc10_008 as RILS_p10_pcc10_08
from output import RILS_p10_pcc10_009 as RILS_p10_pcc10_09
from output import RILS_p10_pcc10_010 as RILS_p10_pcc10_10
from output import RILS_p10_pcc10_011 as RILS_p10_pcc10_11
from output import RILS_p10_pcc10_012 as RILS_p10_pcc10_12
from output import RILS_p10_pcc10_013 as RILS_p10_pcc10_13
from output import RILS_p10_pcc10_014 as RILS_p10_pcc10_14
from output import RILS_p10_pcc10_015 as RILS_p10_pcc10_15
from output import RILS_p10_pcc10_016 as RILS_p10_pcc10_16
from output import RILS_p10_pcc10_017 as RILS_p10_pcc10_17
from output import RILS_p10_pcc10_018 as RILS_p10_pcc10_18
from output import RILS_p10_pcc10_019 as RILS_p10_pcc10_19
from output import RILS_p10_pcc10_020 as RILS_p10_pcc10_20
from output import RILS_p10_pcc10_021 as RILS_p10_pcc10_21
from output import RILS_p10_pcc10_022 as RILS_p10_pcc10_22
from output import RILS_p10_pcc10_023 as RILS_p10_pcc10_23
from output import RILS_p10_pcc10_024 as RILS_p10_pcc10_24
from output import RILS_p10_pcc10_025 as RILS_p10_pcc10_25
from output import RILS_p10_pcc10_026 as RILS_p10_pcc10_26
from output import RILS_p10_pcc10_027 as RILS_p10_pcc10_27
from output import RILS_p10_pcc10_028 as RILS_p10_pcc10_28
from output import RILS_p10_pcc10_029 as RILS_p10_pcc10_29
from output import RILS_p10_pcc10_030 as RILS_p10_pcc10_30
from output import RILS_p10_pcc10_031 as RILS_p10_pcc10_31
from output import RILS_p10_pcc10_032 as RILS_p10_pcc10_32
from output import RILS_p10_pcc10_033 as RILS_p10_pcc10_33
from output import RILS_p10_pcc10_034 as RILS_p10_pcc10_34
from output import RILS_p10_pcc10_035 as RILS_p10_pcc10_35
from output import RILS_p10_pcc10_036 as RILS_p10_pcc10_36
from output import RILS_p10_pcc10_037 as RILS_p10_pcc10_37
from output import RILS_p10_pcc10_038 as RILS_p10_pcc10_38
from output import RILS_p10_pcc10_039 as RILS_p10_pcc10_39
from output import RILS_p10_pcc10_040 as RILS_p10_pcc10_40
from output import RILS_p10_pcc10_041 as RILS_p10_pcc10_41
from output import RILS_p10_pcc10_042 as RILS_p10_pcc10_42
from output import RILS_p10_pcc10_043 as RILS_p10_pcc10_43
from output import RILS_p10_pcc10_044 as RILS_p10_pcc10_44
from output import RILS_p10_pcc10_045 as RILS_p10_pcc10_45
from output import RILS_p10_pcc10_046 as RILS_p10_pcc10_46
from output import RILS_p10_pcc10_047 as RILS_p10_pcc10_47
from output import RILS_p10_pcc10_048 as RILS_p10_pcc10_48
from output import RILS_p10_pcc10_049 as RILS_p10_pcc10_49
from output import RILS_p10_pcc10_050 as RILS_p10_pcc10_50
from output import RILS_p10_pcc10_051 as RILS_p10_pcc10_51
from output import RILS_p10_pcc10_052 as RILS_p10_pcc10_52
from output import RILS_p10_pcc10_053 as RILS_p10_pcc10_53
from output import RILS_p10_pcc10_054 as RILS_p10_pcc10_54
from output import RILS_p10_pcc10_055 as RILS_p10_pcc10_55
from output import RILS_p10_pcc10_056 as RILS_p10_pcc10_56
from output import RILS_p10_pcc10_057 as RILS_p10_pcc10_57
from output import RILS_p10_pcc10_058 as RILS_p10_pcc10_58
from output import RILS_p10_pcc10_059 as RILS_p10_pcc10_59
from output import RILS_p10_pcc10_060 as RILS_p10_pcc10_60
from output import RILS_p10_pcc10_061 as RILS_p10_pcc10_61
from output import RILS_p10_pcc10_062 as RILS_p10_pcc10_62
from output import RILS_p10_pcc10_063 as RILS_p10_pcc10_63
from output import RILS_p10_pcc10_064 as RILS_p10_pcc10_64
from output import RILS_p10_pcc10_065 as RILS_p10_pcc10_65
from output import RILS_p10_pcc10_066 as RILS_p10_pcc10_66
from output import RILS_p10_pcc10_067 as RILS_p10_pcc10_67
from output import RILS_p10_pcc10_068 as RILS_p10_pcc10_68
from output import RILS_p10_pcc10_069 as RILS_p10_pcc10_69
from output import RILS_p10_pcc10_070 as RILS_p10_pcc10_70
from output import RILS_p10_pcc10_071 as RILS_p10_pcc10_71
from output import RILS_p10_pcc10_072 as RILS_p10_pcc10_72
from output import RILS_p10_pcc10_073 as RILS_p10_pcc10_73
from output import RILS_p10_pcc10_074 as RILS_p10_pcc10_74
from output import RILS_p10_pcc10_075 as RILS_p10_pcc10_75
from output import RILS_p10_pcc10_076 as RILS_p10_pcc10_76
from output import RILS_p10_pcc10_077 as RILS_p10_pcc10_77
from output import RILS_p10_pcc10_078 as RILS_p10_pcc10_78
from output import RILS_p10_pcc10_079 as RILS_p10_pcc10_79
from output import RILS_p10_pcc10_080 as RILS_p10_pcc10_80
from output import RILS_p10_pcc10_081 as RILS_p10_pcc10_81
from output import RILS_p10_pcc10_082 as RILS_p10_pcc10_82
from output import RILS_p10_pcc10_083 as RILS_p10_pcc10_83
from output import RILS_p10_pcc10_084 as RILS_p10_pcc10_84
from output import RILS_p10_pcc10_085 as RILS_p10_pcc10_85
from output import RILS_p10_pcc10_086 as RILS_p10_pcc10_86
from output import RILS_p10_pcc10_087 as RILS_p10_pcc10_87
from output import RILS_p10_pcc10_088 as RILS_p10_pcc10_88
from output import RILS_p10_pcc10_089 as RILS_p10_pcc10_89
from output import RILS_p10_pcc10_090 as RILS_p10_pcc10_90
from output import RILS_p10_pcc10_091 as RILS_p10_pcc10_91
from output import RILS_p10_pcc10_092 as RILS_p10_pcc10_92
from output import RILS_p10_pcc10_093 as RILS_p10_pcc10_93
from output import RILS_p10_pcc10_094 as RILS_p10_pcc10_94
from output import RILS_p10_pcc10_095 as RILS_p10_pcc10_95
from output import RILS_p10_pcc10_096 as RILS_p10_pcc10_96
from output import RILS_p10_pcc10_097 as RILS_p10_pcc10_97
from output import RILS_p10_pcc10_098 as RILS_p10_pcc10_98
from output import RILS_p10_pcc10_099 as RILS_p10_pcc10_99
from output import RILS_p10_pcc10_100 as RILS_p10_pcc10_100
from output import RILS_p10_pcc10_101 as RILS_p10_pcc10_101
from output import RILS_p10_pcc10_102 as RILS_p10_pcc10_102
from output import RILS_p10_pcc10_103 as RILS_p10_pcc10_103
from output import RILS_p10_pcc10_104 as RILS_p10_pcc10_104
from output import RILS_p10_pcc10_105 as RILS_p10_pcc10_105
from output import RILS_p10_pcc10_106 as RILS_p10_pcc10_106
from output import RILS_p10_pcc10_107 as RILS_p10_pcc10_107
from output import RILS_p10_pcc10_108 as RILS_p10_pcc10_108
from output import RILS_p10_pcc10_109 as RILS_p10_pcc10_109
from output import RILS_p10_pcc10_110 as RILS_p10_pcc10_110
from output import RILS_p10_pcc10_111 as RILS_p10_pcc10_111
from output import RILS_p10_pcc10_112 as RILS_p10_pcc10_112
from output import RILS_p10_pcc10_113 as RILS_p10_pcc10_113
from output import RILS_p10_pcc10_114 as RILS_p10_pcc10_114
from output import RILS_p10_pcc10_115 as RILS_p10_pcc10_115
from output import RILS_p10_pcc10_116 as RILS_p10_pcc10_116
from output import RILS_p10_pcc10_117 as RILS_p10_pcc10_117
from output import RILS_p10_pcc10_118 as RILS_p10_pcc10_118
from output import RILS_p10_pcc10_119 as RILS_p10_pcc10_119
from output import RILS_p10_pcc10_120 as RILS_p10_pcc10_120
from output import RILS_p10_pcc10_121 as RILS_p10_pcc10_121
from output import RILS_p10_pcc10_122 as RILS_p10_pcc10_122
from output import RILS_p10_pcc10_123 as RILS_p10_pcc10_123
from output import RILS_p10_pcc10_124 as RILS_p10_pcc10_124
from output import RILS_p10_pcc10_125 as RILS_p10_pcc10_125
from output import RILS_p10_pcc10_126 as RILS_p10_pcc10_126
from output import RILS_p10_pcc10_127 as RILS_p10_pcc10_127
from output import RILS_p10_pcc10_128 as RILS_p10_pcc10_128
from output import RILS_p10_pcc10_129 as RILS_p10_pcc10_129
from output import RILS_p10_pcc10_130 as RILS_p10_pcc10_130
from output import RILS_p10_pcc10_131 as RILS_p10_pcc10_131
from output import RILS_p10_pcc10_132 as RILS_p10_pcc10_132
from output import RILS_p10_pcc10_133 as RILS_p10_pcc10_133
from output import RILS_p10_pcc10_134 as RILS_p10_pcc10_134
from output import RILS_p10_pcc10_135 as RILS_p10_pcc10_135
from output import RILS_p10_pcc10_136 as RILS_p10_pcc10_136
from output import RILS_p10_pcc10_137 as RILS_p10_pcc10_137
from output import RILS_p10_pcc10_138 as RILS_p10_pcc10_138
from output import RILS_p10_pcc10_139 as RILS_p10_pcc10_139
from output import RILS_p10_pcc10_140 as RILS_p10_pcc10_140
from output import RILS_p10_pcc10_141 as RILS_p10_pcc10_141
from output import RILS_p10_pcc10_142 as RILS_p10_pcc10_142
from output import RILS_p10_pcc10_143 as RILS_p10_pcc10_143
from output import RILS_p10_pcc10_144 as RILS_p10_pcc10_144
from output import RILS_p10_pcc10_145 as RILS_p10_pcc10_145
from output import RILS_p10_pcc10_146 as RILS_p10_pcc10_146
from output import RILS_p10_pcc10_147 as RILS_p10_pcc10_147
from output import RILS_p10_pcc10_148 as RILS_p10_pcc10_148
from output import RILS_p10_pcc10_149 as RILS_p10_pcc10_149
from output import RILS_p10_pcc10_150 as RILS_p10_pcc10_150
from output import RILS_p10_pcc10_151 as RILS_p10_pcc10_151
from output import RILS_p10_pcc10_152 as RILS_p10_pcc10_152
from output import RILS_p10_pcc10_153 as RILS_p10_pcc10_153
from output import RILS_p10_pcc10_154 as RILS_p10_pcc10_154
from output import RILS_p10_pcc10_155 as RILS_p10_pcc10_155
from output import RILS_p10_pcc10_156 as RILS_p10_pcc10_156
from output import RILS_p10_pcc10_157 as RILS_p10_pcc10_157
from output import RILS_p10_pcc10_158 as RILS_p10_pcc10_158
from output import RILS_p10_pcc10_159 as RILS_p10_pcc10_159
from output import RILS_p10_pcc10_160 as RILS_p10_pcc10_160
from output import RILS_p10_pcc10_161 as RILS_p10_pcc10_161
from output import RILS_p10_pcc10_162 as RILS_p10_pcc10_162
from output import RILS_p10_pcc10_163 as RILS_p10_pcc10_163
from output import RILS_p10_pcc10_164 as RILS_p10_pcc10_164
from output import RILS_p10_pcc10_165 as RILS_p10_pcc10_165
from output import RILS_p10_pcc10_166 as RILS_p10_pcc10_166
from output import RILS_p10_pcc10_167 as RILS_p10_pcc10_167
from output import RILS_p10_pcc10_168 as RILS_p10_pcc10_168
from output import RILS_p10_pcc10_169 as RILS_p10_pcc10_169
from output import RILS_p10_pcc10_170 as RILS_p10_pcc10_170
from output import RILS_p10_pcc10_171 as RILS_p10_pcc10_171
from output import RILS_p10_pcc10_172 as RILS_p10_pcc10_172
from output import RILS_p10_pcc10_173 as RILS_p10_pcc10_173
from output import RILS_p10_pcc10_174 as RILS_p10_pcc10_174
from output import RILS_p10_pcc10_175 as RILS_p10_pcc10_175
from output import RILS_p10_pcc10_176 as RILS_p10_pcc10_176
from output import RILS_p10_pcc10_177 as RILS_p10_pcc10_177
from output import RILS_p10_pcc10_178 as RILS_p10_pcc10_178
from output import RILS_p10_pcc10_179 as RILS_p10_pcc10_179
from output import RILS_p10_pcc10_180 as RILS_p10_pcc10_180
from output import RILS_p10_pcc10_181 as RILS_p10_pcc10_181
from output import RILS_p10_pcc10_182 as RILS_p10_pcc10_182
from output import RILS_p10_pcc10_183 as RILS_p10_pcc10_183
from output import RILS_p10_pcc10_184 as RILS_p10_pcc10_184
from output import RILS_p10_pcc10_185 as RILS_p10_pcc10_185
from output import RILS_p10_pcc10_186 as RILS_p10_pcc10_186
from output import RILS_p10_pcc10_187 as RILS_p10_pcc10_187
from output import RILS_p10_pcc10_188 as RILS_p10_pcc10_188
from output import RILS_p10_pcc10_189 as RILS_p10_pcc10_189
from output import RILS_p10_pcc10_190 as RILS_p10_pcc10_190
from output import RILS_p10_pcc10_191 as RILS_p10_pcc10_191
from output import RILS_p10_pcc10_192 as RILS_p10_pcc10_192
from output import RILS_p10_pcc10_193 as RILS_p10_pcc10_193
from output import RILS_p10_pcc10_194 as RILS_p10_pcc10_194
from output import RILS_p10_pcc10_195 as RILS_p10_pcc10_195
from output import RILS_p10_pcc10_196 as RILS_p10_pcc10_196
from output import RILS_p10_pcc10_197 as RILS_p10_pcc10_197
from output import RILS_p10_pcc10_198 as RILS_p10_pcc10_198
from output import RILS_p10_pcc10_199 as RILS_p10_pcc10_199
from output import RILS_p10_pcc0_000 as RILS_p10_pcc0_00
from output import RILS_p10_pcc0_001 as RILS_p10_pcc0_01
from output import RILS_p10_pcc0_002 as RILS_p10_pcc0_02
from output import RILS_p10_pcc0_003 as RILS_p10_pcc0_03
from output import RILS_p10_pcc0_004 as RILS_p10_pcc0_04
from output import RILS_p10_pcc0_005 as RILS_p10_pcc0_05
from output import RILS_p10_pcc0_006 as RILS_p10_pcc0_06
from output import RILS_p10_pcc0_007 as RILS_p10_pcc0_07
from output import RILS_p10_pcc0_008 as RILS_p10_pcc0_08
from output import RILS_p10_pcc0_009 as RILS_p10_pcc0_09
from output import RILS_p10_pcc0_010 as RILS_p10_pcc0_10
from output import RILS_p10_pcc0_011 as RILS_p10_pcc0_11
from output import RILS_p10_pcc0_012 as RILS_p10_pcc0_12
from output import RILS_p10_pcc0_013 as RILS_p10_pcc0_13
from output import RILS_p10_pcc0_014 as RILS_p10_pcc0_14
from output import RILS_p10_pcc0_015 as RILS_p10_pcc0_15
from output import RILS_p10_pcc0_016 as RILS_p10_pcc0_16
from output import RILS_p10_pcc0_017 as RILS_p10_pcc0_17
from output import RILS_p10_pcc0_018 as RILS_p10_pcc0_18
from output import RILS_p10_pcc0_019 as RILS_p10_pcc0_19
from output import RILS_p10_pcc0_020 as RILS_p10_pcc0_20
from output import RILS_p10_pcc0_021 as RILS_p10_pcc0_21
from output import RILS_p10_pcc0_022 as RILS_p10_pcc0_22
from output import RILS_p10_pcc0_023 as RILS_p10_pcc0_23
from output import RILS_p10_pcc0_024 as RILS_p10_pcc0_24
from output import RILS_p10_pcc0_025 as RILS_p10_pcc0_25
from output import RILS_p10_pcc0_026 as RILS_p10_pcc0_26
from output import RILS_p10_pcc0_027 as RILS_p10_pcc0_27
from output import RILS_p10_pcc0_028 as RILS_p10_pcc0_28
from output import RILS_p10_pcc0_029 as RILS_p10_pcc0_29
from output import RILS_p10_pcc0_030 as RILS_p10_pcc0_30
from output import RILS_p10_pcc0_031 as RILS_p10_pcc0_31
from output import RILS_p10_pcc0_032 as RILS_p10_pcc0_32
from output import RILS_p10_pcc0_033 as RILS_p10_pcc0_33
from output import RILS_p10_pcc0_034 as RILS_p10_pcc0_34
from output import RILS_p10_pcc0_035 as RILS_p10_pcc0_35
from output import RILS_p10_pcc0_036 as RILS_p10_pcc0_36
from output import RILS_p10_pcc0_037 as RILS_p10_pcc0_37
from output import RILS_p10_pcc0_038 as RILS_p10_pcc0_38
from output import RILS_p10_pcc0_039 as RILS_p10_pcc0_39
from output import RILS_p10_pcc0_040 as RILS_p10_pcc0_40
from output import RILS_p10_pcc0_041 as RILS_p10_pcc0_41
from output import RILS_p10_pcc0_042 as RILS_p10_pcc0_42
from output import RILS_p10_pcc0_043 as RILS_p10_pcc0_43
from output import RILS_p10_pcc0_044 as RILS_p10_pcc0_44
from output import RILS_p10_pcc0_045 as RILS_p10_pcc0_45
from output import RILS_p10_pcc0_046 as RILS_p10_pcc0_46
from output import RILS_p10_pcc0_047 as RILS_p10_pcc0_47
from output import RILS_p10_pcc0_048 as RILS_p10_pcc0_48
from output import RILS_p10_pcc0_049 as RILS_p10_pcc0_49
from output import RILS_p10_pcc0_050 as RILS_p10_pcc0_50
from output import RILS_p10_pcc0_051 as RILS_p10_pcc0_51
from output import RILS_p10_pcc0_052 as RILS_p10_pcc0_52
from output import RILS_p10_pcc0_053 as RILS_p10_pcc0_53
from output import RILS_p10_pcc0_054 as RILS_p10_pcc0_54
from output import RILS_p10_pcc0_055 as RILS_p10_pcc0_55
from output import RILS_p10_pcc0_056 as RILS_p10_pcc0_56
from output import RILS_p10_pcc0_057 as RILS_p10_pcc0_57
from output import RILS_p10_pcc0_058 as RILS_p10_pcc0_58
from output import RILS_p10_pcc0_059 as RILS_p10_pcc0_59
from output import RILS_p10_pcc0_060 as RILS_p10_pcc0_60
from output import RILS_p10_pcc0_061 as RILS_p10_pcc0_61
from output import RILS_p10_pcc0_062 as RILS_p10_pcc0_62
from output import RILS_p10_pcc0_063 as RILS_p10_pcc0_63
from output import RILS_p10_pcc0_064 as RILS_p10_pcc0_64
from output import RILS_p10_pcc0_065 as RILS_p10_pcc0_65
from output import RILS_p10_pcc0_066 as RILS_p10_pcc0_66
from output import RILS_p10_pcc0_067 as RILS_p10_pcc0_67
from output import RILS_p10_pcc0_068 as RILS_p10_pcc0_68
from output import RILS_p10_pcc0_069 as RILS_p10_pcc0_69
from output import RILS_p10_pcc0_070 as RILS_p10_pcc0_70
from output import RILS_p10_pcc0_071 as RILS_p10_pcc0_71
from output import RILS_p10_pcc0_072 as RILS_p10_pcc0_72
from output import RILS_p10_pcc0_073 as RILS_p10_pcc0_73
from output import RILS_p10_pcc0_074 as RILS_p10_pcc0_74
from output import RILS_p10_pcc0_075 as RILS_p10_pcc0_75
from output import RILS_p10_pcc0_076 as RILS_p10_pcc0_76
from output import RILS_p10_pcc0_077 as RILS_p10_pcc0_77
from output import RILS_p10_pcc0_078 as RILS_p10_pcc0_78
from output import RILS_p10_pcc0_079 as RILS_p10_pcc0_79
from output import RILS_p10_pcc0_080 as RILS_p10_pcc0_80
from output import RILS_p10_pcc0_081 as RILS_p10_pcc0_81
from output import RILS_p10_pcc0_082 as RILS_p10_pcc0_82
from output import RILS_p10_pcc0_083 as RILS_p10_pcc0_83
from output import RILS_p10_pcc0_084 as RILS_p10_pcc0_84
from output import RILS_p10_pcc0_085 as RILS_p10_pcc0_85
from output import RILS_p10_pcc0_086 as RILS_p10_pcc0_86
from output import RILS_p10_pcc0_087 as RILS_p10_pcc0_87
from output import RILS_p10_pcc0_088 as RILS_p10_pcc0_88
from output import RILS_p10_pcc0_089 as RILS_p10_pcc0_89
from output import RILS_p10_pcc0_090 as RILS_p10_pcc0_90
from output import RILS_p10_pcc0_091 as RILS_p10_pcc0_91
from output import RILS_p10_pcc0_092 as RILS_p10_pcc0_92
from output import RILS_p10_pcc0_093 as RILS_p10_pcc0_93
from output import RILS_p10_pcc0_094 as RILS_p10_pcc0_94
from output import RILS_p10_pcc0_095 as RILS_p10_pcc0_95
from output import RILS_p10_pcc0_096 as RILS_p10_pcc0_96
from output import RILS_p10_pcc0_097 as RILS_p10_pcc0_97
from output import RILS_p10_pcc0_098 as RILS_p10_pcc0_98
from output import RILS_p10_pcc0_099 as RILS_p10_pcc0_99
from output import RILS_p10_pcc0_100 as RILS_p10_pcc0_100
from output import RILS_p10_pcc0_101 as RILS_p10_pcc0_101
from output import RILS_p10_pcc0_102 as RILS_p10_pcc0_102
from output import RILS_p10_pcc0_103 as RILS_p10_pcc0_103
from output import RILS_p10_pcc0_104 as RILS_p10_pcc0_104
from output import RILS_p10_pcc0_105 as RILS_p10_pcc0_105
from output import RILS_p10_pcc0_106 as RILS_p10_pcc0_106
from output import RILS_p10_pcc0_107 as RILS_p10_pcc0_107
from output import RILS_p10_pcc0_108 as RILS_p10_pcc0_108
from output import RILS_p10_pcc0_109 as RILS_p10_pcc0_109
from output import RILS_p10_pcc0_110 as RILS_p10_pcc0_110
from output import RILS_p10_pcc0_111 as RILS_p10_pcc0_111
from output import RILS_p10_pcc0_112 as RILS_p10_pcc0_112
from output import RILS_p10_pcc0_113 as RILS_p10_pcc0_113
from output import RILS_p10_pcc0_114 as RILS_p10_pcc0_114
from output import RILS_p10_pcc0_115 as RILS_p10_pcc0_115
from output import RILS_p10_pcc0_116 as RILS_p10_pcc0_116
from output import RILS_p10_pcc0_117 as RILS_p10_pcc0_117
from output import RILS_p10_pcc0_118 as RILS_p10_pcc0_118
from output import RILS_p10_pcc0_119 as RILS_p10_pcc0_119
from output import RILS_p10_pcc0_120 as RILS_p10_pcc0_120
from output import RILS_p10_pcc0_121 as RILS_p10_pcc0_121
from output import RILS_p10_pcc0_122 as RILS_p10_pcc0_122
from output import RILS_p10_pcc0_123 as RILS_p10_pcc0_123
from output import RILS_p10_pcc0_124 as RILS_p10_pcc0_124
from output import RILS_p10_pcc0_125 as RILS_p10_pcc0_125
from output import RILS_p10_pcc0_126 as RILS_p10_pcc0_126
from output import RILS_p10_pcc0_127 as RILS_p10_pcc0_127
from output import RILS_p10_pcc0_128 as RILS_p10_pcc0_128
from output import RILS_p10_pcc0_129 as RILS_p10_pcc0_129
from output import RILS_p10_pcc0_130 as RILS_p10_pcc0_130
from output import RILS_p10_pcc0_131 as RILS_p10_pcc0_131
from output import RILS_p10_pcc0_132 as RILS_p10_pcc0_132
from output import RILS_p10_pcc0_133 as RILS_p10_pcc0_133
from output import RILS_p10_pcc0_134 as RILS_p10_pcc0_134
from output import RILS_p10_pcc0_135 as RILS_p10_pcc0_135
from output import RILS_p10_pcc0_136 as RILS_p10_pcc0_136
from output import RILS_p10_pcc0_137 as RILS_p10_pcc0_137
from output import RILS_p10_pcc0_138 as RILS_p10_pcc0_138
from output import RILS_p10_pcc0_139 as RILS_p10_pcc0_139
from output import RILS_p10_pcc0_140 as RILS_p10_pcc0_140
from output import RILS_p10_pcc0_141 as RILS_p10_pcc0_141
from output import RILS_p10_pcc0_142 as RILS_p10_pcc0_142
from output import RILS_p10_pcc0_143 as RILS_p10_pcc0_143
from output import RILS_p10_pcc0_144 as RILS_p10_pcc0_144
from output import RILS_p10_pcc0_145 as RILS_p10_pcc0_145
from output import RILS_p10_pcc0_146 as RILS_p10_pcc0_146
from output import RILS_p10_pcc0_147 as RILS_p10_pcc0_147
from output import RILS_p10_pcc0_148 as RILS_p10_pcc0_148
from output import RILS_p10_pcc0_149 as RILS_p10_pcc0_149
from output import RILS_p10_pcc0_150 as RILS_p10_pcc0_150
from output import RILS_p10_pcc0_151 as RILS_p10_pcc0_151
from output import RILS_p10_pcc0_152 as RILS_p10_pcc0_152
from output import RILS_p10_pcc0_153 as RILS_p10_pcc0_153
from output import RILS_p10_pcc0_154 as RILS_p10_pcc0_154
from output import RILS_p10_pcc0_155 as RILS_p10_pcc0_155
from output import RILS_p10_pcc0_156 as RILS_p10_pcc0_156
from output import RILS_p10_pcc0_157 as RILS_p10_pcc0_157
from output import RILS_p10_pcc0_158 as RILS_p10_pcc0_158
from output import RILS_p10_pcc0_159 as RILS_p10_pcc0_159
from output import RILS_p10_pcc0_160 as RILS_p10_pcc0_160
from output import RILS_p10_pcc0_161 as RILS_p10_pcc0_161
from output import RILS_p10_pcc0_162 as RILS_p10_pcc0_162
from output import RILS_p10_pcc0_163 as RILS_p10_pcc0_163
from output import RILS_p10_pcc0_164 as RILS_p10_pcc0_164
from output import RILS_p10_pcc0_165 as RILS_p10_pcc0_165
from output import RILS_p10_pcc0_166 as RILS_p10_pcc0_166
from output import RILS_p10_pcc0_167 as RILS_p10_pcc0_167
from output import RILS_p10_pcc0_168 as RILS_p10_pcc0_168
from output import RILS_p10_pcc0_169 as RILS_p10_pcc0_169
from output import RILS_p10_pcc0_170 as RILS_p10_pcc0_170
from output import RILS_p10_pcc0_171 as RILS_p10_pcc0_171
from output import RILS_p10_pcc0_172 as RILS_p10_pcc0_172
from output import RILS_p10_pcc0_173 as RILS_p10_pcc0_173
from output import RILS_p10_pcc0_174 as RILS_p10_pcc0_174
from output import RILS_p10_pcc0_175 as RILS_p10_pcc0_175
from output import RILS_p10_pcc0_176 as RILS_p10_pcc0_176
from output import RILS_p10_pcc0_177 as RILS_p10_pcc0_177
from output import RILS_p10_pcc0_178 as RILS_p10_pcc0_178
from output import RILS_p10_pcc0_179 as RILS_p10_pcc0_179
from output import RILS_p10_pcc0_180 as RILS_p10_pcc0_180
from output import RILS_p10_pcc0_181 as RILS_p10_pcc0_181
from output import RILS_p10_pcc0_182 as RILS_p10_pcc0_182
from output import RILS_p10_pcc0_183 as RILS_p10_pcc0_183
from output import RILS_p10_pcc0_184 as RILS_p10_pcc0_184
from output import RILS_p10_pcc0_185 as RILS_p10_pcc0_185
from output import RILS_p10_pcc0_186 as RILS_p10_pcc0_186
from output import RILS_p10_pcc0_187 as RILS_p10_pcc0_187
from output import RILS_p10_pcc0_188 as RILS_p10_pcc0_188
from output import RILS_p10_pcc0_189 as RILS_p10_pcc0_189
from output import RILS_p10_pcc0_190 as RILS_p10_pcc0_190
from output import RILS_p10_pcc0_191 as RILS_p10_pcc0_191
from output import RILS_p10_pcc0_192 as RILS_p10_pcc0_192
from output import RILS_p10_pcc0_193 as RILS_p10_pcc0_193
from output import RILS_p10_pcc0_194 as RILS_p10_pcc0_194
from output import RILS_p10_pcc0_195 as RILS_p10_pcc0_195
from output import RILS_p10_pcc0_196 as RILS_p10_pcc0_196
from output import RILS_p10_pcc0_197 as RILS_p10_pcc0_197
from output import RILS_p10_pcc0_198 as RILS_p10_pcc0_198
from output import RILS_p10_pcc0_199 as RILS_p10_pcc0_199
from output import RO_p01_efm200_000 as RO_p01_efm200_00
from output import RO_p01_efm200_001 as RO_p01_efm200_01
from output import RO_p01_efm200_002 as RO_p01_efm200_02
from output import RO_p01_efm200_003 as RO_p01_efm200_03
from output import RO_p01_efm200_004 as RO_p01_efm200_04
from output import RO_p01_efm200_005 as RO_p01_efm200_05
from output import RO_p01_efm200_006 as RO_p01_efm200_06
from output import RO_p01_efm200_007 as RO_p01_efm200_07
from output import RO_p01_efm200_008 as RO_p01_efm200_08
from output import RO_p01_efm200_009 as RO_p01_efm200_09
from output import RO_p01_efm200_010 as RO_p01_efm200_10
from output import RO_p01_efm200_011 as RO_p01_efm200_11
from output import RO_p01_efm200_012 as RO_p01_efm200_12
from output import RO_p01_efm200_013 as RO_p01_efm200_13
from output import RO_p01_efm200_014 as RO_p01_efm200_14
from output import RO_p01_efm200_015 as RO_p01_efm200_15
from output import RO_p01_efm200_016 as RO_p01_efm200_16
from output import RO_p01_efm200_017 as RO_p01_efm200_17
from output import RO_p01_efm200_018 as RO_p01_efm200_18
from output import RO_p01_efm200_019 as RO_p01_efm200_19
from output import RO_p01_efm200_020 as RO_p01_efm200_20
from output import RO_p01_efm200_021 as RO_p01_efm200_21
from output import RO_p01_efm200_022 as RO_p01_efm200_22
from output import RO_p01_efm200_023 as RO_p01_efm200_23
from output import RO_p01_efm200_024 as RO_p01_efm200_24
from output import RO_p01_efm200_025 as RO_p01_efm200_25
from output import RO_p01_efm200_026 as RO_p01_efm200_26
from output import RO_p01_efm200_027 as RO_p01_efm200_27
from output import RO_p01_efm200_028 as RO_p01_efm200_28
from output import RO_p01_efm200_029 as RO_p01_efm200_29
from output import RO_p01_efm200_030 as RO_p01_efm200_30
from output import RO_p01_efm200_031 as RO_p01_efm200_31
from output import RO_p01_efm200_032 as RO_p01_efm200_32
from output import RO_p01_efm200_033 as RO_p01_efm200_33
from output import RO_p01_efm200_034 as RO_p01_efm200_34
from output import RO_p01_efm200_035 as RO_p01_efm200_35
from output import RO_p01_efm200_036 as RO_p01_efm200_36
from output import RO_p01_efm200_037 as RO_p01_efm200_37
from output import RO_p01_efm200_038 as RO_p01_efm200_38
from output import RO_p01_efm200_039 as RO_p01_efm200_39
from output import RO_p01_efm200_040 as RO_p01_efm200_40
from output import RO_p01_efm200_041 as RO_p01_efm200_41
from output import RO_p01_efm200_042 as RO_p01_efm200_42
from output import RO_p01_efm200_043 as RO_p01_efm200_43
from output import RO_p01_efm200_044 as RO_p01_efm200_44
from output import RO_p01_efm200_045 as RO_p01_efm200_45
from output import RO_p01_efm200_046 as RO_p01_efm200_46
from output import RO_p01_efm200_047 as RO_p01_efm200_47
from output import RO_p01_efm200_048 as RO_p01_efm200_48
from output import RO_p01_efm200_049 as RO_p01_efm200_49
from output import RO_p01_efm200_050 as RO_p01_efm200_50
from output import RO_p01_efm200_051 as RO_p01_efm200_51
from output import RO_p01_efm200_052 as RO_p01_efm200_52
from output import RO_p01_efm200_053 as RO_p01_efm200_53
from output import RO_p01_efm200_054 as RO_p01_efm200_54
from output import RO_p01_efm200_055 as RO_p01_efm200_55
from output import RO_p01_efm200_056 as RO_p01_efm200_56
from output import RO_p01_efm200_057 as RO_p01_efm200_57
from output import RO_p01_efm200_058 as RO_p01_efm200_58
from output import RO_p01_efm200_059 as RO_p01_efm200_59
from output import RO_p01_efm200_060 as RO_p01_efm200_60
from output import RO_p01_efm200_061 as RO_p01_efm200_61
from output import RO_p01_efm200_062 as RO_p01_efm200_62
from output import RO_p01_efm200_063 as RO_p01_efm200_63
from output import RO_p01_efm200_064 as RO_p01_efm200_64
from output import RO_p01_efm200_065 as RO_p01_efm200_65
from output import RO_p01_efm200_066 as RO_p01_efm200_66
from output import RO_p01_efm200_067 as RO_p01_efm200_67
from output import RO_p01_efm200_068 as RO_p01_efm200_68
from output import RO_p01_efm200_069 as RO_p01_efm200_69
from output import RO_p01_efm200_070 as RO_p01_efm200_70
from output import RO_p01_efm200_071 as RO_p01_efm200_71
from output import RO_p01_efm200_072 as RO_p01_efm200_72
from output import RO_p01_efm200_073 as RO_p01_efm200_73
from output import RO_p01_efm200_074 as RO_p01_efm200_74
from output import RO_p01_efm200_075 as RO_p01_efm200_75
from output import RO_p01_efm200_076 as RO_p01_efm200_76
from output import RO_p01_efm200_077 as RO_p01_efm200_77
from output import RO_p01_efm200_078 as RO_p01_efm200_78
from output import RO_p01_efm200_079 as RO_p01_efm200_79
from output import RO_p01_efm200_080 as RO_p01_efm200_80
from output import RO_p01_efm200_081 as RO_p01_efm200_81
from output import RO_p01_efm200_082 as RO_p01_efm200_82
from output import RO_p01_efm200_083 as RO_p01_efm200_83
from output import RO_p01_efm200_084 as RO_p01_efm200_84
from output import RO_p01_efm200_085 as RO_p01_efm200_85
from output import RO_p01_efm200_086 as RO_p01_efm200_86
from output import RO_p01_efm200_087 as RO_p01_efm200_87
from output import RO_p01_efm200_088 as RO_p01_efm200_88
from output import RO_p01_efm200_089 as RO_p01_efm200_89
from output import RO_p01_efm200_090 as RO_p01_efm200_90
from output import RO_p01_efm200_091 as RO_p01_efm200_91
from output import RO_p01_efm200_092 as RO_p01_efm200_92
from output import RO_p01_efm200_093 as RO_p01_efm200_93
from output import RO_p01_efm200_094 as RO_p01_efm200_94
from output import RO_p01_efm200_095 as RO_p01_efm200_95
from output import RO_p01_efm200_096 as RO_p01_efm200_96
from output import RO_p01_efm200_097 as RO_p01_efm200_97
from output import RO_p01_efm200_098 as RO_p01_efm200_98
from output import RO_p01_efm200_099 as RO_p01_efm200_99
from output import RO_p01_ef0_000 as RO_p01_ef0_00
from output import RO_p01_ef0_001 as RO_p01_ef0_01
from output import RO_p01_ef0_002 as RO_p01_ef0_02
from output import RO_p01_ef0_003 as RO_p01_ef0_03
from output import RO_p01_ef0_004 as RO_p01_ef0_04
from output import RO_p01_ef0_005 as RO_p01_ef0_05
from output import RO_p01_ef0_006 as RO_p01_ef0_06
from output import RO_p01_ef0_007 as RO_p01_ef0_07
from output import RO_p01_ef0_008 as RO_p01_ef0_08
from output import RO_p01_ef0_009 as RO_p01_ef0_09
from output import RO_p01_ef0_010 as RO_p01_ef0_10
from output import RO_p01_ef0_011 as RO_p01_ef0_11
from output import RO_p01_ef0_012 as RO_p01_ef0_12
from output import RO_p01_ef0_013 as RO_p01_ef0_13
from output import RO_p01_ef0_014 as RO_p01_ef0_14
from output import RO_p01_ef0_015 as RO_p01_ef0_15
from output import RO_p01_ef0_016 as RO_p01_ef0_16
from output import RO_p01_ef0_017 as RO_p01_ef0_17
from output import RO_p01_ef0_018 as RO_p01_ef0_18
from output import RO_p01_ef0_019 as RO_p01_ef0_19
from output import RO_p01_ef0_020 as RO_p01_ef0_20
from output import RO_p01_ef0_021 as RO_p01_ef0_21
from output import RO_p01_ef0_022 as RO_p01_ef0_22
from output import RO_p01_ef0_023 as RO_p01_ef0_23
from output import RO_p01_ef0_024 as RO_p01_ef0_24
from output import RO_p01_ef0_025 as RO_p01_ef0_25
from output import RO_p01_ef0_026 as RO_p01_ef0_26
from output import RO_p01_ef0_027 as RO_p01_ef0_27
from output import RO_p01_ef0_028 as RO_p01_ef0_28
from output import RO_p01_ef0_029 as RO_p01_ef0_29
from output import RO_p01_ef0_030 as RO_p01_ef0_30
from output import RO_p01_ef0_031 as RO_p01_ef0_31
from output import RO_p01_ef0_032 as RO_p01_ef0_32
from output import RO_p01_ef0_033 as RO_p01_ef0_33
from output import RO_p01_ef0_034 as RO_p01_ef0_34
from output import RO_p01_ef0_035 as RO_p01_ef0_35
from output import RO_p01_ef0_036 as RO_p01_ef0_36
from output import RO_p01_ef0_037 as RO_p01_ef0_37
from output import RO_p01_ef0_038 as RO_p01_ef0_38
from output import RO_p01_ef0_039 as RO_p01_ef0_39
from output import RO_p01_ef0_040 as RO_p01_ef0_40
from output import RO_p01_ef0_041 as RO_p01_ef0_41
from output import RO_p01_ef0_042 as RO_p01_ef0_42
from output import RO_p01_ef0_043 as RO_p01_ef0_43
from output import RO_p01_ef0_044 as RO_p01_ef0_44
from output import RO_p01_ef0_045 as RO_p01_ef0_45
from output import RO_p01_ef0_046 as RO_p01_ef0_46
from output import RO_p01_ef0_047 as RO_p01_ef0_47
from output import RO_p01_ef0_048 as RO_p01_ef0_48
from output import RO_p01_ef0_049 as RO_p01_ef0_49
from output import RO_p01_ef0_050 as RO_p01_ef0_50
from output import RO_p01_ef0_051 as RO_p01_ef0_51
from output import RO_p01_ef0_052 as RO_p01_ef0_52
from output import RO_p01_ef0_053 as RO_p01_ef0_53
from output import RO_p01_ef0_054 as RO_p01_ef0_54
from output import RO_p01_ef0_055 as RO_p01_ef0_55
from output import RO_p01_ef0_056 as RO_p01_ef0_56
from output import RO_p01_ef0_057 as RO_p01_ef0_57
from output import RO_p01_ef0_058 as RO_p01_ef0_58
from output import RO_p01_ef0_059 as RO_p01_ef0_59
from output import RO_p01_ef0_060 as RO_p01_ef0_60
from output import RO_p01_ef0_061 as RO_p01_ef0_61
from output import RO_p01_ef0_062 as RO_p01_ef0_62
from output import RO_p01_ef0_063 as RO_p01_ef0_63
from output import RO_p01_ef0_064 as RO_p01_ef0_64
from output import RO_p01_ef0_065 as RO_p01_ef0_65
from output import RO_p01_ef0_066 as RO_p01_ef0_66
from output import RO_p01_ef0_067 as RO_p01_ef0_67
from output import RO_p01_ef0_068 as RO_p01_ef0_68
from output import RO_p01_ef0_069 as RO_p01_ef0_69
from output import RO_p01_ef0_070 as RO_p01_ef0_70
from output import RO_p01_ef0_071 as RO_p01_ef0_71
from output import RO_p01_ef0_072 as RO_p01_ef0_72
from output import RO_p01_ef0_073 as RO_p01_ef0_73
from output import RO_p01_ef0_074 as RO_p01_ef0_74
from output import RO_p01_ef0_075 as RO_p01_ef0_75
from output import RO_p01_ef0_076 as RO_p01_ef0_76
from output import RO_p01_ef0_077 as RO_p01_ef0_77
from output import RO_p01_ef0_078 as RO_p01_ef0_78
from output import RO_p01_ef0_079 as RO_p01_ef0_79
from output import RO_p01_ef0_080 as RO_p01_ef0_80
from output import RO_p01_ef0_081 as RO_p01_ef0_81
from output import RO_p01_ef0_082 as RO_p01_ef0_82
from output import RO_p01_ef0_083 as RO_p01_ef0_83
from output import RO_p01_ef0_084 as RO_p01_ef0_84
from output import RO_p01_ef0_085 as RO_p01_ef0_85
from output import RO_p01_ef0_086 as RO_p01_ef0_86
from output import RO_p01_ef0_087 as RO_p01_ef0_87
from output import RO_p01_ef0_088 as RO_p01_ef0_88
from output import RO_p01_ef0_089 as RO_p01_ef0_89
from output import RO_p01_ef0_090 as RO_p01_ef0_90
from output import RO_p01_ef0_091 as RO_p01_ef0_91
from output import RO_p01_ef0_092 as RO_p01_ef0_92
from output import RO_p01_ef0_093 as RO_p01_ef0_93
from output import RO_p01_ef0_094 as RO_p01_ef0_94
from output import RO_p01_ef0_095 as RO_p01_ef0_95
from output import RO_p01_ef0_096 as RO_p01_ef0_96
from output import RO_p01_ef0_097 as RO_p01_ef0_97
from output import RO_p01_ef0_098 as RO_p01_ef0_98
from output import RO_p01_ef0_099 as RO_p01_ef0_99
from output import bs_RO_p01_ef0_00125 as bs_RO_p01_ef0_00125
from output import bs_RO_p01_ef0_00250 as bs_RO_p01_ef0_00250
from output import bs_RO_p01_ef0_00500 as bs_RO_p01_ef0_00500
from output import bs_RO_p01_ef0_01000 as bs_RO_p01_ef0_01000
from output import bs_RO_p01_ef0_02000 as bs_RO_p01_ef0_02000
from output import bs_RO_p01_ef0_04000 as bs_RO_p01_ef0_04000
from output import bs_RO_p01_ef0_08000 as bs_RO_p01_ef0_08000
from output import bs_RO_p01_ef0_16000 as bs_RO_p01_ef0_16000
from output import bs_RO_p01_ef0_32000 as bs_RO_p01_ef0_32000
print('Importing completed')


def flip(items, ncol):
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])


# RIL and RILS: Number of customers

############### Maximum number of customers
print('Creating max_prov_customers_RIL_p01')

max_prov_customers_RIL_p01 = zip(RIL_p01_00.prov_cn_max, RIL_p01_01.prov_cn_max, RIL_p01_02.prov_cn_max, RIL_p01_03.prov_cn_max, RIL_p01_04.prov_cn_max,
                          RIL_p01_05.prov_cn_max, RIL_p01_06.prov_cn_max, RIL_p01_07.prov_cn_max, RIL_p01_08.prov_cn_max, RIL_p01_09.prov_cn_max,
                          RIL_p01_10.prov_cn_max, RIL_p01_11.prov_cn_max, RIL_p01_12.prov_cn_max, RIL_p01_13.prov_cn_max, RIL_p01_14.prov_cn_max,
                          RIL_p01_15.prov_cn_max, RIL_p01_16.prov_cn_max, RIL_p01_17.prov_cn_max, RIL_p01_18.prov_cn_max, RIL_p01_19.prov_cn_max,
                          RIL_p01_20.prov_cn_max, RIL_p01_21.prov_cn_max, RIL_p01_22.prov_cn_max, RIL_p01_23.prov_cn_max, RIL_p01_24.prov_cn_max,
                          RIL_p01_25.prov_cn_max, RIL_p01_26.prov_cn_max, RIL_p01_27.prov_cn_max, RIL_p01_28.prov_cn_max, RIL_p01_29.prov_cn_max,
                          RIL_p01_30.prov_cn_max, RIL_p01_31.prov_cn_max, RIL_p01_32.prov_cn_max, RIL_p01_33.prov_cn_max, RIL_p01_34.prov_cn_max,
                          RIL_p01_35.prov_cn_max, RIL_p01_36.prov_cn_max, RIL_p01_37.prov_cn_max, RIL_p01_38.prov_cn_max, RIL_p01_39.prov_cn_max,
                          RIL_p01_40.prov_cn_max, RIL_p01_40.prov_cn_max, RIL_p01_41.prov_cn_max, RIL_p01_42.prov_cn_max, RIL_p01_43.prov_cn_max,
                          RIL_p01_44.prov_cn_max, RIL_p01_45.prov_cn_max, RIL_p01_46.prov_cn_max, RIL_p01_47.prov_cn_max, RIL_p01_48.prov_cn_max,
                          RIL_p01_49.prov_cn_max, RIL_p01_50.prov_cn_max, RIL_p01_51.prov_cn_max, RIL_p01_52.prov_cn_max, RIL_p01_53.prov_cn_max,
                          RIL_p01_54.prov_cn_max, RIL_p01_55.prov_cn_max, RIL_p01_56.prov_cn_max, RIL_p01_57.prov_cn_max, RIL_p01_58.prov_cn_max,
                          RIL_p01_59.prov_cn_max, RIL_p01_60.prov_cn_max, RIL_p01_61.prov_cn_max, RIL_p01_62.prov_cn_max, RIL_p01_63.prov_cn_max,
                          RIL_p01_64.prov_cn_max, RIL_p01_65.prov_cn_max, RIL_p01_66.prov_cn_max, RIL_p01_67.prov_cn_max, RIL_p01_68.prov_cn_max,
                          RIL_p01_69.prov_cn_max, RIL_p01_70.prov_cn_max, RIL_p01_71.prov_cn_max, RIL_p01_72.prov_cn_max, RIL_p01_73.prov_cn_max,
                          RIL_p01_74.prov_cn_max, RIL_p01_75.prov_cn_max, RIL_p01_76.prov_cn_max, RIL_p01_77.prov_cn_max, RIL_p01_78.prov_cn_max,
                          RIL_p01_79.prov_cn_max, RIL_p01_80.prov_cn_max, RIL_p01_81.prov_cn_max, RIL_p01_82.prov_cn_max, RIL_p01_83.prov_cn_max,
                          RIL_p01_84.prov_cn_max, RIL_p01_85.prov_cn_max, RIL_p01_86.prov_cn_max, RIL_p01_87.prov_cn_max, RIL_p01_88.prov_cn_max,
                          RIL_p01_89.prov_cn_max, RIL_p01_90.prov_cn_max, RIL_p01_91.prov_cn_max, RIL_p01_92.prov_cn_max, RIL_p01_93.prov_cn_max,
                          RIL_p01_94.prov_cn_max, RIL_p01_95.prov_cn_max, RIL_p01_96.prov_cn_max, RIL_p01_97.prov_cn_max, RIL_p01_98.prov_cn_max,
                          RIL_p01_99.prov_cn_max, RIL_p01_100.prov_cn_max,
                          RIL_p01_101.prov_cn_max, RIL_p01_102.prov_cn_max, RIL_p01_103.prov_cn_max, RIL_p01_104.prov_cn_max, RIL_p01_105.prov_cn_max,
                          RIL_p01_106.prov_cn_max, RIL_p01_107.prov_cn_max, RIL_p01_108.prov_cn_max, RIL_p01_109.prov_cn_max, RIL_p01_110.prov_cn_max,
                          RIL_p01_111.prov_cn_max, RIL_p01_112.prov_cn_max, RIL_p01_113.prov_cn_max, RIL_p01_114.prov_cn_max, RIL_p01_115.prov_cn_max,
                          RIL_p01_116.prov_cn_max, RIL_p01_117.prov_cn_max, RIL_p01_118.prov_cn_max, RIL_p01_119.prov_cn_max, RIL_p01_120.prov_cn_max,
                          RIL_p01_121.prov_cn_max, RIL_p01_122.prov_cn_max, RIL_p01_123.prov_cn_max, RIL_p01_124.prov_cn_max, RIL_p01_125.prov_cn_max,
                          RIL_p01_126.prov_cn_max, RIL_p01_127.prov_cn_max, RIL_p01_128.prov_cn_max, RIL_p01_129.prov_cn_max, RIL_p01_130.prov_cn_max,
                          RIL_p01_131.prov_cn_max, RIL_p01_132.prov_cn_max, RIL_p01_133.prov_cn_max, RIL_p01_134.prov_cn_max, RIL_p01_135.prov_cn_max,
                          RIL_p01_136.prov_cn_max, RIL_p01_137.prov_cn_max, RIL_p01_138.prov_cn_max, RIL_p01_139.prov_cn_max, RIL_p01_140.prov_cn_max,
                          RIL_p01_140.prov_cn_max, RIL_p01_141.prov_cn_max, RIL_p01_142.prov_cn_max, RIL_p01_143.prov_cn_max, RIL_p01_144.prov_cn_max,
                          RIL_p01_145.prov_cn_max, RIL_p01_146.prov_cn_max, RIL_p01_147.prov_cn_max, RIL_p01_148.prov_cn_max, RIL_p01_149.prov_cn_max,
                          RIL_p01_150.prov_cn_max, RIL_p01_151.prov_cn_max, RIL_p01_152.prov_cn_max, RIL_p01_153.prov_cn_max, RIL_p01_154.prov_cn_max,
                          RIL_p01_155.prov_cn_max, RIL_p01_156.prov_cn_max, RIL_p01_157.prov_cn_max, RIL_p01_158.prov_cn_max, RIL_p01_159.prov_cn_max,
                          RIL_p01_160.prov_cn_max, RIL_p01_161.prov_cn_max, RIL_p01_162.prov_cn_max, RIL_p01_163.prov_cn_max, RIL_p01_164.prov_cn_max,
                          RIL_p01_165.prov_cn_max, RIL_p01_166.prov_cn_max, RIL_p01_167.prov_cn_max, RIL_p01_168.prov_cn_max, RIL_p01_169.prov_cn_max,
                          RIL_p01_170.prov_cn_max, RIL_p01_171.prov_cn_max, RIL_p01_172.prov_cn_max, RIL_p01_173.prov_cn_max, RIL_p01_174.prov_cn_max,
                          RIL_p01_175.prov_cn_max, RIL_p01_176.prov_cn_max, RIL_p01_177.prov_cn_max, RIL_p01_178.prov_cn_max, RIL_p01_179.prov_cn_max,
                          RIL_p01_180.prov_cn_max, RIL_p01_181.prov_cn_max, RIL_p01_182.prov_cn_max, RIL_p01_183.prov_cn_max, RIL_p01_184.prov_cn_max,
                          RIL_p01_185.prov_cn_max, RIL_p01_186.prov_cn_max, RIL_p01_187.prov_cn_max, RIL_p01_188.prov_cn_max, RIL_p01_189.prov_cn_max,
                          RIL_p01_190.prov_cn_max, RIL_p01_191.prov_cn_max, RIL_p01_192.prov_cn_max, RIL_p01_193.prov_cn_max, RIL_p01_194.prov_cn_max,
                          RIL_p01_195.prov_cn_max, RIL_p01_196.prov_cn_max, RIL_p01_197.prov_cn_max, RIL_p01_198.prov_cn_max, RIL_p01_199.prov_cn_max)


max_prov_customers_RIL_p01_mean = [np.mean(i) for i in max_prov_customers_RIL_p01]
max_prov_customers_RIL_p01_lower = [np.percentile(i, 10) for i in max_prov_customers_RIL_p01]
max_prov_customers_RIL_p01_upper = [np.percentile(i, 90) for i in max_prov_customers_RIL_p01]

print('Creating max_prov_customers_RIL_p10')

max_prov_customers_RIL_p10 = zip(RIL_p10_00.prov_cn_max, RIL_p10_01.prov_cn_max, RIL_p10_02.prov_cn_max, RIL_p10_03.prov_cn_max, RIL_p10_04.prov_cn_max,
                          RIL_p10_05.prov_cn_max, RIL_p10_06.prov_cn_max, RIL_p10_07.prov_cn_max, RIL_p10_08.prov_cn_max, RIL_p10_09.prov_cn_max,
                          RIL_p10_10.prov_cn_max, RIL_p10_11.prov_cn_max, RIL_p10_12.prov_cn_max, RIL_p10_13.prov_cn_max, RIL_p10_14.prov_cn_max,
                          RIL_p10_15.prov_cn_max, RIL_p10_16.prov_cn_max, RIL_p10_17.prov_cn_max, RIL_p10_18.prov_cn_max, RIL_p10_19.prov_cn_max,
                          RIL_p10_20.prov_cn_max, RIL_p10_21.prov_cn_max, RIL_p10_22.prov_cn_max, RIL_p10_23.prov_cn_max, RIL_p10_24.prov_cn_max,
                          RIL_p10_25.prov_cn_max, RIL_p10_26.prov_cn_max, RIL_p10_27.prov_cn_max, RIL_p10_28.prov_cn_max, RIL_p10_29.prov_cn_max,
                          RIL_p10_30.prov_cn_max, RIL_p10_31.prov_cn_max, RIL_p10_32.prov_cn_max, RIL_p10_33.prov_cn_max, RIL_p10_34.prov_cn_max,
                          RIL_p10_35.prov_cn_max, RIL_p10_36.prov_cn_max, RIL_p10_37.prov_cn_max, RIL_p10_38.prov_cn_max, RIL_p10_39.prov_cn_max,
                          RIL_p10_40.prov_cn_max, RIL_p10_40.prov_cn_max, RIL_p10_41.prov_cn_max, RIL_p10_42.prov_cn_max, RIL_p10_43.prov_cn_max,
                          RIL_p10_44.prov_cn_max, RIL_p10_45.prov_cn_max, RIL_p10_46.prov_cn_max, RIL_p10_47.prov_cn_max, RIL_p10_48.prov_cn_max,
                          RIL_p10_49.prov_cn_max, RIL_p10_50.prov_cn_max, RIL_p10_51.prov_cn_max, RIL_p10_52.prov_cn_max, RIL_p10_53.prov_cn_max,
                          RIL_p10_54.prov_cn_max, RIL_p10_55.prov_cn_max, RIL_p10_56.prov_cn_max, RIL_p10_57.prov_cn_max, RIL_p10_58.prov_cn_max,
                          RIL_p10_59.prov_cn_max, RIL_p10_60.prov_cn_max, RIL_p10_61.prov_cn_max, RIL_p10_62.prov_cn_max, RIL_p10_63.prov_cn_max,
                          RIL_p10_64.prov_cn_max, RIL_p10_65.prov_cn_max, RIL_p10_66.prov_cn_max, RIL_p10_67.prov_cn_max, RIL_p10_68.prov_cn_max,
                          RIL_p10_69.prov_cn_max, RIL_p10_70.prov_cn_max, RIL_p10_71.prov_cn_max, RIL_p10_72.prov_cn_max, RIL_p10_73.prov_cn_max,
                          RIL_p10_74.prov_cn_max, RIL_p10_75.prov_cn_max, RIL_p10_76.prov_cn_max, RIL_p10_77.prov_cn_max, RIL_p10_78.prov_cn_max,
                          RIL_p10_79.prov_cn_max, RIL_p10_80.prov_cn_max, RIL_p10_81.prov_cn_max, RIL_p10_82.prov_cn_max, RIL_p10_83.prov_cn_max,
                          RIL_p10_84.prov_cn_max, RIL_p10_85.prov_cn_max, RIL_p10_86.prov_cn_max, RIL_p10_87.prov_cn_max, RIL_p10_88.prov_cn_max,
                          RIL_p10_89.prov_cn_max, RIL_p10_90.prov_cn_max, RIL_p10_91.prov_cn_max, RIL_p10_92.prov_cn_max, RIL_p10_93.prov_cn_max,
                          RIL_p10_94.prov_cn_max, RIL_p10_95.prov_cn_max, RIL_p10_96.prov_cn_max, RIL_p10_97.prov_cn_max, RIL_p10_98.prov_cn_max,
                          RIL_p10_99.prov_cn_max, RIL_p10_100.prov_cn_max,
                          RIL_p10_101.prov_cn_max, RIL_p10_102.prov_cn_max, RIL_p10_103.prov_cn_max, RIL_p10_104.prov_cn_max, RIL_p10_105.prov_cn_max,
                          RIL_p10_106.prov_cn_max, RIL_p10_107.prov_cn_max, RIL_p10_108.prov_cn_max, RIL_p10_109.prov_cn_max, RIL_p10_110.prov_cn_max,
                          RIL_p10_111.prov_cn_max, RIL_p10_112.prov_cn_max, RIL_p10_113.prov_cn_max, RIL_p10_114.prov_cn_max, RIL_p10_115.prov_cn_max,
                          RIL_p10_116.prov_cn_max, RIL_p10_117.prov_cn_max, RIL_p10_118.prov_cn_max, RIL_p10_119.prov_cn_max, RIL_p10_120.prov_cn_max,
                          RIL_p10_121.prov_cn_max, RIL_p10_122.prov_cn_max, RIL_p10_123.prov_cn_max, RIL_p10_124.prov_cn_max, RIL_p10_125.prov_cn_max,
                          RIL_p10_126.prov_cn_max, RIL_p10_127.prov_cn_max, RIL_p10_128.prov_cn_max, RIL_p10_129.prov_cn_max, RIL_p10_130.prov_cn_max,
                          RIL_p10_131.prov_cn_max, RIL_p10_132.prov_cn_max, RIL_p10_133.prov_cn_max, RIL_p10_134.prov_cn_max, RIL_p10_135.prov_cn_max,
                          RIL_p10_136.prov_cn_max, RIL_p10_137.prov_cn_max, RIL_p10_138.prov_cn_max, RIL_p10_139.prov_cn_max, RIL_p10_140.prov_cn_max,
                          RIL_p10_140.prov_cn_max, RIL_p10_141.prov_cn_max, RIL_p10_142.prov_cn_max, RIL_p10_143.prov_cn_max, RIL_p10_144.prov_cn_max,
                          RIL_p10_145.prov_cn_max, RIL_p10_146.prov_cn_max, RIL_p10_147.prov_cn_max, RIL_p10_148.prov_cn_max, RIL_p10_149.prov_cn_max,
                          RIL_p10_150.prov_cn_max, RIL_p10_151.prov_cn_max, RIL_p10_152.prov_cn_max, RIL_p10_153.prov_cn_max, RIL_p10_154.prov_cn_max,
                          RIL_p10_155.prov_cn_max, RIL_p10_156.prov_cn_max, RIL_p10_157.prov_cn_max, RIL_p10_158.prov_cn_max, RIL_p10_159.prov_cn_max,
                          RIL_p10_160.prov_cn_max, RIL_p10_161.prov_cn_max, RIL_p10_162.prov_cn_max, RIL_p10_163.prov_cn_max, RIL_p10_164.prov_cn_max,
                          RIL_p10_165.prov_cn_max, RIL_p10_166.prov_cn_max, RIL_p10_167.prov_cn_max, RIL_p10_168.prov_cn_max, RIL_p10_169.prov_cn_max,
                          RIL_p10_170.prov_cn_max, RIL_p10_171.prov_cn_max, RIL_p10_172.prov_cn_max, RIL_p10_173.prov_cn_max, RIL_p10_174.prov_cn_max,
                          RIL_p10_175.prov_cn_max, RIL_p10_176.prov_cn_max, RIL_p10_177.prov_cn_max, RIL_p10_178.prov_cn_max, RIL_p10_179.prov_cn_max,
                          RIL_p10_180.prov_cn_max, RIL_p10_181.prov_cn_max, RIL_p10_182.prov_cn_max, RIL_p10_183.prov_cn_max, RIL_p10_184.prov_cn_max,
                          RIL_p10_185.prov_cn_max, RIL_p10_186.prov_cn_max, RIL_p10_187.prov_cn_max, RIL_p10_188.prov_cn_max, RIL_p10_189.prov_cn_max,
                          RIL_p10_190.prov_cn_max, RIL_p10_191.prov_cn_max, RIL_p10_192.prov_cn_max, RIL_p10_193.prov_cn_max, RIL_p10_194.prov_cn_max,
                          RIL_p10_195.prov_cn_max, RIL_p10_196.prov_cn_max, RIL_p10_197.prov_cn_max, RIL_p10_198.prov_cn_max, RIL_p10_199.prov_cn_max)


max_prov_customers_RIL_p10_mean = [np.mean(i) for i in max_prov_customers_RIL_p10]
max_prov_customers_RIL_p10_lower = [np.percentile(i, 10) for i in max_prov_customers_RIL_p10]
max_prov_customers_RIL_p10_upper = [np.percentile(i, 90) for i in max_prov_customers_RIL_p10]

print('Creating max_prov_rev_RILS_p01')
max_prov_customers_RILS_p01 = zip(RILS_p01_00.prov_cn_max, RILS_p01_01.prov_cn_max, RILS_p01_02.prov_cn_max, RILS_p01_03.prov_cn_max, RILS_p01_04.prov_cn_max,
                          RILS_p01_05.prov_cn_max, RILS_p01_06.prov_cn_max, RILS_p01_07.prov_cn_max, RILS_p01_08.prov_cn_max, RILS_p01_09.prov_cn_max,
                          RILS_p01_10.prov_cn_max, RILS_p01_11.prov_cn_max, RILS_p01_12.prov_cn_max, RILS_p01_13.prov_cn_max, RILS_p01_14.prov_cn_max,
                          RILS_p01_15.prov_cn_max, RILS_p01_16.prov_cn_max, RILS_p01_17.prov_cn_max, RILS_p01_18.prov_cn_max, RILS_p01_19.prov_cn_max,
                          RILS_p01_20.prov_cn_max, RILS_p01_21.prov_cn_max, RILS_p01_22.prov_cn_max, RILS_p01_23.prov_cn_max, RILS_p01_24.prov_cn_max,
                          RILS_p01_25.prov_cn_max, RILS_p01_26.prov_cn_max, RILS_p01_27.prov_cn_max, RILS_p01_28.prov_cn_max, RILS_p01_29.prov_cn_max,
                          RILS_p01_30.prov_cn_max, RILS_p01_31.prov_cn_max, RILS_p01_32.prov_cn_max, RILS_p01_33.prov_cn_max, RILS_p01_34.prov_cn_max,
                          RILS_p01_35.prov_cn_max, RILS_p01_36.prov_cn_max, RILS_p01_37.prov_cn_max, RILS_p01_38.prov_cn_max, RILS_p01_39.prov_cn_max,
                          RILS_p01_40.prov_cn_max, RILS_p01_40.prov_cn_max, RILS_p01_41.prov_cn_max, RILS_p01_42.prov_cn_max, RILS_p01_43.prov_cn_max,
                          RILS_p01_44.prov_cn_max, RILS_p01_45.prov_cn_max, RILS_p01_46.prov_cn_max, RILS_p01_47.prov_cn_max, RILS_p01_48.prov_cn_max,
                          RILS_p01_49.prov_cn_max, RILS_p01_50.prov_cn_max, RILS_p01_51.prov_cn_max, RILS_p01_52.prov_cn_max, RILS_p01_53.prov_cn_max,
                          RILS_p01_54.prov_cn_max, RILS_p01_55.prov_cn_max, RILS_p01_56.prov_cn_max, RILS_p01_57.prov_cn_max, RILS_p01_58.prov_cn_max,
                          RILS_p01_59.prov_cn_max, RILS_p01_60.prov_cn_max, RILS_p01_61.prov_cn_max, RILS_p01_62.prov_cn_max, RILS_p01_63.prov_cn_max,
                          RILS_p01_64.prov_cn_max, RILS_p01_65.prov_cn_max, RILS_p01_66.prov_cn_max, RILS_p01_67.prov_cn_max, RILS_p01_68.prov_cn_max,
                          RILS_p01_69.prov_cn_max, RILS_p01_70.prov_cn_max, RILS_p01_71.prov_cn_max, RILS_p01_72.prov_cn_max, RILS_p01_73.prov_cn_max,
                          RILS_p01_74.prov_cn_max, RILS_p01_75.prov_cn_max, RILS_p01_76.prov_cn_max, RILS_p01_77.prov_cn_max, RILS_p01_78.prov_cn_max,
                          RILS_p01_79.prov_cn_max, RILS_p01_80.prov_cn_max, RILS_p01_81.prov_cn_max, RILS_p01_82.prov_cn_max, RILS_p01_83.prov_cn_max,
                          RILS_p01_84.prov_cn_max, RILS_p01_85.prov_cn_max, RILS_p01_86.prov_cn_max, RILS_p01_87.prov_cn_max, RILS_p01_88.prov_cn_max,
                          RILS_p01_89.prov_cn_max, RILS_p01_90.prov_cn_max, RILS_p01_91.prov_cn_max, RILS_p01_92.prov_cn_max, RILS_p01_93.prov_cn_max,
                          RILS_p01_94.prov_cn_max, RILS_p01_95.prov_cn_max, RILS_p01_96.prov_cn_max, RILS_p01_97.prov_cn_max, RILS_p01_98.prov_cn_max,
                          RILS_p01_99.prov_cn_max, RILS_p01_100.prov_cn_max,
                          RILS_p01_101.prov_cn_max, RILS_p01_102.prov_cn_max, RILS_p01_103.prov_cn_max, RILS_p01_104.prov_cn_max, RILS_p01_105.prov_cn_max,
                          RILS_p01_106.prov_cn_max, RILS_p01_107.prov_cn_max, RILS_p01_108.prov_cn_max, RILS_p01_109.prov_cn_max, RILS_p01_110.prov_cn_max,
                          RILS_p01_111.prov_cn_max, RILS_p01_112.prov_cn_max, RILS_p01_113.prov_cn_max, RILS_p01_114.prov_cn_max, RILS_p01_115.prov_cn_max,
                          RILS_p01_116.prov_cn_max, RILS_p01_117.prov_cn_max, RILS_p01_118.prov_cn_max, RILS_p01_119.prov_cn_max, RILS_p01_120.prov_cn_max,
                          RILS_p01_121.prov_cn_max, RILS_p01_122.prov_cn_max, RILS_p01_123.prov_cn_max, RILS_p01_124.prov_cn_max, RILS_p01_125.prov_cn_max,
                          RILS_p01_126.prov_cn_max, RILS_p01_127.prov_cn_max, RILS_p01_128.prov_cn_max, RILS_p01_129.prov_cn_max, RILS_p01_130.prov_cn_max,
                          RILS_p01_131.prov_cn_max, RILS_p01_132.prov_cn_max, RILS_p01_133.prov_cn_max, RILS_p01_134.prov_cn_max, RILS_p01_135.prov_cn_max,
                          RILS_p01_136.prov_cn_max, RILS_p01_137.prov_cn_max, RILS_p01_138.prov_cn_max, RILS_p01_139.prov_cn_max, RILS_p01_140.prov_cn_max,
                          RILS_p01_140.prov_cn_max, RILS_p01_141.prov_cn_max, RILS_p01_142.prov_cn_max, RILS_p01_143.prov_cn_max, RILS_p01_144.prov_cn_max,
                          RILS_p01_145.prov_cn_max, RILS_p01_146.prov_cn_max, RILS_p01_147.prov_cn_max, RILS_p01_148.prov_cn_max, RILS_p01_149.prov_cn_max,
                          RILS_p01_150.prov_cn_max, RILS_p01_151.prov_cn_max, RILS_p01_152.prov_cn_max, RILS_p01_153.prov_cn_max, RILS_p01_154.prov_cn_max,
                          RILS_p01_155.prov_cn_max, RILS_p01_156.prov_cn_max, RILS_p01_157.prov_cn_max, RILS_p01_158.prov_cn_max, RILS_p01_159.prov_cn_max,
                          RILS_p01_160.prov_cn_max, RILS_p01_161.prov_cn_max, RILS_p01_162.prov_cn_max, RILS_p01_163.prov_cn_max, RILS_p01_164.prov_cn_max,
                          RILS_p01_165.prov_cn_max, RILS_p01_166.prov_cn_max, RILS_p01_167.prov_cn_max, RILS_p01_168.prov_cn_max, RILS_p01_169.prov_cn_max,
                          RILS_p01_170.prov_cn_max, RILS_p01_171.prov_cn_max, RILS_p01_172.prov_cn_max, RILS_p01_173.prov_cn_max, RILS_p01_174.prov_cn_max,
                          RILS_p01_175.prov_cn_max, RILS_p01_176.prov_cn_max, RILS_p01_177.prov_cn_max, RILS_p01_178.prov_cn_max, RILS_p01_179.prov_cn_max,
                          RILS_p01_180.prov_cn_max, RILS_p01_181.prov_cn_max, RILS_p01_182.prov_cn_max, RILS_p01_183.prov_cn_max, RILS_p01_184.prov_cn_max,
                          RILS_p01_185.prov_cn_max, RILS_p01_186.prov_cn_max, RILS_p01_187.prov_cn_max, RILS_p01_188.prov_cn_max, RILS_p01_189.prov_cn_max,
                          RILS_p01_190.prov_cn_max, RILS_p01_191.prov_cn_max, RILS_p01_192.prov_cn_max, RILS_p01_193.prov_cn_max, RILS_p01_194.prov_cn_max,
                          RILS_p01_195.prov_cn_max, RILS_p01_196.prov_cn_max, RILS_p01_197.prov_cn_max, RILS_p01_198.prov_cn_max, RILS_p01_199.prov_cn_max)


max_prov_customers_RILS_p01_mean = [np.mean(i) for i in max_prov_customers_RILS_p01]
max_prov_customers_RILS_p01_lower = [np.percentile(i, 10) for i in max_prov_customers_RILS_p01]
max_prov_customers_RILS_p01_upper = [np.percentile(i, 90) for i in max_prov_customers_RILS_p01]


print('Creating max_prov_customers_RILS_p10')

max_prov_customers_RILS_p10 = zip(RILS_p10_00.prov_cn_max, RILS_p10_01.prov_cn_max, RILS_p10_02.prov_cn_max, RILS_p10_03.prov_cn_max, RILS_p10_04.prov_cn_max,
                          RILS_p10_05.prov_cn_max, RILS_p10_06.prov_cn_max, RILS_p10_07.prov_cn_max, RILS_p10_08.prov_cn_max, RILS_p10_09.prov_cn_max,
                          RILS_p10_10.prov_cn_max, RILS_p10_11.prov_cn_max, RILS_p10_12.prov_cn_max, RILS_p10_13.prov_cn_max, RILS_p10_14.prov_cn_max,
                          RILS_p10_15.prov_cn_max, RILS_p10_16.prov_cn_max, RILS_p10_17.prov_cn_max, RILS_p10_18.prov_cn_max, RILS_p10_19.prov_cn_max,
                          RILS_p10_20.prov_cn_max, RILS_p10_21.prov_cn_max, RILS_p10_22.prov_cn_max, RILS_p10_23.prov_cn_max, RILS_p10_24.prov_cn_max,
                          RILS_p10_25.prov_cn_max, RILS_p10_26.prov_cn_max, RILS_p10_27.prov_cn_max, RILS_p10_28.prov_cn_max, RILS_p10_29.prov_cn_max,
                          RILS_p10_30.prov_cn_max, RILS_p10_31.prov_cn_max, RILS_p10_32.prov_cn_max, RILS_p10_33.prov_cn_max, RILS_p10_34.prov_cn_max,
                          RILS_p10_35.prov_cn_max, RILS_p10_36.prov_cn_max, RILS_p10_37.prov_cn_max, RILS_p10_38.prov_cn_max, RILS_p10_39.prov_cn_max,
                          RILS_p10_40.prov_cn_max, RILS_p10_40.prov_cn_max, RILS_p10_41.prov_cn_max, RILS_p10_42.prov_cn_max, RILS_p10_43.prov_cn_max,
                          RILS_p10_44.prov_cn_max, RILS_p10_45.prov_cn_max, RILS_p10_46.prov_cn_max, RILS_p10_47.prov_cn_max, RILS_p10_48.prov_cn_max,
                          RILS_p10_49.prov_cn_max, RILS_p10_50.prov_cn_max, RILS_p10_51.prov_cn_max, RILS_p10_52.prov_cn_max, RILS_p10_53.prov_cn_max,
                          RILS_p10_54.prov_cn_max, RILS_p10_55.prov_cn_max, RILS_p10_56.prov_cn_max, RILS_p10_57.prov_cn_max, RILS_p10_58.prov_cn_max,
                          RILS_p10_59.prov_cn_max, RILS_p10_60.prov_cn_max, RILS_p10_61.prov_cn_max, RILS_p10_62.prov_cn_max, RILS_p10_63.prov_cn_max,
                          RILS_p10_64.prov_cn_max, RILS_p10_65.prov_cn_max, RILS_p10_66.prov_cn_max, RILS_p10_67.prov_cn_max, RILS_p10_68.prov_cn_max,
                          RILS_p10_69.prov_cn_max, RILS_p10_70.prov_cn_max, RILS_p10_71.prov_cn_max, RILS_p10_72.prov_cn_max, RILS_p10_73.prov_cn_max,
                          RILS_p10_74.prov_cn_max, RILS_p10_75.prov_cn_max, RILS_p10_76.prov_cn_max, RILS_p10_77.prov_cn_max, RILS_p10_78.prov_cn_max,
                          RILS_p10_79.prov_cn_max, RILS_p10_80.prov_cn_max, RILS_p10_81.prov_cn_max, RILS_p10_82.prov_cn_max, RILS_p10_83.prov_cn_max,
                          RILS_p10_84.prov_cn_max, RILS_p10_85.prov_cn_max, RILS_p10_86.prov_cn_max, RILS_p10_87.prov_cn_max, RILS_p10_88.prov_cn_max,
                          RILS_p10_89.prov_cn_max, RILS_p10_90.prov_cn_max, RILS_p10_91.prov_cn_max, RILS_p10_92.prov_cn_max, RILS_p10_93.prov_cn_max,
                          RILS_p10_94.prov_cn_max, RILS_p10_95.prov_cn_max, RILS_p10_96.prov_cn_max, RILS_p10_97.prov_cn_max, RILS_p10_98.prov_cn_max,
                          RILS_p10_99.prov_cn_max, RILS_p10_100.prov_cn_max,
                          RILS_p10_101.prov_cn_max, RILS_p10_102.prov_cn_max, RILS_p10_103.prov_cn_max, RILS_p10_104.prov_cn_max, RILS_p10_105.prov_cn_max,
                          RILS_p10_106.prov_cn_max, RILS_p10_107.prov_cn_max, RILS_p10_108.prov_cn_max, RILS_p10_109.prov_cn_max, RILS_p10_110.prov_cn_max,
                          RILS_p10_111.prov_cn_max, RILS_p10_112.prov_cn_max, RILS_p10_113.prov_cn_max, RILS_p10_114.prov_cn_max, RILS_p10_115.prov_cn_max,
                          RILS_p10_116.prov_cn_max, RILS_p10_117.prov_cn_max, RILS_p10_118.prov_cn_max, RILS_p10_119.prov_cn_max, RILS_p10_120.prov_cn_max,
                          RILS_p10_121.prov_cn_max, RILS_p10_122.prov_cn_max, RILS_p10_123.prov_cn_max, RILS_p10_124.prov_cn_max, RILS_p10_125.prov_cn_max,
                          RILS_p10_126.prov_cn_max, RILS_p10_127.prov_cn_max, RILS_p10_128.prov_cn_max, RILS_p10_129.prov_cn_max, RILS_p10_130.prov_cn_max,
                          RILS_p10_131.prov_cn_max, RILS_p10_132.prov_cn_max, RILS_p10_133.prov_cn_max, RILS_p10_134.prov_cn_max, RILS_p10_135.prov_cn_max,
                          RILS_p10_136.prov_cn_max, RILS_p10_137.prov_cn_max, RILS_p10_138.prov_cn_max, RILS_p10_139.prov_cn_max, RILS_p10_140.prov_cn_max,
                          RILS_p10_140.prov_cn_max, RILS_p10_141.prov_cn_max, RILS_p10_142.prov_cn_max, RILS_p10_143.prov_cn_max, RILS_p10_144.prov_cn_max,
                          RILS_p10_145.prov_cn_max, RILS_p10_146.prov_cn_max, RILS_p10_147.prov_cn_max, RILS_p10_148.prov_cn_max, RILS_p10_149.prov_cn_max,
                          RILS_p10_150.prov_cn_max, RILS_p10_151.prov_cn_max, RILS_p10_152.prov_cn_max, RILS_p10_153.prov_cn_max, RILS_p10_154.prov_cn_max,
                          RILS_p10_155.prov_cn_max, RILS_p10_156.prov_cn_max, RILS_p10_157.prov_cn_max, RILS_p10_158.prov_cn_max, RILS_p10_159.prov_cn_max,
                          RILS_p10_160.prov_cn_max, RILS_p10_161.prov_cn_max, RILS_p10_162.prov_cn_max, RILS_p10_163.prov_cn_max, RILS_p10_164.prov_cn_max,
                          RILS_p10_165.prov_cn_max, RILS_p10_166.prov_cn_max, RILS_p10_167.prov_cn_max, RILS_p10_168.prov_cn_max, RILS_p10_169.prov_cn_max,
                          RILS_p10_170.prov_cn_max, RILS_p10_171.prov_cn_max, RILS_p10_172.prov_cn_max, RILS_p10_173.prov_cn_max, RILS_p10_174.prov_cn_max,
                          RILS_p10_175.prov_cn_max, RILS_p10_176.prov_cn_max, RILS_p10_177.prov_cn_max, RILS_p10_178.prov_cn_max, RILS_p10_179.prov_cn_max,
                          RILS_p10_180.prov_cn_max, RILS_p10_181.prov_cn_max, RILS_p10_182.prov_cn_max, RILS_p10_183.prov_cn_max, RILS_p10_184.prov_cn_max,
                          RILS_p10_185.prov_cn_max, RILS_p10_186.prov_cn_max, RILS_p10_187.prov_cn_max, RILS_p10_188.prov_cn_max, RILS_p10_189.prov_cn_max,
                          RILS_p10_190.prov_cn_max, RILS_p10_191.prov_cn_max, RILS_p10_192.prov_cn_max, RILS_p10_193.prov_cn_max, RILS_p10_194.prov_cn_max,
                          RILS_p10_195.prov_cn_max, RILS_p10_196.prov_cn_max, RILS_p10_197.prov_cn_max, RILS_p10_198.prov_cn_max, RILS_p10_199.prov_cn_max)


max_prov_customers_RILS_p10_mean = [np.mean(i) for i in max_prov_customers_RILS_p10]
max_prov_customers_RILS_p10_lower = [np.percentile(i, 10) for i in max_prov_customers_RILS_p10]
max_prov_customers_RILS_p10_upper = [np.percentile(i, 90) for i in max_prov_customers_RILS_p10]

########################################################

# Submission fees and transaction fees for RIL10 and RILS10

print('Creating sub_fee_buyer_av_RIL_p10')

sub_fee_buyer_av_RIL_p10 = zip(RIL_p10_00.sub_fee_buyer_av, RIL_p10_01.sub_fee_buyer_av, RIL_p10_02.sub_fee_buyer_av, RIL_p10_03.sub_fee_buyer_av, RIL_p10_04.sub_fee_buyer_av,
                          RIL_p10_05.sub_fee_buyer_av, RIL_p10_06.sub_fee_buyer_av, RIL_p10_07.sub_fee_buyer_av, RIL_p10_08.sub_fee_buyer_av, RIL_p10_09.sub_fee_buyer_av,
                          RIL_p10_10.sub_fee_buyer_av, RIL_p10_11.sub_fee_buyer_av, RIL_p10_12.sub_fee_buyer_av, RIL_p10_13.sub_fee_buyer_av, RIL_p10_14.sub_fee_buyer_av,
                          RIL_p10_15.sub_fee_buyer_av, RIL_p10_16.sub_fee_buyer_av, RIL_p10_17.sub_fee_buyer_av, RIL_p10_18.sub_fee_buyer_av, RIL_p10_19.sub_fee_buyer_av,
                          RIL_p10_20.sub_fee_buyer_av, RIL_p10_21.sub_fee_buyer_av, RIL_p10_22.sub_fee_buyer_av, RIL_p10_23.sub_fee_buyer_av, RIL_p10_24.sub_fee_buyer_av,
                          RIL_p10_25.sub_fee_buyer_av, RIL_p10_26.sub_fee_buyer_av, RIL_p10_27.sub_fee_buyer_av, RIL_p10_28.sub_fee_buyer_av, RIL_p10_29.sub_fee_buyer_av,
                          RIL_p10_30.sub_fee_buyer_av, RIL_p10_31.sub_fee_buyer_av, RIL_p10_32.sub_fee_buyer_av, RIL_p10_33.sub_fee_buyer_av, RIL_p10_34.sub_fee_buyer_av,
                          RIL_p10_35.sub_fee_buyer_av, RIL_p10_36.sub_fee_buyer_av, RIL_p10_37.sub_fee_buyer_av, RIL_p10_38.sub_fee_buyer_av, RIL_p10_39.sub_fee_buyer_av,
                          RIL_p10_40.sub_fee_buyer_av, RIL_p10_40.sub_fee_buyer_av, RIL_p10_41.sub_fee_buyer_av, RIL_p10_42.sub_fee_buyer_av, RIL_p10_43.sub_fee_buyer_av,
                          RIL_p10_44.sub_fee_buyer_av, RIL_p10_45.sub_fee_buyer_av, RIL_p10_46.sub_fee_buyer_av, RIL_p10_47.sub_fee_buyer_av, RIL_p10_48.sub_fee_buyer_av,
                          RIL_p10_49.sub_fee_buyer_av, RIL_p10_50.sub_fee_buyer_av, RIL_p10_51.sub_fee_buyer_av, RIL_p10_52.sub_fee_buyer_av, RIL_p10_53.sub_fee_buyer_av,
                          RIL_p10_54.sub_fee_buyer_av, RIL_p10_55.sub_fee_buyer_av, RIL_p10_56.sub_fee_buyer_av, RIL_p10_57.sub_fee_buyer_av, RIL_p10_58.sub_fee_buyer_av,
                          RIL_p10_59.sub_fee_buyer_av, RIL_p10_60.sub_fee_buyer_av, RIL_p10_61.sub_fee_buyer_av, RIL_p10_62.sub_fee_buyer_av, RIL_p10_63.sub_fee_buyer_av,
                          RIL_p10_64.sub_fee_buyer_av, RIL_p10_65.sub_fee_buyer_av, RIL_p10_66.sub_fee_buyer_av, RIL_p10_67.sub_fee_buyer_av, RIL_p10_68.sub_fee_buyer_av,
                          RIL_p10_69.sub_fee_buyer_av, RIL_p10_70.sub_fee_buyer_av, RIL_p10_71.sub_fee_buyer_av, RIL_p10_72.sub_fee_buyer_av, RIL_p10_73.sub_fee_buyer_av,
                          RIL_p10_74.sub_fee_buyer_av, RIL_p10_75.sub_fee_buyer_av, RIL_p10_76.sub_fee_buyer_av, RIL_p10_77.sub_fee_buyer_av, RIL_p10_78.sub_fee_buyer_av,
                          RIL_p10_79.sub_fee_buyer_av, RIL_p10_80.sub_fee_buyer_av, RIL_p10_81.sub_fee_buyer_av, RIL_p10_82.sub_fee_buyer_av, RIL_p10_83.sub_fee_buyer_av,
                          RIL_p10_84.sub_fee_buyer_av, RIL_p10_85.sub_fee_buyer_av, RIL_p10_86.sub_fee_buyer_av, RIL_p10_87.sub_fee_buyer_av, RIL_p10_88.sub_fee_buyer_av,
                          RIL_p10_89.sub_fee_buyer_av, RIL_p10_90.sub_fee_buyer_av, RIL_p10_91.sub_fee_buyer_av, RIL_p10_92.sub_fee_buyer_av, RIL_p10_93.sub_fee_buyer_av,
                          RIL_p10_94.sub_fee_buyer_av, RIL_p10_95.sub_fee_buyer_av, RIL_p10_96.sub_fee_buyer_av, RIL_p10_97.sub_fee_buyer_av, RIL_p10_98.sub_fee_buyer_av,
                          RIL_p10_99.sub_fee_buyer_av, RIL_p10_100.sub_fee_buyer_av,
                          RIL_p10_101.sub_fee_buyer_av, RIL_p10_102.sub_fee_buyer_av, RIL_p10_103.sub_fee_buyer_av, RIL_p10_104.sub_fee_buyer_av, RIL_p10_105.sub_fee_buyer_av,
                          RIL_p10_106.sub_fee_buyer_av, RIL_p10_107.sub_fee_buyer_av, RIL_p10_108.sub_fee_buyer_av, RIL_p10_109.sub_fee_buyer_av, RIL_p10_110.sub_fee_buyer_av,
                          RIL_p10_111.sub_fee_buyer_av, RIL_p10_112.sub_fee_buyer_av, RIL_p10_113.sub_fee_buyer_av, RIL_p10_114.sub_fee_buyer_av, RIL_p10_115.sub_fee_buyer_av,
                          RIL_p10_116.sub_fee_buyer_av, RIL_p10_117.sub_fee_buyer_av, RIL_p10_118.sub_fee_buyer_av, RIL_p10_119.sub_fee_buyer_av, RIL_p10_120.sub_fee_buyer_av,
                          RIL_p10_121.sub_fee_buyer_av, RIL_p10_122.sub_fee_buyer_av, RIL_p10_123.sub_fee_buyer_av, RIL_p10_124.sub_fee_buyer_av, RIL_p10_125.sub_fee_buyer_av,
                          RIL_p10_126.sub_fee_buyer_av, RIL_p10_127.sub_fee_buyer_av, RIL_p10_128.sub_fee_buyer_av, RIL_p10_129.sub_fee_buyer_av, RIL_p10_130.sub_fee_buyer_av,
                          RIL_p10_131.sub_fee_buyer_av, RIL_p10_132.sub_fee_buyer_av, RIL_p10_133.sub_fee_buyer_av, RIL_p10_134.sub_fee_buyer_av, RIL_p10_135.sub_fee_buyer_av,
                          RIL_p10_136.sub_fee_buyer_av, RIL_p10_137.sub_fee_buyer_av, RIL_p10_138.sub_fee_buyer_av, RIL_p10_139.sub_fee_buyer_av,
                          RIL_p10_140.sub_fee_buyer_av, RIL_p10_141.sub_fee_buyer_av, RIL_p10_142.sub_fee_buyer_av, RIL_p10_143.sub_fee_buyer_av, RIL_p10_144.sub_fee_buyer_av,
                          RIL_p10_145.sub_fee_buyer_av, RIL_p10_146.sub_fee_buyer_av, RIL_p10_147.sub_fee_buyer_av, RIL_p10_148.sub_fee_buyer_av, RIL_p10_149.sub_fee_buyer_av,
                          RIL_p10_150.sub_fee_buyer_av, RIL_p10_151.sub_fee_buyer_av, RIL_p10_152.sub_fee_buyer_av, RIL_p10_153.sub_fee_buyer_av, RIL_p10_154.sub_fee_buyer_av,
                          RIL_p10_155.sub_fee_buyer_av, RIL_p10_156.sub_fee_buyer_av, RIL_p10_157.sub_fee_buyer_av, RIL_p10_158.sub_fee_buyer_av, RIL_p10_159.sub_fee_buyer_av,
                          RIL_p10_160.sub_fee_buyer_av, RIL_p10_161.sub_fee_buyer_av, RIL_p10_162.sub_fee_buyer_av, RIL_p10_163.sub_fee_buyer_av, RIL_p10_164.sub_fee_buyer_av,
                          RIL_p10_165.sub_fee_buyer_av, RIL_p10_166.sub_fee_buyer_av, RIL_p10_167.sub_fee_buyer_av, RIL_p10_168.sub_fee_buyer_av, RIL_p10_169.sub_fee_buyer_av,
                          RIL_p10_170.sub_fee_buyer_av, RIL_p10_171.sub_fee_buyer_av, RIL_p10_172.sub_fee_buyer_av, RIL_p10_173.sub_fee_buyer_av, RIL_p10_174.sub_fee_buyer_av,
                          RIL_p10_175.sub_fee_buyer_av, RIL_p10_176.sub_fee_buyer_av, RIL_p10_177.sub_fee_buyer_av, RIL_p10_178.sub_fee_buyer_av, RIL_p10_179.sub_fee_buyer_av,
                          RIL_p10_180.sub_fee_buyer_av, RIL_p10_181.sub_fee_buyer_av, RIL_p10_182.sub_fee_buyer_av, RIL_p10_183.sub_fee_buyer_av, RIL_p10_184.sub_fee_buyer_av,
                          RIL_p10_185.sub_fee_buyer_av, RIL_p10_186.sub_fee_buyer_av, RIL_p10_187.sub_fee_buyer_av, RIL_p10_188.sub_fee_buyer_av, RIL_p10_189.sub_fee_buyer_av,
                          RIL_p10_190.sub_fee_buyer_av, RIL_p10_191.sub_fee_buyer_av, RIL_p10_192.sub_fee_buyer_av, RIL_p10_193.sub_fee_buyer_av, RIL_p10_194.sub_fee_buyer_av,
                          RIL_p10_195.sub_fee_buyer_av, RIL_p10_196.sub_fee_buyer_av, RIL_p10_197.sub_fee_buyer_av, RIL_p10_198.sub_fee_buyer_av, RIL_p10_199.sub_fee_buyer_av)


sub_fee_buyer_av_RIL_p10_mean = [np.mean(i) for i in sub_fee_buyer_av_RIL_p10]
sub_fee_buyer_av_RIL_p10_lower = [np.percentile(i, 10) for i in sub_fee_buyer_av_RIL_p10]
sub_fee_buyer_av_RIL_p10_upper = [np.percentile(i, 90) for i in sub_fee_buyer_av_RIL_p10]

print('Creating sub_fee_buyer_av_RILS_p10')
sub_fee_buyer_av_RILS_p10 = zip(RILS_p10_00.sub_fee_buyer_av, RILS_p10_01.sub_fee_buyer_av, RILS_p10_02.sub_fee_buyer_av, RILS_p10_03.sub_fee_buyer_av, RILS_p10_04.sub_fee_buyer_av,
                          RILS_p10_05.sub_fee_buyer_av, RILS_p10_06.sub_fee_buyer_av, RILS_p10_07.sub_fee_buyer_av, RILS_p10_08.sub_fee_buyer_av, RILS_p10_09.sub_fee_buyer_av,
                          RILS_p10_10.sub_fee_buyer_av, RILS_p10_11.sub_fee_buyer_av, RILS_p10_12.sub_fee_buyer_av, RILS_p10_13.sub_fee_buyer_av, RILS_p10_14.sub_fee_buyer_av,
                          RILS_p10_15.sub_fee_buyer_av, RILS_p10_16.sub_fee_buyer_av, RILS_p10_17.sub_fee_buyer_av, RILS_p10_18.sub_fee_buyer_av, RILS_p10_19.sub_fee_buyer_av,
                          RILS_p10_20.sub_fee_buyer_av, RILS_p10_21.sub_fee_buyer_av, RILS_p10_22.sub_fee_buyer_av, RILS_p10_23.sub_fee_buyer_av, RILS_p10_24.sub_fee_buyer_av,
                          RILS_p10_25.sub_fee_buyer_av, RILS_p10_26.sub_fee_buyer_av, RILS_p10_27.sub_fee_buyer_av, RILS_p10_28.sub_fee_buyer_av, RILS_p10_29.sub_fee_buyer_av,
                          RILS_p10_30.sub_fee_buyer_av, RILS_p10_31.sub_fee_buyer_av, RILS_p10_32.sub_fee_buyer_av, RILS_p10_33.sub_fee_buyer_av, RILS_p10_34.sub_fee_buyer_av,
                          RILS_p10_35.sub_fee_buyer_av, RILS_p10_36.sub_fee_buyer_av, RILS_p10_37.sub_fee_buyer_av, RILS_p10_38.sub_fee_buyer_av, RILS_p10_39.sub_fee_buyer_av,
                          RILS_p10_40.sub_fee_buyer_av, RILS_p10_40.sub_fee_buyer_av, RILS_p10_41.sub_fee_buyer_av, RILS_p10_42.sub_fee_buyer_av, RILS_p10_43.sub_fee_buyer_av,
                          RILS_p10_44.sub_fee_buyer_av, RILS_p10_45.sub_fee_buyer_av, RILS_p10_46.sub_fee_buyer_av, RILS_p10_47.sub_fee_buyer_av, RILS_p10_48.sub_fee_buyer_av,
                          RILS_p10_49.sub_fee_buyer_av, RILS_p10_50.sub_fee_buyer_av, RILS_p10_51.sub_fee_buyer_av, RILS_p10_52.sub_fee_buyer_av, RILS_p10_53.sub_fee_buyer_av,
                          RILS_p10_54.sub_fee_buyer_av, RILS_p10_55.sub_fee_buyer_av, RILS_p10_56.sub_fee_buyer_av, RILS_p10_57.sub_fee_buyer_av, RILS_p10_58.sub_fee_buyer_av,
                          RILS_p10_59.sub_fee_buyer_av, RILS_p10_60.sub_fee_buyer_av, RILS_p10_61.sub_fee_buyer_av, RILS_p10_62.sub_fee_buyer_av, RILS_p10_63.sub_fee_buyer_av,
                          RILS_p10_64.sub_fee_buyer_av, RILS_p10_65.sub_fee_buyer_av, RILS_p10_66.sub_fee_buyer_av, RILS_p10_67.sub_fee_buyer_av, RILS_p10_68.sub_fee_buyer_av,
                          RILS_p10_69.sub_fee_buyer_av, RILS_p10_70.sub_fee_buyer_av, RILS_p10_71.sub_fee_buyer_av, RILS_p10_72.sub_fee_buyer_av, RILS_p10_73.sub_fee_buyer_av,
                          RILS_p10_74.sub_fee_buyer_av, RILS_p10_75.sub_fee_buyer_av, RILS_p10_76.sub_fee_buyer_av, RILS_p10_77.sub_fee_buyer_av, RILS_p10_78.sub_fee_buyer_av,
                          RILS_p10_79.sub_fee_buyer_av, RILS_p10_80.sub_fee_buyer_av, RILS_p10_81.sub_fee_buyer_av, RILS_p10_82.sub_fee_buyer_av, RILS_p10_83.sub_fee_buyer_av,
                          RILS_p10_84.sub_fee_buyer_av, RILS_p10_85.sub_fee_buyer_av, RILS_p10_86.sub_fee_buyer_av, RILS_p10_87.sub_fee_buyer_av, RILS_p10_88.sub_fee_buyer_av,
                          RILS_p10_89.sub_fee_buyer_av, RILS_p10_90.sub_fee_buyer_av, RILS_p10_91.sub_fee_buyer_av, RILS_p10_92.sub_fee_buyer_av, RILS_p10_93.sub_fee_buyer_av,
                          RILS_p10_94.sub_fee_buyer_av, RILS_p10_95.sub_fee_buyer_av, RILS_p10_96.sub_fee_buyer_av, RILS_p10_97.sub_fee_buyer_av, RILS_p10_98.sub_fee_buyer_av,
                          RILS_p10_99.sub_fee_buyer_av, RILS_p10_100.sub_fee_buyer_av,
                          RILS_p10_101.sub_fee_buyer_av, RILS_p10_102.sub_fee_buyer_av, RILS_p10_103.sub_fee_buyer_av, RILS_p10_104.sub_fee_buyer_av, RILS_p10_105.sub_fee_buyer_av,
                          RILS_p10_106.sub_fee_buyer_av, RILS_p10_107.sub_fee_buyer_av, RILS_p10_108.sub_fee_buyer_av, RILS_p10_109.sub_fee_buyer_av, RILS_p10_110.sub_fee_buyer_av,
                          RILS_p10_111.sub_fee_buyer_av, RILS_p10_112.sub_fee_buyer_av, RILS_p10_113.sub_fee_buyer_av, RILS_p10_114.sub_fee_buyer_av, RILS_p10_115.sub_fee_buyer_av,
                          RILS_p10_116.sub_fee_buyer_av, RILS_p10_117.sub_fee_buyer_av, RILS_p10_118.sub_fee_buyer_av, RILS_p10_119.sub_fee_buyer_av, RILS_p10_120.sub_fee_buyer_av,
                          RILS_p10_121.sub_fee_buyer_av, RILS_p10_122.sub_fee_buyer_av, RILS_p10_123.sub_fee_buyer_av, RILS_p10_124.sub_fee_buyer_av, RILS_p10_125.sub_fee_buyer_av,
                          RILS_p10_126.sub_fee_buyer_av, RILS_p10_127.sub_fee_buyer_av, RILS_p10_128.sub_fee_buyer_av, RILS_p10_129.sub_fee_buyer_av, RILS_p10_130.sub_fee_buyer_av,
                          RILS_p10_131.sub_fee_buyer_av, RILS_p10_132.sub_fee_buyer_av, RILS_p10_133.sub_fee_buyer_av, RILS_p10_134.sub_fee_buyer_av, RILS_p10_135.sub_fee_buyer_av,
                          RILS_p10_136.sub_fee_buyer_av, RILS_p10_137.sub_fee_buyer_av, RILS_p10_138.sub_fee_buyer_av, RILS_p10_139.sub_fee_buyer_av, RILS_p10_140.sub_fee_buyer_av,
                          RILS_p10_140.sub_fee_buyer_av, RILS_p10_141.sub_fee_buyer_av, RILS_p10_142.sub_fee_buyer_av, RILS_p10_143.sub_fee_buyer_av, RILS_p10_144.sub_fee_buyer_av,
                          RILS_p10_145.sub_fee_buyer_av, RILS_p10_146.sub_fee_buyer_av, RILS_p10_147.sub_fee_buyer_av, RILS_p10_148.sub_fee_buyer_av, RILS_p10_149.sub_fee_buyer_av,
                          RILS_p10_150.sub_fee_buyer_av, RILS_p10_151.sub_fee_buyer_av, RILS_p10_152.sub_fee_buyer_av, RILS_p10_153.sub_fee_buyer_av, RILS_p10_154.sub_fee_buyer_av,
                          RILS_p10_155.sub_fee_buyer_av, RILS_p10_156.sub_fee_buyer_av, RILS_p10_157.sub_fee_buyer_av, RILS_p10_158.sub_fee_buyer_av, RILS_p10_159.sub_fee_buyer_av,
                          RILS_p10_160.sub_fee_buyer_av, RILS_p10_161.sub_fee_buyer_av, RILS_p10_162.sub_fee_buyer_av, RILS_p10_163.sub_fee_buyer_av, RILS_p10_164.sub_fee_buyer_av,
                          RILS_p10_165.sub_fee_buyer_av, RILS_p10_166.sub_fee_buyer_av, RILS_p10_167.sub_fee_buyer_av, RILS_p10_168.sub_fee_buyer_av, RILS_p10_169.sub_fee_buyer_av,
                          RILS_p10_170.sub_fee_buyer_av, RILS_p10_171.sub_fee_buyer_av, RILS_p10_172.sub_fee_buyer_av, RILS_p10_173.sub_fee_buyer_av, RILS_p10_174.sub_fee_buyer_av,
                          RILS_p10_175.sub_fee_buyer_av, RILS_p10_176.sub_fee_buyer_av, RILS_p10_177.sub_fee_buyer_av, RILS_p10_178.sub_fee_buyer_av, RILS_p10_179.sub_fee_buyer_av,
                          RILS_p10_180.sub_fee_buyer_av, RILS_p10_181.sub_fee_buyer_av, RILS_p10_182.sub_fee_buyer_av, RILS_p10_183.sub_fee_buyer_av, RILS_p10_184.sub_fee_buyer_av,
                          RILS_p10_185.sub_fee_buyer_av, RILS_p10_186.sub_fee_buyer_av, RILS_p10_187.sub_fee_buyer_av, RILS_p10_188.sub_fee_buyer_av, RILS_p10_189.sub_fee_buyer_av,
                          RILS_p10_190.sub_fee_buyer_av, RILS_p10_191.sub_fee_buyer_av, RILS_p10_192.sub_fee_buyer_av, RILS_p10_193.sub_fee_buyer_av, RILS_p10_194.sub_fee_buyer_av,
                          RILS_p10_195.sub_fee_buyer_av, RILS_p10_196.sub_fee_buyer_av, RILS_p10_197.sub_fee_buyer_av, RILS_p10_198.sub_fee_buyer_av, RILS_p10_199.sub_fee_buyer_av)


sub_fee_buyer_av_RILS_p10_mean = [np.mean(i) for i in sub_fee_buyer_av_RILS_p10]
sub_fee_buyer_av_RILS_p10_lower = [np.percentile(i, 10) for i in sub_fee_buyer_av_RILS_p10]
sub_fee_buyer_av_RILS_p10_upper = [np.percentile(i, 90) for i in sub_fee_buyer_av_RILS_p10]

print('Creating sub_fee_seller_av_RIL_p10')
sub_fee_seller_av_RIL_p10 = zip(RIL_p10_00.sub_fee_seller_av, RIL_p10_01.sub_fee_seller_av, RIL_p10_02.sub_fee_seller_av, RIL_p10_03.sub_fee_seller_av, RIL_p10_04.sub_fee_seller_av,
                          RIL_p10_05.sub_fee_seller_av, RIL_p10_06.sub_fee_seller_av, RIL_p10_07.sub_fee_seller_av, RIL_p10_08.sub_fee_seller_av, RIL_p10_09.sub_fee_seller_av,
                          RIL_p10_10.sub_fee_seller_av, RIL_p10_11.sub_fee_seller_av, RIL_p10_12.sub_fee_seller_av, RIL_p10_13.sub_fee_seller_av, RIL_p10_14.sub_fee_seller_av,
                          RIL_p10_15.sub_fee_seller_av, RIL_p10_16.sub_fee_seller_av, RIL_p10_17.sub_fee_seller_av, RIL_p10_18.sub_fee_seller_av, RIL_p10_19.sub_fee_seller_av,
                          RIL_p10_20.sub_fee_seller_av, RIL_p10_21.sub_fee_seller_av, RIL_p10_22.sub_fee_seller_av, RIL_p10_23.sub_fee_seller_av, RIL_p10_24.sub_fee_seller_av,
                          RIL_p10_25.sub_fee_seller_av, RIL_p10_26.sub_fee_seller_av, RIL_p10_27.sub_fee_seller_av, RIL_p10_28.sub_fee_seller_av, RIL_p10_29.sub_fee_seller_av,
                          RIL_p10_30.sub_fee_seller_av, RIL_p10_31.sub_fee_seller_av, RIL_p10_32.sub_fee_seller_av, RIL_p10_33.sub_fee_seller_av, RIL_p10_34.sub_fee_seller_av,
                          RIL_p10_35.sub_fee_seller_av, RIL_p10_36.sub_fee_seller_av, RIL_p10_37.sub_fee_seller_av, RIL_p10_38.sub_fee_seller_av, RIL_p10_39.sub_fee_seller_av,
                          RIL_p10_40.sub_fee_seller_av, RIL_p10_40.sub_fee_seller_av, RIL_p10_41.sub_fee_seller_av, RIL_p10_42.sub_fee_seller_av, RIL_p10_43.sub_fee_seller_av,
                          RIL_p10_44.sub_fee_seller_av, RIL_p10_45.sub_fee_seller_av, RIL_p10_46.sub_fee_seller_av, RIL_p10_47.sub_fee_seller_av, RIL_p10_48.sub_fee_seller_av,
                          RIL_p10_49.sub_fee_seller_av, RIL_p10_50.sub_fee_seller_av, RIL_p10_51.sub_fee_seller_av, RIL_p10_52.sub_fee_seller_av, RIL_p10_53.sub_fee_seller_av,
                          RIL_p10_54.sub_fee_seller_av, RIL_p10_55.sub_fee_seller_av, RIL_p10_56.sub_fee_seller_av, RIL_p10_57.sub_fee_seller_av, RIL_p10_58.sub_fee_seller_av,
                          RIL_p10_59.sub_fee_seller_av, RIL_p10_60.sub_fee_seller_av, RIL_p10_61.sub_fee_seller_av, RIL_p10_62.sub_fee_seller_av, RIL_p10_63.sub_fee_seller_av,
                          RIL_p10_64.sub_fee_seller_av, RIL_p10_65.sub_fee_seller_av, RIL_p10_66.sub_fee_seller_av, RIL_p10_67.sub_fee_seller_av, RIL_p10_68.sub_fee_seller_av,
                          RIL_p10_69.sub_fee_seller_av, RIL_p10_70.sub_fee_seller_av, RIL_p10_71.sub_fee_seller_av, RIL_p10_72.sub_fee_seller_av, RIL_p10_73.sub_fee_seller_av,
                          RIL_p10_74.sub_fee_seller_av, RIL_p10_75.sub_fee_seller_av, RIL_p10_76.sub_fee_seller_av, RIL_p10_77.sub_fee_seller_av, RIL_p10_78.sub_fee_seller_av,
                          RIL_p10_79.sub_fee_seller_av, RIL_p10_80.sub_fee_seller_av, RIL_p10_81.sub_fee_seller_av, RIL_p10_82.sub_fee_seller_av, RIL_p10_83.sub_fee_seller_av,
                          RIL_p10_84.sub_fee_seller_av, RIL_p10_85.sub_fee_seller_av, RIL_p10_86.sub_fee_seller_av, RIL_p10_87.sub_fee_seller_av, RIL_p10_88.sub_fee_seller_av,
                          RIL_p10_89.sub_fee_seller_av, RIL_p10_90.sub_fee_seller_av, RIL_p10_91.sub_fee_seller_av, RIL_p10_92.sub_fee_seller_av, RIL_p10_93.sub_fee_seller_av,
                          RIL_p10_94.sub_fee_seller_av, RIL_p10_95.sub_fee_seller_av, RIL_p10_96.sub_fee_seller_av, RIL_p10_97.sub_fee_seller_av, RIL_p10_98.sub_fee_seller_av,
                          RIL_p10_99.sub_fee_seller_av, RIL_p10_100.sub_fee_seller_av,
                          RIL_p10_101.sub_fee_seller_av, RIL_p10_102.sub_fee_seller_av, RIL_p10_103.sub_fee_seller_av, RIL_p10_104.sub_fee_seller_av, RIL_p10_105.sub_fee_seller_av,
                          RIL_p10_106.sub_fee_seller_av, RIL_p10_107.sub_fee_seller_av, RIL_p10_108.sub_fee_seller_av, RIL_p10_109.sub_fee_seller_av, RIL_p10_110.sub_fee_seller_av,
                          RIL_p10_111.sub_fee_seller_av, RIL_p10_112.sub_fee_seller_av, RIL_p10_113.sub_fee_seller_av, RIL_p10_114.sub_fee_seller_av, RIL_p10_115.sub_fee_seller_av,
                          RIL_p10_116.sub_fee_seller_av, RIL_p10_117.sub_fee_seller_av, RIL_p10_118.sub_fee_seller_av, RIL_p10_119.sub_fee_seller_av, RIL_p10_120.sub_fee_seller_av,
                          RIL_p10_121.sub_fee_seller_av, RIL_p10_122.sub_fee_seller_av, RIL_p10_123.sub_fee_seller_av, RIL_p10_124.sub_fee_seller_av, RIL_p10_125.sub_fee_seller_av,
                          RIL_p10_126.sub_fee_seller_av, RIL_p10_127.sub_fee_seller_av, RIL_p10_128.sub_fee_seller_av, RIL_p10_129.sub_fee_seller_av, RIL_p10_130.sub_fee_seller_av,
                          RIL_p10_131.sub_fee_seller_av, RIL_p10_132.sub_fee_seller_av, RIL_p10_133.sub_fee_seller_av, RIL_p10_134.sub_fee_seller_av, RIL_p10_135.sub_fee_seller_av,
                          RIL_p10_136.sub_fee_seller_av, RIL_p10_137.sub_fee_seller_av, RIL_p10_138.sub_fee_seller_av, RIL_p10_139.sub_fee_seller_av,
                          RIL_p10_140.sub_fee_seller_av, RIL_p10_141.sub_fee_seller_av, RIL_p10_142.sub_fee_seller_av, RIL_p10_143.sub_fee_seller_av, RIL_p10_144.sub_fee_seller_av,
                          RIL_p10_145.sub_fee_seller_av, RIL_p10_146.sub_fee_seller_av, RIL_p10_147.sub_fee_seller_av, RIL_p10_148.sub_fee_seller_av, RIL_p10_149.sub_fee_seller_av,
                          RIL_p10_150.sub_fee_seller_av, RIL_p10_151.sub_fee_seller_av, RIL_p10_152.sub_fee_seller_av, RIL_p10_153.sub_fee_seller_av, RIL_p10_154.sub_fee_seller_av,
                          RIL_p10_155.sub_fee_seller_av, RIL_p10_156.sub_fee_seller_av, RIL_p10_157.sub_fee_seller_av, RIL_p10_158.sub_fee_seller_av, RIL_p10_159.sub_fee_seller_av,
                          RIL_p10_160.sub_fee_seller_av, RIL_p10_161.sub_fee_seller_av, RIL_p10_162.sub_fee_seller_av, RIL_p10_163.sub_fee_seller_av, RIL_p10_164.sub_fee_seller_av,
                          RIL_p10_165.sub_fee_seller_av, RIL_p10_166.sub_fee_seller_av, RIL_p10_167.sub_fee_seller_av, RIL_p10_168.sub_fee_seller_av, RIL_p10_169.sub_fee_seller_av,
                          RIL_p10_170.sub_fee_seller_av, RIL_p10_171.sub_fee_seller_av, RIL_p10_172.sub_fee_seller_av, RIL_p10_173.sub_fee_seller_av, RIL_p10_174.sub_fee_seller_av,
                          RIL_p10_175.sub_fee_seller_av, RIL_p10_176.sub_fee_seller_av, RIL_p10_177.sub_fee_seller_av, RIL_p10_178.sub_fee_seller_av, RIL_p10_179.sub_fee_seller_av,
                          RIL_p10_180.sub_fee_seller_av, RIL_p10_181.sub_fee_seller_av, RIL_p10_182.sub_fee_seller_av, RIL_p10_183.sub_fee_seller_av, RIL_p10_184.sub_fee_seller_av,
                          RIL_p10_185.sub_fee_seller_av, RIL_p10_186.sub_fee_seller_av, RIL_p10_187.sub_fee_seller_av, RIL_p10_188.sub_fee_seller_av, RIL_p10_189.sub_fee_seller_av,
                          RIL_p10_190.sub_fee_seller_av, RIL_p10_191.sub_fee_seller_av, RIL_p10_192.sub_fee_seller_av, RIL_p10_193.sub_fee_seller_av, RIL_p10_194.sub_fee_seller_av,
                          RIL_p10_195.sub_fee_seller_av, RIL_p10_196.sub_fee_seller_av, RIL_p10_197.sub_fee_seller_av, RIL_p10_198.sub_fee_seller_av, RIL_p10_199.sub_fee_seller_av)


sub_fee_seller_av_RIL_p10_mean = [np.mean(i) for i in sub_fee_seller_av_RIL_p10]
sub_fee_seller_av_RIL_p10_lower = [np.percentile(i, 10) for i in sub_fee_seller_av_RIL_p10]
sub_fee_seller_av_RIL_p10_upper = [np.percentile(i, 90) for i in sub_fee_seller_av_RIL_p10]

print('Creating sub_fee_seller_av_RILS_p10')
sub_fee_seller_av_RILS_p10 = zip(RILS_p10_00.sub_fee_seller_av, RILS_p10_01.sub_fee_seller_av, RILS_p10_02.sub_fee_seller_av, RILS_p10_03.sub_fee_seller_av, RILS_p10_04.sub_fee_seller_av,
                          RILS_p10_05.sub_fee_seller_av, RILS_p10_06.sub_fee_seller_av, RILS_p10_07.sub_fee_seller_av, RILS_p10_08.sub_fee_seller_av, RILS_p10_09.sub_fee_seller_av,
                          RILS_p10_10.sub_fee_seller_av, RILS_p10_11.sub_fee_seller_av, RILS_p10_12.sub_fee_seller_av, RILS_p10_13.sub_fee_seller_av, RILS_p10_14.sub_fee_seller_av,
                          RILS_p10_15.sub_fee_seller_av, RILS_p10_16.sub_fee_seller_av, RILS_p10_17.sub_fee_seller_av, RILS_p10_18.sub_fee_seller_av, RILS_p10_19.sub_fee_seller_av,
                          RILS_p10_20.sub_fee_seller_av, RILS_p10_21.sub_fee_seller_av, RILS_p10_22.sub_fee_seller_av, RILS_p10_23.sub_fee_seller_av, RILS_p10_24.sub_fee_seller_av,
                          RILS_p10_25.sub_fee_seller_av, RILS_p10_26.sub_fee_seller_av, RILS_p10_27.sub_fee_seller_av, RILS_p10_28.sub_fee_seller_av, RILS_p10_29.sub_fee_seller_av,
                          RILS_p10_30.sub_fee_seller_av, RILS_p10_31.sub_fee_seller_av, RILS_p10_32.sub_fee_seller_av, RILS_p10_33.sub_fee_seller_av, RILS_p10_34.sub_fee_seller_av,
                          RILS_p10_35.sub_fee_seller_av, RILS_p10_36.sub_fee_seller_av, RILS_p10_37.sub_fee_seller_av, RILS_p10_38.sub_fee_seller_av, RILS_p10_39.sub_fee_seller_av,
                          RILS_p10_40.sub_fee_seller_av, RILS_p10_40.sub_fee_seller_av, RILS_p10_41.sub_fee_seller_av, RILS_p10_42.sub_fee_seller_av, RILS_p10_43.sub_fee_seller_av,
                          RILS_p10_44.sub_fee_seller_av, RILS_p10_45.sub_fee_seller_av, RILS_p10_46.sub_fee_seller_av, RILS_p10_47.sub_fee_seller_av, RILS_p10_48.sub_fee_seller_av,
                          RILS_p10_49.sub_fee_seller_av, RILS_p10_50.sub_fee_seller_av, RILS_p10_51.sub_fee_seller_av, RILS_p10_52.sub_fee_seller_av, RILS_p10_53.sub_fee_seller_av,
                          RILS_p10_54.sub_fee_seller_av, RILS_p10_55.sub_fee_seller_av, RILS_p10_56.sub_fee_seller_av, RILS_p10_57.sub_fee_seller_av, RILS_p10_58.sub_fee_seller_av,
                          RILS_p10_59.sub_fee_seller_av, RILS_p10_60.sub_fee_seller_av, RILS_p10_61.sub_fee_seller_av, RILS_p10_62.sub_fee_seller_av, RILS_p10_63.sub_fee_seller_av,
                          RILS_p10_64.sub_fee_seller_av, RILS_p10_65.sub_fee_seller_av, RILS_p10_66.sub_fee_seller_av, RILS_p10_67.sub_fee_seller_av, RILS_p10_68.sub_fee_seller_av,
                          RILS_p10_69.sub_fee_seller_av, RILS_p10_70.sub_fee_seller_av, RILS_p10_71.sub_fee_seller_av, RILS_p10_72.sub_fee_seller_av, RILS_p10_73.sub_fee_seller_av,
                          RILS_p10_74.sub_fee_seller_av, RILS_p10_75.sub_fee_seller_av, RILS_p10_76.sub_fee_seller_av, RILS_p10_77.sub_fee_seller_av, RILS_p10_78.sub_fee_seller_av,
                          RILS_p10_79.sub_fee_seller_av, RILS_p10_80.sub_fee_seller_av, RILS_p10_81.sub_fee_seller_av, RILS_p10_82.sub_fee_seller_av, RILS_p10_83.sub_fee_seller_av,
                          RILS_p10_84.sub_fee_seller_av, RILS_p10_85.sub_fee_seller_av, RILS_p10_86.sub_fee_seller_av, RILS_p10_87.sub_fee_seller_av, RILS_p10_88.sub_fee_seller_av,
                          RILS_p10_89.sub_fee_seller_av, RILS_p10_90.sub_fee_seller_av, RILS_p10_91.sub_fee_seller_av, RILS_p10_92.sub_fee_seller_av, RILS_p10_93.sub_fee_seller_av,
                          RILS_p10_94.sub_fee_seller_av, RILS_p10_95.sub_fee_seller_av, RILS_p10_96.sub_fee_seller_av, RILS_p10_97.sub_fee_seller_av, RILS_p10_98.sub_fee_seller_av,
                          RILS_p10_99.sub_fee_seller_av, RILS_p10_100.sub_fee_seller_av,
                          RILS_p10_101.sub_fee_seller_av, RILS_p10_102.sub_fee_seller_av, RILS_p10_103.sub_fee_seller_av, RILS_p10_104.sub_fee_seller_av, RILS_p10_105.sub_fee_seller_av,
                          RILS_p10_106.sub_fee_seller_av, RILS_p10_107.sub_fee_seller_av, RILS_p10_108.sub_fee_seller_av, RILS_p10_109.sub_fee_seller_av, RILS_p10_110.sub_fee_seller_av,
                          RILS_p10_111.sub_fee_seller_av, RILS_p10_112.sub_fee_seller_av, RILS_p10_113.sub_fee_seller_av, RILS_p10_114.sub_fee_seller_av, RILS_p10_115.sub_fee_seller_av,
                          RILS_p10_116.sub_fee_seller_av, RILS_p10_117.sub_fee_seller_av, RILS_p10_118.sub_fee_seller_av, RILS_p10_119.sub_fee_seller_av, RILS_p10_120.sub_fee_seller_av,
                          RILS_p10_121.sub_fee_seller_av, RILS_p10_122.sub_fee_seller_av, RILS_p10_123.sub_fee_seller_av, RILS_p10_124.sub_fee_seller_av, RILS_p10_125.sub_fee_seller_av,
                          RILS_p10_126.sub_fee_seller_av, RILS_p10_127.sub_fee_seller_av, RILS_p10_128.sub_fee_seller_av, RILS_p10_129.sub_fee_seller_av, RILS_p10_130.sub_fee_seller_av,
                          RILS_p10_131.sub_fee_seller_av, RILS_p10_132.sub_fee_seller_av, RILS_p10_133.sub_fee_seller_av, RILS_p10_134.sub_fee_seller_av, RILS_p10_135.sub_fee_seller_av,
                          RILS_p10_136.sub_fee_seller_av, RILS_p10_137.sub_fee_seller_av, RILS_p10_138.sub_fee_seller_av, RILS_p10_139.sub_fee_seller_av, RILS_p10_140.sub_fee_seller_av,
                          RILS_p10_140.sub_fee_seller_av, RILS_p10_141.sub_fee_seller_av, RILS_p10_142.sub_fee_seller_av, RILS_p10_143.sub_fee_seller_av, RILS_p10_144.sub_fee_seller_av,
                          RILS_p10_145.sub_fee_seller_av, RILS_p10_146.sub_fee_seller_av, RILS_p10_147.sub_fee_seller_av, RILS_p10_148.sub_fee_seller_av, RILS_p10_149.sub_fee_seller_av,
                          RILS_p10_150.sub_fee_seller_av, RILS_p10_151.sub_fee_seller_av, RILS_p10_152.sub_fee_seller_av, RILS_p10_153.sub_fee_seller_av, RILS_p10_154.sub_fee_seller_av,
                          RILS_p10_155.sub_fee_seller_av, RILS_p10_156.sub_fee_seller_av, RILS_p10_157.sub_fee_seller_av, RILS_p10_158.sub_fee_seller_av, RILS_p10_159.sub_fee_seller_av,
                          RILS_p10_160.sub_fee_seller_av, RILS_p10_161.sub_fee_seller_av, RILS_p10_162.sub_fee_seller_av, RILS_p10_163.sub_fee_seller_av, RILS_p10_164.sub_fee_seller_av,
                          RILS_p10_165.sub_fee_seller_av, RILS_p10_166.sub_fee_seller_av, RILS_p10_167.sub_fee_seller_av, RILS_p10_168.sub_fee_seller_av, RILS_p10_169.sub_fee_seller_av,
                          RILS_p10_170.sub_fee_seller_av, RILS_p10_171.sub_fee_seller_av, RILS_p10_172.sub_fee_seller_av, RILS_p10_173.sub_fee_seller_av, RILS_p10_174.sub_fee_seller_av,
                          RILS_p10_175.sub_fee_seller_av, RILS_p10_176.sub_fee_seller_av, RILS_p10_177.sub_fee_seller_av, RILS_p10_178.sub_fee_seller_av, RILS_p10_179.sub_fee_seller_av,
                          RILS_p10_180.sub_fee_seller_av, RILS_p10_181.sub_fee_seller_av, RILS_p10_182.sub_fee_seller_av, RILS_p10_183.sub_fee_seller_av, RILS_p10_184.sub_fee_seller_av,
                          RILS_p10_185.sub_fee_seller_av, RILS_p10_186.sub_fee_seller_av, RILS_p10_187.sub_fee_seller_av, RILS_p10_188.sub_fee_seller_av, RILS_p10_189.sub_fee_seller_av,
                          RILS_p10_190.sub_fee_seller_av, RILS_p10_191.sub_fee_seller_av, RILS_p10_192.sub_fee_seller_av, RILS_p10_193.sub_fee_seller_av, RILS_p10_194.sub_fee_seller_av,
                          RILS_p10_195.sub_fee_seller_av, RILS_p10_196.sub_fee_seller_av, RILS_p10_197.sub_fee_seller_av, RILS_p10_198.sub_fee_seller_av, RILS_p10_199.sub_fee_seller_av)


sub_fee_seller_av_RILS_p10_mean = [np.mean(i) for i in sub_fee_seller_av_RILS_p10]
sub_fee_seller_av_RILS_p10_lower = [np.percentile(i, 10) for i in sub_fee_seller_av_RILS_p10]
sub_fee_seller_av_RILS_p10_upper = [np.percentile(i, 90) for i in sub_fee_seller_av_RILS_p10]

print('Creating trans_fee_b_av_RIL_p10')
trans_fee_b_av_RIL_p10 = zip(RIL_p10_00.trans_fee_b_av, RIL_p10_01.trans_fee_b_av, RIL_p10_02.trans_fee_b_av, RIL_p10_03.trans_fee_b_av, RIL_p10_04.trans_fee_b_av,
                          RIL_p10_05.trans_fee_b_av, RIL_p10_06.trans_fee_b_av, RIL_p10_07.trans_fee_b_av, RIL_p10_08.trans_fee_b_av, RIL_p10_09.trans_fee_b_av,
                          RIL_p10_10.trans_fee_b_av, RIL_p10_11.trans_fee_b_av, RIL_p10_12.trans_fee_b_av, RIL_p10_13.trans_fee_b_av, RIL_p10_14.trans_fee_b_av,
                          RIL_p10_15.trans_fee_b_av, RIL_p10_16.trans_fee_b_av, RIL_p10_17.trans_fee_b_av, RIL_p10_18.trans_fee_b_av, RIL_p10_19.trans_fee_b_av,
                          RIL_p10_20.trans_fee_b_av, RIL_p10_21.trans_fee_b_av, RIL_p10_22.trans_fee_b_av, RIL_p10_23.trans_fee_b_av, RIL_p10_24.trans_fee_b_av,
                          RIL_p10_25.trans_fee_b_av, RIL_p10_26.trans_fee_b_av, RIL_p10_27.trans_fee_b_av, RIL_p10_28.trans_fee_b_av, RIL_p10_29.trans_fee_b_av,
                          RIL_p10_30.trans_fee_b_av, RIL_p10_31.trans_fee_b_av, RIL_p10_32.trans_fee_b_av, RIL_p10_33.trans_fee_b_av, RIL_p10_34.trans_fee_b_av,
                          RIL_p10_35.trans_fee_b_av, RIL_p10_36.trans_fee_b_av, RIL_p10_37.trans_fee_b_av, RIL_p10_38.trans_fee_b_av, RIL_p10_39.trans_fee_b_av,
                          RIL_p10_40.trans_fee_b_av, RIL_p10_40.trans_fee_b_av, RIL_p10_41.trans_fee_b_av, RIL_p10_42.trans_fee_b_av, RIL_p10_43.trans_fee_b_av,
                          RIL_p10_44.trans_fee_b_av, RIL_p10_45.trans_fee_b_av, RIL_p10_46.trans_fee_b_av, RIL_p10_47.trans_fee_b_av, RIL_p10_48.trans_fee_b_av,
                          RIL_p10_49.trans_fee_b_av, RIL_p10_50.trans_fee_b_av, RIL_p10_51.trans_fee_b_av, RIL_p10_52.trans_fee_b_av, RIL_p10_53.trans_fee_b_av,
                          RIL_p10_54.trans_fee_b_av, RIL_p10_55.trans_fee_b_av, RIL_p10_56.trans_fee_b_av, RIL_p10_57.trans_fee_b_av, RIL_p10_58.trans_fee_b_av,
                          RIL_p10_59.trans_fee_b_av, RIL_p10_60.trans_fee_b_av, RIL_p10_61.trans_fee_b_av, RIL_p10_62.trans_fee_b_av, RIL_p10_63.trans_fee_b_av,
                          RIL_p10_64.trans_fee_b_av, RIL_p10_65.trans_fee_b_av, RIL_p10_66.trans_fee_b_av, RIL_p10_67.trans_fee_b_av, RIL_p10_68.trans_fee_b_av,
                          RIL_p10_69.trans_fee_b_av, RIL_p10_70.trans_fee_b_av, RIL_p10_71.trans_fee_b_av, RIL_p10_72.trans_fee_b_av, RIL_p10_73.trans_fee_b_av,
                          RIL_p10_74.trans_fee_b_av, RIL_p10_75.trans_fee_b_av, RIL_p10_76.trans_fee_b_av, RIL_p10_77.trans_fee_b_av, RIL_p10_78.trans_fee_b_av,
                          RIL_p10_79.trans_fee_b_av, RIL_p10_80.trans_fee_b_av, RIL_p10_81.trans_fee_b_av, RIL_p10_82.trans_fee_b_av, RIL_p10_83.trans_fee_b_av,
                          RIL_p10_84.trans_fee_b_av, RIL_p10_85.trans_fee_b_av, RIL_p10_86.trans_fee_b_av, RIL_p10_87.trans_fee_b_av, RIL_p10_88.trans_fee_b_av,
                          RIL_p10_89.trans_fee_b_av, RIL_p10_90.trans_fee_b_av, RIL_p10_91.trans_fee_b_av, RIL_p10_92.trans_fee_b_av, RIL_p10_93.trans_fee_b_av,
                          RIL_p10_94.trans_fee_b_av, RIL_p10_95.trans_fee_b_av, RIL_p10_96.trans_fee_b_av, RIL_p10_97.trans_fee_b_av, RIL_p10_98.trans_fee_b_av,
                          RIL_p10_99.trans_fee_b_av, RIL_p10_100.trans_fee_b_av,
                          RIL_p10_101.trans_fee_b_av, RIL_p10_102.trans_fee_b_av, RIL_p10_103.trans_fee_b_av, RIL_p10_104.trans_fee_b_av, RIL_p10_105.trans_fee_b_av,
                          RIL_p10_106.trans_fee_b_av, RIL_p10_107.trans_fee_b_av, RIL_p10_108.trans_fee_b_av, RIL_p10_109.trans_fee_b_av, RIL_p10_110.trans_fee_b_av,
                          RIL_p10_111.trans_fee_b_av, RIL_p10_112.trans_fee_b_av, RIL_p10_113.trans_fee_b_av, RIL_p10_114.trans_fee_b_av, RIL_p10_115.trans_fee_b_av,
                          RIL_p10_116.trans_fee_b_av, RIL_p10_117.trans_fee_b_av, RIL_p10_118.trans_fee_b_av, RIL_p10_119.trans_fee_b_av, RIL_p10_120.trans_fee_b_av,
                          RIL_p10_121.trans_fee_b_av, RIL_p10_122.trans_fee_b_av, RIL_p10_123.trans_fee_b_av, RIL_p10_124.trans_fee_b_av, RIL_p10_125.trans_fee_b_av,
                          RIL_p10_126.trans_fee_b_av, RIL_p10_127.trans_fee_b_av, RIL_p10_128.trans_fee_b_av, RIL_p10_129.trans_fee_b_av, RIL_p10_130.trans_fee_b_av,
                          RIL_p10_131.trans_fee_b_av, RIL_p10_132.trans_fee_b_av, RIL_p10_133.trans_fee_b_av, RIL_p10_134.trans_fee_b_av, RIL_p10_135.trans_fee_b_av,
                          RIL_p10_136.trans_fee_b_av, RIL_p10_137.trans_fee_b_av, RIL_p10_138.trans_fee_b_av, RIL_p10_139.trans_fee_b_av, RIL_p10_140.trans_fee_b_av,
                          RIL_p10_140.trans_fee_b_av, RIL_p10_141.trans_fee_b_av, RIL_p10_142.trans_fee_b_av, RIL_p10_143.trans_fee_b_av, RIL_p10_144.trans_fee_b_av,
                          RIL_p10_145.trans_fee_b_av, RIL_p10_146.trans_fee_b_av, RIL_p10_147.trans_fee_b_av, RIL_p10_148.trans_fee_b_av, RIL_p10_149.trans_fee_b_av,
                          RIL_p10_150.trans_fee_b_av, RIL_p10_151.trans_fee_b_av, RIL_p10_152.trans_fee_b_av, RIL_p10_153.trans_fee_b_av, RIL_p10_154.trans_fee_b_av,
                          RIL_p10_155.trans_fee_b_av, RIL_p10_156.trans_fee_b_av, RIL_p10_157.trans_fee_b_av, RIL_p10_158.trans_fee_b_av, RIL_p10_159.trans_fee_b_av,
                          RIL_p10_160.trans_fee_b_av, RIL_p10_161.trans_fee_b_av, RIL_p10_162.trans_fee_b_av, RIL_p10_163.trans_fee_b_av, RIL_p10_164.trans_fee_b_av,
                          RIL_p10_165.trans_fee_b_av, RIL_p10_166.trans_fee_b_av, RIL_p10_167.trans_fee_b_av, RIL_p10_168.trans_fee_b_av, RIL_p10_169.trans_fee_b_av,
                          RIL_p10_170.trans_fee_b_av, RIL_p10_171.trans_fee_b_av, RIL_p10_172.trans_fee_b_av, RIL_p10_173.trans_fee_b_av, RIL_p10_174.trans_fee_b_av,
                          RIL_p10_175.trans_fee_b_av, RIL_p10_176.trans_fee_b_av, RIL_p10_177.trans_fee_b_av, RIL_p10_178.trans_fee_b_av, RIL_p10_179.trans_fee_b_av,
                          RIL_p10_180.trans_fee_b_av, RIL_p10_181.trans_fee_b_av, RIL_p10_182.trans_fee_b_av, RIL_p10_183.trans_fee_b_av, RIL_p10_184.trans_fee_b_av,
                          RIL_p10_185.trans_fee_b_av, RIL_p10_186.trans_fee_b_av, RIL_p10_187.trans_fee_b_av, RIL_p10_188.trans_fee_b_av, RIL_p10_189.trans_fee_b_av,
                          RIL_p10_190.trans_fee_b_av, RIL_p10_191.trans_fee_b_av, RIL_p10_192.trans_fee_b_av, RIL_p10_193.trans_fee_b_av, RIL_p10_194.trans_fee_b_av,
                          RIL_p10_195.trans_fee_b_av, RIL_p10_196.trans_fee_b_av, RIL_p10_197.trans_fee_b_av, RIL_p10_198.trans_fee_b_av, RIL_p10_199.trans_fee_b_av)


trans_fee_b_av_RIL_p10_mean = [np.mean(i) for i in trans_fee_b_av_RIL_p10]
trans_fee_b_av_RIL_p10_lower = [np.percentile(i, 10) for i in trans_fee_b_av_RIL_p10]
trans_fee_b_av_RIL_p10_upper = [np.percentile(i, 90) for i in trans_fee_b_av_RIL_p10]


print('Creating max_prov_rev_RILS_p10')
trans_fee_b_av_RILS_p10 = zip(RILS_p10_00.trans_fee_b_av, RILS_p10_01.trans_fee_b_av, RILS_p10_02.trans_fee_b_av, RILS_p10_03.trans_fee_b_av, RILS_p10_04.trans_fee_b_av,
                          RILS_p10_05.trans_fee_b_av, RILS_p10_06.trans_fee_b_av, RILS_p10_07.trans_fee_b_av, RILS_p10_08.trans_fee_b_av, RILS_p10_09.trans_fee_b_av,
                          RILS_p10_10.trans_fee_b_av, RILS_p10_11.trans_fee_b_av, RILS_p10_12.trans_fee_b_av, RILS_p10_13.trans_fee_b_av, RILS_p10_14.trans_fee_b_av,
                          RILS_p10_15.trans_fee_b_av, RILS_p10_16.trans_fee_b_av, RILS_p10_17.trans_fee_b_av, RILS_p10_18.trans_fee_b_av, RILS_p10_19.trans_fee_b_av,
                          RILS_p10_20.trans_fee_b_av, RILS_p10_21.trans_fee_b_av, RILS_p10_22.trans_fee_b_av, RILS_p10_23.trans_fee_b_av, RILS_p10_24.trans_fee_b_av,
                          RILS_p10_25.trans_fee_b_av, RILS_p10_26.trans_fee_b_av, RILS_p10_27.trans_fee_b_av, RILS_p10_28.trans_fee_b_av, RILS_p10_29.trans_fee_b_av,
                          RILS_p10_30.trans_fee_b_av, RILS_p10_31.trans_fee_b_av, RILS_p10_32.trans_fee_b_av, RILS_p10_33.trans_fee_b_av, RILS_p10_34.trans_fee_b_av,
                          RILS_p10_35.trans_fee_b_av, RILS_p10_36.trans_fee_b_av, RILS_p10_37.trans_fee_b_av, RILS_p10_38.trans_fee_b_av, RILS_p10_39.trans_fee_b_av,
                          RILS_p10_40.trans_fee_b_av, RILS_p10_40.trans_fee_b_av, RILS_p10_41.trans_fee_b_av, RILS_p10_42.trans_fee_b_av, RILS_p10_43.trans_fee_b_av,
                          RILS_p10_44.trans_fee_b_av, RILS_p10_45.trans_fee_b_av, RILS_p10_46.trans_fee_b_av, RILS_p10_47.trans_fee_b_av, RILS_p10_48.trans_fee_b_av,
                          RILS_p10_49.trans_fee_b_av, RILS_p10_50.trans_fee_b_av, RILS_p10_51.trans_fee_b_av, RILS_p10_52.trans_fee_b_av, RILS_p10_53.trans_fee_b_av,
                          RILS_p10_54.trans_fee_b_av, RILS_p10_55.trans_fee_b_av, RILS_p10_56.trans_fee_b_av, RILS_p10_57.trans_fee_b_av, RILS_p10_58.trans_fee_b_av,
                          RILS_p10_59.trans_fee_b_av, RILS_p10_60.trans_fee_b_av, RILS_p10_61.trans_fee_b_av, RILS_p10_62.trans_fee_b_av, RILS_p10_63.trans_fee_b_av,
                          RILS_p10_64.trans_fee_b_av, RILS_p10_65.trans_fee_b_av, RILS_p10_66.trans_fee_b_av, RILS_p10_67.trans_fee_b_av, RILS_p10_68.trans_fee_b_av,
                          RILS_p10_69.trans_fee_b_av, RILS_p10_70.trans_fee_b_av, RILS_p10_71.trans_fee_b_av, RILS_p10_72.trans_fee_b_av, RILS_p10_73.trans_fee_b_av,
                          RILS_p10_74.trans_fee_b_av, RILS_p10_75.trans_fee_b_av, RILS_p10_76.trans_fee_b_av, RILS_p10_77.trans_fee_b_av, RILS_p10_78.trans_fee_b_av,
                          RILS_p10_79.trans_fee_b_av, RILS_p10_80.trans_fee_b_av, RILS_p10_81.trans_fee_b_av, RILS_p10_82.trans_fee_b_av, RILS_p10_83.trans_fee_b_av,
                          RILS_p10_84.trans_fee_b_av, RILS_p10_85.trans_fee_b_av, RILS_p10_86.trans_fee_b_av, RILS_p10_87.trans_fee_b_av, RILS_p10_88.trans_fee_b_av,
                          RILS_p10_89.trans_fee_b_av, RILS_p10_90.trans_fee_b_av, RILS_p10_91.trans_fee_b_av, RILS_p10_92.trans_fee_b_av, RILS_p10_93.trans_fee_b_av,
                          RILS_p10_94.trans_fee_b_av, RILS_p10_95.trans_fee_b_av, RILS_p10_96.trans_fee_b_av, RILS_p10_97.trans_fee_b_av, RILS_p10_98.trans_fee_b_av,
                          RILS_p10_99.trans_fee_b_av, RILS_p10_100.trans_fee_b_av,
                          RILS_p10_101.trans_fee_b_av, RILS_p10_102.trans_fee_b_av, RILS_p10_103.trans_fee_b_av, RILS_p10_104.trans_fee_b_av, RILS_p10_105.trans_fee_b_av,
                          RILS_p10_106.trans_fee_b_av, RILS_p10_107.trans_fee_b_av, RILS_p10_108.trans_fee_b_av, RILS_p10_109.trans_fee_b_av, RILS_p10_110.trans_fee_b_av,
                          RILS_p10_111.trans_fee_b_av, RILS_p10_112.trans_fee_b_av, RILS_p10_113.trans_fee_b_av, RILS_p10_114.trans_fee_b_av, RILS_p10_115.trans_fee_b_av,
                          RILS_p10_116.trans_fee_b_av, RILS_p10_117.trans_fee_b_av, RILS_p10_118.trans_fee_b_av, RILS_p10_119.trans_fee_b_av, RILS_p10_120.trans_fee_b_av,
                          RILS_p10_121.trans_fee_b_av, RILS_p10_122.trans_fee_b_av, RILS_p10_123.trans_fee_b_av, RILS_p10_124.trans_fee_b_av, RILS_p10_125.trans_fee_b_av,
                          RILS_p10_126.trans_fee_b_av, RILS_p10_127.trans_fee_b_av, RILS_p10_128.trans_fee_b_av, RILS_p10_129.trans_fee_b_av, RILS_p10_130.trans_fee_b_av,
                          RILS_p10_131.trans_fee_b_av, RILS_p10_132.trans_fee_b_av, RILS_p10_133.trans_fee_b_av, RILS_p10_134.trans_fee_b_av, RILS_p10_135.trans_fee_b_av,
                          RILS_p10_136.trans_fee_b_av, RILS_p10_137.trans_fee_b_av, RILS_p10_138.trans_fee_b_av, RILS_p10_139.trans_fee_b_av, RILS_p10_140.trans_fee_b_av,
                          RILS_p10_140.trans_fee_b_av, RILS_p10_141.trans_fee_b_av, RILS_p10_142.trans_fee_b_av, RILS_p10_143.trans_fee_b_av, RILS_p10_144.trans_fee_b_av,
                          RILS_p10_145.trans_fee_b_av, RILS_p10_146.trans_fee_b_av, RILS_p10_147.trans_fee_b_av, RILS_p10_148.trans_fee_b_av, RILS_p10_149.trans_fee_b_av,
                          RILS_p10_150.trans_fee_b_av, RILS_p10_151.trans_fee_b_av, RILS_p10_152.trans_fee_b_av, RILS_p10_153.trans_fee_b_av, RILS_p10_154.trans_fee_b_av,
                          RILS_p10_155.trans_fee_b_av, RILS_p10_156.trans_fee_b_av, RILS_p10_157.trans_fee_b_av, RILS_p10_158.trans_fee_b_av, RILS_p10_159.trans_fee_b_av,
                          RILS_p10_160.trans_fee_b_av, RILS_p10_161.trans_fee_b_av, RILS_p10_162.trans_fee_b_av, RILS_p10_163.trans_fee_b_av, RILS_p10_164.trans_fee_b_av,
                          RILS_p10_165.trans_fee_b_av, RILS_p10_166.trans_fee_b_av, RILS_p10_167.trans_fee_b_av, RILS_p10_168.trans_fee_b_av, RILS_p10_169.trans_fee_b_av,
                          RILS_p10_170.trans_fee_b_av, RILS_p10_171.trans_fee_b_av, RILS_p10_172.trans_fee_b_av, RILS_p10_173.trans_fee_b_av, RILS_p10_174.trans_fee_b_av,
                          RILS_p10_175.trans_fee_b_av, RILS_p10_176.trans_fee_b_av, RILS_p10_177.trans_fee_b_av, RILS_p10_178.trans_fee_b_av, RILS_p10_179.trans_fee_b_av,
                          RILS_p10_180.trans_fee_b_av, RILS_p10_181.trans_fee_b_av, RILS_p10_182.trans_fee_b_av, RILS_p10_183.trans_fee_b_av, RILS_p10_184.trans_fee_b_av,
                          RILS_p10_185.trans_fee_b_av, RILS_p10_186.trans_fee_b_av, RILS_p10_187.trans_fee_b_av, RILS_p10_188.trans_fee_b_av, RILS_p10_189.trans_fee_b_av,
                          RILS_p10_190.trans_fee_b_av, RILS_p10_191.trans_fee_b_av, RILS_p10_192.trans_fee_b_av, RILS_p10_193.trans_fee_b_av, RILS_p10_194.trans_fee_b_av,
                          RILS_p10_195.trans_fee_b_av, RILS_p10_196.trans_fee_b_av, RILS_p10_197.trans_fee_b_av, RILS_p10_198.trans_fee_b_av, RILS_p10_199.trans_fee_b_av)


trans_fee_b_av_RILS_p10_mean = [np.mean(i) for i in trans_fee_b_av_RILS_p10]
trans_fee_b_av_RILS_p10_lower = [np.percentile(i, 10) for i in trans_fee_b_av_RILS_p10]
trans_fee_b_av_RILS_p10_upper = [np.percentile(i, 90) for i in trans_fee_b_av_RILS_p10]

print('Creating max_prov_rev_RILS_p10')
trans_fee_b_av_RILS_p10 = zip(RILS_p10_00.trans_fee_b_av, RILS_p10_01.trans_fee_b_av, RILS_p10_02.trans_fee_b_av, RILS_p10_03.trans_fee_b_av, RILS_p10_04.trans_fee_b_av,
                          RILS_p10_05.trans_fee_b_av, RILS_p10_06.trans_fee_b_av, RILS_p10_07.trans_fee_b_av, RILS_p10_08.trans_fee_b_av, RILS_p10_09.trans_fee_b_av,
                          RILS_p10_10.trans_fee_b_av, RILS_p10_11.trans_fee_b_av, RILS_p10_12.trans_fee_b_av, RILS_p10_13.trans_fee_b_av, RILS_p10_14.trans_fee_b_av,
                          RILS_p10_15.trans_fee_b_av, RILS_p10_16.trans_fee_b_av, RILS_p10_17.trans_fee_b_av, RILS_p10_18.trans_fee_b_av, RILS_p10_19.trans_fee_b_av,
                          RILS_p10_20.trans_fee_b_av, RILS_p10_21.trans_fee_b_av, RILS_p10_22.trans_fee_b_av, RILS_p10_23.trans_fee_b_av, RILS_p10_24.trans_fee_b_av,
                          RILS_p10_25.trans_fee_b_av, RILS_p10_26.trans_fee_b_av, RILS_p10_27.trans_fee_b_av, RILS_p10_28.trans_fee_b_av, RILS_p10_29.trans_fee_b_av,
                          RILS_p10_30.trans_fee_b_av, RILS_p10_31.trans_fee_b_av, RILS_p10_32.trans_fee_b_av, RILS_p10_33.trans_fee_b_av, RILS_p10_34.trans_fee_b_av,
                          RILS_p10_35.trans_fee_b_av, RILS_p10_36.trans_fee_b_av, RILS_p10_37.trans_fee_b_av, RILS_p10_38.trans_fee_b_av, RILS_p10_39.trans_fee_b_av,
                          RILS_p10_40.trans_fee_b_av, RILS_p10_40.trans_fee_b_av, RILS_p10_41.trans_fee_b_av, RILS_p10_42.trans_fee_b_av, RILS_p10_43.trans_fee_b_av,
                          RILS_p10_44.trans_fee_b_av, RILS_p10_45.trans_fee_b_av, RILS_p10_46.trans_fee_b_av, RILS_p10_47.trans_fee_b_av, RILS_p10_48.trans_fee_b_av,
                          RILS_p10_49.trans_fee_b_av, RILS_p10_50.trans_fee_b_av, RILS_p10_51.trans_fee_b_av, RILS_p10_52.trans_fee_b_av, RILS_p10_53.trans_fee_b_av,
                          RILS_p10_54.trans_fee_b_av, RILS_p10_55.trans_fee_b_av, RILS_p10_56.trans_fee_b_av, RILS_p10_57.trans_fee_b_av, RILS_p10_58.trans_fee_b_av,
                          RILS_p10_59.trans_fee_b_av, RILS_p10_60.trans_fee_b_av, RILS_p10_61.trans_fee_b_av, RILS_p10_62.trans_fee_b_av, RILS_p10_63.trans_fee_b_av,
                          RILS_p10_64.trans_fee_b_av, RILS_p10_65.trans_fee_b_av, RILS_p10_66.trans_fee_b_av, RILS_p10_67.trans_fee_b_av, RILS_p10_68.trans_fee_b_av,
                          RILS_p10_69.trans_fee_b_av, RILS_p10_70.trans_fee_b_av, RILS_p10_71.trans_fee_b_av, RILS_p10_72.trans_fee_b_av, RILS_p10_73.trans_fee_b_av,
                          RILS_p10_74.trans_fee_b_av, RILS_p10_75.trans_fee_b_av, RILS_p10_76.trans_fee_b_av, RILS_p10_77.trans_fee_b_av, RILS_p10_78.trans_fee_b_av,
                          RILS_p10_79.trans_fee_b_av, RILS_p10_80.trans_fee_b_av, RILS_p10_81.trans_fee_b_av, RILS_p10_82.trans_fee_b_av, RILS_p10_83.trans_fee_b_av,
                          RILS_p10_84.trans_fee_b_av, RILS_p10_85.trans_fee_b_av, RILS_p10_86.trans_fee_b_av, RILS_p10_87.trans_fee_b_av, RILS_p10_88.trans_fee_b_av,
                          RILS_p10_89.trans_fee_b_av, RILS_p10_90.trans_fee_b_av, RILS_p10_91.trans_fee_b_av, RILS_p10_92.trans_fee_b_av, RILS_p10_93.trans_fee_b_av,
                          RILS_p10_94.trans_fee_b_av, RILS_p10_95.trans_fee_b_av, RILS_p10_96.trans_fee_b_av, RILS_p10_97.trans_fee_b_av, RILS_p10_98.trans_fee_b_av,
                          RILS_p10_99.trans_fee_b_av, RILS_p10_100.trans_fee_b_av,
                          RILS_p10_101.trans_fee_b_av, RILS_p10_102.trans_fee_b_av, RILS_p10_103.trans_fee_b_av, RILS_p10_104.trans_fee_b_av, RILS_p10_105.trans_fee_b_av,
                          RILS_p10_106.trans_fee_b_av, RILS_p10_107.trans_fee_b_av, RILS_p10_108.trans_fee_b_av, RILS_p10_109.trans_fee_b_av, RILS_p10_110.trans_fee_b_av,
                          RILS_p10_111.trans_fee_b_av, RILS_p10_112.trans_fee_b_av, RILS_p10_113.trans_fee_b_av, RILS_p10_114.trans_fee_b_av, RILS_p10_115.trans_fee_b_av,
                          RILS_p10_116.trans_fee_b_av, RILS_p10_117.trans_fee_b_av, RILS_p10_118.trans_fee_b_av, RILS_p10_119.trans_fee_b_av, RILS_p10_120.trans_fee_b_av,
                          RILS_p10_121.trans_fee_b_av, RILS_p10_122.trans_fee_b_av, RILS_p10_123.trans_fee_b_av, RILS_p10_124.trans_fee_b_av, RILS_p10_125.trans_fee_b_av,
                          RILS_p10_126.trans_fee_b_av, RILS_p10_127.trans_fee_b_av, RILS_p10_128.trans_fee_b_av, RILS_p10_129.trans_fee_b_av, RILS_p10_130.trans_fee_b_av,
                          RILS_p10_131.trans_fee_b_av, RILS_p10_132.trans_fee_b_av, RILS_p10_133.trans_fee_b_av, RILS_p10_134.trans_fee_b_av, RILS_p10_135.trans_fee_b_av,
                          RILS_p10_136.trans_fee_b_av, RILS_p10_137.trans_fee_b_av, RILS_p10_138.trans_fee_b_av, RILS_p10_139.trans_fee_b_av, RILS_p10_140.trans_fee_b_av,
                          RILS_p10_140.trans_fee_b_av, RILS_p10_141.trans_fee_b_av, RILS_p10_142.trans_fee_b_av, RILS_p10_143.trans_fee_b_av, RILS_p10_144.trans_fee_b_av,
                          RILS_p10_145.trans_fee_b_av, RILS_p10_146.trans_fee_b_av, RILS_p10_147.trans_fee_b_av, RILS_p10_148.trans_fee_b_av, RILS_p10_149.trans_fee_b_av,
                          RILS_p10_150.trans_fee_b_av, RILS_p10_151.trans_fee_b_av, RILS_p10_152.trans_fee_b_av, RILS_p10_153.trans_fee_b_av, RILS_p10_154.trans_fee_b_av,
                          RILS_p10_155.trans_fee_b_av, RILS_p10_156.trans_fee_b_av, RILS_p10_157.trans_fee_b_av, RILS_p10_158.trans_fee_b_av, RILS_p10_159.trans_fee_b_av,
                          RILS_p10_160.trans_fee_b_av, RILS_p10_161.trans_fee_b_av, RILS_p10_162.trans_fee_b_av, RILS_p10_163.trans_fee_b_av, RILS_p10_164.trans_fee_b_av,
                          RILS_p10_165.trans_fee_b_av, RILS_p10_166.trans_fee_b_av, RILS_p10_167.trans_fee_b_av, RILS_p10_168.trans_fee_b_av, RILS_p10_169.trans_fee_b_av,
                          RILS_p10_170.trans_fee_b_av, RILS_p10_171.trans_fee_b_av, RILS_p10_172.trans_fee_b_av, RILS_p10_173.trans_fee_b_av, RILS_p10_174.trans_fee_b_av,
                          RILS_p10_175.trans_fee_b_av, RILS_p10_176.trans_fee_b_av, RILS_p10_177.trans_fee_b_av, RILS_p10_178.trans_fee_b_av, RILS_p10_179.trans_fee_b_av,
                          RILS_p10_180.trans_fee_b_av, RILS_p10_181.trans_fee_b_av, RILS_p10_182.trans_fee_b_av, RILS_p10_183.trans_fee_b_av, RILS_p10_184.trans_fee_b_av,
                          RILS_p10_185.trans_fee_b_av, RILS_p10_186.trans_fee_b_av, RILS_p10_187.trans_fee_b_av, RILS_p10_188.trans_fee_b_av, RILS_p10_189.trans_fee_b_av,
                          RILS_p10_190.trans_fee_b_av, RILS_p10_191.trans_fee_b_av, RILS_p10_192.trans_fee_b_av, RILS_p10_193.trans_fee_b_av, RILS_p10_194.trans_fee_b_av,
                          RILS_p10_195.trans_fee_b_av, RILS_p10_196.trans_fee_b_av, RILS_p10_197.trans_fee_b_av, RILS_p10_198.trans_fee_b_av, RILS_p10_199.trans_fee_b_av)


trans_fee_b_av_RILS_p10_mean = [np.mean(i) for i in trans_fee_b_av_RILS_p10]
trans_fee_b_av_RILS_p10_lower = [np.percentile(i, 10) for i in trans_fee_b_av_RILS_p10]
trans_fee_b_av_RILS_p10_upper = [np.percentile(i, 90) for i in trans_fee_b_av_RILS_p10]


print('Creating trans_fee_s_av_RIL_p10')
trans_fee_s_av_RIL_p10 = zip(RIL_p10_00.trans_fee_s_av, RIL_p10_01.trans_fee_s_av, RIL_p10_02.trans_fee_s_av, RIL_p10_03.trans_fee_s_av, RIL_p10_04.trans_fee_s_av,
                          RIL_p10_05.trans_fee_s_av, RIL_p10_06.trans_fee_s_av, RIL_p10_07.trans_fee_s_av, RIL_p10_08.trans_fee_s_av, RIL_p10_09.trans_fee_s_av,
                          RIL_p10_10.trans_fee_s_av, RIL_p10_11.trans_fee_s_av, RIL_p10_12.trans_fee_s_av, RIL_p10_13.trans_fee_s_av, RIL_p10_14.trans_fee_s_av,
                          RIL_p10_15.trans_fee_s_av, RIL_p10_16.trans_fee_s_av, RIL_p10_17.trans_fee_s_av, RIL_p10_18.trans_fee_s_av, RIL_p10_19.trans_fee_s_av,
                          RIL_p10_20.trans_fee_s_av, RIL_p10_21.trans_fee_s_av, RIL_p10_22.trans_fee_s_av, RIL_p10_23.trans_fee_s_av, RIL_p10_24.trans_fee_s_av,
                          RIL_p10_25.trans_fee_s_av, RIL_p10_26.trans_fee_s_av, RIL_p10_27.trans_fee_s_av, RIL_p10_28.trans_fee_s_av, RIL_p10_29.trans_fee_s_av,
                          RIL_p10_30.trans_fee_s_av, RIL_p10_31.trans_fee_s_av, RIL_p10_32.trans_fee_s_av, RIL_p10_33.trans_fee_s_av, RIL_p10_34.trans_fee_s_av,
                          RIL_p10_35.trans_fee_s_av, RIL_p10_36.trans_fee_s_av, RIL_p10_37.trans_fee_s_av, RIL_p10_38.trans_fee_s_av, RIL_p10_39.trans_fee_s_av,
                          RIL_p10_40.trans_fee_s_av, RIL_p10_40.trans_fee_s_av, RIL_p10_41.trans_fee_s_av, RIL_p10_42.trans_fee_s_av, RIL_p10_43.trans_fee_s_av,
                          RIL_p10_44.trans_fee_s_av, RIL_p10_45.trans_fee_s_av, RIL_p10_46.trans_fee_s_av, RIL_p10_47.trans_fee_s_av, RIL_p10_48.trans_fee_s_av,
                          RIL_p10_49.trans_fee_s_av, RIL_p10_50.trans_fee_s_av, RIL_p10_51.trans_fee_s_av, RIL_p10_52.trans_fee_s_av, RIL_p10_53.trans_fee_s_av,
                          RIL_p10_54.trans_fee_s_av, RIL_p10_55.trans_fee_s_av, RIL_p10_56.trans_fee_s_av, RIL_p10_57.trans_fee_s_av, RIL_p10_58.trans_fee_s_av,
                          RIL_p10_59.trans_fee_s_av, RIL_p10_60.trans_fee_s_av, RIL_p10_61.trans_fee_s_av, RIL_p10_62.trans_fee_s_av, RIL_p10_63.trans_fee_s_av,
                          RIL_p10_64.trans_fee_s_av, RIL_p10_65.trans_fee_s_av, RIL_p10_66.trans_fee_s_av, RIL_p10_67.trans_fee_s_av, RIL_p10_68.trans_fee_s_av,
                          RIL_p10_69.trans_fee_s_av, RIL_p10_70.trans_fee_s_av, RIL_p10_71.trans_fee_s_av, RIL_p10_72.trans_fee_s_av, RIL_p10_73.trans_fee_s_av,
                          RIL_p10_74.trans_fee_s_av, RIL_p10_75.trans_fee_s_av, RIL_p10_76.trans_fee_s_av, RIL_p10_77.trans_fee_s_av, RIL_p10_78.trans_fee_s_av,
                          RIL_p10_79.trans_fee_s_av, RIL_p10_80.trans_fee_s_av, RIL_p10_81.trans_fee_s_av, RIL_p10_82.trans_fee_s_av, RIL_p10_83.trans_fee_s_av,
                          RIL_p10_84.trans_fee_s_av, RIL_p10_85.trans_fee_s_av, RIL_p10_86.trans_fee_s_av, RIL_p10_87.trans_fee_s_av, RIL_p10_88.trans_fee_s_av,
                          RIL_p10_89.trans_fee_s_av, RIL_p10_90.trans_fee_s_av, RIL_p10_91.trans_fee_s_av, RIL_p10_92.trans_fee_s_av, RIL_p10_93.trans_fee_s_av,
                          RIL_p10_94.trans_fee_s_av, RIL_p10_95.trans_fee_s_av, RIL_p10_96.trans_fee_s_av, RIL_p10_97.trans_fee_s_av, RIL_p10_98.trans_fee_s_av,
                          RIL_p10_99.trans_fee_s_av, RIL_p10_100.trans_fee_s_av,
                          RIL_p10_101.trans_fee_s_av, RIL_p10_102.trans_fee_s_av, RIL_p10_103.trans_fee_s_av, RIL_p10_104.trans_fee_s_av, RIL_p10_105.trans_fee_s_av,
                          RIL_p10_106.trans_fee_s_av, RIL_p10_107.trans_fee_s_av, RIL_p10_108.trans_fee_s_av, RIL_p10_109.trans_fee_s_av, RIL_p10_110.trans_fee_s_av,
                          RIL_p10_111.trans_fee_s_av, RIL_p10_112.trans_fee_s_av, RIL_p10_113.trans_fee_s_av, RIL_p10_114.trans_fee_s_av, RIL_p10_115.trans_fee_s_av,
                          RIL_p10_116.trans_fee_s_av, RIL_p10_117.trans_fee_s_av, RIL_p10_118.trans_fee_s_av, RIL_p10_119.trans_fee_s_av, RIL_p10_120.trans_fee_s_av,
                          RIL_p10_121.trans_fee_s_av, RIL_p10_122.trans_fee_s_av, RIL_p10_123.trans_fee_s_av, RIL_p10_124.trans_fee_s_av, RIL_p10_125.trans_fee_s_av,
                          RIL_p10_126.trans_fee_s_av, RIL_p10_127.trans_fee_s_av, RIL_p10_128.trans_fee_s_av, RIL_p10_129.trans_fee_s_av, RIL_p10_130.trans_fee_s_av,
                          RIL_p10_131.trans_fee_s_av, RIL_p10_132.trans_fee_s_av, RIL_p10_133.trans_fee_s_av, RIL_p10_134.trans_fee_s_av, RIL_p10_135.trans_fee_s_av,
                          RIL_p10_136.trans_fee_s_av, RIL_p10_137.trans_fee_s_av, RIL_p10_138.trans_fee_s_av, RIL_p10_139.trans_fee_s_av, RIL_p10_140.trans_fee_s_av,
                          RIL_p10_140.trans_fee_s_av, RIL_p10_141.trans_fee_s_av, RIL_p10_142.trans_fee_s_av, RIL_p10_143.trans_fee_s_av, RIL_p10_144.trans_fee_s_av,
                          RIL_p10_145.trans_fee_s_av, RIL_p10_146.trans_fee_s_av, RIL_p10_147.trans_fee_s_av, RIL_p10_148.trans_fee_s_av, RIL_p10_149.trans_fee_s_av,
                          RIL_p10_150.trans_fee_s_av, RIL_p10_151.trans_fee_s_av, RIL_p10_152.trans_fee_s_av, RIL_p10_153.trans_fee_s_av, RIL_p10_154.trans_fee_s_av,
                          RIL_p10_155.trans_fee_s_av, RIL_p10_156.trans_fee_s_av, RIL_p10_157.trans_fee_s_av, RIL_p10_158.trans_fee_s_av, RIL_p10_159.trans_fee_s_av,
                          RIL_p10_160.trans_fee_s_av, RIL_p10_161.trans_fee_s_av, RIL_p10_162.trans_fee_s_av, RIL_p10_163.trans_fee_s_av, RIL_p10_164.trans_fee_s_av,
                          RIL_p10_165.trans_fee_s_av, RIL_p10_166.trans_fee_s_av, RIL_p10_167.trans_fee_s_av, RIL_p10_168.trans_fee_s_av, RIL_p10_169.trans_fee_s_av,
                          RIL_p10_170.trans_fee_s_av, RIL_p10_171.trans_fee_s_av, RIL_p10_172.trans_fee_s_av, RIL_p10_173.trans_fee_s_av, RIL_p10_174.trans_fee_s_av,
                          RIL_p10_175.trans_fee_s_av, RIL_p10_176.trans_fee_s_av, RIL_p10_177.trans_fee_s_av, RIL_p10_178.trans_fee_s_av, RIL_p10_179.trans_fee_s_av,
                          RIL_p10_180.trans_fee_s_av, RIL_p10_181.trans_fee_s_av, RIL_p10_182.trans_fee_s_av, RIL_p10_183.trans_fee_s_av, RIL_p10_184.trans_fee_s_av,
                          RIL_p10_185.trans_fee_s_av, RIL_p10_186.trans_fee_s_av, RIL_p10_187.trans_fee_s_av, RIL_p10_188.trans_fee_s_av, RIL_p10_189.trans_fee_s_av,
                          RIL_p10_190.trans_fee_s_av, RIL_p10_191.trans_fee_s_av, RIL_p10_192.trans_fee_s_av, RIL_p10_193.trans_fee_s_av, RIL_p10_194.trans_fee_s_av,
                          RIL_p10_195.trans_fee_s_av, RIL_p10_196.trans_fee_s_av, RIL_p10_197.trans_fee_s_av, RIL_p10_198.trans_fee_s_av, RIL_p10_199.trans_fee_s_av)


trans_fee_s_av_RIL_p10_mean = [np.mean(i) for i in trans_fee_s_av_RIL_p10]
trans_fee_s_av_RIL_p10_lower = [np.percentile(i, 10) for i in trans_fee_s_av_RIL_p10]
trans_fee_s_av_RIL_p10_upper = [np.percentile(i, 90) for i in trans_fee_s_av_RIL_p10]


print('Creating trans_fee_s_av_RILS_p10')
trans_fee_s_av_RILS_p10 = zip(RILS_p10_00.trans_fee_s_av, RILS_p10_01.trans_fee_s_av, RILS_p10_02.trans_fee_s_av, RILS_p10_03.trans_fee_s_av, RILS_p10_04.trans_fee_s_av,
                          RILS_p10_05.trans_fee_s_av, RILS_p10_06.trans_fee_s_av, RILS_p10_07.trans_fee_s_av, RILS_p10_08.trans_fee_s_av, RILS_p10_09.trans_fee_s_av,
                          RILS_p10_10.trans_fee_s_av, RILS_p10_11.trans_fee_s_av, RILS_p10_12.trans_fee_s_av, RILS_p10_13.trans_fee_s_av, RILS_p10_14.trans_fee_s_av,
                          RILS_p10_15.trans_fee_s_av, RILS_p10_16.trans_fee_s_av, RILS_p10_17.trans_fee_s_av, RILS_p10_18.trans_fee_s_av, RILS_p10_19.trans_fee_s_av,
                          RILS_p10_20.trans_fee_s_av, RILS_p10_21.trans_fee_s_av, RILS_p10_22.trans_fee_s_av, RILS_p10_23.trans_fee_s_av, RILS_p10_24.trans_fee_s_av,
                          RILS_p10_25.trans_fee_s_av, RILS_p10_26.trans_fee_s_av, RILS_p10_27.trans_fee_s_av, RILS_p10_28.trans_fee_s_av, RILS_p10_29.trans_fee_s_av,
                          RILS_p10_30.trans_fee_s_av, RILS_p10_31.trans_fee_s_av, RILS_p10_32.trans_fee_s_av, RILS_p10_33.trans_fee_s_av, RILS_p10_34.trans_fee_s_av,
                          RILS_p10_35.trans_fee_s_av, RILS_p10_36.trans_fee_s_av, RILS_p10_37.trans_fee_s_av, RILS_p10_38.trans_fee_s_av, RILS_p10_39.trans_fee_s_av,
                          RILS_p10_40.trans_fee_s_av, RILS_p10_40.trans_fee_s_av, RILS_p10_41.trans_fee_s_av, RILS_p10_42.trans_fee_s_av, RILS_p10_43.trans_fee_s_av,
                          RILS_p10_44.trans_fee_s_av, RILS_p10_45.trans_fee_s_av, RILS_p10_46.trans_fee_s_av, RILS_p10_47.trans_fee_s_av, RILS_p10_48.trans_fee_s_av,
                          RILS_p10_49.trans_fee_s_av, RILS_p10_50.trans_fee_s_av, RILS_p10_51.trans_fee_s_av, RILS_p10_52.trans_fee_s_av, RILS_p10_53.trans_fee_s_av,
                          RILS_p10_54.trans_fee_s_av, RILS_p10_55.trans_fee_s_av, RILS_p10_56.trans_fee_s_av, RILS_p10_57.trans_fee_s_av, RILS_p10_58.trans_fee_s_av,
                          RILS_p10_59.trans_fee_s_av, RILS_p10_60.trans_fee_s_av, RILS_p10_61.trans_fee_s_av, RILS_p10_62.trans_fee_s_av, RILS_p10_63.trans_fee_s_av,
                          RILS_p10_64.trans_fee_s_av, RILS_p10_65.trans_fee_s_av, RILS_p10_66.trans_fee_s_av, RILS_p10_67.trans_fee_s_av, RILS_p10_68.trans_fee_s_av,
                          RILS_p10_69.trans_fee_s_av, RILS_p10_70.trans_fee_s_av, RILS_p10_71.trans_fee_s_av, RILS_p10_72.trans_fee_s_av, RILS_p10_73.trans_fee_s_av,
                          RILS_p10_74.trans_fee_s_av, RILS_p10_75.trans_fee_s_av, RILS_p10_76.trans_fee_s_av, RILS_p10_77.trans_fee_s_av, RILS_p10_78.trans_fee_s_av,
                          RILS_p10_79.trans_fee_s_av, RILS_p10_80.trans_fee_s_av, RILS_p10_81.trans_fee_s_av, RILS_p10_82.trans_fee_s_av, RILS_p10_83.trans_fee_s_av,
                          RILS_p10_84.trans_fee_s_av, RILS_p10_85.trans_fee_s_av, RILS_p10_86.trans_fee_s_av, RILS_p10_87.trans_fee_s_av, RILS_p10_88.trans_fee_s_av,
                          RILS_p10_89.trans_fee_s_av, RILS_p10_90.trans_fee_s_av, RILS_p10_91.trans_fee_s_av, RILS_p10_92.trans_fee_s_av, RILS_p10_93.trans_fee_s_av,
                          RILS_p10_94.trans_fee_s_av, RILS_p10_95.trans_fee_s_av, RILS_p10_96.trans_fee_s_av, RILS_p10_97.trans_fee_s_av, RILS_p10_98.trans_fee_s_av,
                          RILS_p10_99.trans_fee_s_av, RILS_p10_100.trans_fee_s_av,
                          RILS_p10_101.trans_fee_s_av, RILS_p10_102.trans_fee_s_av, RILS_p10_103.trans_fee_s_av, RILS_p10_104.trans_fee_s_av, RILS_p10_105.trans_fee_s_av,
                          RILS_p10_106.trans_fee_s_av, RILS_p10_107.trans_fee_s_av, RILS_p10_108.trans_fee_s_av, RILS_p10_109.trans_fee_s_av, RILS_p10_110.trans_fee_s_av,
                          RILS_p10_111.trans_fee_s_av, RILS_p10_112.trans_fee_s_av, RILS_p10_113.trans_fee_s_av, RILS_p10_114.trans_fee_s_av, RILS_p10_115.trans_fee_s_av,
                          RILS_p10_116.trans_fee_s_av, RILS_p10_117.trans_fee_s_av, RILS_p10_118.trans_fee_s_av, RILS_p10_119.trans_fee_s_av, RILS_p10_120.trans_fee_s_av,
                          RILS_p10_121.trans_fee_s_av, RILS_p10_122.trans_fee_s_av, RILS_p10_123.trans_fee_s_av, RILS_p10_124.trans_fee_s_av, RILS_p10_125.trans_fee_s_av,
                          RILS_p10_126.trans_fee_s_av, RILS_p10_127.trans_fee_s_av, RILS_p10_128.trans_fee_s_av, RILS_p10_129.trans_fee_s_av, RILS_p10_130.trans_fee_s_av,
                          RILS_p10_131.trans_fee_s_av, RILS_p10_132.trans_fee_s_av, RILS_p10_133.trans_fee_s_av, RILS_p10_134.trans_fee_s_av, RILS_p10_135.trans_fee_s_av,
                          RILS_p10_136.trans_fee_s_av, RILS_p10_137.trans_fee_s_av, RILS_p10_138.trans_fee_s_av, RILS_p10_139.trans_fee_s_av, RILS_p10_140.trans_fee_s_av,
                          RILS_p10_140.trans_fee_s_av, RILS_p10_141.trans_fee_s_av, RILS_p10_142.trans_fee_s_av, RILS_p10_143.trans_fee_s_av, RILS_p10_144.trans_fee_s_av,
                          RILS_p10_145.trans_fee_s_av, RILS_p10_146.trans_fee_s_av, RILS_p10_147.trans_fee_s_av, RILS_p10_148.trans_fee_s_av, RILS_p10_149.trans_fee_s_av,
                          RILS_p10_150.trans_fee_s_av, RILS_p10_151.trans_fee_s_av, RILS_p10_152.trans_fee_s_av, RILS_p10_153.trans_fee_s_av, RILS_p10_154.trans_fee_s_av,
                          RILS_p10_155.trans_fee_s_av, RILS_p10_156.trans_fee_s_av, RILS_p10_157.trans_fee_s_av, RILS_p10_158.trans_fee_s_av, RILS_p10_159.trans_fee_s_av,
                          RILS_p10_160.trans_fee_s_av, RILS_p10_161.trans_fee_s_av, RILS_p10_162.trans_fee_s_av, RILS_p10_163.trans_fee_s_av, RILS_p10_164.trans_fee_s_av,
                          RILS_p10_165.trans_fee_s_av, RILS_p10_166.trans_fee_s_av, RILS_p10_167.trans_fee_s_av, RILS_p10_168.trans_fee_s_av, RILS_p10_169.trans_fee_s_av,
                          RILS_p10_170.trans_fee_s_av, RILS_p10_171.trans_fee_s_av, RILS_p10_172.trans_fee_s_av, RILS_p10_173.trans_fee_s_av, RILS_p10_174.trans_fee_s_av,
                          RILS_p10_175.trans_fee_s_av, RILS_p10_176.trans_fee_s_av, RILS_p10_177.trans_fee_s_av, RILS_p10_178.trans_fee_s_av, RILS_p10_179.trans_fee_s_av,
                          RILS_p10_180.trans_fee_s_av, RILS_p10_181.trans_fee_s_av, RILS_p10_182.trans_fee_s_av, RILS_p10_183.trans_fee_s_av, RILS_p10_184.trans_fee_s_av,
                          RILS_p10_185.trans_fee_s_av, RILS_p10_186.trans_fee_s_av, RILS_p10_187.trans_fee_s_av, RILS_p10_188.trans_fee_s_av, RILS_p10_189.trans_fee_s_av,
                          RILS_p10_190.trans_fee_s_av, RILS_p10_191.trans_fee_s_av, RILS_p10_192.trans_fee_s_av, RILS_p10_193.trans_fee_s_av, RILS_p10_194.trans_fee_s_av,
                          RILS_p10_195.trans_fee_s_av, RILS_p10_196.trans_fee_s_av, RILS_p10_197.trans_fee_s_av, RILS_p10_198.trans_fee_s_av, RILS_p10_199.trans_fee_s_av)


trans_fee_s_av_RILS_p10_mean = [np.mean(i) for i in trans_fee_s_av_RILS_p10]
trans_fee_s_av_RILS_p10_lower = [np.percentile(i, 10) for i in trans_fee_s_av_RILS_p10]
trans_fee_s_av_RILS_p10_upper = [np.percentile(i, 90) for i in trans_fee_s_av_RILS_p10]

############################################
print('Creating buyer_rev_av_RIL_p10')
buyer_rev_av_RIL_p10 = zip(RIL_p10_00.buyer_rev_av, RIL_p10_01.buyer_rev_av, RIL_p10_02.buyer_rev_av, RIL_p10_03.buyer_rev_av, RIL_p10_04.buyer_rev_av,
                          RIL_p10_05.buyer_rev_av, RIL_p10_06.buyer_rev_av, RIL_p10_07.buyer_rev_av, RIL_p10_08.buyer_rev_av, RIL_p10_09.buyer_rev_av,
                          RIL_p10_10.buyer_rev_av, RIL_p10_11.buyer_rev_av, RIL_p10_12.buyer_rev_av, RIL_p10_13.buyer_rev_av, RIL_p10_14.buyer_rev_av,
                          RIL_p10_15.buyer_rev_av, RIL_p10_16.buyer_rev_av, RIL_p10_17.buyer_rev_av, RIL_p10_18.buyer_rev_av, RIL_p10_19.buyer_rev_av,
                          RIL_p10_20.buyer_rev_av, RIL_p10_21.buyer_rev_av, RIL_p10_22.buyer_rev_av, RIL_p10_23.buyer_rev_av, RIL_p10_24.buyer_rev_av,
                          RIL_p10_25.buyer_rev_av, RIL_p10_26.buyer_rev_av, RIL_p10_27.buyer_rev_av, RIL_p10_28.buyer_rev_av, RIL_p10_29.buyer_rev_av,
                          RIL_p10_30.buyer_rev_av, RIL_p10_31.buyer_rev_av, RIL_p10_32.buyer_rev_av, RIL_p10_33.buyer_rev_av, RIL_p10_34.buyer_rev_av,
                          RIL_p10_35.buyer_rev_av, RIL_p10_36.buyer_rev_av, RIL_p10_37.buyer_rev_av, RIL_p10_38.buyer_rev_av, RIL_p10_39.buyer_rev_av,
                          RIL_p10_40.buyer_rev_av, RIL_p10_40.buyer_rev_av, RIL_p10_41.buyer_rev_av, RIL_p10_42.buyer_rev_av, RIL_p10_43.buyer_rev_av,
                          RIL_p10_44.buyer_rev_av, RIL_p10_45.buyer_rev_av, RIL_p10_46.buyer_rev_av, RIL_p10_47.buyer_rev_av, RIL_p10_48.buyer_rev_av,
                          RIL_p10_49.buyer_rev_av, RIL_p10_50.buyer_rev_av, RIL_p10_51.buyer_rev_av, RIL_p10_52.buyer_rev_av, RIL_p10_53.buyer_rev_av,
                          RIL_p10_54.buyer_rev_av, RIL_p10_55.buyer_rev_av, RIL_p10_56.buyer_rev_av, RIL_p10_57.buyer_rev_av, RIL_p10_58.buyer_rev_av,
                          RIL_p10_59.buyer_rev_av, RIL_p10_60.buyer_rev_av, RIL_p10_61.buyer_rev_av, RIL_p10_62.buyer_rev_av, RIL_p10_63.buyer_rev_av,
                          RIL_p10_64.buyer_rev_av, RIL_p10_65.buyer_rev_av, RIL_p10_66.buyer_rev_av, RIL_p10_67.buyer_rev_av, RIL_p10_68.buyer_rev_av,
                          RIL_p10_69.buyer_rev_av, RIL_p10_70.buyer_rev_av, RIL_p10_71.buyer_rev_av, RIL_p10_72.buyer_rev_av, RIL_p10_73.buyer_rev_av,
                          RIL_p10_74.buyer_rev_av, RIL_p10_75.buyer_rev_av, RIL_p10_76.buyer_rev_av, RIL_p10_77.buyer_rev_av, RIL_p10_78.buyer_rev_av,
                          RIL_p10_79.buyer_rev_av, RIL_p10_80.buyer_rev_av, RIL_p10_81.buyer_rev_av, RIL_p10_82.buyer_rev_av, RIL_p10_83.buyer_rev_av,
                          RIL_p10_84.buyer_rev_av, RIL_p10_85.buyer_rev_av, RIL_p10_86.buyer_rev_av, RIL_p10_87.buyer_rev_av, RIL_p10_88.buyer_rev_av,
                          RIL_p10_89.buyer_rev_av, RIL_p10_90.buyer_rev_av, RIL_p10_91.buyer_rev_av, RIL_p10_92.buyer_rev_av, RIL_p10_93.buyer_rev_av,
                          RIL_p10_94.buyer_rev_av, RIL_p10_95.buyer_rev_av, RIL_p10_96.buyer_rev_av, RIL_p10_97.buyer_rev_av, RIL_p10_98.buyer_rev_av,
                          RIL_p10_99.buyer_rev_av, RIL_p10_100.buyer_rev_av,
                          RIL_p10_101.buyer_rev_av, RIL_p10_102.buyer_rev_av, RIL_p10_103.buyer_rev_av, RIL_p10_104.buyer_rev_av, RIL_p10_105.buyer_rev_av,
                          RIL_p10_106.buyer_rev_av, RIL_p10_107.buyer_rev_av, RIL_p10_108.buyer_rev_av, RIL_p10_109.buyer_rev_av, RIL_p10_110.buyer_rev_av,
                          RIL_p10_111.buyer_rev_av, RIL_p10_112.buyer_rev_av, RIL_p10_113.buyer_rev_av, RIL_p10_114.buyer_rev_av, RIL_p10_115.buyer_rev_av,
                          RIL_p10_116.buyer_rev_av, RIL_p10_117.buyer_rev_av, RIL_p10_118.buyer_rev_av, RIL_p10_119.buyer_rev_av, RIL_p10_120.buyer_rev_av,
                          RIL_p10_121.buyer_rev_av, RIL_p10_122.buyer_rev_av, RIL_p10_123.buyer_rev_av, RIL_p10_124.buyer_rev_av, RIL_p10_125.buyer_rev_av,
                          RIL_p10_126.buyer_rev_av, RIL_p10_127.buyer_rev_av, RIL_p10_128.buyer_rev_av, RIL_p10_129.buyer_rev_av, RIL_p10_130.buyer_rev_av,
                          RIL_p10_131.buyer_rev_av, RIL_p10_132.buyer_rev_av, RIL_p10_133.buyer_rev_av, RIL_p10_134.buyer_rev_av, RIL_p10_135.buyer_rev_av,
                          RIL_p10_136.buyer_rev_av, RIL_p10_137.buyer_rev_av, RIL_p10_138.buyer_rev_av, RIL_p10_139.buyer_rev_av, RIL_p10_140.buyer_rev_av,
                          RIL_p10_140.buyer_rev_av, RIL_p10_141.buyer_rev_av, RIL_p10_142.buyer_rev_av, RIL_p10_143.buyer_rev_av, RIL_p10_144.buyer_rev_av,
                          RIL_p10_145.buyer_rev_av, RIL_p10_146.buyer_rev_av, RIL_p10_147.buyer_rev_av, RIL_p10_148.buyer_rev_av, RIL_p10_149.buyer_rev_av,
                          RIL_p10_150.buyer_rev_av, RIL_p10_151.buyer_rev_av, RIL_p10_152.buyer_rev_av, RIL_p10_153.buyer_rev_av, RIL_p10_154.buyer_rev_av,
                          RIL_p10_155.buyer_rev_av, RIL_p10_156.buyer_rev_av, RIL_p10_157.buyer_rev_av, RIL_p10_158.buyer_rev_av, RIL_p10_159.buyer_rev_av,
                          RIL_p10_160.buyer_rev_av, RIL_p10_161.buyer_rev_av, RIL_p10_162.buyer_rev_av, RIL_p10_163.buyer_rev_av, RIL_p10_164.buyer_rev_av,
                          RIL_p10_165.buyer_rev_av, RIL_p10_166.buyer_rev_av, RIL_p10_167.buyer_rev_av, RIL_p10_168.buyer_rev_av, RIL_p10_169.buyer_rev_av,
                          RIL_p10_170.buyer_rev_av, RIL_p10_171.buyer_rev_av, RIL_p10_172.buyer_rev_av, RIL_p10_173.buyer_rev_av, RIL_p10_174.buyer_rev_av,
                          RIL_p10_175.buyer_rev_av, RIL_p10_176.buyer_rev_av, RIL_p10_177.buyer_rev_av, RIL_p10_178.buyer_rev_av, RIL_p10_179.buyer_rev_av,
                          RIL_p10_180.buyer_rev_av, RIL_p10_181.buyer_rev_av, RIL_p10_182.buyer_rev_av, RIL_p10_183.buyer_rev_av, RIL_p10_184.buyer_rev_av,
                          RIL_p10_185.buyer_rev_av, RIL_p10_186.buyer_rev_av, RIL_p10_187.buyer_rev_av, RIL_p10_188.buyer_rev_av, RIL_p10_189.buyer_rev_av,
                          RIL_p10_190.buyer_rev_av, RIL_p10_191.buyer_rev_av, RIL_p10_192.buyer_rev_av, RIL_p10_193.buyer_rev_av, RIL_p10_194.buyer_rev_av,
                          RIL_p10_195.buyer_rev_av, RIL_p10_196.buyer_rev_av, RIL_p10_197.buyer_rev_av, RIL_p10_198.buyer_rev_av, RIL_p10_199.buyer_rev_av)


buyer_rev_av_RIL_p10_mean = [np.mean(i) for i in buyer_rev_av_RIL_p10]
buyer_rev_av_RIL_p10_lower = [np.percentile(i, 10) for i in buyer_rev_av_RIL_p10]
buyer_rev_av_RIL_p10_upper = [np.percentile(i, 90) for i in buyer_rev_av_RIL_p10]
###############




############ Average revenue customers
print('Creating seller_rev_av_RIL_p10')
seller_rev_av_RIL_p10 = zip(RIL_p10_00.seller_rev_av, RIL_p10_01.seller_rev_av, RIL_p10_02.seller_rev_av, RIL_p10_03.seller_rev_av, RIL_p10_04.seller_rev_av,
                          RIL_p10_05.seller_rev_av, RIL_p10_06.seller_rev_av, RIL_p10_07.seller_rev_av, RIL_p10_08.seller_rev_av, RIL_p10_09.seller_rev_av,
                          RIL_p10_10.seller_rev_av, RIL_p10_11.seller_rev_av, RIL_p10_12.seller_rev_av, RIL_p10_13.seller_rev_av, RIL_p10_14.seller_rev_av,
                          RIL_p10_15.seller_rev_av, RIL_p10_16.seller_rev_av, RIL_p10_17.seller_rev_av, RIL_p10_18.seller_rev_av, RIL_p10_19.seller_rev_av,
                          RIL_p10_20.seller_rev_av, RIL_p10_21.seller_rev_av, RIL_p10_22.seller_rev_av, RIL_p10_23.seller_rev_av, RIL_p10_24.seller_rev_av,
                          RIL_p10_25.seller_rev_av, RIL_p10_26.seller_rev_av, RIL_p10_27.seller_rev_av, RIL_p10_28.seller_rev_av, RIL_p10_29.seller_rev_av,
                          RIL_p10_30.seller_rev_av, RIL_p10_31.seller_rev_av, RIL_p10_32.seller_rev_av, RIL_p10_33.seller_rev_av, RIL_p10_34.seller_rev_av,
                          RIL_p10_35.seller_rev_av, RIL_p10_36.seller_rev_av, RIL_p10_37.seller_rev_av, RIL_p10_38.seller_rev_av, RIL_p10_39.seller_rev_av,
                          RIL_p10_40.seller_rev_av, RIL_p10_40.seller_rev_av, RIL_p10_41.seller_rev_av, RIL_p10_42.seller_rev_av, RIL_p10_43.seller_rev_av,
                          RIL_p10_44.seller_rev_av, RIL_p10_45.seller_rev_av, RIL_p10_46.seller_rev_av, RIL_p10_47.seller_rev_av, RIL_p10_48.seller_rev_av,
                          RIL_p10_49.seller_rev_av, RIL_p10_50.seller_rev_av, RIL_p10_51.seller_rev_av, RIL_p10_52.seller_rev_av, RIL_p10_53.seller_rev_av,
                          RIL_p10_54.seller_rev_av, RIL_p10_55.seller_rev_av, RIL_p10_56.seller_rev_av, RIL_p10_57.seller_rev_av, RIL_p10_58.seller_rev_av,
                          RIL_p10_59.seller_rev_av, RIL_p10_60.seller_rev_av, RIL_p10_61.seller_rev_av, RIL_p10_62.seller_rev_av, RIL_p10_63.seller_rev_av,
                          RIL_p10_64.seller_rev_av, RIL_p10_65.seller_rev_av, RIL_p10_66.seller_rev_av, RIL_p10_67.seller_rev_av, RIL_p10_68.seller_rev_av,
                          RIL_p10_69.seller_rev_av, RIL_p10_70.seller_rev_av, RIL_p10_71.seller_rev_av, RIL_p10_72.seller_rev_av, RIL_p10_73.seller_rev_av,
                          RIL_p10_74.seller_rev_av, RIL_p10_75.seller_rev_av, RIL_p10_76.seller_rev_av, RIL_p10_77.seller_rev_av, RIL_p10_78.seller_rev_av,
                          RIL_p10_79.seller_rev_av, RIL_p10_80.seller_rev_av, RIL_p10_81.seller_rev_av, RIL_p10_82.seller_rev_av, RIL_p10_83.seller_rev_av,
                          RIL_p10_84.seller_rev_av, RIL_p10_85.seller_rev_av, RIL_p10_86.seller_rev_av, RIL_p10_87.seller_rev_av, RIL_p10_88.seller_rev_av,
                          RIL_p10_89.seller_rev_av, RIL_p10_90.seller_rev_av, RIL_p10_91.seller_rev_av, RIL_p10_92.seller_rev_av, RIL_p10_93.seller_rev_av,
                          RIL_p10_94.seller_rev_av, RIL_p10_95.seller_rev_av, RIL_p10_96.seller_rev_av, RIL_p10_97.seller_rev_av, RIL_p10_98.seller_rev_av,
                          RIL_p10_99.seller_rev_av, RIL_p10_100.seller_rev_av,
                          RIL_p10_101.seller_rev_av, RIL_p10_102.seller_rev_av, RIL_p10_103.seller_rev_av, RIL_p10_104.seller_rev_av, RIL_p10_105.seller_rev_av,
                          RIL_p10_106.seller_rev_av, RIL_p10_107.seller_rev_av, RIL_p10_108.seller_rev_av, RIL_p10_109.seller_rev_av, RIL_p10_110.seller_rev_av,
                          RIL_p10_111.seller_rev_av, RIL_p10_112.seller_rev_av, RIL_p10_113.seller_rev_av, RIL_p10_114.seller_rev_av, RIL_p10_115.seller_rev_av,
                          RIL_p10_116.seller_rev_av, RIL_p10_117.seller_rev_av, RIL_p10_118.seller_rev_av, RIL_p10_119.seller_rev_av, RIL_p10_120.seller_rev_av,
                          RIL_p10_121.seller_rev_av, RIL_p10_122.seller_rev_av, RIL_p10_123.seller_rev_av, RIL_p10_124.seller_rev_av, RIL_p10_125.seller_rev_av,
                          RIL_p10_126.seller_rev_av, RIL_p10_127.seller_rev_av, RIL_p10_128.seller_rev_av, RIL_p10_129.seller_rev_av, RIL_p10_130.seller_rev_av,
                          RIL_p10_131.seller_rev_av, RIL_p10_132.seller_rev_av, RIL_p10_133.seller_rev_av, RIL_p10_134.seller_rev_av, RIL_p10_135.seller_rev_av,
                          RIL_p10_136.seller_rev_av, RIL_p10_137.seller_rev_av, RIL_p10_138.seller_rev_av, RIL_p10_139.seller_rev_av, RIL_p10_140.seller_rev_av,
                          RIL_p10_140.seller_rev_av, RIL_p10_141.seller_rev_av, RIL_p10_142.seller_rev_av, RIL_p10_143.seller_rev_av, RIL_p10_144.seller_rev_av,
                          RIL_p10_145.seller_rev_av, RIL_p10_146.seller_rev_av, RIL_p10_147.seller_rev_av, RIL_p10_148.seller_rev_av, RIL_p10_149.seller_rev_av,
                          RIL_p10_150.seller_rev_av, RIL_p10_151.seller_rev_av, RIL_p10_152.seller_rev_av, RIL_p10_153.seller_rev_av, RIL_p10_154.seller_rev_av,
                          RIL_p10_155.seller_rev_av, RIL_p10_156.seller_rev_av, RIL_p10_157.seller_rev_av, RIL_p10_158.seller_rev_av, RIL_p10_159.seller_rev_av,
                          RIL_p10_160.seller_rev_av, RIL_p10_161.seller_rev_av, RIL_p10_162.seller_rev_av, RIL_p10_163.seller_rev_av, RIL_p10_164.seller_rev_av,
                          RIL_p10_165.seller_rev_av, RIL_p10_166.seller_rev_av, RIL_p10_167.seller_rev_av, RIL_p10_168.seller_rev_av, RIL_p10_169.seller_rev_av,
                          RIL_p10_170.seller_rev_av, RIL_p10_171.seller_rev_av, RIL_p10_172.seller_rev_av, RIL_p10_173.seller_rev_av, RIL_p10_174.seller_rev_av,
                          RIL_p10_175.seller_rev_av, RIL_p10_176.seller_rev_av, RIL_p10_177.seller_rev_av, RIL_p10_178.seller_rev_av, RIL_p10_179.seller_rev_av,
                          RIL_p10_180.seller_rev_av, RIL_p10_181.seller_rev_av, RIL_p10_182.seller_rev_av, RIL_p10_183.seller_rev_av, RIL_p10_184.seller_rev_av,
                          RIL_p10_185.seller_rev_av, RIL_p10_186.seller_rev_av, RIL_p10_187.seller_rev_av, RIL_p10_188.seller_rev_av, RIL_p10_189.seller_rev_av,
                          RIL_p10_190.seller_rev_av, RIL_p10_191.seller_rev_av, RIL_p10_192.seller_rev_av, RIL_p10_193.seller_rev_av, RIL_p10_194.seller_rev_av,
                          RIL_p10_195.seller_rev_av, RIL_p10_196.seller_rev_av, RIL_p10_197.seller_rev_av, RIL_p10_198.seller_rev_av, RIL_p10_199.seller_rev_av)


seller_rev_av_RIL_p10_mean = [np.mean(i) for i in seller_rev_av_RIL_p10]
seller_rev_av_RIL_p10_lower = [np.percentile(i, 10) for i in seller_rev_av_RIL_p10]
seller_rev_av_RIL_p10_upper = [np.percentile(i, 90) for i in seller_rev_av_RIL_p10]
###############



############ Average revenue customers
print('Creating prov_rev_av_RIL_p10')
prov_rev_av_RIL_p10 = zip(RIL_p10_00.prov_rev_av, RIL_p10_01.prov_rev_av, RIL_p10_02.prov_rev_av, RIL_p10_03.prov_rev_av, RIL_p10_04.prov_rev_av,
                          RIL_p10_05.prov_rev_av, RIL_p10_06.prov_rev_av, RIL_p10_07.prov_rev_av, RIL_p10_08.prov_rev_av, RIL_p10_09.prov_rev_av,
                          RIL_p10_10.prov_rev_av, RIL_p10_11.prov_rev_av, RIL_p10_12.prov_rev_av, RIL_p10_13.prov_rev_av, RIL_p10_14.prov_rev_av,
                          RIL_p10_15.prov_rev_av, RIL_p10_16.prov_rev_av, RIL_p10_17.prov_rev_av, RIL_p10_18.prov_rev_av, RIL_p10_19.prov_rev_av,
                          RIL_p10_20.prov_rev_av, RIL_p10_21.prov_rev_av, RIL_p10_22.prov_rev_av, RIL_p10_23.prov_rev_av, RIL_p10_24.prov_rev_av,
                          RIL_p10_25.prov_rev_av, RIL_p10_26.prov_rev_av, RIL_p10_27.prov_rev_av, RIL_p10_28.prov_rev_av, RIL_p10_29.prov_rev_av,
                          RIL_p10_30.prov_rev_av, RIL_p10_31.prov_rev_av, RIL_p10_32.prov_rev_av, RIL_p10_33.prov_rev_av, RIL_p10_34.prov_rev_av,
                          RIL_p10_35.prov_rev_av, RIL_p10_36.prov_rev_av, RIL_p10_37.prov_rev_av, RIL_p10_38.prov_rev_av, RIL_p10_39.prov_rev_av,
                          RIL_p10_40.prov_rev_av, RIL_p10_40.prov_rev_av, RIL_p10_41.prov_rev_av, RIL_p10_42.prov_rev_av, RIL_p10_43.prov_rev_av,
                          RIL_p10_44.prov_rev_av, RIL_p10_45.prov_rev_av, RIL_p10_46.prov_rev_av, RIL_p10_47.prov_rev_av, RIL_p10_48.prov_rev_av,
                          RIL_p10_49.prov_rev_av, RIL_p10_50.prov_rev_av, RIL_p10_51.prov_rev_av, RIL_p10_52.prov_rev_av, RIL_p10_53.prov_rev_av,
                          RIL_p10_54.prov_rev_av, RIL_p10_55.prov_rev_av, RIL_p10_56.prov_rev_av, RIL_p10_57.prov_rev_av, RIL_p10_58.prov_rev_av,
                          RIL_p10_59.prov_rev_av, RIL_p10_60.prov_rev_av, RIL_p10_61.prov_rev_av, RIL_p10_62.prov_rev_av, RIL_p10_63.prov_rev_av,
                          RIL_p10_64.prov_rev_av, RIL_p10_65.prov_rev_av, RIL_p10_66.prov_rev_av, RIL_p10_67.prov_rev_av, RIL_p10_68.prov_rev_av,
                          RIL_p10_69.prov_rev_av, RIL_p10_70.prov_rev_av, RIL_p10_71.prov_rev_av, RIL_p10_72.prov_rev_av, RIL_p10_73.prov_rev_av,
                          RIL_p10_74.prov_rev_av, RIL_p10_75.prov_rev_av, RIL_p10_76.prov_rev_av, RIL_p10_77.prov_rev_av, RIL_p10_78.prov_rev_av,
                          RIL_p10_79.prov_rev_av, RIL_p10_80.prov_rev_av, RIL_p10_81.prov_rev_av, RIL_p10_82.prov_rev_av, RIL_p10_83.prov_rev_av,
                          RIL_p10_84.prov_rev_av, RIL_p10_85.prov_rev_av, RIL_p10_86.prov_rev_av, RIL_p10_87.prov_rev_av, RIL_p10_88.prov_rev_av,
                          RIL_p10_89.prov_rev_av, RIL_p10_90.prov_rev_av, RIL_p10_91.prov_rev_av, RIL_p10_92.prov_rev_av, RIL_p10_93.prov_rev_av,
                          RIL_p10_94.prov_rev_av, RIL_p10_95.prov_rev_av, RIL_p10_96.prov_rev_av, RIL_p10_97.prov_rev_av, RIL_p10_98.prov_rev_av,
                          RIL_p10_99.prov_rev_av, RIL_p10_100.prov_rev_av,
                          RIL_p10_101.prov_rev_av, RIL_p10_102.prov_rev_av, RIL_p10_103.prov_rev_av, RIL_p10_104.prov_rev_av, RIL_p10_105.prov_rev_av,
                          RIL_p10_106.prov_rev_av, RIL_p10_107.prov_rev_av, RIL_p10_108.prov_rev_av, RIL_p10_109.prov_rev_av, RIL_p10_110.prov_rev_av,
                          RIL_p10_111.prov_rev_av, RIL_p10_112.prov_rev_av, RIL_p10_113.prov_rev_av, RIL_p10_114.prov_rev_av, RIL_p10_115.prov_rev_av,
                          RIL_p10_116.prov_rev_av, RIL_p10_117.prov_rev_av, RIL_p10_118.prov_rev_av, RIL_p10_119.prov_rev_av, RIL_p10_120.prov_rev_av,
                          RIL_p10_121.prov_rev_av, RIL_p10_122.prov_rev_av, RIL_p10_123.prov_rev_av, RIL_p10_124.prov_rev_av, RIL_p10_125.prov_rev_av,
                          RIL_p10_126.prov_rev_av, RIL_p10_127.prov_rev_av, RIL_p10_128.prov_rev_av, RIL_p10_129.prov_rev_av, RIL_p10_130.prov_rev_av,
                          RIL_p10_131.prov_rev_av, RIL_p10_132.prov_rev_av, RIL_p10_133.prov_rev_av, RIL_p10_134.prov_rev_av, RIL_p10_135.prov_rev_av,
                          RIL_p10_136.prov_rev_av, RIL_p10_137.prov_rev_av, RIL_p10_138.prov_rev_av, RIL_p10_139.prov_rev_av, RIL_p10_140.prov_rev_av,
                          RIL_p10_140.prov_rev_av, RIL_p10_141.prov_rev_av, RIL_p10_142.prov_rev_av, RIL_p10_143.prov_rev_av, RIL_p10_144.prov_rev_av,
                          RIL_p10_145.prov_rev_av, RIL_p10_146.prov_rev_av, RIL_p10_147.prov_rev_av, RIL_p10_148.prov_rev_av, RIL_p10_149.prov_rev_av,
                          RIL_p10_150.prov_rev_av, RIL_p10_151.prov_rev_av, RIL_p10_152.prov_rev_av, RIL_p10_153.prov_rev_av, RIL_p10_154.prov_rev_av,
                          RIL_p10_155.prov_rev_av, RIL_p10_156.prov_rev_av, RIL_p10_157.prov_rev_av, RIL_p10_158.prov_rev_av, RIL_p10_159.prov_rev_av,
                          RIL_p10_160.prov_rev_av, RIL_p10_161.prov_rev_av, RIL_p10_162.prov_rev_av, RIL_p10_163.prov_rev_av, RIL_p10_164.prov_rev_av,
                          RIL_p10_165.prov_rev_av, RIL_p10_166.prov_rev_av, RIL_p10_167.prov_rev_av, RIL_p10_168.prov_rev_av, RIL_p10_169.prov_rev_av,
                          RIL_p10_170.prov_rev_av, RIL_p10_171.prov_rev_av, RIL_p10_172.prov_rev_av, RIL_p10_173.prov_rev_av, RIL_p10_174.prov_rev_av,
                          RIL_p10_175.prov_rev_av, RIL_p10_176.prov_rev_av, RIL_p10_177.prov_rev_av, RIL_p10_178.prov_rev_av, RIL_p10_179.prov_rev_av,
                          RIL_p10_180.prov_rev_av, RIL_p10_181.prov_rev_av, RIL_p10_182.prov_rev_av, RIL_p10_183.prov_rev_av, RIL_p10_184.prov_rev_av,
                          RIL_p10_185.prov_rev_av, RIL_p10_186.prov_rev_av, RIL_p10_187.prov_rev_av, RIL_p10_188.prov_rev_av, RIL_p10_189.prov_rev_av,
                          RIL_p10_190.prov_rev_av, RIL_p10_191.prov_rev_av, RIL_p10_192.prov_rev_av, RIL_p10_193.prov_rev_av, RIL_p10_194.prov_rev_av,
                          RIL_p10_195.prov_rev_av, RIL_p10_196.prov_rev_av, RIL_p10_197.prov_rev_av, RIL_p10_198.prov_rev_av, RIL_p10_199.prov_rev_av)


prov_rev_av_RIL_p10_mean = [np.mean(i) for i in prov_rev_av_RIL_p10]
prov_rev_av_RIL_p10_lower = [np.percentile(i, 10) for i in prov_rev_av_RIL_p10]
prov_rev_av_RIL_p10_upper = [np.percentile(i, 90) for i in prov_rev_av_RIL_p10]
###############


print('Creating buyer_rev_av_RILS_p10')
buyer_rev_av_RILS_p10 = zip(RILS_p10_00.buyer_rev_av, RILS_p10_01.buyer_rev_av, RILS_p10_02.buyer_rev_av, RILS_p10_03.buyer_rev_av, RILS_p10_04.buyer_rev_av,
                          RILS_p10_05.buyer_rev_av, RILS_p10_06.buyer_rev_av, RILS_p10_07.buyer_rev_av, RILS_p10_08.buyer_rev_av, RILS_p10_09.buyer_rev_av,
                          RILS_p10_10.buyer_rev_av, RILS_p10_11.buyer_rev_av, RILS_p10_12.buyer_rev_av, RILS_p10_13.buyer_rev_av, RILS_p10_14.buyer_rev_av,
                          RILS_p10_15.buyer_rev_av, RILS_p10_16.buyer_rev_av, RILS_p10_17.buyer_rev_av, RILS_p10_18.buyer_rev_av, RILS_p10_19.buyer_rev_av,
                          RILS_p10_20.buyer_rev_av, RILS_p10_21.buyer_rev_av, RILS_p10_22.buyer_rev_av, RILS_p10_23.buyer_rev_av, RILS_p10_24.buyer_rev_av,
                          RILS_p10_25.buyer_rev_av, RILS_p10_26.buyer_rev_av, RILS_p10_27.buyer_rev_av, RILS_p10_28.buyer_rev_av, RILS_p10_29.buyer_rev_av,
                          RILS_p10_30.buyer_rev_av, RILS_p10_31.buyer_rev_av, RILS_p10_32.buyer_rev_av, RILS_p10_33.buyer_rev_av, RILS_p10_34.buyer_rev_av,
                          RILS_p10_35.buyer_rev_av, RILS_p10_36.buyer_rev_av, RILS_p10_37.buyer_rev_av, RILS_p10_38.buyer_rev_av, RILS_p10_39.buyer_rev_av,
                          RILS_p10_40.buyer_rev_av, RILS_p10_40.buyer_rev_av, RILS_p10_41.buyer_rev_av, RILS_p10_42.buyer_rev_av, RILS_p10_43.buyer_rev_av,
                          RILS_p10_44.buyer_rev_av, RILS_p10_45.buyer_rev_av, RILS_p10_46.buyer_rev_av, RILS_p10_47.buyer_rev_av, RILS_p10_48.buyer_rev_av,
                          RILS_p10_49.buyer_rev_av, RILS_p10_50.buyer_rev_av, RILS_p10_51.buyer_rev_av, RILS_p10_52.buyer_rev_av, RILS_p10_53.buyer_rev_av,
                          RILS_p10_54.buyer_rev_av, RILS_p10_55.buyer_rev_av, RILS_p10_56.buyer_rev_av, RILS_p10_57.buyer_rev_av, RILS_p10_58.buyer_rev_av,
                          RILS_p10_59.buyer_rev_av, RILS_p10_60.buyer_rev_av, RILS_p10_61.buyer_rev_av, RILS_p10_62.buyer_rev_av, RILS_p10_63.buyer_rev_av,
                          RILS_p10_64.buyer_rev_av, RILS_p10_65.buyer_rev_av, RILS_p10_66.buyer_rev_av, RILS_p10_67.buyer_rev_av, RILS_p10_68.buyer_rev_av,
                          RILS_p10_69.buyer_rev_av, RILS_p10_70.buyer_rev_av, RILS_p10_71.buyer_rev_av, RILS_p10_72.buyer_rev_av, RILS_p10_73.buyer_rev_av,
                          RILS_p10_74.buyer_rev_av, RILS_p10_75.buyer_rev_av, RILS_p10_76.buyer_rev_av, RILS_p10_77.buyer_rev_av, RILS_p10_78.buyer_rev_av,
                          RILS_p10_79.buyer_rev_av, RILS_p10_80.buyer_rev_av, RILS_p10_81.buyer_rev_av, RILS_p10_82.buyer_rev_av, RILS_p10_83.buyer_rev_av,
                          RILS_p10_84.buyer_rev_av, RILS_p10_85.buyer_rev_av, RILS_p10_86.buyer_rev_av, RILS_p10_87.buyer_rev_av, RILS_p10_88.buyer_rev_av,
                          RILS_p10_89.buyer_rev_av, RILS_p10_90.buyer_rev_av, RILS_p10_91.buyer_rev_av, RILS_p10_92.buyer_rev_av, RILS_p10_93.buyer_rev_av,
                          RILS_p10_94.buyer_rev_av, RILS_p10_95.buyer_rev_av, RILS_p10_96.buyer_rev_av, RILS_p10_97.buyer_rev_av, RILS_p10_98.buyer_rev_av,
                          RILS_p10_99.buyer_rev_av, RILS_p10_100.buyer_rev_av,
                          RILS_p10_101.buyer_rev_av, RILS_p10_102.buyer_rev_av, RILS_p10_103.buyer_rev_av, RILS_p10_104.buyer_rev_av, RILS_p10_105.buyer_rev_av,
                          RILS_p10_106.buyer_rev_av, RILS_p10_107.buyer_rev_av, RILS_p10_108.buyer_rev_av, RILS_p10_109.buyer_rev_av, RILS_p10_110.buyer_rev_av,
                          RILS_p10_111.buyer_rev_av, RILS_p10_112.buyer_rev_av, RILS_p10_113.buyer_rev_av, RILS_p10_114.buyer_rev_av, RILS_p10_115.buyer_rev_av,
                          RILS_p10_116.buyer_rev_av, RILS_p10_117.buyer_rev_av, RILS_p10_118.buyer_rev_av, RILS_p10_119.buyer_rev_av, RILS_p10_120.buyer_rev_av,
                          RILS_p10_121.buyer_rev_av, RILS_p10_122.buyer_rev_av, RILS_p10_123.buyer_rev_av, RILS_p10_124.buyer_rev_av, RILS_p10_125.buyer_rev_av,
                          RILS_p10_126.buyer_rev_av, RILS_p10_127.buyer_rev_av, RILS_p10_128.buyer_rev_av, RILS_p10_129.buyer_rev_av, RILS_p10_130.buyer_rev_av,
                          RILS_p10_131.buyer_rev_av, RILS_p10_132.buyer_rev_av, RILS_p10_133.buyer_rev_av, RILS_p10_134.buyer_rev_av, RILS_p10_135.buyer_rev_av,
                          RILS_p10_136.buyer_rev_av, RILS_p10_137.buyer_rev_av, RILS_p10_138.buyer_rev_av, RILS_p10_139.buyer_rev_av, RILS_p10_140.buyer_rev_av,
                          RILS_p10_140.buyer_rev_av, RILS_p10_141.buyer_rev_av, RILS_p10_142.buyer_rev_av, RILS_p10_143.buyer_rev_av, RILS_p10_144.buyer_rev_av,
                          RILS_p10_145.buyer_rev_av, RILS_p10_146.buyer_rev_av, RILS_p10_147.buyer_rev_av, RILS_p10_148.buyer_rev_av, RILS_p10_149.buyer_rev_av,
                          RILS_p10_150.buyer_rev_av, RILS_p10_151.buyer_rev_av, RILS_p10_152.buyer_rev_av, RILS_p10_153.buyer_rev_av, RILS_p10_154.buyer_rev_av,
                          RILS_p10_155.buyer_rev_av, RILS_p10_156.buyer_rev_av, RILS_p10_157.buyer_rev_av, RILS_p10_158.buyer_rev_av, RILS_p10_159.buyer_rev_av,
                          RILS_p10_160.buyer_rev_av, RILS_p10_161.buyer_rev_av, RILS_p10_162.buyer_rev_av, RILS_p10_163.buyer_rev_av, RILS_p10_164.buyer_rev_av,
                          RILS_p10_165.buyer_rev_av, RILS_p10_166.buyer_rev_av, RILS_p10_167.buyer_rev_av, RILS_p10_168.buyer_rev_av, RILS_p10_169.buyer_rev_av,
                          RILS_p10_170.buyer_rev_av, RILS_p10_171.buyer_rev_av, RILS_p10_172.buyer_rev_av, RILS_p10_173.buyer_rev_av, RILS_p10_174.buyer_rev_av,
                          RILS_p10_175.buyer_rev_av, RILS_p10_176.buyer_rev_av, RILS_p10_177.buyer_rev_av, RILS_p10_178.buyer_rev_av, RILS_p10_179.buyer_rev_av,
                          RILS_p10_180.buyer_rev_av, RILS_p10_181.buyer_rev_av, RILS_p10_182.buyer_rev_av, RILS_p10_183.buyer_rev_av, RILS_p10_184.buyer_rev_av,
                          RILS_p10_185.buyer_rev_av, RILS_p10_186.buyer_rev_av, RILS_p10_187.buyer_rev_av, RILS_p10_188.buyer_rev_av, RILS_p10_189.buyer_rev_av,
                          RILS_p10_190.buyer_rev_av, RILS_p10_191.buyer_rev_av, RILS_p10_192.buyer_rev_av, RILS_p10_193.buyer_rev_av, RILS_p10_194.buyer_rev_av,
                          RILS_p10_195.buyer_rev_av, RILS_p10_196.buyer_rev_av, RILS_p10_197.buyer_rev_av, RILS_p10_198.buyer_rev_av, RILS_p10_199.buyer_rev_av)


buyer_rev_av_RILS_p10_mean = [np.mean(i) for i in buyer_rev_av_RILS_p10]
buyer_rev_av_RILS_p10_lower = [np.percentile(i, 10) for i in buyer_rev_av_RILS_p10]
buyer_rev_av_RILS_p10_upper = [np.percentile(i, 90) for i in buyer_rev_av_RILS_p10]
###############




############ Average revenue customers
print('Creating seller_rev_av_RILS_p10')
seller_rev_av_RILS_p10 = zip(RILS_p10_00.seller_rev_av, RILS_p10_01.seller_rev_av, RILS_p10_02.seller_rev_av, RILS_p10_03.seller_rev_av, RILS_p10_04.seller_rev_av,
                          RILS_p10_05.seller_rev_av, RILS_p10_06.seller_rev_av, RILS_p10_07.seller_rev_av, RILS_p10_08.seller_rev_av, RILS_p10_09.seller_rev_av,
                          RILS_p10_10.seller_rev_av, RILS_p10_11.seller_rev_av, RILS_p10_12.seller_rev_av, RILS_p10_13.seller_rev_av, RILS_p10_14.seller_rev_av,
                          RILS_p10_15.seller_rev_av, RILS_p10_16.seller_rev_av, RILS_p10_17.seller_rev_av, RILS_p10_18.seller_rev_av, RILS_p10_19.seller_rev_av,
                          RILS_p10_20.seller_rev_av, RILS_p10_21.seller_rev_av, RILS_p10_22.seller_rev_av, RILS_p10_23.seller_rev_av, RILS_p10_24.seller_rev_av,
                          RILS_p10_25.seller_rev_av, RILS_p10_26.seller_rev_av, RILS_p10_27.seller_rev_av, RILS_p10_28.seller_rev_av, RILS_p10_29.seller_rev_av,
                          RILS_p10_30.seller_rev_av, RILS_p10_31.seller_rev_av, RILS_p10_32.seller_rev_av, RILS_p10_33.seller_rev_av, RILS_p10_34.seller_rev_av,
                          RILS_p10_35.seller_rev_av, RILS_p10_36.seller_rev_av, RILS_p10_37.seller_rev_av, RILS_p10_38.seller_rev_av, RILS_p10_39.seller_rev_av,
                          RILS_p10_40.seller_rev_av, RILS_p10_40.seller_rev_av, RILS_p10_41.seller_rev_av, RILS_p10_42.seller_rev_av, RILS_p10_43.seller_rev_av,
                          RILS_p10_44.seller_rev_av, RILS_p10_45.seller_rev_av, RILS_p10_46.seller_rev_av, RILS_p10_47.seller_rev_av, RILS_p10_48.seller_rev_av,
                          RILS_p10_49.seller_rev_av, RILS_p10_50.seller_rev_av, RILS_p10_51.seller_rev_av, RILS_p10_52.seller_rev_av, RILS_p10_53.seller_rev_av,
                          RILS_p10_54.seller_rev_av, RILS_p10_55.seller_rev_av, RILS_p10_56.seller_rev_av, RILS_p10_57.seller_rev_av, RILS_p10_58.seller_rev_av,
                          RILS_p10_59.seller_rev_av, RILS_p10_60.seller_rev_av, RILS_p10_61.seller_rev_av, RILS_p10_62.seller_rev_av, RILS_p10_63.seller_rev_av,
                          RILS_p10_64.seller_rev_av, RILS_p10_65.seller_rev_av, RILS_p10_66.seller_rev_av, RILS_p10_67.seller_rev_av, RILS_p10_68.seller_rev_av,
                          RILS_p10_69.seller_rev_av, RILS_p10_70.seller_rev_av, RILS_p10_71.seller_rev_av, RILS_p10_72.seller_rev_av, RILS_p10_73.seller_rev_av,
                          RILS_p10_74.seller_rev_av, RILS_p10_75.seller_rev_av, RILS_p10_76.seller_rev_av, RILS_p10_77.seller_rev_av, RILS_p10_78.seller_rev_av,
                          RILS_p10_79.seller_rev_av, RILS_p10_80.seller_rev_av, RILS_p10_81.seller_rev_av, RILS_p10_82.seller_rev_av, RILS_p10_83.seller_rev_av,
                          RILS_p10_84.seller_rev_av, RILS_p10_85.seller_rev_av, RILS_p10_86.seller_rev_av, RILS_p10_87.seller_rev_av, RILS_p10_88.seller_rev_av,
                          RILS_p10_89.seller_rev_av, RILS_p10_90.seller_rev_av, RILS_p10_91.seller_rev_av, RILS_p10_92.seller_rev_av, RILS_p10_93.seller_rev_av,
                          RILS_p10_94.seller_rev_av, RILS_p10_95.seller_rev_av, RILS_p10_96.seller_rev_av, RILS_p10_97.seller_rev_av, RILS_p10_98.seller_rev_av,
                          RILS_p10_99.seller_rev_av, RILS_p10_100.seller_rev_av,
                          RILS_p10_101.seller_rev_av, RILS_p10_102.seller_rev_av, RILS_p10_103.seller_rev_av, RILS_p10_104.seller_rev_av, RILS_p10_105.seller_rev_av,
                          RILS_p10_106.seller_rev_av, RILS_p10_107.seller_rev_av, RILS_p10_108.seller_rev_av, RILS_p10_109.seller_rev_av, RILS_p10_110.seller_rev_av,
                          RILS_p10_111.seller_rev_av, RILS_p10_112.seller_rev_av, RILS_p10_113.seller_rev_av, RILS_p10_114.seller_rev_av, RILS_p10_115.seller_rev_av,
                          RILS_p10_116.seller_rev_av, RILS_p10_117.seller_rev_av, RILS_p10_118.seller_rev_av, RILS_p10_119.seller_rev_av, RILS_p10_120.seller_rev_av,
                          RILS_p10_121.seller_rev_av, RILS_p10_122.seller_rev_av, RILS_p10_123.seller_rev_av, RILS_p10_124.seller_rev_av, RILS_p10_125.seller_rev_av,
                          RILS_p10_126.seller_rev_av, RILS_p10_127.seller_rev_av, RILS_p10_128.seller_rev_av, RILS_p10_129.seller_rev_av, RILS_p10_130.seller_rev_av,
                          RILS_p10_131.seller_rev_av, RILS_p10_132.seller_rev_av, RILS_p10_133.seller_rev_av, RILS_p10_134.seller_rev_av, RILS_p10_135.seller_rev_av,
                          RILS_p10_136.seller_rev_av, RILS_p10_137.seller_rev_av, RILS_p10_138.seller_rev_av, RILS_p10_139.seller_rev_av, RILS_p10_140.seller_rev_av,
                          RILS_p10_140.seller_rev_av, RILS_p10_141.seller_rev_av, RILS_p10_142.seller_rev_av, RILS_p10_143.seller_rev_av, RILS_p10_144.seller_rev_av,
                          RILS_p10_145.seller_rev_av, RILS_p10_146.seller_rev_av, RILS_p10_147.seller_rev_av, RILS_p10_148.seller_rev_av, RILS_p10_149.seller_rev_av,
                          RILS_p10_150.seller_rev_av, RILS_p10_151.seller_rev_av, RILS_p10_152.seller_rev_av, RILS_p10_153.seller_rev_av, RILS_p10_154.seller_rev_av,
                          RILS_p10_155.seller_rev_av, RILS_p10_156.seller_rev_av, RILS_p10_157.seller_rev_av, RILS_p10_158.seller_rev_av, RILS_p10_159.seller_rev_av,
                          RILS_p10_160.seller_rev_av, RILS_p10_161.seller_rev_av, RILS_p10_162.seller_rev_av, RILS_p10_163.seller_rev_av, RILS_p10_164.seller_rev_av,
                          RILS_p10_165.seller_rev_av, RILS_p10_166.seller_rev_av, RILS_p10_167.seller_rev_av, RILS_p10_168.seller_rev_av, RILS_p10_169.seller_rev_av,
                          RILS_p10_170.seller_rev_av, RILS_p10_171.seller_rev_av, RILS_p10_172.seller_rev_av, RILS_p10_173.seller_rev_av, RILS_p10_174.seller_rev_av,
                          RILS_p10_175.seller_rev_av, RILS_p10_176.seller_rev_av, RILS_p10_177.seller_rev_av, RILS_p10_178.seller_rev_av, RILS_p10_179.seller_rev_av,
                          RILS_p10_180.seller_rev_av, RILS_p10_181.seller_rev_av, RILS_p10_182.seller_rev_av, RILS_p10_183.seller_rev_av, RILS_p10_184.seller_rev_av,
                          RILS_p10_185.seller_rev_av, RILS_p10_186.seller_rev_av, RILS_p10_187.seller_rev_av, RILS_p10_188.seller_rev_av, RILS_p10_189.seller_rev_av,
                          RILS_p10_190.seller_rev_av, RILS_p10_191.seller_rev_av, RILS_p10_192.seller_rev_av, RILS_p10_193.seller_rev_av, RILS_p10_194.seller_rev_av,
                          RILS_p10_195.seller_rev_av, RILS_p10_196.seller_rev_av, RILS_p10_197.seller_rev_av, RILS_p10_198.seller_rev_av, RILS_p10_199.seller_rev_av)


seller_rev_av_RILS_p10_mean = [np.mean(i) for i in seller_rev_av_RILS_p10]
seller_rev_av_RILS_p10_lower = [np.percentile(i, 10) for i in seller_rev_av_RILS_p10]
seller_rev_av_RILS_p10_upper = [np.percentile(i, 90) for i in seller_rev_av_RILS_p10]
###############



############ Average revenue customers
print('Creating prov_rev_av_RILS_p10')
prov_rev_av_RILS_p10 = zip(RILS_p10_00.prov_rev_av, RILS_p10_01.prov_rev_av, RILS_p10_02.prov_rev_av, RILS_p10_03.prov_rev_av, RILS_p10_04.prov_rev_av,
                          RILS_p10_05.prov_rev_av, RILS_p10_06.prov_rev_av, RILS_p10_07.prov_rev_av, RILS_p10_08.prov_rev_av, RILS_p10_09.prov_rev_av,
                          RILS_p10_10.prov_rev_av, RILS_p10_11.prov_rev_av, RILS_p10_12.prov_rev_av, RILS_p10_13.prov_rev_av, RILS_p10_14.prov_rev_av,
                          RILS_p10_15.prov_rev_av, RILS_p10_16.prov_rev_av, RILS_p10_17.prov_rev_av, RILS_p10_18.prov_rev_av, RILS_p10_19.prov_rev_av,
                          RILS_p10_20.prov_rev_av, RILS_p10_21.prov_rev_av, RILS_p10_22.prov_rev_av, RILS_p10_23.prov_rev_av, RILS_p10_24.prov_rev_av,
                          RILS_p10_25.prov_rev_av, RILS_p10_26.prov_rev_av, RILS_p10_27.prov_rev_av, RILS_p10_28.prov_rev_av, RILS_p10_29.prov_rev_av,
                          RILS_p10_30.prov_rev_av, RILS_p10_31.prov_rev_av, RILS_p10_32.prov_rev_av, RILS_p10_33.prov_rev_av, RILS_p10_34.prov_rev_av,
                          RILS_p10_35.prov_rev_av, RILS_p10_36.prov_rev_av, RILS_p10_37.prov_rev_av, RILS_p10_38.prov_rev_av, RILS_p10_39.prov_rev_av,
                          RILS_p10_40.prov_rev_av, RILS_p10_40.prov_rev_av, RILS_p10_41.prov_rev_av, RILS_p10_42.prov_rev_av, RILS_p10_43.prov_rev_av,
                          RILS_p10_44.prov_rev_av, RILS_p10_45.prov_rev_av, RILS_p10_46.prov_rev_av, RILS_p10_47.prov_rev_av, RILS_p10_48.prov_rev_av,
                          RILS_p10_49.prov_rev_av, RILS_p10_50.prov_rev_av, RILS_p10_51.prov_rev_av, RILS_p10_52.prov_rev_av, RILS_p10_53.prov_rev_av,
                          RILS_p10_54.prov_rev_av, RILS_p10_55.prov_rev_av, RILS_p10_56.prov_rev_av, RILS_p10_57.prov_rev_av, RILS_p10_58.prov_rev_av,
                          RILS_p10_59.prov_rev_av, RILS_p10_60.prov_rev_av, RILS_p10_61.prov_rev_av, RILS_p10_62.prov_rev_av, RILS_p10_63.prov_rev_av,
                          RILS_p10_64.prov_rev_av, RILS_p10_65.prov_rev_av, RILS_p10_66.prov_rev_av, RILS_p10_67.prov_rev_av, RILS_p10_68.prov_rev_av,
                          RILS_p10_69.prov_rev_av, RILS_p10_70.prov_rev_av, RILS_p10_71.prov_rev_av, RILS_p10_72.prov_rev_av, RILS_p10_73.prov_rev_av,
                          RILS_p10_74.prov_rev_av, RILS_p10_75.prov_rev_av, RILS_p10_76.prov_rev_av, RILS_p10_77.prov_rev_av, RILS_p10_78.prov_rev_av,
                          RILS_p10_79.prov_rev_av, RILS_p10_80.prov_rev_av, RILS_p10_81.prov_rev_av, RILS_p10_82.prov_rev_av, RILS_p10_83.prov_rev_av,
                          RILS_p10_84.prov_rev_av, RILS_p10_85.prov_rev_av, RILS_p10_86.prov_rev_av, RILS_p10_87.prov_rev_av, RILS_p10_88.prov_rev_av,
                          RILS_p10_89.prov_rev_av, RILS_p10_90.prov_rev_av, RILS_p10_91.prov_rev_av, RILS_p10_92.prov_rev_av, RILS_p10_93.prov_rev_av,
                          RILS_p10_94.prov_rev_av, RILS_p10_95.prov_rev_av, RILS_p10_96.prov_rev_av, RILS_p10_97.prov_rev_av, RILS_p10_98.prov_rev_av,
                          RILS_p10_99.prov_rev_av, RILS_p10_100.prov_rev_av,
                          RILS_p10_101.prov_rev_av, RILS_p10_102.prov_rev_av, RILS_p10_103.prov_rev_av, RILS_p10_104.prov_rev_av, RILS_p10_105.prov_rev_av,
                          RILS_p10_106.prov_rev_av, RILS_p10_107.prov_rev_av, RILS_p10_108.prov_rev_av, RILS_p10_109.prov_rev_av, RILS_p10_110.prov_rev_av,
                          RILS_p10_111.prov_rev_av, RILS_p10_112.prov_rev_av, RILS_p10_113.prov_rev_av, RILS_p10_114.prov_rev_av, RILS_p10_115.prov_rev_av,
                          RILS_p10_116.prov_rev_av, RILS_p10_117.prov_rev_av, RILS_p10_118.prov_rev_av, RILS_p10_119.prov_rev_av, RILS_p10_120.prov_rev_av,
                          RILS_p10_121.prov_rev_av, RILS_p10_122.prov_rev_av, RILS_p10_123.prov_rev_av, RILS_p10_124.prov_rev_av, RILS_p10_125.prov_rev_av,
                          RILS_p10_126.prov_rev_av, RILS_p10_127.prov_rev_av, RILS_p10_128.prov_rev_av, RILS_p10_129.prov_rev_av, RILS_p10_130.prov_rev_av,
                          RILS_p10_131.prov_rev_av, RILS_p10_132.prov_rev_av, RILS_p10_133.prov_rev_av, RILS_p10_134.prov_rev_av, RILS_p10_135.prov_rev_av,
                          RILS_p10_136.prov_rev_av, RILS_p10_137.prov_rev_av, RILS_p10_138.prov_rev_av, RILS_p10_139.prov_rev_av, RILS_p10_140.prov_rev_av,
                          RILS_p10_140.prov_rev_av, RILS_p10_141.prov_rev_av, RILS_p10_142.prov_rev_av, RILS_p10_143.prov_rev_av, RILS_p10_144.prov_rev_av,
                          RILS_p10_145.prov_rev_av, RILS_p10_146.prov_rev_av, RILS_p10_147.prov_rev_av, RILS_p10_148.prov_rev_av, RILS_p10_149.prov_rev_av,
                          RILS_p10_150.prov_rev_av, RILS_p10_151.prov_rev_av, RILS_p10_152.prov_rev_av, RILS_p10_153.prov_rev_av, RILS_p10_154.prov_rev_av,
                          RILS_p10_155.prov_rev_av, RILS_p10_156.prov_rev_av, RILS_p10_157.prov_rev_av, RILS_p10_158.prov_rev_av, RILS_p10_159.prov_rev_av,
                          RILS_p10_160.prov_rev_av, RILS_p10_161.prov_rev_av, RILS_p10_162.prov_rev_av, RILS_p10_163.prov_rev_av, RILS_p10_164.prov_rev_av,
                          RILS_p10_165.prov_rev_av, RILS_p10_166.prov_rev_av, RILS_p10_167.prov_rev_av, RILS_p10_168.prov_rev_av, RILS_p10_169.prov_rev_av,
                          RILS_p10_170.prov_rev_av, RILS_p10_171.prov_rev_av, RILS_p10_172.prov_rev_av, RILS_p10_173.prov_rev_av, RILS_p10_174.prov_rev_av,
                          RILS_p10_175.prov_rev_av, RILS_p10_176.prov_rev_av, RILS_p10_177.prov_rev_av, RILS_p10_178.prov_rev_av, RILS_p10_179.prov_rev_av,
                          RILS_p10_180.prov_rev_av, RILS_p10_181.prov_rev_av, RILS_p10_182.prov_rev_av, RILS_p10_183.prov_rev_av, RILS_p10_184.prov_rev_av,
                          RILS_p10_185.prov_rev_av, RILS_p10_186.prov_rev_av, RILS_p10_187.prov_rev_av, RILS_p10_188.prov_rev_av, RILS_p10_189.prov_rev_av,
                          RILS_p10_190.prov_rev_av, RILS_p10_191.prov_rev_av, RILS_p10_192.prov_rev_av, RILS_p10_193.prov_rev_av, RILS_p10_194.prov_rev_av,
                          RILS_p10_195.prov_rev_av, RILS_p10_196.prov_rev_av, RILS_p10_197.prov_rev_av, RILS_p10_198.prov_rev_av, RILS_p10_199.prov_rev_av)


prov_rev_av_RILS_p10_mean = [np.mean(i) for i in prov_rev_av_RILS_p10]
prov_rev_av_RILS_p10_lower = [np.percentile(i, 10) for i in prov_rev_av_RILS_p10]
prov_rev_av_RILS_p10_upper = [np.percentile(i, 90) for i in prov_rev_av_RILS_p10]
###############

print('Creating max_prov_customers_RILS_p10_pcc0')

max_prov_customers_RILS_p10_pcc0 = zip(RILS_p10_pcc0_00.prov_cn_max, RILS_p10_pcc0_01.prov_cn_max, RILS_p10_pcc0_02.prov_cn_max, RILS_p10_pcc0_03.prov_cn_max, RILS_p10_pcc0_04.prov_cn_max,
                          RILS_p10_pcc0_05.prov_cn_max, RILS_p10_pcc0_06.prov_cn_max, RILS_p10_pcc0_07.prov_cn_max, RILS_p10_pcc0_08.prov_cn_max, RILS_p10_pcc0_09.prov_cn_max,
                          RILS_p10_pcc0_10.prov_cn_max, RILS_p10_pcc0_11.prov_cn_max, RILS_p10_pcc0_12.prov_cn_max, RILS_p10_pcc0_13.prov_cn_max, RILS_p10_pcc0_14.prov_cn_max,
                          RILS_p10_pcc0_15.prov_cn_max, RILS_p10_pcc0_16.prov_cn_max, RILS_p10_pcc0_17.prov_cn_max, RILS_p10_pcc0_18.prov_cn_max, RILS_p10_pcc0_19.prov_cn_max,
                          RILS_p10_pcc0_20.prov_cn_max, RILS_p10_pcc0_21.prov_cn_max, RILS_p10_pcc0_22.prov_cn_max, RILS_p10_pcc0_23.prov_cn_max, RILS_p10_pcc0_24.prov_cn_max,
                          RILS_p10_pcc0_25.prov_cn_max, RILS_p10_pcc0_26.prov_cn_max, RILS_p10_pcc0_27.prov_cn_max, RILS_p10_pcc0_28.prov_cn_max, RILS_p10_pcc0_29.prov_cn_max,
                          RILS_p10_pcc0_30.prov_cn_max, RILS_p10_pcc0_31.prov_cn_max, RILS_p10_pcc0_32.prov_cn_max, RILS_p10_pcc0_33.prov_cn_max, RILS_p10_pcc0_34.prov_cn_max,
                          RILS_p10_pcc0_35.prov_cn_max, RILS_p10_pcc0_36.prov_cn_max, RILS_p10_pcc0_37.prov_cn_max, RILS_p10_pcc0_38.prov_cn_max, RILS_p10_pcc0_39.prov_cn_max,
                          RILS_p10_pcc0_40.prov_cn_max, RILS_p10_pcc0_40.prov_cn_max, RILS_p10_pcc0_41.prov_cn_max, RILS_p10_pcc0_42.prov_cn_max, RILS_p10_pcc0_43.prov_cn_max,
                          RILS_p10_pcc0_44.prov_cn_max, RILS_p10_pcc0_45.prov_cn_max, RILS_p10_pcc0_46.prov_cn_max, RILS_p10_pcc0_47.prov_cn_max, RILS_p10_pcc0_48.prov_cn_max,
                          RILS_p10_pcc0_49.prov_cn_max, RILS_p10_pcc0_50.prov_cn_max, RILS_p10_pcc0_51.prov_cn_max, RILS_p10_pcc0_52.prov_cn_max, RILS_p10_pcc0_53.prov_cn_max,
                          RILS_p10_pcc0_54.prov_cn_max, RILS_p10_pcc0_55.prov_cn_max, RILS_p10_pcc0_56.prov_cn_max, RILS_p10_pcc0_57.prov_cn_max, RILS_p10_pcc0_58.prov_cn_max,
                          RILS_p10_pcc0_59.prov_cn_max, RILS_p10_pcc0_60.prov_cn_max, RILS_p10_pcc0_61.prov_cn_max, RILS_p10_pcc0_62.prov_cn_max, RILS_p10_pcc0_63.prov_cn_max,
                          RILS_p10_pcc0_64.prov_cn_max, RILS_p10_pcc0_65.prov_cn_max, RILS_p10_pcc0_66.prov_cn_max, RILS_p10_pcc0_67.prov_cn_max, RILS_p10_pcc0_68.prov_cn_max,
                          RILS_p10_pcc0_69.prov_cn_max, RILS_p10_pcc0_70.prov_cn_max, RILS_p10_pcc0_71.prov_cn_max, RILS_p10_pcc0_72.prov_cn_max, RILS_p10_pcc0_73.prov_cn_max,
                          RILS_p10_pcc0_74.prov_cn_max, RILS_p10_pcc0_75.prov_cn_max, RILS_p10_pcc0_76.prov_cn_max, RILS_p10_pcc0_77.prov_cn_max, RILS_p10_pcc0_78.prov_cn_max,
                          RILS_p10_pcc0_79.prov_cn_max, RILS_p10_pcc0_80.prov_cn_max, RILS_p10_pcc0_81.prov_cn_max, RILS_p10_pcc0_82.prov_cn_max, RILS_p10_pcc0_83.prov_cn_max,
                          RILS_p10_pcc0_84.prov_cn_max, RILS_p10_pcc0_85.prov_cn_max, RILS_p10_pcc0_86.prov_cn_max, RILS_p10_pcc0_87.prov_cn_max, RILS_p10_pcc0_88.prov_cn_max,
                          RILS_p10_pcc0_89.prov_cn_max, RILS_p10_pcc0_90.prov_cn_max, RILS_p10_pcc0_91.prov_cn_max, RILS_p10_pcc0_92.prov_cn_max, RILS_p10_pcc0_93.prov_cn_max,
                          RILS_p10_pcc0_94.prov_cn_max, RILS_p10_pcc0_95.prov_cn_max, RILS_p10_pcc0_96.prov_cn_max, RILS_p10_pcc0_97.prov_cn_max, RILS_p10_pcc0_98.prov_cn_max,
                          RILS_p10_pcc0_99.prov_cn_max, RILS_p10_pcc0_100.prov_cn_max,
                          RILS_p10_pcc0_101.prov_cn_max, RILS_p10_pcc0_102.prov_cn_max, RILS_p10_pcc0_103.prov_cn_max, RILS_p10_pcc0_104.prov_cn_max, RILS_p10_pcc0_105.prov_cn_max,
                          RILS_p10_pcc0_106.prov_cn_max, RILS_p10_pcc0_107.prov_cn_max, RILS_p10_pcc0_108.prov_cn_max, RILS_p10_pcc0_109.prov_cn_max, RILS_p10_pcc0_110.prov_cn_max,
                          RILS_p10_pcc0_111.prov_cn_max, RILS_p10_pcc0_112.prov_cn_max, RILS_p10_pcc0_113.prov_cn_max, RILS_p10_pcc0_114.prov_cn_max, RILS_p10_pcc0_115.prov_cn_max,
                          RILS_p10_pcc0_116.prov_cn_max, RILS_p10_pcc0_117.prov_cn_max, RILS_p10_pcc0_118.prov_cn_max, RILS_p10_pcc0_119.prov_cn_max, RILS_p10_pcc0_120.prov_cn_max,
                          RILS_p10_pcc0_121.prov_cn_max, RILS_p10_pcc0_122.prov_cn_max, RILS_p10_pcc0_123.prov_cn_max, RILS_p10_pcc0_124.prov_cn_max, RILS_p10_pcc0_125.prov_cn_max,
                          RILS_p10_pcc0_126.prov_cn_max, RILS_p10_pcc0_127.prov_cn_max, RILS_p10_pcc0_128.prov_cn_max, RILS_p10_pcc0_129.prov_cn_max, RILS_p10_pcc0_130.prov_cn_max,
                          RILS_p10_pcc0_131.prov_cn_max, RILS_p10_pcc0_132.prov_cn_max, RILS_p10_pcc0_133.prov_cn_max, RILS_p10_pcc0_134.prov_cn_max, RILS_p10_pcc0_135.prov_cn_max,
                          RILS_p10_pcc0_136.prov_cn_max, RILS_p10_pcc0_137.prov_cn_max, RILS_p10_pcc0_138.prov_cn_max, RILS_p10_pcc0_139.prov_cn_max, RILS_p10_pcc0_140.prov_cn_max,
                          RILS_p10_pcc0_140.prov_cn_max, RILS_p10_pcc0_141.prov_cn_max, RILS_p10_pcc0_142.prov_cn_max, RILS_p10_pcc0_143.prov_cn_max, RILS_p10_pcc0_144.prov_cn_max,
                          RILS_p10_pcc0_145.prov_cn_max, RILS_p10_pcc0_146.prov_cn_max, RILS_p10_pcc0_147.prov_cn_max, RILS_p10_pcc0_148.prov_cn_max, RILS_p10_pcc0_149.prov_cn_max,
                          RILS_p10_pcc0_150.prov_cn_max, RILS_p10_pcc0_151.prov_cn_max, RILS_p10_pcc0_152.prov_cn_max, RILS_p10_pcc0_153.prov_cn_max, RILS_p10_pcc0_154.prov_cn_max,
                          RILS_p10_pcc0_155.prov_cn_max, RILS_p10_pcc0_156.prov_cn_max, RILS_p10_pcc0_157.prov_cn_max, RILS_p10_pcc0_158.prov_cn_max, RILS_p10_pcc0_159.prov_cn_max,
                          RILS_p10_pcc0_160.prov_cn_max, RILS_p10_pcc0_161.prov_cn_max, RILS_p10_pcc0_162.prov_cn_max, RILS_p10_pcc0_163.prov_cn_max, RILS_p10_pcc0_164.prov_cn_max,
                          RILS_p10_pcc0_165.prov_cn_max, RILS_p10_pcc0_166.prov_cn_max, RILS_p10_pcc0_167.prov_cn_max, RILS_p10_pcc0_168.prov_cn_max, RILS_p10_pcc0_169.prov_cn_max,
                          RILS_p10_pcc0_170.prov_cn_max, RILS_p10_pcc0_171.prov_cn_max, RILS_p10_pcc0_172.prov_cn_max, RILS_p10_pcc0_173.prov_cn_max, RILS_p10_pcc0_174.prov_cn_max,
                          RILS_p10_pcc0_175.prov_cn_max, RILS_p10_pcc0_176.prov_cn_max, RILS_p10_pcc0_177.prov_cn_max, RILS_p10_pcc0_178.prov_cn_max, RILS_p10_pcc0_179.prov_cn_max,
                          RILS_p10_pcc0_180.prov_cn_max, RILS_p10_pcc0_181.prov_cn_max, RILS_p10_pcc0_182.prov_cn_max, RILS_p10_pcc0_183.prov_cn_max, RILS_p10_pcc0_184.prov_cn_max,
                          RILS_p10_pcc0_185.prov_cn_max, RILS_p10_pcc0_186.prov_cn_max, RILS_p10_pcc0_187.prov_cn_max, RILS_p10_pcc0_188.prov_cn_max, RILS_p10_pcc0_189.prov_cn_max,
                          RILS_p10_pcc0_190.prov_cn_max, RILS_p10_pcc0_191.prov_cn_max, RILS_p10_pcc0_192.prov_cn_max, RILS_p10_pcc0_193.prov_cn_max, RILS_p10_pcc0_194.prov_cn_max,
                          RILS_p10_pcc0_195.prov_cn_max, RILS_p10_pcc0_196.prov_cn_max, RILS_p10_pcc0_197.prov_cn_max, RILS_p10_pcc0_198.prov_cn_max, RILS_p10_pcc0_199.prov_cn_max)


max_prov_customers_RILS_p10_pcc0_mean = [np.mean(i) for i in max_prov_customers_RILS_p10_pcc0]
max_prov_customers_RILS_p10_pcc0_lower = [np.percentile(i, 10) for i in max_prov_customers_RILS_p10_pcc0]
max_prov_customers_RILS_p10_pcc0_upper = [np.percentile(i, 90) for i in max_prov_customers_RILS_p10_pcc0]

print('Creating max_prov_customers_RILS_p10_pcc10')

max_prov_customers_RILS_p10_pcc10 = zip(RILS_p10_pcc10_00.prov_cn_max, RILS_p10_pcc10_01.prov_cn_max, RILS_p10_pcc10_02.prov_cn_max, RILS_p10_pcc10_03.prov_cn_max, RILS_p10_pcc10_04.prov_cn_max,
                          RILS_p10_pcc10_05.prov_cn_max, RILS_p10_pcc10_06.prov_cn_max, RILS_p10_pcc10_07.prov_cn_max, RILS_p10_pcc10_08.prov_cn_max, RILS_p10_pcc10_09.prov_cn_max,
                          RILS_p10_pcc10_10.prov_cn_max, RILS_p10_pcc10_11.prov_cn_max, RILS_p10_pcc10_12.prov_cn_max, RILS_p10_pcc10_13.prov_cn_max, RILS_p10_pcc10_14.prov_cn_max,
                          RILS_p10_pcc10_15.prov_cn_max, RILS_p10_pcc10_16.prov_cn_max, RILS_p10_pcc10_17.prov_cn_max, RILS_p10_pcc10_18.prov_cn_max, RILS_p10_pcc10_19.prov_cn_max,
                          RILS_p10_pcc10_20.prov_cn_max, RILS_p10_pcc10_21.prov_cn_max, RILS_p10_pcc10_22.prov_cn_max, RILS_p10_pcc10_23.prov_cn_max, RILS_p10_pcc10_24.prov_cn_max,
                          RILS_p10_pcc10_25.prov_cn_max, RILS_p10_pcc10_26.prov_cn_max, RILS_p10_pcc10_27.prov_cn_max, RILS_p10_pcc10_28.prov_cn_max, RILS_p10_pcc10_29.prov_cn_max,
                          RILS_p10_pcc10_30.prov_cn_max, RILS_p10_pcc10_31.prov_cn_max, RILS_p10_pcc10_32.prov_cn_max, RILS_p10_pcc10_33.prov_cn_max, RILS_p10_pcc10_34.prov_cn_max,
                          RILS_p10_pcc10_35.prov_cn_max, RILS_p10_pcc10_36.prov_cn_max, RILS_p10_pcc10_37.prov_cn_max, RILS_p10_pcc10_38.prov_cn_max, RILS_p10_pcc10_39.prov_cn_max,
                          RILS_p10_pcc10_40.prov_cn_max, RILS_p10_pcc10_40.prov_cn_max, RILS_p10_pcc10_41.prov_cn_max, RILS_p10_pcc10_42.prov_cn_max, RILS_p10_pcc10_43.prov_cn_max,
                          RILS_p10_pcc10_44.prov_cn_max, RILS_p10_pcc10_45.prov_cn_max, RILS_p10_pcc10_46.prov_cn_max, RILS_p10_pcc10_47.prov_cn_max, RILS_p10_pcc10_48.prov_cn_max,
                          RILS_p10_pcc10_49.prov_cn_max, RILS_p10_pcc10_50.prov_cn_max, RILS_p10_pcc10_51.prov_cn_max, RILS_p10_pcc10_52.prov_cn_max, RILS_p10_pcc10_53.prov_cn_max,
                          RILS_p10_pcc10_54.prov_cn_max, RILS_p10_pcc10_55.prov_cn_max, RILS_p10_pcc10_56.prov_cn_max, RILS_p10_pcc10_57.prov_cn_max, RILS_p10_pcc10_58.prov_cn_max,
                          RILS_p10_pcc10_59.prov_cn_max, RILS_p10_pcc10_60.prov_cn_max, RILS_p10_pcc10_61.prov_cn_max, RILS_p10_pcc10_62.prov_cn_max, RILS_p10_pcc10_63.prov_cn_max,
                          RILS_p10_pcc10_64.prov_cn_max, RILS_p10_pcc10_65.prov_cn_max, RILS_p10_pcc10_66.prov_cn_max, RILS_p10_pcc10_67.prov_cn_max, RILS_p10_pcc10_68.prov_cn_max,
                          RILS_p10_pcc10_69.prov_cn_max, RILS_p10_pcc10_70.prov_cn_max, RILS_p10_pcc10_71.prov_cn_max, RILS_p10_pcc10_72.prov_cn_max, RILS_p10_pcc10_73.prov_cn_max,
                          RILS_p10_pcc10_74.prov_cn_max, RILS_p10_pcc10_75.prov_cn_max, RILS_p10_pcc10_76.prov_cn_max, RILS_p10_pcc10_77.prov_cn_max, RILS_p10_pcc10_78.prov_cn_max,
                          RILS_p10_pcc10_79.prov_cn_max, RILS_p10_pcc10_80.prov_cn_max, RILS_p10_pcc10_81.prov_cn_max, RILS_p10_pcc10_82.prov_cn_max, RILS_p10_pcc10_83.prov_cn_max,
                          RILS_p10_pcc10_84.prov_cn_max, RILS_p10_pcc10_85.prov_cn_max, RILS_p10_pcc10_86.prov_cn_max, RILS_p10_pcc10_87.prov_cn_max, RILS_p10_pcc10_88.prov_cn_max,
                          RILS_p10_pcc10_89.prov_cn_max, RILS_p10_pcc10_90.prov_cn_max, RILS_p10_pcc10_91.prov_cn_max, RILS_p10_pcc10_92.prov_cn_max, RILS_p10_pcc10_93.prov_cn_max,
                          RILS_p10_pcc10_94.prov_cn_max, RILS_p10_pcc10_95.prov_cn_max, RILS_p10_pcc10_96.prov_cn_max, RILS_p10_pcc10_97.prov_cn_max, RILS_p10_pcc10_98.prov_cn_max,
                          RILS_p10_pcc10_99.prov_cn_max)# , RILS_p10_pcc10_100.prov_cn_max)
                          # RILS_p10_pcc10_101.prov_cn_max, RILS_p10_pcc10_102.prov_cn_max, RILS_p10_pcc10_103.prov_cn_max, RILS_p10_pcc10_104.prov_cn_max, RILS_p10_pcc10_105.prov_cn_max,
                          # RILS_p10_pcc10_106.prov_cn_max, RILS_p10_pcc10_107.prov_cn_max, RILS_p10_pcc10_108.prov_cn_max, RILS_p10_pcc10_109.prov_cn_max, RILS_p10_pcc10_110.prov_cn_max,
                          # RILS_p10_pcc10_111.prov_cn_max, RILS_p10_pcc10_112.prov_cn_max, RILS_p10_pcc10_113.prov_cn_max, RILS_p10_pcc10_114.prov_cn_max, RILS_p10_pcc10_115.prov_cn_max,
                          # RILS_p10_pcc10_116.prov_cn_max, RILS_p10_pcc10_117.prov_cn_max, RILS_p10_pcc10_118.prov_cn_max, RILS_p10_pcc10_119.prov_cn_max, RILS_p10_pcc10_120.prov_cn_max,
                          # RILS_p10_pcc10_121.prov_cn_max, RILS_p10_pcc10_122.prov_cn_max, RILS_p10_pcc10_123.prov_cn_max, RILS_p10_pcc10_124.prov_cn_max, RILS_p10_pcc10_125.prov_cn_max,
                          # RILS_p10_pcc10_126.prov_cn_max, RILS_p10_pcc10_127.prov_cn_max, RILS_p10_pcc10_128.prov_cn_max, RILS_p10_pcc10_129.prov_cn_max, RILS_p10_pcc10_130.prov_cn_max,
                          # RILS_p10_pcc10_131.prov_cn_max, RILS_p10_pcc10_132.prov_cn_max, RILS_p10_pcc10_133.prov_cn_max, RILS_p10_pcc10_134.prov_cn_max, RILS_p10_pcc10_135.prov_cn_max,
                          # RILS_p10_pcc10_136.prov_cn_max, RILS_p10_pcc10_137.prov_cn_max, RILS_p10_pcc10_138.prov_cn_max, RILS_p10_pcc10_139.prov_cn_max, RILS_p10_pcc10_140.prov_cn_max,
                          # RILS_p10_pcc10_140.prov_cn_max, RILS_p10_pcc10_141.prov_cn_max, RILS_p10_pcc10_142.prov_cn_max, RILS_p10_pcc10_143.prov_cn_max, RILS_p10_pcc10_144.prov_cn_max,
                          # RILS_p10_pcc10_145.prov_cn_max, RILS_p10_pcc10_146.prov_cn_max, RILS_p10_pcc10_147.prov_cn_max, RILS_p10_pcc10_148.prov_cn_max, RILS_p10_pcc10_149.prov_cn_max,
                          # RILS_p10_pcc10_150.prov_cn_max, RILS_p10_pcc10_151.prov_cn_max, RILS_p10_pcc10_152.prov_cn_max, RILS_p10_pcc10_153.prov_cn_max, RILS_p10_pcc10_154.prov_cn_max,
                          # RILS_p10_pcc10_155.prov_cn_max, RILS_p10_pcc10_156.prov_cn_max, RILS_p10_pcc10_157.prov_cn_max, RILS_p10_pcc10_158.prov_cn_max, RILS_p10_pcc10_159.prov_cn_max,
                          # RILS_p10_pcc10_160.prov_cn_max, RILS_p10_pcc10_161.prov_cn_max, RILS_p10_pcc10_162.prov_cn_max, RILS_p10_pcc10_163.prov_cn_max, RILS_p10_pcc10_164.prov_cn_max,
                          # RILS_p10_pcc10_165.prov_cn_max, RILS_p10_pcc10_166.prov_cn_max, RILS_p10_pcc10_167.prov_cn_max, RILS_p10_pcc10_168.prov_cn_max, RILS_p10_pcc10_169.prov_cn_max,
                          # RILS_p10_pcc10_170.prov_cn_max, RILS_p10_pcc10_171.prov_cn_max, RILS_p10_pcc10_172.prov_cn_max, RILS_p10_pcc10_173.prov_cn_max, RILS_p10_pcc10_174.prov_cn_max,
                          # RILS_p10_pcc10_175.prov_cn_max, RILS_p10_pcc10_176.prov_cn_max, RILS_p10_pcc10_177.prov_cn_max, RILS_p10_pcc10_178.prov_cn_max, RILS_p10_pcc10_179.prov_cn_max,
                          # RILS_p10_pcc10_180.prov_cn_max, RILS_p10_pcc10_181.prov_cn_max, RILS_p10_pcc10_182.prov_cn_max, RILS_p10_pcc10_183.prov_cn_max, RILS_p10_pcc10_184.prov_cn_max,
                          # RILS_p10_pcc10_185.prov_cn_max, RILS_p10_pcc10_186.prov_cn_max, RILS_p10_pcc10_187.prov_cn_max, RILS_p10_pcc10_188.prov_cn_max, RILS_p10_pcc10_189.prov_cn_max,
                          # RILS_p10_pcc10_190.prov_cn_max, RILS_p10_pcc10_191.prov_cn_max, RILS_p10_pcc10_192.prov_cn_max, RILS_p10_pcc10_193.prov_cn_max, RILS_p10_pcc10_194.prov_cn_max,
                          # RILS_p10_pcc10_195.prov_cn_max, RILS_p10_pcc10_196.prov_cn_max, RILS_p10_pcc10_197.prov_cn_max, RILS_p10_pcc10_198.prov_cn_max, RILS_p10_pcc10_199.prov_cn_max)


max_prov_customers_RILS_p10_pcc10_mean = [np.mean(i) for i in max_prov_customers_RILS_p10_pcc10]
max_prov_customers_RILS_p10_pcc10_lower = [np.percentile(i, 10) for i in max_prov_customers_RILS_p10_pcc10]
max_prov_customers_RILS_p10_pcc10_upper = [np.percentile(i, 90) for i in max_prov_customers_RILS_p10_pcc10]


print('Creating buyer_rev_av_RO_p01_ef0')
buyer_rev_av_RO_p01_ef0 = zip(RO_p01_ef0_00.buyer_rev_av, RO_p01_ef0_01.buyer_rev_av, RO_p01_ef0_02.buyer_rev_av, RO_p01_ef0_03.buyer_rev_av, RO_p01_ef0_04.buyer_rev_av,
                          RO_p01_ef0_05.buyer_rev_av, RO_p01_ef0_06.buyer_rev_av, RO_p01_ef0_07.buyer_rev_av, RO_p01_ef0_08.buyer_rev_av, RO_p01_ef0_09.buyer_rev_av,
                          RO_p01_ef0_10.buyer_rev_av, RO_p01_ef0_11.buyer_rev_av, RO_p01_ef0_12.buyer_rev_av, RO_p01_ef0_13.buyer_rev_av, RO_p01_ef0_14.buyer_rev_av,
                          RO_p01_ef0_15.buyer_rev_av, RO_p01_ef0_16.buyer_rev_av, RO_p01_ef0_17.buyer_rev_av, RO_p01_ef0_18.buyer_rev_av, RO_p01_ef0_19.buyer_rev_av,
                          RO_p01_ef0_20.buyer_rev_av, RO_p01_ef0_21.buyer_rev_av, RO_p01_ef0_22.buyer_rev_av, RO_p01_ef0_23.buyer_rev_av, RO_p01_ef0_24.buyer_rev_av,
                          RO_p01_ef0_25.buyer_rev_av, RO_p01_ef0_26.buyer_rev_av, RO_p01_ef0_27.buyer_rev_av, RO_p01_ef0_28.buyer_rev_av, RO_p01_ef0_29.buyer_rev_av,
                          RO_p01_ef0_30.buyer_rev_av, RO_p01_ef0_31.buyer_rev_av, RO_p01_ef0_32.buyer_rev_av, RO_p01_ef0_33.buyer_rev_av, RO_p01_ef0_34.buyer_rev_av,
                          RO_p01_ef0_35.buyer_rev_av, RO_p01_ef0_36.buyer_rev_av, RO_p01_ef0_37.buyer_rev_av, RO_p01_ef0_38.buyer_rev_av, RO_p01_ef0_39.buyer_rev_av,
                          RO_p01_ef0_40.buyer_rev_av, RO_p01_ef0_40.buyer_rev_av, RO_p01_ef0_41.buyer_rev_av, RO_p01_ef0_42.buyer_rev_av, RO_p01_ef0_43.buyer_rev_av,
                          RO_p01_ef0_44.buyer_rev_av, RO_p01_ef0_45.buyer_rev_av, RO_p01_ef0_46.buyer_rev_av, RO_p01_ef0_47.buyer_rev_av, RO_p01_ef0_48.buyer_rev_av,
                          RO_p01_ef0_49.buyer_rev_av, RO_p01_ef0_50.buyer_rev_av, RO_p01_ef0_51.buyer_rev_av, RO_p01_ef0_52.buyer_rev_av, RO_p01_ef0_53.buyer_rev_av,
                          RO_p01_ef0_54.buyer_rev_av, RO_p01_ef0_55.buyer_rev_av, RO_p01_ef0_56.buyer_rev_av, RO_p01_ef0_57.buyer_rev_av, RO_p01_ef0_58.buyer_rev_av,
                          RO_p01_ef0_59.buyer_rev_av, RO_p01_ef0_60.buyer_rev_av, RO_p01_ef0_61.buyer_rev_av, RO_p01_ef0_62.buyer_rev_av, RO_p01_ef0_63.buyer_rev_av,
                          RO_p01_ef0_64.buyer_rev_av, RO_p01_ef0_65.buyer_rev_av, RO_p01_ef0_66.buyer_rev_av, RO_p01_ef0_67.buyer_rev_av, RO_p01_ef0_68.buyer_rev_av,
                          RO_p01_ef0_69.buyer_rev_av, RO_p01_ef0_70.buyer_rev_av, RO_p01_ef0_71.buyer_rev_av, RO_p01_ef0_72.buyer_rev_av, RO_p01_ef0_73.buyer_rev_av,
                          RO_p01_ef0_74.buyer_rev_av, RO_p01_ef0_75.buyer_rev_av, RO_p01_ef0_76.buyer_rev_av, RO_p01_ef0_77.buyer_rev_av, RO_p01_ef0_78.buyer_rev_av,
                          RO_p01_ef0_79.buyer_rev_av, RO_p01_ef0_80.buyer_rev_av, RO_p01_ef0_81.buyer_rev_av, RO_p01_ef0_82.buyer_rev_av, RO_p01_ef0_83.buyer_rev_av,
                          RO_p01_ef0_84.buyer_rev_av, RO_p01_ef0_85.buyer_rev_av, RO_p01_ef0_86.buyer_rev_av, RO_p01_ef0_87.buyer_rev_av, RO_p01_ef0_88.buyer_rev_av,
                          RO_p01_ef0_89.buyer_rev_av, RO_p01_ef0_90.buyer_rev_av, RO_p01_ef0_91.buyer_rev_av, RO_p01_ef0_92.buyer_rev_av, RO_p01_ef0_93.buyer_rev_av,
                          RO_p01_ef0_94.buyer_rev_av, RO_p01_ef0_95.buyer_rev_av, RO_p01_ef0_96.buyer_rev_av, RO_p01_ef0_97.buyer_rev_av, RO_p01_ef0_98.buyer_rev_av,
                          RO_p01_ef0_99.buyer_rev_av)


buyer_rev_av_RO_p01_ef0_mean = [np.mean(i) for i in buyer_rev_av_RO_p01_ef0]
buyer_rev_av_RO_p01_ef0_lower = [np.percentile(i, 10) for i in buyer_rev_av_RO_p01_ef0]
buyer_rev_av_RO_p01_ef0_upper = [np.percentile(i, 90) for i in buyer_rev_av_RO_p01_ef0]

print('Creating seller_rev_av_RO_p01_ef0')
seller_rev_av_RO_p01_ef0 = zip(RO_p01_ef0_00.seller_rev_av, RO_p01_ef0_01.seller_rev_av, RO_p01_ef0_02.seller_rev_av, RO_p01_ef0_03.seller_rev_av, RO_p01_ef0_04.seller_rev_av,
                          RO_p01_ef0_05.seller_rev_av, RO_p01_ef0_06.seller_rev_av, RO_p01_ef0_07.seller_rev_av, RO_p01_ef0_08.seller_rev_av, RO_p01_ef0_09.seller_rev_av,
                          RO_p01_ef0_10.seller_rev_av, RO_p01_ef0_11.seller_rev_av, RO_p01_ef0_12.seller_rev_av, RO_p01_ef0_13.seller_rev_av, RO_p01_ef0_14.seller_rev_av,
                          RO_p01_ef0_15.seller_rev_av, RO_p01_ef0_16.seller_rev_av, RO_p01_ef0_17.seller_rev_av, RO_p01_ef0_18.seller_rev_av, RO_p01_ef0_19.seller_rev_av,
                          RO_p01_ef0_20.seller_rev_av, RO_p01_ef0_21.seller_rev_av, RO_p01_ef0_22.seller_rev_av, RO_p01_ef0_23.seller_rev_av, RO_p01_ef0_24.seller_rev_av,
                          RO_p01_ef0_25.seller_rev_av, RO_p01_ef0_26.seller_rev_av, RO_p01_ef0_27.seller_rev_av, RO_p01_ef0_28.seller_rev_av, RO_p01_ef0_29.seller_rev_av,
                          RO_p01_ef0_30.seller_rev_av, RO_p01_ef0_31.seller_rev_av, RO_p01_ef0_32.seller_rev_av, RO_p01_ef0_33.seller_rev_av, RO_p01_ef0_34.seller_rev_av,
                          RO_p01_ef0_35.seller_rev_av, RO_p01_ef0_36.seller_rev_av, RO_p01_ef0_37.seller_rev_av, RO_p01_ef0_38.seller_rev_av, RO_p01_ef0_39.seller_rev_av,
                          RO_p01_ef0_40.seller_rev_av, RO_p01_ef0_40.seller_rev_av, RO_p01_ef0_41.seller_rev_av, RO_p01_ef0_42.seller_rev_av, RO_p01_ef0_43.seller_rev_av,
                          RO_p01_ef0_44.seller_rev_av, RO_p01_ef0_45.seller_rev_av, RO_p01_ef0_46.seller_rev_av, RO_p01_ef0_47.seller_rev_av, RO_p01_ef0_48.seller_rev_av,
                          RO_p01_ef0_49.seller_rev_av, RO_p01_ef0_50.seller_rev_av, RO_p01_ef0_51.seller_rev_av, RO_p01_ef0_52.seller_rev_av, RO_p01_ef0_53.seller_rev_av,
                          RO_p01_ef0_54.seller_rev_av, RO_p01_ef0_55.seller_rev_av, RO_p01_ef0_56.seller_rev_av, RO_p01_ef0_57.seller_rev_av, RO_p01_ef0_58.seller_rev_av,
                          RO_p01_ef0_59.seller_rev_av, RO_p01_ef0_60.seller_rev_av, RO_p01_ef0_61.seller_rev_av, RO_p01_ef0_62.seller_rev_av, RO_p01_ef0_63.seller_rev_av,
                          RO_p01_ef0_64.seller_rev_av, RO_p01_ef0_65.seller_rev_av, RO_p01_ef0_66.seller_rev_av, RO_p01_ef0_67.seller_rev_av, RO_p01_ef0_68.seller_rev_av,
                          RO_p01_ef0_69.seller_rev_av, RO_p01_ef0_70.seller_rev_av, RO_p01_ef0_71.seller_rev_av, RO_p01_ef0_72.seller_rev_av, RO_p01_ef0_73.seller_rev_av,
                          RO_p01_ef0_74.seller_rev_av, RO_p01_ef0_75.seller_rev_av, RO_p01_ef0_76.seller_rev_av, RO_p01_ef0_77.seller_rev_av, RO_p01_ef0_78.seller_rev_av,
                          RO_p01_ef0_79.seller_rev_av, RO_p01_ef0_80.seller_rev_av, RO_p01_ef0_81.seller_rev_av, RO_p01_ef0_82.seller_rev_av, RO_p01_ef0_83.seller_rev_av,
                          RO_p01_ef0_84.seller_rev_av, RO_p01_ef0_85.seller_rev_av, RO_p01_ef0_86.seller_rev_av, RO_p01_ef0_87.seller_rev_av, RO_p01_ef0_88.seller_rev_av,
                          RO_p01_ef0_89.seller_rev_av, RO_p01_ef0_90.seller_rev_av, RO_p01_ef0_91.seller_rev_av, RO_p01_ef0_92.seller_rev_av, RO_p01_ef0_93.seller_rev_av,
                          RO_p01_ef0_94.seller_rev_av, RO_p01_ef0_95.seller_rev_av, RO_p01_ef0_96.seller_rev_av, RO_p01_ef0_97.seller_rev_av, RO_p01_ef0_98.seller_rev_av,
                          RO_p01_ef0_99.seller_rev_av)


seller_rev_av_RO_p01_ef0_mean = [np.mean(i) for i in seller_rev_av_RO_p01_ef0]
seller_rev_av_RO_p01_ef0_lower = [np.percentile(i, 10) for i in seller_rev_av_RO_p01_ef0]
seller_rev_av_RO_p01_ef0_upper = [np.percentile(i, 90) for i in seller_rev_av_RO_p01_ef0]

print('Creating buyer_rev_av_RO_p01_efm200')
buyer_rev_av_RO_p01_efm200 = zip(RO_p01_efm200_00.buyer_rev_av, RO_p01_efm200_01.buyer_rev_av, RO_p01_efm200_02.buyer_rev_av, RO_p01_efm200_03.buyer_rev_av, RO_p01_efm200_04.buyer_rev_av,
                          RO_p01_efm200_05.buyer_rev_av, RO_p01_efm200_06.buyer_rev_av, RO_p01_efm200_07.buyer_rev_av, RO_p01_efm200_08.buyer_rev_av, RO_p01_efm200_09.buyer_rev_av,
                          RO_p01_efm200_10.buyer_rev_av, RO_p01_efm200_11.buyer_rev_av, RO_p01_efm200_12.buyer_rev_av, RO_p01_efm200_13.buyer_rev_av, RO_p01_efm200_14.buyer_rev_av,
                          RO_p01_efm200_15.buyer_rev_av, RO_p01_efm200_16.buyer_rev_av, RO_p01_efm200_17.buyer_rev_av, RO_p01_efm200_18.buyer_rev_av, RO_p01_efm200_19.buyer_rev_av,
                          RO_p01_efm200_20.buyer_rev_av, RO_p01_efm200_21.buyer_rev_av, RO_p01_efm200_22.buyer_rev_av, RO_p01_efm200_23.buyer_rev_av, RO_p01_efm200_24.buyer_rev_av,
                          RO_p01_efm200_25.buyer_rev_av, RO_p01_efm200_26.buyer_rev_av, RO_p01_efm200_27.buyer_rev_av, RO_p01_efm200_28.buyer_rev_av, RO_p01_efm200_29.buyer_rev_av,
                          RO_p01_efm200_30.buyer_rev_av, RO_p01_efm200_31.buyer_rev_av, RO_p01_efm200_32.buyer_rev_av, RO_p01_efm200_33.buyer_rev_av, RO_p01_efm200_34.buyer_rev_av,
                          RO_p01_efm200_35.buyer_rev_av, RO_p01_efm200_36.buyer_rev_av, RO_p01_efm200_37.buyer_rev_av, RO_p01_efm200_38.buyer_rev_av, RO_p01_efm200_39.buyer_rev_av,
                          RO_p01_efm200_40.buyer_rev_av, RO_p01_efm200_40.buyer_rev_av, RO_p01_efm200_41.buyer_rev_av, RO_p01_efm200_42.buyer_rev_av, RO_p01_efm200_43.buyer_rev_av,
                          RO_p01_efm200_44.buyer_rev_av, RO_p01_efm200_45.buyer_rev_av, RO_p01_efm200_46.buyer_rev_av, RO_p01_efm200_47.buyer_rev_av, RO_p01_efm200_48.buyer_rev_av,
                          RO_p01_efm200_49.buyer_rev_av, RO_p01_efm200_50.buyer_rev_av, RO_p01_efm200_51.buyer_rev_av, RO_p01_efm200_52.buyer_rev_av, RO_p01_efm200_53.buyer_rev_av,
                          RO_p01_efm200_54.buyer_rev_av, RO_p01_efm200_55.buyer_rev_av, RO_p01_efm200_56.buyer_rev_av, RO_p01_efm200_57.buyer_rev_av, RO_p01_efm200_58.buyer_rev_av,
                          RO_p01_efm200_59.buyer_rev_av, RO_p01_efm200_60.buyer_rev_av, RO_p01_efm200_61.buyer_rev_av, RO_p01_efm200_62.buyer_rev_av, RO_p01_efm200_63.buyer_rev_av,
                          RO_p01_efm200_64.buyer_rev_av, RO_p01_efm200_65.buyer_rev_av, RO_p01_efm200_66.buyer_rev_av, RO_p01_efm200_67.buyer_rev_av, RO_p01_efm200_68.buyer_rev_av,
                          RO_p01_efm200_69.buyer_rev_av, RO_p01_efm200_70.buyer_rev_av, RO_p01_efm200_71.buyer_rev_av, RO_p01_efm200_72.buyer_rev_av, RO_p01_efm200_73.buyer_rev_av,
                          RO_p01_efm200_74.buyer_rev_av, RO_p01_efm200_75.buyer_rev_av, RO_p01_efm200_76.buyer_rev_av, RO_p01_efm200_77.buyer_rev_av, RO_p01_efm200_78.buyer_rev_av,
                          RO_p01_efm200_79.buyer_rev_av, RO_p01_efm200_80.buyer_rev_av, RO_p01_efm200_81.buyer_rev_av, RO_p01_efm200_82.buyer_rev_av, RO_p01_efm200_83.buyer_rev_av,
                          RO_p01_efm200_84.buyer_rev_av, RO_p01_efm200_85.buyer_rev_av, RO_p01_efm200_86.buyer_rev_av, RO_p01_efm200_87.buyer_rev_av, RO_p01_efm200_88.buyer_rev_av,
                          RO_p01_efm200_89.buyer_rev_av, RO_p01_efm200_90.buyer_rev_av, RO_p01_efm200_91.buyer_rev_av, RO_p01_efm200_92.buyer_rev_av, RO_p01_efm200_93.buyer_rev_av,
                          RO_p01_efm200_94.buyer_rev_av, RO_p01_efm200_95.buyer_rev_av, RO_p01_efm200_96.buyer_rev_av, RO_p01_efm200_97.buyer_rev_av, RO_p01_efm200_98.buyer_rev_av,
                          RO_p01_efm200_99.buyer_rev_av)


buyer_rev_av_RO_p01_efm200_mean = [np.mean(i) for i in buyer_rev_av_RO_p01_efm200]
buyer_rev_av_RO_p01_efm200_lower = [np.percentile(i, 10) for i in buyer_rev_av_RO_p01_efm200]
buyer_rev_av_RO_p01_efm200_upper = [np.percentile(i, 90) for i in buyer_rev_av_RO_p01_efm200]

print('Creating prov_rev_av_RO_p01_ef0')
prov_rev_av_RO_p01_ef0 = zip(RO_p01_ef0_00.prov_rev_av, RO_p01_ef0_01.prov_rev_av, RO_p01_ef0_02.prov_rev_av, RO_p01_ef0_03.prov_rev_av, RO_p01_ef0_04.prov_rev_av,
                          RO_p01_ef0_05.prov_rev_av, RO_p01_ef0_06.prov_rev_av, RO_p01_ef0_07.prov_rev_av, RO_p01_ef0_08.prov_rev_av, RO_p01_ef0_09.prov_rev_av,
                          RO_p01_ef0_10.prov_rev_av, RO_p01_ef0_11.prov_rev_av, RO_p01_ef0_12.prov_rev_av, RO_p01_ef0_13.prov_rev_av, RO_p01_ef0_14.prov_rev_av,
                          RO_p01_ef0_15.prov_rev_av, RO_p01_ef0_16.prov_rev_av, RO_p01_ef0_17.prov_rev_av, RO_p01_ef0_18.prov_rev_av, RO_p01_ef0_19.prov_rev_av,
                          RO_p01_ef0_20.prov_rev_av, RO_p01_ef0_21.prov_rev_av, RO_p01_ef0_22.prov_rev_av, RO_p01_ef0_23.prov_rev_av, RO_p01_ef0_24.prov_rev_av,
                          RO_p01_ef0_25.prov_rev_av, RO_p01_ef0_26.prov_rev_av, RO_p01_ef0_27.prov_rev_av, RO_p01_ef0_28.prov_rev_av, RO_p01_ef0_29.prov_rev_av,
                          RO_p01_ef0_30.prov_rev_av, RO_p01_ef0_31.prov_rev_av, RO_p01_ef0_32.prov_rev_av, RO_p01_ef0_33.prov_rev_av, RO_p01_ef0_34.prov_rev_av,
                          RO_p01_ef0_35.prov_rev_av, RO_p01_ef0_36.prov_rev_av, RO_p01_ef0_37.prov_rev_av, RO_p01_ef0_38.prov_rev_av, RO_p01_ef0_39.prov_rev_av,
                          RO_p01_ef0_40.prov_rev_av, RO_p01_ef0_40.prov_rev_av, RO_p01_ef0_41.prov_rev_av, RO_p01_ef0_42.prov_rev_av, RO_p01_ef0_43.prov_rev_av,
                          RO_p01_ef0_44.prov_rev_av, RO_p01_ef0_45.prov_rev_av, RO_p01_ef0_46.prov_rev_av, RO_p01_ef0_47.prov_rev_av, RO_p01_ef0_48.prov_rev_av,
                          RO_p01_ef0_49.prov_rev_av, RO_p01_ef0_50.prov_rev_av, RO_p01_ef0_51.prov_rev_av, RO_p01_ef0_52.prov_rev_av, RO_p01_ef0_53.prov_rev_av,
                          RO_p01_ef0_54.prov_rev_av, RO_p01_ef0_55.prov_rev_av, RO_p01_ef0_56.prov_rev_av, RO_p01_ef0_57.prov_rev_av, RO_p01_ef0_58.prov_rev_av,
                          RO_p01_ef0_59.prov_rev_av, RO_p01_ef0_60.prov_rev_av, RO_p01_ef0_61.prov_rev_av, RO_p01_ef0_62.prov_rev_av, RO_p01_ef0_63.prov_rev_av,
                          RO_p01_ef0_64.prov_rev_av, RO_p01_ef0_65.prov_rev_av, RO_p01_ef0_66.prov_rev_av, RO_p01_ef0_67.prov_rev_av, RO_p01_ef0_68.prov_rev_av,
                          RO_p01_ef0_69.prov_rev_av, RO_p01_ef0_70.prov_rev_av, RO_p01_ef0_71.prov_rev_av, RO_p01_ef0_72.prov_rev_av, RO_p01_ef0_73.prov_rev_av,
                          RO_p01_ef0_74.prov_rev_av, RO_p01_ef0_75.prov_rev_av, RO_p01_ef0_76.prov_rev_av, RO_p01_ef0_77.prov_rev_av, RO_p01_ef0_78.prov_rev_av,
                          RO_p01_ef0_79.prov_rev_av, RO_p01_ef0_80.prov_rev_av, RO_p01_ef0_81.prov_rev_av, RO_p01_ef0_82.prov_rev_av, RO_p01_ef0_83.prov_rev_av,
                          RO_p01_ef0_84.prov_rev_av, RO_p01_ef0_85.prov_rev_av, RO_p01_ef0_86.prov_rev_av, RO_p01_ef0_87.prov_rev_av, RO_p01_ef0_88.prov_rev_av,
                          RO_p01_ef0_89.prov_rev_av, RO_p01_ef0_90.prov_rev_av, RO_p01_ef0_91.prov_rev_av, RO_p01_ef0_92.prov_rev_av, RO_p01_ef0_93.prov_rev_av,
                          RO_p01_ef0_94.prov_rev_av, RO_p01_ef0_95.prov_rev_av, RO_p01_ef0_96.prov_rev_av, RO_p01_ef0_97.prov_rev_av, RO_p01_ef0_98.prov_rev_av,
                          RO_p01_ef0_99.prov_rev_av)


prov_rev_av_RO_p01_ef0_mean = [np.mean(i) for i in prov_rev_av_RO_p01_ef0]
prov_rev_av_RO_p01_ef0_lower = [np.percentile(i, 10) for i in prov_rev_av_RO_p01_ef0]
prov_rev_av_RO_p01_ef0_upper = [np.percentile(i, 90) for i in prov_rev_av_RO_p01_ef0]

print('Creating trans_fee_b_av_RO_p01_ef0')
trans_fee_b_av_RO_p01_ef0 = zip(RO_p01_ef0_00.trans_fee_b_av, RO_p01_ef0_01.trans_fee_b_av, RO_p01_ef0_02.trans_fee_b_av, RO_p01_ef0_03.trans_fee_b_av, RO_p01_ef0_04.trans_fee_b_av, 
                          RO_p01_ef0_05.trans_fee_b_av, RO_p01_ef0_06.trans_fee_b_av, RO_p01_ef0_07.trans_fee_b_av, RO_p01_ef0_08.trans_fee_b_av, RO_p01_ef0_09.trans_fee_b_av, 
                          RO_p01_ef0_10.trans_fee_b_av, RO_p01_ef0_11.trans_fee_b_av, RO_p01_ef0_12.trans_fee_b_av, RO_p01_ef0_13.trans_fee_b_av, RO_p01_ef0_14.trans_fee_b_av, 
                          RO_p01_ef0_15.trans_fee_b_av, RO_p01_ef0_16.trans_fee_b_av, RO_p01_ef0_17.trans_fee_b_av, RO_p01_ef0_18.trans_fee_b_av, RO_p01_ef0_19.trans_fee_b_av, 
                          RO_p01_ef0_20.trans_fee_b_av, RO_p01_ef0_21.trans_fee_b_av, RO_p01_ef0_22.trans_fee_b_av, RO_p01_ef0_23.trans_fee_b_av, RO_p01_ef0_24.trans_fee_b_av, 
                          RO_p01_ef0_25.trans_fee_b_av, RO_p01_ef0_26.trans_fee_b_av, RO_p01_ef0_27.trans_fee_b_av, RO_p01_ef0_28.trans_fee_b_av, RO_p01_ef0_29.trans_fee_b_av, 
                          RO_p01_ef0_30.trans_fee_b_av, RO_p01_ef0_31.trans_fee_b_av, RO_p01_ef0_32.trans_fee_b_av, RO_p01_ef0_33.trans_fee_b_av, RO_p01_ef0_34.trans_fee_b_av, 
                          RO_p01_ef0_35.trans_fee_b_av, RO_p01_ef0_36.trans_fee_b_av, RO_p01_ef0_37.trans_fee_b_av, RO_p01_ef0_38.trans_fee_b_av, RO_p01_ef0_39.trans_fee_b_av, 
                          RO_p01_ef0_40.trans_fee_b_av, RO_p01_ef0_40.trans_fee_b_av, RO_p01_ef0_41.trans_fee_b_av, RO_p01_ef0_42.trans_fee_b_av, RO_p01_ef0_43.trans_fee_b_av, 
                          RO_p01_ef0_44.trans_fee_b_av, RO_p01_ef0_45.trans_fee_b_av, RO_p01_ef0_46.trans_fee_b_av, RO_p01_ef0_47.trans_fee_b_av, RO_p01_ef0_48.trans_fee_b_av, 
                          RO_p01_ef0_49.trans_fee_b_av, RO_p01_ef0_50.trans_fee_b_av, RO_p01_ef0_51.trans_fee_b_av, RO_p01_ef0_52.trans_fee_b_av, RO_p01_ef0_53.trans_fee_b_av, 
                          RO_p01_ef0_54.trans_fee_b_av, RO_p01_ef0_55.trans_fee_b_av, RO_p01_ef0_56.trans_fee_b_av, RO_p01_ef0_57.trans_fee_b_av, RO_p01_ef0_58.trans_fee_b_av, 
                          RO_p01_ef0_59.trans_fee_b_av, RO_p01_ef0_60.trans_fee_b_av, RO_p01_ef0_61.trans_fee_b_av, RO_p01_ef0_62.trans_fee_b_av, RO_p01_ef0_63.trans_fee_b_av, 
                          RO_p01_ef0_64.trans_fee_b_av, RO_p01_ef0_65.trans_fee_b_av, RO_p01_ef0_66.trans_fee_b_av, RO_p01_ef0_67.trans_fee_b_av, RO_p01_ef0_68.trans_fee_b_av, 
                          RO_p01_ef0_69.trans_fee_b_av, RO_p01_ef0_70.trans_fee_b_av, RO_p01_ef0_71.trans_fee_b_av, RO_p01_ef0_72.trans_fee_b_av, RO_p01_ef0_73.trans_fee_b_av, 
                          RO_p01_ef0_74.trans_fee_b_av, RO_p01_ef0_75.trans_fee_b_av, RO_p01_ef0_76.trans_fee_b_av, RO_p01_ef0_77.trans_fee_b_av, RO_p01_ef0_78.trans_fee_b_av, 
                          RO_p01_ef0_79.trans_fee_b_av, RO_p01_ef0_80.trans_fee_b_av, RO_p01_ef0_81.trans_fee_b_av, RO_p01_ef0_82.trans_fee_b_av, RO_p01_ef0_83.trans_fee_b_av, 
                          RO_p01_ef0_84.trans_fee_b_av, RO_p01_ef0_85.trans_fee_b_av, RO_p01_ef0_86.trans_fee_b_av, RO_p01_ef0_87.trans_fee_b_av, RO_p01_ef0_88.trans_fee_b_av, 
                          RO_p01_ef0_89.trans_fee_b_av, RO_p01_ef0_90.trans_fee_b_av, RO_p01_ef0_91.trans_fee_b_av, RO_p01_ef0_92.trans_fee_b_av, RO_p01_ef0_93.trans_fee_b_av, 
                          RO_p01_ef0_94.trans_fee_b_av, RO_p01_ef0_95.trans_fee_b_av, RO_p01_ef0_96.trans_fee_b_av, RO_p01_ef0_97.trans_fee_b_av, RO_p01_ef0_98.trans_fee_b_av, 
                          RO_p01_ef0_99.trans_fee_b_av)


trans_fee_b_av_RO_p01_ef0_mean = [np.mean(i) for i in trans_fee_b_av_RO_p01_ef0]
trans_fee_b_av_RO_p01_ef0_lower = [np.percentile(i, 10) for i in trans_fee_b_av_RO_p01_ef0]
trans_fee_b_av_RO_p01_ef0_upper = [np.percentile(i, 90) for i in trans_fee_b_av_RO_p01_ef0]

print('Creating seller_rev_av_RO_p01_efm200')
seller_rev_av_RO_p01_efm200 = zip(RO_p01_efm200_00.seller_rev_av, RO_p01_efm200_01.seller_rev_av, RO_p01_efm200_02.seller_rev_av, RO_p01_efm200_03.seller_rev_av, RO_p01_efm200_04.seller_rev_av,
                          RO_p01_efm200_05.seller_rev_av, RO_p01_efm200_06.seller_rev_av, RO_p01_efm200_07.seller_rev_av, RO_p01_efm200_08.seller_rev_av, RO_p01_efm200_09.seller_rev_av,
                          RO_p01_efm200_10.seller_rev_av, RO_p01_efm200_11.seller_rev_av, RO_p01_efm200_12.seller_rev_av, RO_p01_efm200_13.seller_rev_av, RO_p01_efm200_14.seller_rev_av,
                          RO_p01_efm200_15.seller_rev_av, RO_p01_efm200_16.seller_rev_av, RO_p01_efm200_17.seller_rev_av, RO_p01_efm200_18.seller_rev_av, RO_p01_efm200_19.seller_rev_av,
                          RO_p01_efm200_20.seller_rev_av, RO_p01_efm200_21.seller_rev_av, RO_p01_efm200_22.seller_rev_av, RO_p01_efm200_23.seller_rev_av, RO_p01_efm200_24.seller_rev_av,
                          RO_p01_efm200_25.seller_rev_av, RO_p01_efm200_26.seller_rev_av, RO_p01_efm200_27.seller_rev_av, RO_p01_efm200_28.seller_rev_av, RO_p01_efm200_29.seller_rev_av,
                          RO_p01_efm200_30.seller_rev_av, RO_p01_efm200_31.seller_rev_av, RO_p01_efm200_32.seller_rev_av, RO_p01_efm200_33.seller_rev_av, RO_p01_efm200_34.seller_rev_av,
                          RO_p01_efm200_35.seller_rev_av, RO_p01_efm200_36.seller_rev_av, RO_p01_efm200_37.seller_rev_av, RO_p01_efm200_38.seller_rev_av, RO_p01_efm200_39.seller_rev_av,
                          RO_p01_efm200_40.seller_rev_av, RO_p01_efm200_40.seller_rev_av, RO_p01_efm200_41.seller_rev_av, RO_p01_efm200_42.seller_rev_av, RO_p01_efm200_43.seller_rev_av,
                          RO_p01_efm200_44.seller_rev_av, RO_p01_efm200_45.seller_rev_av, RO_p01_efm200_46.seller_rev_av, RO_p01_efm200_47.seller_rev_av, RO_p01_efm200_48.seller_rev_av,
                          RO_p01_efm200_49.seller_rev_av, RO_p01_efm200_50.seller_rev_av, RO_p01_efm200_51.seller_rev_av, RO_p01_efm200_52.seller_rev_av, RO_p01_efm200_53.seller_rev_av,
                          RO_p01_efm200_54.seller_rev_av, RO_p01_efm200_55.seller_rev_av, RO_p01_efm200_56.seller_rev_av, RO_p01_efm200_57.seller_rev_av, RO_p01_efm200_58.seller_rev_av,
                          RO_p01_efm200_59.seller_rev_av, RO_p01_efm200_60.seller_rev_av, RO_p01_efm200_61.seller_rev_av, RO_p01_efm200_62.seller_rev_av, RO_p01_efm200_63.seller_rev_av,
                          RO_p01_efm200_64.seller_rev_av, RO_p01_efm200_65.seller_rev_av, RO_p01_efm200_66.seller_rev_av, RO_p01_efm200_67.seller_rev_av, RO_p01_efm200_68.seller_rev_av,
                          RO_p01_efm200_69.seller_rev_av, RO_p01_efm200_70.seller_rev_av, RO_p01_efm200_71.seller_rev_av, RO_p01_efm200_72.seller_rev_av, RO_p01_efm200_73.seller_rev_av,
                          RO_p01_efm200_74.seller_rev_av, RO_p01_efm200_75.seller_rev_av, RO_p01_efm200_76.seller_rev_av, RO_p01_efm200_77.seller_rev_av, RO_p01_efm200_78.seller_rev_av,
                          RO_p01_efm200_79.seller_rev_av, RO_p01_efm200_80.seller_rev_av, RO_p01_efm200_81.seller_rev_av, RO_p01_efm200_82.seller_rev_av, RO_p01_efm200_83.seller_rev_av,
                          RO_p01_efm200_84.seller_rev_av, RO_p01_efm200_85.seller_rev_av, RO_p01_efm200_86.seller_rev_av, RO_p01_efm200_87.seller_rev_av, RO_p01_efm200_88.seller_rev_av,
                          RO_p01_efm200_89.seller_rev_av, RO_p01_efm200_90.seller_rev_av, RO_p01_efm200_91.seller_rev_av, RO_p01_efm200_92.seller_rev_av, RO_p01_efm200_93.seller_rev_av,
                          RO_p01_efm200_94.seller_rev_av, RO_p01_efm200_95.seller_rev_av, RO_p01_efm200_96.seller_rev_av, RO_p01_efm200_97.seller_rev_av, RO_p01_efm200_98.seller_rev_av,
                          RO_p01_efm200_99.seller_rev_av)


seller_rev_av_RO_p01_efm200_mean = [np.mean(i) for i in seller_rev_av_RO_p01_efm200]
seller_rev_av_RO_p01_efm200_lower = [np.percentile(i, 10) for i in seller_rev_av_RO_p01_efm200]
seller_rev_av_RO_p01_efm200_upper = [np.percentile(i, 90) for i in seller_rev_av_RO_p01_efm200]

print('Creating trans_fee_b_av_RO_p01_efm200')
trans_fee_b_av_RO_p01_efm200 = zip(RO_p01_efm200_00.trans_fee_b_av, RO_p01_efm200_01.trans_fee_b_av, RO_p01_efm200_02.trans_fee_b_av, RO_p01_efm200_03.trans_fee_b_av, RO_p01_efm200_04.trans_fee_b_av, 
                          RO_p01_efm200_05.trans_fee_b_av, RO_p01_efm200_06.trans_fee_b_av, RO_p01_efm200_07.trans_fee_b_av, RO_p01_efm200_08.trans_fee_b_av, RO_p01_efm200_09.trans_fee_b_av, 
                          RO_p01_efm200_10.trans_fee_b_av, RO_p01_efm200_11.trans_fee_b_av, RO_p01_efm200_12.trans_fee_b_av, RO_p01_efm200_13.trans_fee_b_av, RO_p01_efm200_14.trans_fee_b_av, 
                          RO_p01_efm200_15.trans_fee_b_av, RO_p01_efm200_16.trans_fee_b_av, RO_p01_efm200_17.trans_fee_b_av, RO_p01_efm200_18.trans_fee_b_av, RO_p01_efm200_19.trans_fee_b_av, 
                          RO_p01_efm200_20.trans_fee_b_av, RO_p01_efm200_21.trans_fee_b_av, RO_p01_efm200_22.trans_fee_b_av, RO_p01_efm200_23.trans_fee_b_av, RO_p01_efm200_24.trans_fee_b_av, 
                          RO_p01_efm200_25.trans_fee_b_av, RO_p01_efm200_26.trans_fee_b_av, RO_p01_efm200_27.trans_fee_b_av, RO_p01_efm200_28.trans_fee_b_av, RO_p01_efm200_29.trans_fee_b_av, 
                          RO_p01_efm200_30.trans_fee_b_av, RO_p01_efm200_31.trans_fee_b_av, RO_p01_efm200_32.trans_fee_b_av, RO_p01_efm200_33.trans_fee_b_av, RO_p01_efm200_34.trans_fee_b_av, 
                          RO_p01_efm200_35.trans_fee_b_av, RO_p01_efm200_36.trans_fee_b_av, RO_p01_efm200_37.trans_fee_b_av, RO_p01_efm200_38.trans_fee_b_av, RO_p01_efm200_39.trans_fee_b_av, 
                          RO_p01_efm200_40.trans_fee_b_av, RO_p01_efm200_40.trans_fee_b_av, RO_p01_efm200_41.trans_fee_b_av, RO_p01_efm200_42.trans_fee_b_av, RO_p01_efm200_43.trans_fee_b_av, 
                          RO_p01_efm200_44.trans_fee_b_av, RO_p01_efm200_45.trans_fee_b_av, RO_p01_efm200_46.trans_fee_b_av, RO_p01_efm200_47.trans_fee_b_av, RO_p01_efm200_48.trans_fee_b_av, 
                          RO_p01_efm200_49.trans_fee_b_av, RO_p01_efm200_50.trans_fee_b_av, RO_p01_efm200_51.trans_fee_b_av, RO_p01_efm200_52.trans_fee_b_av, RO_p01_efm200_53.trans_fee_b_av, 
                          RO_p01_efm200_54.trans_fee_b_av, RO_p01_efm200_55.trans_fee_b_av, RO_p01_efm200_56.trans_fee_b_av, RO_p01_efm200_57.trans_fee_b_av, RO_p01_efm200_58.trans_fee_b_av, 
                          RO_p01_efm200_59.trans_fee_b_av, RO_p01_efm200_60.trans_fee_b_av, RO_p01_efm200_61.trans_fee_b_av, RO_p01_efm200_62.trans_fee_b_av, RO_p01_efm200_63.trans_fee_b_av, 
                          RO_p01_efm200_64.trans_fee_b_av, RO_p01_efm200_65.trans_fee_b_av, RO_p01_efm200_66.trans_fee_b_av, RO_p01_efm200_67.trans_fee_b_av, RO_p01_efm200_68.trans_fee_b_av, 
                          RO_p01_efm200_69.trans_fee_b_av, RO_p01_efm200_70.trans_fee_b_av, RO_p01_efm200_71.trans_fee_b_av, RO_p01_efm200_72.trans_fee_b_av, RO_p01_efm200_73.trans_fee_b_av, 
                          RO_p01_efm200_74.trans_fee_b_av, RO_p01_efm200_75.trans_fee_b_av, RO_p01_efm200_76.trans_fee_b_av, RO_p01_efm200_77.trans_fee_b_av, RO_p01_efm200_78.trans_fee_b_av, 
                          RO_p01_efm200_79.trans_fee_b_av, RO_p01_efm200_80.trans_fee_b_av, RO_p01_efm200_81.trans_fee_b_av, RO_p01_efm200_82.trans_fee_b_av, RO_p01_efm200_83.trans_fee_b_av, 
                          RO_p01_efm200_84.trans_fee_b_av, RO_p01_efm200_85.trans_fee_b_av, RO_p01_efm200_86.trans_fee_b_av, RO_p01_efm200_87.trans_fee_b_av, RO_p01_efm200_88.trans_fee_b_av, 
                          RO_p01_efm200_89.trans_fee_b_av, RO_p01_efm200_90.trans_fee_b_av, RO_p01_efm200_91.trans_fee_b_av, RO_p01_efm200_92.trans_fee_b_av, RO_p01_efm200_93.trans_fee_b_av, 
                          RO_p01_efm200_94.trans_fee_b_av, RO_p01_efm200_95.trans_fee_b_av, RO_p01_efm200_96.trans_fee_b_av, RO_p01_efm200_97.trans_fee_b_av, RO_p01_efm200_98.trans_fee_b_av, 
                          RO_p01_efm200_99.trans_fee_b_av)


trans_fee_b_av_RO_p01_efm200_mean = [np.mean(i) for i in trans_fee_b_av_RO_p01_efm200]
trans_fee_b_av_RO_p01_efm200_lower = [np.percentile(i, 10) for i in trans_fee_b_av_RO_p01_efm200]
trans_fee_b_av_RO_p01_efm200_upper = [np.percentile(i, 90) for i in trans_fee_b_av_RO_p01_efm200]

print('Creating trans_fee_s_av_RO_p01_ef0')
trans_fee_s_av_RO_p01_ef0 = zip(RO_p01_ef0_00.trans_fee_s_av, RO_p01_ef0_01.trans_fee_s_av, RO_p01_ef0_02.trans_fee_s_av, RO_p01_ef0_03.trans_fee_s_av, RO_p01_ef0_04.trans_fee_s_av, 
                          RO_p01_ef0_05.trans_fee_s_av, RO_p01_ef0_06.trans_fee_s_av, RO_p01_ef0_07.trans_fee_s_av, RO_p01_ef0_08.trans_fee_s_av, RO_p01_ef0_09.trans_fee_s_av, 
                          RO_p01_ef0_10.trans_fee_s_av, RO_p01_ef0_11.trans_fee_s_av, RO_p01_ef0_12.trans_fee_s_av, RO_p01_ef0_13.trans_fee_s_av, RO_p01_ef0_14.trans_fee_s_av, 
                          RO_p01_ef0_15.trans_fee_s_av, RO_p01_ef0_16.trans_fee_s_av, RO_p01_ef0_17.trans_fee_s_av, RO_p01_ef0_18.trans_fee_s_av, RO_p01_ef0_19.trans_fee_s_av, 
                          RO_p01_ef0_20.trans_fee_s_av, RO_p01_ef0_21.trans_fee_s_av, RO_p01_ef0_22.trans_fee_s_av, RO_p01_ef0_23.trans_fee_s_av, RO_p01_ef0_24.trans_fee_s_av, 
                          RO_p01_ef0_25.trans_fee_s_av, RO_p01_ef0_26.trans_fee_s_av, RO_p01_ef0_27.trans_fee_s_av, RO_p01_ef0_28.trans_fee_s_av, RO_p01_ef0_29.trans_fee_s_av, 
                          RO_p01_ef0_30.trans_fee_s_av, RO_p01_ef0_31.trans_fee_s_av, RO_p01_ef0_32.trans_fee_s_av, RO_p01_ef0_33.trans_fee_s_av, RO_p01_ef0_34.trans_fee_s_av, 
                          RO_p01_ef0_35.trans_fee_s_av, RO_p01_ef0_36.trans_fee_s_av, RO_p01_ef0_37.trans_fee_s_av, RO_p01_ef0_38.trans_fee_s_av, RO_p01_ef0_39.trans_fee_s_av, 
                          RO_p01_ef0_40.trans_fee_s_av, RO_p01_ef0_40.trans_fee_s_av, RO_p01_ef0_41.trans_fee_s_av, RO_p01_ef0_42.trans_fee_s_av, RO_p01_ef0_43.trans_fee_s_av, 
                          RO_p01_ef0_44.trans_fee_s_av, RO_p01_ef0_45.trans_fee_s_av, RO_p01_ef0_46.trans_fee_s_av, RO_p01_ef0_47.trans_fee_s_av, RO_p01_ef0_48.trans_fee_s_av, 
                          RO_p01_ef0_49.trans_fee_s_av, RO_p01_ef0_50.trans_fee_s_av, RO_p01_ef0_51.trans_fee_s_av, RO_p01_ef0_52.trans_fee_s_av, RO_p01_ef0_53.trans_fee_s_av, 
                          RO_p01_ef0_54.trans_fee_s_av, RO_p01_ef0_55.trans_fee_s_av, RO_p01_ef0_56.trans_fee_s_av, RO_p01_ef0_57.trans_fee_s_av, RO_p01_ef0_58.trans_fee_s_av, 
                          RO_p01_ef0_59.trans_fee_s_av, RO_p01_ef0_60.trans_fee_s_av, RO_p01_ef0_61.trans_fee_s_av, RO_p01_ef0_62.trans_fee_s_av, RO_p01_ef0_63.trans_fee_s_av, 
                          RO_p01_ef0_64.trans_fee_s_av, RO_p01_ef0_65.trans_fee_s_av, RO_p01_ef0_66.trans_fee_s_av, RO_p01_ef0_67.trans_fee_s_av, RO_p01_ef0_68.trans_fee_s_av, 
                          RO_p01_ef0_69.trans_fee_s_av, RO_p01_ef0_70.trans_fee_s_av, RO_p01_ef0_71.trans_fee_s_av, RO_p01_ef0_72.trans_fee_s_av, RO_p01_ef0_73.trans_fee_s_av, 
                          RO_p01_ef0_74.trans_fee_s_av, RO_p01_ef0_75.trans_fee_s_av, RO_p01_ef0_76.trans_fee_s_av, RO_p01_ef0_77.trans_fee_s_av, RO_p01_ef0_78.trans_fee_s_av, 
                          RO_p01_ef0_79.trans_fee_s_av, RO_p01_ef0_80.trans_fee_s_av, RO_p01_ef0_81.trans_fee_s_av, RO_p01_ef0_82.trans_fee_s_av, RO_p01_ef0_83.trans_fee_s_av, 
                          RO_p01_ef0_84.trans_fee_s_av, RO_p01_ef0_85.trans_fee_s_av, RO_p01_ef0_86.trans_fee_s_av, RO_p01_ef0_87.trans_fee_s_av, RO_p01_ef0_88.trans_fee_s_av, 
                          RO_p01_ef0_89.trans_fee_s_av, RO_p01_ef0_90.trans_fee_s_av, RO_p01_ef0_91.trans_fee_s_av, RO_p01_ef0_92.trans_fee_s_av, RO_p01_ef0_93.trans_fee_s_av, 
                          RO_p01_ef0_94.trans_fee_s_av, RO_p01_ef0_95.trans_fee_s_av, RO_p01_ef0_96.trans_fee_s_av, RO_p01_ef0_97.trans_fee_s_av, RO_p01_ef0_98.trans_fee_s_av, 
                          RO_p01_ef0_99.trans_fee_s_av)


trans_fee_s_av_RO_p01_ef0_mean = [np.mean(i) for i in trans_fee_s_av_RO_p01_ef0]
trans_fee_s_av_RO_p01_ef0_lower = [np.percentile(i, 10) for i in trans_fee_s_av_RO_p01_ef0]
trans_fee_s_av_RO_p01_ef0_upper = [np.percentile(i, 90) for i in trans_fee_s_av_RO_p01_ef0]

print('Creating trans_fee_s_av_RO_p01_efm200')
trans_fee_s_av_RO_p01_efm200 = zip(RO_p01_efm200_00.trans_fee_s_av, RO_p01_efm200_01.trans_fee_s_av, RO_p01_efm200_02.trans_fee_s_av, RO_p01_efm200_03.trans_fee_s_av, RO_p01_efm200_04.trans_fee_s_av, 
                          RO_p01_efm200_05.trans_fee_s_av, RO_p01_efm200_06.trans_fee_s_av, RO_p01_efm200_07.trans_fee_s_av, RO_p01_efm200_08.trans_fee_s_av, RO_p01_efm200_09.trans_fee_s_av, 
                          RO_p01_efm200_10.trans_fee_s_av, RO_p01_efm200_11.trans_fee_s_av, RO_p01_efm200_12.trans_fee_s_av, RO_p01_efm200_13.trans_fee_s_av, RO_p01_efm200_14.trans_fee_s_av, 
                          RO_p01_efm200_15.trans_fee_s_av, RO_p01_efm200_16.trans_fee_s_av, RO_p01_efm200_17.trans_fee_s_av, RO_p01_efm200_18.trans_fee_s_av, RO_p01_efm200_19.trans_fee_s_av, 
                          RO_p01_efm200_20.trans_fee_s_av, RO_p01_efm200_21.trans_fee_s_av, RO_p01_efm200_22.trans_fee_s_av, RO_p01_efm200_23.trans_fee_s_av, RO_p01_efm200_24.trans_fee_s_av, 
                          RO_p01_efm200_25.trans_fee_s_av, RO_p01_efm200_26.trans_fee_s_av, RO_p01_efm200_27.trans_fee_s_av, RO_p01_efm200_28.trans_fee_s_av, RO_p01_efm200_29.trans_fee_s_av, 
                          RO_p01_efm200_30.trans_fee_s_av, RO_p01_efm200_31.trans_fee_s_av, RO_p01_efm200_32.trans_fee_s_av, RO_p01_efm200_33.trans_fee_s_av, RO_p01_efm200_34.trans_fee_s_av, 
                          RO_p01_efm200_35.trans_fee_s_av, RO_p01_efm200_36.trans_fee_s_av, RO_p01_efm200_37.trans_fee_s_av, RO_p01_efm200_38.trans_fee_s_av, RO_p01_efm200_39.trans_fee_s_av, 
                          RO_p01_efm200_40.trans_fee_s_av, RO_p01_efm200_40.trans_fee_s_av, RO_p01_efm200_41.trans_fee_s_av, RO_p01_efm200_42.trans_fee_s_av, RO_p01_efm200_43.trans_fee_s_av, 
                          RO_p01_efm200_44.trans_fee_s_av, RO_p01_efm200_45.trans_fee_s_av, RO_p01_efm200_46.trans_fee_s_av, RO_p01_efm200_47.trans_fee_s_av, RO_p01_efm200_48.trans_fee_s_av, 
                          RO_p01_efm200_49.trans_fee_s_av, RO_p01_efm200_50.trans_fee_s_av, RO_p01_efm200_51.trans_fee_s_av, RO_p01_efm200_52.trans_fee_s_av, RO_p01_efm200_53.trans_fee_s_av, 
                          RO_p01_efm200_54.trans_fee_s_av, RO_p01_efm200_55.trans_fee_s_av, RO_p01_efm200_56.trans_fee_s_av, RO_p01_efm200_57.trans_fee_s_av, RO_p01_efm200_58.trans_fee_s_av, 
                          RO_p01_efm200_59.trans_fee_s_av, RO_p01_efm200_60.trans_fee_s_av, RO_p01_efm200_61.trans_fee_s_av, RO_p01_efm200_62.trans_fee_s_av, RO_p01_efm200_63.trans_fee_s_av, 
                          RO_p01_efm200_64.trans_fee_s_av, RO_p01_efm200_65.trans_fee_s_av, RO_p01_efm200_66.trans_fee_s_av, RO_p01_efm200_67.trans_fee_s_av, RO_p01_efm200_68.trans_fee_s_av, 
                          RO_p01_efm200_69.trans_fee_s_av, RO_p01_efm200_70.trans_fee_s_av, RO_p01_efm200_71.trans_fee_s_av, RO_p01_efm200_72.trans_fee_s_av, RO_p01_efm200_73.trans_fee_s_av, 
                          RO_p01_efm200_74.trans_fee_s_av, RO_p01_efm200_75.trans_fee_s_av, RO_p01_efm200_76.trans_fee_s_av, RO_p01_efm200_77.trans_fee_s_av, RO_p01_efm200_78.trans_fee_s_av, 
                          RO_p01_efm200_79.trans_fee_s_av, RO_p01_efm200_80.trans_fee_s_av, RO_p01_efm200_81.trans_fee_s_av, RO_p01_efm200_82.trans_fee_s_av, RO_p01_efm200_83.trans_fee_s_av, 
                          RO_p01_efm200_84.trans_fee_s_av, RO_p01_efm200_85.trans_fee_s_av, RO_p01_efm200_86.trans_fee_s_av, RO_p01_efm200_87.trans_fee_s_av, RO_p01_efm200_88.trans_fee_s_av, 
                          RO_p01_efm200_89.trans_fee_s_av, RO_p01_efm200_90.trans_fee_s_av, RO_p01_efm200_91.trans_fee_s_av, RO_p01_efm200_92.trans_fee_s_av, RO_p01_efm200_93.trans_fee_s_av, 
                          RO_p01_efm200_94.trans_fee_s_av, RO_p01_efm200_95.trans_fee_s_av, RO_p01_efm200_96.trans_fee_s_av, RO_p01_efm200_97.trans_fee_s_av, RO_p01_efm200_98.trans_fee_s_av, 
                          RO_p01_efm200_99.trans_fee_s_av)


trans_fee_s_av_RO_p01_efm200_mean = [np.mean(i) for i in trans_fee_s_av_RO_p01_efm200]
trans_fee_s_av_RO_p01_efm200_lower = [np.percentile(i, 10) for i in trans_fee_s_av_RO_p01_efm200]
trans_fee_s_av_RO_p01_efm200_upper = [np.percentile(i, 90) for i in trans_fee_s_av_RO_p01_efm200]

print('Creating prov_rev_av_RO_p01_efm200')
prov_rev_av_RO_p01_efm200 = zip(RO_p01_efm200_00.prov_rev_av, RO_p01_efm200_01.prov_rev_av, RO_p01_efm200_02.prov_rev_av, RO_p01_efm200_03.prov_rev_av, RO_p01_efm200_04.prov_rev_av,
                          RO_p01_efm200_05.prov_rev_av, RO_p01_efm200_06.prov_rev_av, RO_p01_efm200_07.prov_rev_av, RO_p01_efm200_08.prov_rev_av, RO_p01_efm200_09.prov_rev_av,
                          RO_p01_efm200_10.prov_rev_av, RO_p01_efm200_11.prov_rev_av, RO_p01_efm200_12.prov_rev_av, RO_p01_efm200_13.prov_rev_av, RO_p01_efm200_14.prov_rev_av,
                          RO_p01_efm200_15.prov_rev_av, RO_p01_efm200_16.prov_rev_av, RO_p01_efm200_17.prov_rev_av, RO_p01_efm200_18.prov_rev_av, RO_p01_efm200_19.prov_rev_av,
                          RO_p01_efm200_20.prov_rev_av, RO_p01_efm200_21.prov_rev_av, RO_p01_efm200_22.prov_rev_av, RO_p01_efm200_23.prov_rev_av, RO_p01_efm200_24.prov_rev_av,
                          RO_p01_efm200_25.prov_rev_av, RO_p01_efm200_26.prov_rev_av, RO_p01_efm200_27.prov_rev_av, RO_p01_efm200_28.prov_rev_av, RO_p01_efm200_29.prov_rev_av,
                          RO_p01_efm200_30.prov_rev_av, RO_p01_efm200_31.prov_rev_av, RO_p01_efm200_32.prov_rev_av, RO_p01_efm200_33.prov_rev_av, RO_p01_efm200_34.prov_rev_av,
                          RO_p01_efm200_35.prov_rev_av, RO_p01_efm200_36.prov_rev_av, RO_p01_efm200_37.prov_rev_av, RO_p01_efm200_38.prov_rev_av, RO_p01_efm200_39.prov_rev_av,
                          RO_p01_efm200_40.prov_rev_av, RO_p01_efm200_40.prov_rev_av, RO_p01_efm200_41.prov_rev_av, RO_p01_efm200_42.prov_rev_av, RO_p01_efm200_43.prov_rev_av,
                          RO_p01_efm200_44.prov_rev_av, RO_p01_efm200_45.prov_rev_av, RO_p01_efm200_46.prov_rev_av, RO_p01_efm200_47.prov_rev_av, RO_p01_efm200_48.prov_rev_av,
                          RO_p01_efm200_49.prov_rev_av, RO_p01_efm200_50.prov_rev_av, RO_p01_efm200_51.prov_rev_av, RO_p01_efm200_52.prov_rev_av, RO_p01_efm200_53.prov_rev_av,
                          RO_p01_efm200_54.prov_rev_av, RO_p01_efm200_55.prov_rev_av, RO_p01_efm200_56.prov_rev_av, RO_p01_efm200_57.prov_rev_av, RO_p01_efm200_58.prov_rev_av,
                          RO_p01_efm200_59.prov_rev_av, RO_p01_efm200_60.prov_rev_av, RO_p01_efm200_61.prov_rev_av, RO_p01_efm200_62.prov_rev_av, RO_p01_efm200_63.prov_rev_av,
                          RO_p01_efm200_64.prov_rev_av, RO_p01_efm200_65.prov_rev_av, RO_p01_efm200_66.prov_rev_av, RO_p01_efm200_67.prov_rev_av, RO_p01_efm200_68.prov_rev_av,
                          RO_p01_efm200_69.prov_rev_av, RO_p01_efm200_70.prov_rev_av, RO_p01_efm200_71.prov_rev_av, RO_p01_efm200_72.prov_rev_av, RO_p01_efm200_73.prov_rev_av,
                          RO_p01_efm200_74.prov_rev_av, RO_p01_efm200_75.prov_rev_av, RO_p01_efm200_76.prov_rev_av, RO_p01_efm200_77.prov_rev_av, RO_p01_efm200_78.prov_rev_av,
                          RO_p01_efm200_79.prov_rev_av, RO_p01_efm200_80.prov_rev_av, RO_p01_efm200_81.prov_rev_av, RO_p01_efm200_82.prov_rev_av, RO_p01_efm200_83.prov_rev_av,
                          RO_p01_efm200_84.prov_rev_av, RO_p01_efm200_85.prov_rev_av, RO_p01_efm200_86.prov_rev_av, RO_p01_efm200_87.prov_rev_av, RO_p01_efm200_88.prov_rev_av,
                          RO_p01_efm200_89.prov_rev_av, RO_p01_efm200_90.prov_rev_av, RO_p01_efm200_91.prov_rev_av, RO_p01_efm200_92.prov_rev_av, RO_p01_efm200_93.prov_rev_av,
                          RO_p01_efm200_94.prov_rev_av, RO_p01_efm200_95.prov_rev_av, RO_p01_efm200_96.prov_rev_av, RO_p01_efm200_97.prov_rev_av, RO_p01_efm200_98.prov_rev_av,
                          RO_p01_efm200_99.prov_rev_av)


prov_rev_av_RO_p01_efm200_mean = [np.mean(i) for i in prov_rev_av_RO_p01_efm200]
prov_rev_av_RO_p01_efm200_lower = [np.percentile(i, 10) for i in prov_rev_av_RO_p01_efm200]
prov_rev_av_RO_p01_efm200_upper = [np.percentile(i, 90) for i in prov_rev_av_RO_p01_efm200]

bs_trans_fee_b = [bs_RO_p01_ef0_00125.trans_fee_b_av[1:], bs_RO_p01_ef0_00250.trans_fee_b_av[1:], \
                  bs_RO_p01_ef0_00500.trans_fee_b_av[1:], bs_RO_p01_ef0_01000.trans_fee_b_av[1:], \
                  bs_RO_p01_ef0_02000.trans_fee_b_av[1:], bs_RO_p01_ef0_04000.trans_fee_b_av[1:], \
                  bs_RO_p01_ef0_08000.trans_fee_b_av[1:], bs_RO_p01_ef0_16000.trans_fee_b_av[1:], \
                  bs_RO_p01_ef0_32000.trans_fee_b_av[1:]]

bs_trans_fee_b_mean = [ np.mean(i) for i in bs_trans_fee_b ]
bs_trans_fee_b_lower = [ np.percentile(i, 10) for i in bs_trans_fee_b ]
bs_trans_fee_b_upper = [ np.percentile(i, 90) for i in bs_trans_fee_b ]

bs_trans_fee_s = [bs_RO_p01_ef0_00125.trans_fee_s_av[1:], bs_RO_p01_ef0_00250.trans_fee_s_av[1:], \
                  bs_RO_p01_ef0_00500.trans_fee_s_av[1:], bs_RO_p01_ef0_01000.trans_fee_s_av[1:], \
                  bs_RO_p01_ef0_02000.trans_fee_s_av[1:], bs_RO_p01_ef0_04000.trans_fee_s_av[1:], \
                  bs_RO_p01_ef0_08000.trans_fee_s_av[1:], bs_RO_p01_ef0_16000.trans_fee_s_av[1:], \
                  bs_RO_p01_ef0_32000.trans_fee_s_av[1:]]

bs_trans_fee_s_mean = [ np.mean(i) for i in bs_trans_fee_s ]
bs_trans_fee_s_lower = [ np.percentile(i, 10) for i in bs_trans_fee_s ]
bs_trans_fee_s_upper = [ np.percentile(i, 90) for i in bs_trans_fee_s ]


prov_rev_av_RIL_p10_mean = np.asarray(prov_rev_av_RIL_p10_mean)*10
buyer_rev_av_RIL_p10_mean = np.asarray(buyer_rev_av_RIL_p10_mean)*10000
seller_rev_av_RIL_p10_mean = np.asarray(seller_rev_av_RIL_p10_mean)*2000
prov_rev_av_RILS_p10_mean = np.asarray(prov_rev_av_RILS_p10_mean)*10
buyer_rev_av_RILS_p10_mean = np.asarray(buyer_rev_av_RILS_p10_mean)*10000
seller_rev_av_RILS_p10_mean = np.asarray(seller_rev_av_RILS_p10_mean)*2000


pb_rev_av_RIL_p10_mean = prov_rev_av_RIL_p10_mean + buyer_rev_av_RIL_p10_mean
pbs_rev_av_RIL_p10_mean = pb_rev_av_RIL_p10_mean + seller_rev_av_RIL_p10_mean

pb_rev_av_RILS_p10_mean = prov_rev_av_RILS_p10_mean + buyer_rev_av_RILS_p10_mean
pbs_rev_av_RILS_p10_mean = pb_rev_av_RILS_p10_mean + seller_rev_av_RILS_p10_mean


prov_rev_av_RO_p01_ef0_mean = np.asarray(prov_rev_av_RO_p01_ef0_mean)
buyer_rev_av_RO_p01_ef0_mean = np.asarray(buyer_rev_av_RO_p01_ef0_mean)*10000
seller_rev_av_RO_p01_ef0_mean = np.asarray(seller_rev_av_RO_p01_ef0_mean)*2000
prov_rev_av_RO_p01_efm200_mean = np.asarray(prov_rev_av_RO_p01_efm200_mean)
buyer_rev_av_RO_p01_efm200_mean = np.asarray(buyer_rev_av_RO_p01_efm200_mean)*10000
seller_rev_av_RO_p01_efm200_mean = np.asarray(seller_rev_av_RO_p01_efm200_mean)*2000



pb_rev_av_RO_p01_ef0_mean = prov_rev_av_RO_p01_ef0_mean + buyer_rev_av_RO_p01_ef0_mean
pbs_rev_av_RO_p01_ef0_mean = pb_rev_av_RO_p01_ef0_mean + seller_rev_av_RO_p01_ef0_mean

pb_rev_av_RO_p01_efm200_mean = prov_rev_av_RO_p01_efm200_mean + buyer_rev_av_RO_p01_efm200_mean
pbs_rev_av_RO_p01_efm200_mean = pb_rev_av_RO_p01_efm200_mean + seller_rev_av_RO_p01_efm200_mean


print('Creating variables on welfare distribution...'),

rev_RILS_p10 = zip(prov_rev_av_RILS_p10_mean, buyer_rev_av_RILS_p10_mean, seller_rev_av_RILS_p10_mean)
total_rev_RILS_p10 = [sum(rev_RILS_p10[i]) for i in range(len(rev_RILS_p10))]
share_prov_RILS_p10 = [prov_rev_av_RILS_p10_mean[i]/total_rev_RILS_p10[i] for i in range(len(prov_rev_av_RILS_p10_mean))]
share_seller_RILS_p10 = [seller_rev_av_RILS_p10_mean[i]/total_rev_RILS_p10[i] for i in range(len(seller_rev_av_RILS_p10_mean))]
share_buyer_RILS_p10 = [buyer_rev_av_RILS_p10_mean[i]/total_rev_RILS_p10[i] for i in range(len(buyer_rev_av_RILS_p10_mean))]
share_cust_RILS_p10 = [share_seller_RILS_p10[i] + share_buyer_RILS_p10[i] for i in range(len(share_seller_RILS_p10))]
total_share_RILS_p10 = [share_seller_RILS_p10[i] + share_buyer_RILS_p10[i] + share_prov_RILS_p10[i] for i in range(len(share_seller_RILS_p10))]

assert [idx for idx in range(len(total_share_RILS_p10)) if total_share_RILS_p10[idx] > 1.0001 or total_share_RILS_p10[idx] < 0.9999] == [], 'Problem with total share (RILS_p10).'


rev_RIL_p10 = zip(prov_rev_av_RIL_p10_mean, buyer_rev_av_RIL_p10_mean, seller_rev_av_RIL_p10_mean)
total_rev_RIL_p10 = [sum(rev_RIL_p10[i]) for i in range(len(rev_RIL_p10))]
share_prov_RIL_p10 = [prov_rev_av_RIL_p10_mean[i]/total_rev_RIL_p10[i] for i in range(len(prov_rev_av_RIL_p10_mean))]
share_seller_RIL_p10 = [seller_rev_av_RIL_p10_mean[i]/total_rev_RIL_p10[i] for i in range(len(seller_rev_av_RIL_p10_mean))]
share_buyer_RIL_p10 = [buyer_rev_av_RIL_p10_mean[i]/total_rev_RIL_p10[i] for i in range(len(buyer_rev_av_RIL_p10_mean))]
share_cust_RIL_p10 = [share_seller_RIL_p10[i] + share_buyer_RIL_p10[i] for i in range(len(share_seller_RIL_p10))]
total_share_RIL_p10 = [share_seller_RIL_p10[i] + share_buyer_RIL_p10[i] + share_prov_RIL_p10[i] for i in range(len(share_seller_RIL_p10))]

assert [idx for idx in range(len(total_share_RIL_p10)) if total_share_RIL_p10[idx] > 1.0001 or total_share_RIL_p10[idx] < 0.9999] == [], 'Problem with total share (RIL_p01).'


rev_RO_p01_efm200 = zip(prov_rev_av_RO_p01_efm200_mean, buyer_rev_av_RO_p01_efm200_mean, seller_rev_av_RO_p01_efm200_mean)
total_rev_RO_p01_efm200 = [sum(rev_RO_p01_efm200[i]) for i in range(len(rev_RO_p01_efm200))]
share_prov_RO_p01_efm200 = [prov_rev_av_RO_p01_efm200_mean[i]/total_rev_RO_p01_efm200[i] for i in range(len(prov_rev_av_RO_p01_efm200_mean))]
share_seller_RO_p01_efm200 = [seller_rev_av_RO_p01_efm200_mean[i]/total_rev_RO_p01_efm200[i] for i in range(len(seller_rev_av_RO_p01_efm200_mean))]
share_buyer_RO_p01_efm200 = [buyer_rev_av_RO_p01_efm200_mean[i]/total_rev_RO_p01_efm200[i] for i in range(len(buyer_rev_av_RO_p01_efm200_mean))]
share_cust_RO_p01_efm200 = [share_seller_RO_p01_efm200[i] + share_buyer_RO_p01_efm200[i] for i in range(len(share_seller_RO_p01_efm200))]
total_share_RO_p01_efm200 = [share_seller_RO_p01_efm200[i] + share_buyer_RO_p01_efm200[i] + share_prov_RO_p01_efm200[i] for i in range(len(share_seller_RO_p01_efm200))]

assert [idx for idx in range(len(total_share_RO_p01_efm200)) if total_share_RO_p01_efm200[idx] > 1.0001 or total_share_RO_p01_efm200[idx] < 0.9999] == [], 'Problem with total share (RO_p01_efm200).'

rev_RO_p01_ef0 = zip(prov_rev_av_RO_p01_ef0_mean, buyer_rev_av_RO_p01_ef0_mean, seller_rev_av_RO_p01_ef0_mean)
total_rev_RO_p01_ef0 = [sum(rev_RO_p01_ef0[i]) for i in range(len(rev_RO_p01_ef0))]
share_prov_RO_p01_ef0 = [prov_rev_av_RO_p01_ef0_mean[i]/total_rev_RO_p01_ef0[i] for i in range(len(prov_rev_av_RO_p01_ef0_mean))]
share_seller_RO_p01_ef0 = [seller_rev_av_RO_p01_ef0_mean[i]/total_rev_RO_p01_ef0[i] for i in range(len(seller_rev_av_RO_p01_ef0_mean))]
share_buyer_RO_p01_ef0 = [buyer_rev_av_RO_p01_ef0_mean[i]/total_rev_RO_p01_ef0[i] for i in range(len(buyer_rev_av_RO_p01_ef0_mean))]
share_cust_RO_p01_ef0 = [share_seller_RO_p01_ef0[i] + share_buyer_RO_p01_ef0[i] for i in range(len(share_seller_RO_p01_ef0))]
total_share_RO_p01_ef0 = [share_seller_RO_p01_ef0[i] + share_buyer_RO_p01_ef0[i] + share_prov_RO_p01_ef0[i] for i in range(len(share_seller_RO_p01_ef0))]

assert [idx for idx in range(len(total_share_RO_p01_ef0)) if total_share_RO_p01_ef0[idx] > 1.0001 or total_share_RO_p01_ef0[idx] < 0.9999] == [], 'Problem with total share (RO_p01_ef0).'


print('...finished.')


print('Creating variables completed.')
print('Start plotting...')

print('Folder for saving figures: ', fig_dir)

#
time = range(1, 501)
# Max nb of customers

print('Plot 01/10 - 1/4'),
plt.clf()
ylim_max = max(max(max_prov_customers_RIL_p01_upper, max_prov_customers_RIL_p10_upper, max_prov_customers_RILS_p01_upper, max_prov_customers_RILS_p10_upper)) + 20

viridis_color = "#3a538b"
fig, axes = plt.subplots(2, 2, figsize=(15, 9))
axes[0, 0].plot(time,max_prov_customers_RIL_p01_mean, label='Max nb of customers', color=viridis_color)
axes[0, 0].plot(time,max_prov_customers_RIL_p01_upper, color=viridis_color, alpha=0.25, linestyle="-")
axes[0, 0].plot(time,max_prov_customers_RIL_p01_lower, color=viridis_color, alpha=0.25, linestyle="-")
axes[0, 0].fill_between(time, max_prov_customers_RIL_p01_lower, max_prov_customers_RIL_p01_upper, facecolor=viridis_color, alpha=0.15)
axes[0, 0].axhline(y=1200, color='#989898', linestyle="--")
axes[0, 0].legend(loc='best')
axes[0, 0].set_ylim(0, ylim_max)
axes[0, 0].set_title('Reinf. learning, one provider (no satisficing)')
axes[0, 0].set_xlabel('time')
axes[0, 0].set_xlim(0,500)
axes[0, 0].set_ylabel('Max nb of customers')
print('Plot 01/10 - 2/4'),
axes[1, 0].plot(time, max_prov_customers_RIL_p10_mean, label='Max nb of customers', color=viridis_color)
axes[1, 0].plot(time, max_prov_customers_RIL_p10_upper, color=viridis_color, alpha=0.25, linestyle="-")
axes[1, 0].plot(time, max_prov_customers_RIL_p10_lower, color=viridis_color, alpha=0.25, linestyle="-")
axes[1, 0].fill_between(time, max_prov_customers_RIL_p10_lower, max_prov_customers_RIL_p10_upper, facecolor=viridis_color, alpha=0.15)
axes[1, 0].axhline(y=120, color='#989898', linestyle="--")
axes[1, 0].legend(loc='best')
axes[1, 0].set_title('Reinf. learning, ten providers (no satisficing)')
axes[1, 0].set_xlabel('time')
axes[1, 0].set_xlim(0,500)
axes[1, 0].set_ylabel('Max nb of customers')
axes[1, 0].set_ylim(0, ylim_max)
print('Plot 01/10 - 3/4'),
axes[0, 1].plot(time, max_prov_customers_RILS_p01_mean, label='Max nb of customers', color=viridis_color)
axes[0, 1].plot(time, max_prov_customers_RILS_p01_upper, color=viridis_color, alpha=0.25, linestyle="-")
axes[0, 1].plot(time, max_prov_customers_RILS_p01_lower, color=viridis_color, alpha=0.25, linestyle="-")
axes[0, 1].fill_between(time, max_prov_customers_RILS_p01_lower, max_prov_customers_RILS_p01_upper, facecolor=viridis_color, alpha=0.15)
axes[0, 1].axhline(y=1200, color='#989898', linestyle="--")
axes[0, 1].legend(loc='best')
axes[0, 1].set_title('Reinf. learning, one provider (with satisficing)')
axes[0, 1].set_xlabel('time')
axes[0, 1].set_xlim(0,500)
axes[0, 1].set_ylabel('Max nb of customers')
axes[0, 1].set_ylim(0, ylim_max)
print('Plot 01/10 - 4/4'),
axes[1, 1].plot(time, max_prov_customers_RILS_p10_mean, label='Max nb of customers', color=viridis_color)
axes[1, 1].plot(time, max_prov_customers_RILS_p10_upper, color=viridis_color, alpha=0.25, linestyle="-")
axes[1, 1].plot(time, max_prov_customers_RILS_p10_lower, color=viridis_color, alpha=0.25, linestyle="-")
axes[1, 1].fill_between(time, max_prov_customers_RILS_p10_lower, max_prov_customers_RILS_p10_upper, facecolor=viridis_color, alpha=0.15)
axes[1, 1].axhline(y=120, color='#989898', linestyle="--")
axes[1, 1].legend(loc='best')
axes[1, 1].set_title('Reinf. learning, ten providers (with satisficing)')
axes[1, 1].set_xlabel('time')
axes[1, 1].set_xlim(0,500)
axes[1, 1].set_ylabel('Max nb of customers')
axes[1, 1].set_ylim(0, ylim_max)

fig.set_tight_layout(True)
fig_name = fig_dir + "RIL_nb_customers.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 01/10 - finished')



# Prices for the buyers and sellers

print('Plot 02/10 - 1/4'),
plt.clf()
ylim_max = max(max(sub_fee_buyer_av_RIL_p10_mean), max(sub_fee_seller_av_RIL_p10_mean), max(trans_fee_b_av_RIL_p10_mean), max(trans_fee_s_av_RIL_p10_mean), max(sub_fee_seller_av_RILS_p10_mean), max(trans_fee_b_av_RILS_p10_mean), max(trans_fee_b_av_RILS_p10_mean), max(trans_fee_s_av_RILS_p10_mean)) + 20
ylim_min = min(min(sub_fee_buyer_av_RIL_p10_mean), min(sub_fee_seller_av_RIL_p10_mean), min(trans_fee_b_av_RIL_p10_mean), min(trans_fee_s_av_RIL_p10_mean), min(sub_fee_seller_av_RILS_p10_mean), min(trans_fee_b_av_RILS_p10_mean), min(trans_fee_b_av_RILS_p10_mean), min(trans_fee_s_av_RILS_p10_mean)) - 20

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
axes[0, 0].plot(time, sub_fee_buyer_av_RIL_p10_mean, label='Subscription fee buyer')
axes[0, 0].plot(time, sub_fee_seller_av_RIL_p10_mean, label='Subscription fee seller')
axes[0, 0].legend(loc='best')
axes[0, 0].set_ylim(ylim_min, ylim_max)
axes[0, 0].set_title('Reinf. learning, ten providers without satisficing')
axes[0, 0].set_xlabel('time')
axes[0, 0].set_ylabel('Average subscription fee')

print('Plot 02/10 - 2/4'),
axes[0, 1].plot(time, trans_fee_b_av_RIL_p10_mean, label='Transaction fee buyer')
axes[0, 1].plot(time, trans_fee_s_av_RIL_p10_mean, label='Transaction fee seller')
axes[0, 1].legend(loc='best')
axes[0, 1].set_ylim(ylim_min, ylim_max)
axes[0, 1].set_title('Reinf. learning, ten providers without satisficing')
axes[0, 1].set_xlabel('time')
axes[0, 1].set_ylabel('Average transaction fee')

print('Plot 02/10 - 3/4'),
axes[1, 0].plot(time, sub_fee_buyer_av_RILS_p10_mean, label='Subscription fee buyer')
axes[1, 0].plot(time, sub_fee_seller_av_RILS_p10_mean, label='Subscription fee seller')
axes[1, 0].legend(loc='best')
axes[1, 0].set_ylim(ylim_min, ylim_max)
axes[1, 0].set_title('Reinf. learning, ten providers with satisficing')
axes[1, 0].set_xlabel('time')
axes[1, 0].set_ylabel('Average subscription fee')

print('Plot 02/10 - 4/4'),
axes[1, 1].plot(time, trans_fee_b_av_RILS_p10_mean, label='Transaction fee buyer')
axes[1, 1].plot(time, trans_fee_s_av_RILS_p10_mean, label='Transaction fee seller')
axes[1, 1].legend(loc='best')
axes[1, 1].set_ylim(ylim_min, ylim_max)
axes[1, 1].set_title('Reinf. learning, ten providers with satisficing')
axes[1, 1].set_xlabel('time')
axes[1, 1].set_ylabel('Average transaction fee')

fig.set_tight_layout(True)

# plt.show()
fig_name = fig_dir + "RIL10_sub_trans_fees.pdf"
plt.savefig(fig_name, type="pdf")

print('Plot 02/06 - finished')

plt.clf()

y_min_p, y_max_p = -0.05, 1.05
y_min_abs, y_max_abs = -200000, 1800000
mpl.rcParams['axes.spines.bottom'] = False

grey_4_types = ["-","-","-","-"]

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

print('Plot 03/10 - 1/4'),
axes[0, 0].plot(time, prov_rev_av_RIL_p10_mean, label='Provider', linestyle=grey_4_types[0], linewidth=1.0)
axes[0, 0].plot(time, seller_rev_av_RIL_p10_mean, label='Seller', linestyle=grey_4_types[1], linewidth=1.0)
axes[0, 0].plot(time, buyer_rev_av_RIL_p10_mean, label='Buyer', linestyle=grey_4_types[2], linewidth=1.0)


handles, labels = axes[0, 0].get_legend_handles_labels()
axes[0, 0].legend(flip(handles, 2), flip(labels, 2), loc='best', fontsize=10, ncol=2)
axes[0, 0].set_ylim(y_min_abs, y_max_abs)
axes[0, 0].set_title('Reinf. learning, ten providers without satisficing')
axes[0, 0].set_xlabel('time')
axes[0, 0].set_ylabel('Total revenues')
axes[0, 0].axhline(y=0.0, color='black', linewidth=1.0)
axes[0, 0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))

mpl.rcParams['axes.spines.bottom'] = True


print('Plot 03/10 - 2/4'),

axes[0, 1].plot(time, share_prov_RIL_p10, label='Provider', linestyle=grey_4_types[0], linewidth=1.0)
axes[0, 1].plot(time, share_seller_RIL_p10, label='Seller', linestyle=grey_4_types[1], linewidth=1.0)
axes[0, 1].plot(time, share_buyer_RIL_p10, label='Buyer', linestyle=grey_4_types[2], linewidth=1.0)
axes[0, 1].plot(time, share_cust_RIL_p10, label='Customer', linestyle=grey_4_types[3], linewidth=1.0)

handles, labels = axes[0, 1].get_legend_handles_labels()
y_min_p = min(min(share_seller_RIL_p10), min(share_prov_RIL_p10), min(share_buyer_RIL_p10), min(share_cust_RIL_p10))
axes[0, 1].legend(flip(handles, 2), flip(labels, 2), loc='best', fontsize=10, ncol=2)
axes[0, 1].set_ylim(y_min_p, y_max_p)
axes[0, 1].set_title('Reinf. learning, ten providers without satisficing')
axes[0, 1].set_xlabel('time')
axes[0, 1].set_ylabel('Share of total revenues')
axes[0, 1].axhline(y=1.0, color='black', linewidth=1.0)
axes[0, 1].axhline(y=0.0, color='black', linewidth=1.0)

print('Plot 03/10 - 3/4'),

axes[1, 0].plot(time, prov_rev_av_RILS_p10_mean, label='Provider', linestyle=grey_4_types[0], linewidth=1.0)
axes[1, 0].plot(time, seller_rev_av_RILS_p10_mean, label='Seller', linestyle=grey_4_types[1], linewidth=1.0)
axes[1, 0].plot(time, buyer_rev_av_RILS_p10_mean, label='Buyer', linestyle=grey_4_types[2], linewidth=1.0)
handles, labels = axes[1, 0].get_legend_handles_labels()
axes[1, 0].legend(flip(handles, 2), flip(labels, 2), loc='best', fontsize=10, ncol=2)

# axes[1, 0].legend(loc='best', fontsize=10)
axes[1, 0].set_ylim(y_min_abs, y_max_abs)
axes[1, 0].set_title('Reinf. learning, ten providers with satisficing')
axes[1, 0].set_xlabel('time')
axes[1, 0].set_ylabel('Total revenues')
axes[1, 0].axhline(y=0.0, color='black', linewidth=1.0)
axes[1, 0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))



print('Plot 03/10 - 4/4'),

axes[1, 1].plot(time, share_prov_RILS_p10, label='Provider', linestyle=grey_4_types[0], linewidth=1.0)
axes[1, 1].plot(time, share_seller_RILS_p10, label='Seller', linestyle=grey_4_types[1], linewidth=1.0)
axes[1, 1].plot(time, share_buyer_RILS_p10, label='Buyer', linestyle=grey_4_types[2], linewidth=1.0)
axes[1, 1].plot(time, share_cust_RILS_p10, label='Customer', linestyle=grey_4_types[3], linewidth=1.0)

handles, labels = axes[1, 1].get_legend_handles_labels()
axes[1, 1].legend(flip(handles, 2), flip(labels, 2), loc='best', fontsize=10, ncol=2)
axes[1, 1].set_ylim(y_min_p, y_max_p)
axes[1, 1].set_title('Reinf. learning, ten providers with satisficing')
axes[1, 1].set_xlabel('time')
axes[1, 1].set_ylabel('Share of total revenues')
axes[1, 1].axhline(y=1.0, color='black', linewidth=1.0)
axes[1, 1].axhline(y=0.0, color='black', linewidth=1.0)

fig.set_tight_layout(True)
# plt.show()


fig_name = fig_dir + "RIL_welfare.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 03/10 - finished')

########### EXPLS

print('Plot 04/10 - 1/2'),
plt.clf()

fig, axes = plt.subplots(2, sharex=True)

axes[0].plot(time, RILS_p10_00.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_01.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_02.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_03.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_04.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_05.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_06.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_07.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_08.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RILS_p10_09.trans_fee_b_av, alpha=0.25, linewidth=1.0)

axes[0].plot(time, trans_fee_b_av_RILS_p10_mean, linewidth=2.0, color='black')

axes[0].set_title('Reinf. learning, ten providers with satisficing')
axes[0].set_xlabel('time')
axes[0].set_ylabel('Transaction costs buyer')
axes[0].set_ylim(-1000, 1500)


print('Plot 04/10 - 2/2'),


axes[1].plot(time, RILS_p10_00.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_01.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_02.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_03.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_04.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_05.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_06.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_07.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_08.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)
axes[1].plot(time, RILS_p10_09.sub_fee_buyer_av, alpha=0.25, linewidth=1.0)

axes[1].plot(time, sub_fee_buyer_av_RILS_p10_mean, linewidth=2.0, color='black')

axes[1].set_title('Reinf. learning, ten providers with satisficing')
axes[1].set_xlabel('time')
axes[1].set_ylabel('Subscription fees buyer')
axes[1].set_ylim(-1000, 1500)

fig.set_tight_layout(True)
# plt.show()

fig_name = fig_dir + "RILS_trans_prices_b.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 04/10 - finished')

print('Plot 05/10 - 1/2'),
plt.clf()

fig, axes = plt.subplots(2, sharex=True)

axes[0].plot(time, RIL_p10_00.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_01.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_02.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_03.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_04.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_05.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_06.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_07.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_08.trans_fee_b_av, alpha=0.25, linewidth=1.0)
axes[0].plot(time, RIL_p10_09.trans_fee_b_av, alpha=0.25, linewidth=1.0)
y_max = max(max(RIL_p10_00.trans_fee_b_av),
                max(RIL_p10_01.trans_fee_b_av),
                max(RIL_p10_02.trans_fee_b_av),
                max(RIL_p10_03.trans_fee_b_av),
                max(RIL_p10_04.trans_fee_b_av),
                max(RIL_p10_05.trans_fee_b_av),
                max(RIL_p10_06.trans_fee_b_av),
                max(RIL_p10_07.trans_fee_b_av),
                max(RIL_p10_08.trans_fee_b_av),
                max(RIL_p10_09.trans_fee_b_av)) + 50

axes[0].plot(time, trans_fee_b_av_RIL_p10_mean, linewidth=2.0, color='black')

axes[0].set_title('Reinf. learning, ten providers without satisficing')
axes[0].set_xlabel('time')
axes[0].set_ylabel('Transaction costs buyer')
axes[0].set_ylim(-1000, y_max)


print('Plot 05/10 - 2/2'),
singleseries = [RIL_p10_00.sub_fee_buyer_av, RIL_p10_01.sub_fee_buyer_av, RIL_p10_02.sub_fee_buyer_av, RIL_p10_03.sub_fee_buyer_av, RIL_p10_04.sub_fee_buyer_av, RIL_p10_05.sub_fee_buyer_av,RIL_p10_06.sub_fee_buyer_av,RIL_p10_07.sub_fee_buyer_av,RIL_p10_08.sub_fee_buyer_av,RIL_p10_09.sub_fee_buyer_av,trans_fee_b_av_RIL_p10_mean]
y_max = max([max(x) for x in singleseries]) + 50
for series in singleseries:
    axes[1].plot(time, series, linewidth=1.0, alpha=0.25)
axes[1].plot(time, sub_fee_buyer_av_RIL_p10_mean, linewidth=2.0, color='black')
axes[1].set_title('Reinf. learning, ten providers without satisficing')
axes[1].set_xlabel('time')
axes[1].set_ylabel('Subscription fees buyer')
axes[1].set_ylim(-1000, y_max)

fig.set_tight_layout(True)
# plt.show()
fig_name = fig_dir + "RIL_trans_prices_b.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 05/10 - finished')

plt.clf()
ylim_max = max(max(max_prov_customers_RIL_p10_upper, max_prov_customers_RILS_p10_pcc0_upper, max_prov_customers_RILS_p10_pcc10_upper)) + 20
fig, axes = plt.subplots(1, 3, sharey=True ,figsize=(15, 4.5))

print('Plot 06/10 - 1/3'),
axes[0].plot(time, max_prov_customers_RILS_p10_mean, label='Max nb of customers', color=viridis_color)
axes[0].plot(time, max_prov_customers_RILS_p10_upper, color=viridis_color, alpha=0.25)
axes[0].plot(time, max_prov_customers_RILS_p10_lower, color=viridis_color, alpha=0.25)
axes[0].fill_between(time, max_prov_customers_RILS_p10_lower, max_prov_customers_RILS_p10_upper, facecolor=viridis_color, alpha=0.15)
# axes[0].legend(loc='best')
axes[0].set_title('Per customer fixed costs = 25')
axes[0].set_xlabel('time')
axes[0].set_ylabel('Max nb of customers')
axes[0].set_ylim(0, ylim_max)

print('Plo 06/10 - 2/3'),
axes[1].plot(time, max_prov_customers_RILS_p10_pcc10_mean, label='Max nb of customers', color=viridis_color)
axes[1].plot(time, max_prov_customers_RILS_p10_pcc10_upper, color=viridis_color, alpha=0.25)
axes[1].plot(time, max_prov_customers_RILS_p10_pcc10_lower, color=viridis_color, alpha=0.25)
axes[1].fill_between(time, max_prov_customers_RILS_p10_pcc10_lower, max_prov_customers_RILS_p10_pcc10_upper, facecolor=viridis_color, alpha=0.15)
# axes[1].legend(loc='best')
axes[1].set_title('Per customer fixed costs = 10')
axes[1].set_xlabel('time')
axes[1].set_ylim(0, ylim_max)

print('Plot 06/10 - 3/3'),
axes[2].plot(time, max_prov_customers_RILS_p10_pcc0_mean, label='Max nb of customers', color=viridis_color)
axes[2].plot(time, max_prov_customers_RILS_p10_pcc0_upper, color=viridis_color, alpha=0.25)
axes[2].plot(time, max_prov_customers_RILS_p10_pcc0_lower, color=viridis_color, alpha=0.25)
axes[2].fill_between(time, max_prov_customers_RILS_p10_pcc0_lower, max_prov_customers_RILS_p10_pcc0_upper, facecolor=viridis_color, alpha=0.15)
# axes[2].legend(loc='best')
axes[2].set_title('Per customer fixed costs = 0')
axes[2].set_xlabel('time')
axes[2].set_ylim(0, ylim_max)

fig.set_tight_layout(True)
# plt.show()
fig_name = fig_dir + "RILS_pcfc.pdf"
plt.savefig(fig_name, type="pdf")

print('Plot 06/10 - finished')






plt.clf()
y_min, y_max = -0.05, 1.05
time_RO = range(1, 41)

fig, axes = plt.subplots(2, figsize=(5, 8))

grey_4_types = ["-","-","-","-"]

print('Plot 07/10 - 1/2'),

axes[0].plot(time_RO, share_prov_RO_p01_efm200, label='Provider', linewidth=1.0, linestyle=grey_4_types[0])
axes[0].plot(time_RO, share_seller_RO_p01_efm200, label='Share seller', linewidth=1.0, linestyle=grey_4_types[1])
axes[0].plot(time_RO, share_buyer_RO_p01_efm200, label='Share buyer', linewidth=1.0, linestyle=grey_4_types[2])
axes[0].plot(time_RO, share_cust_RO_p01_efm200, label='Share customer', linewidth=1.0, linestyle=grey_4_types[3])
axes[0].axhline(y=1.0, color='black', linewidth=1.0)
axes[0].axhline(y=0.0, color='black', linewidth=1.0)
axes[0].spines['bottom'].set_visible(False)
handles, labels = axes[0].get_legend_handles_labels()
axes[0].legend(flip(handles, 2), flip(labels, 2), loc='best', fontsize=10, ncol=2)
axes[0].set_ylim(y_min, y_max)
axes[0].set_title('Rational optimization, fixed entry fee = -200', fontsize=10)
axes[0].tick_params(axis='y', labelsize=8)
axes[0].yaxis.get_offset_text().set_size(8)
axes[0].set_xlabel('time', fontsize=10)
axes[0].set_ylabel('Share of total revenue', fontsize=10)


print('Plot 07/10 - 2/2'),
axes[1].plot(time_RO, share_prov_RO_p01_ef0, label='Provider', linewidth=1.0, linestyle=grey_4_types[0])
axes[1].plot(time_RO, share_seller_RO_p01_ef0, label='Share seller', linewidth=1.0, linestyle=grey_4_types[1])
axes[1].plot(time_RO, share_buyer_RO_p01_ef0, label='Share buyer', linewidth=1.0, linestyle=grey_4_types[2])
axes[1].plot(time_RO, share_cust_RO_p01_ef0, label='Share customer', linewidth=1.0, linestyle=grey_4_types[3])
axes[1].axhline(y=1.0, color='black', linewidth=1.0)
axes[1].axhline(y=0.0, color='black', linewidth=1.0)

handles, labels = axes[1].get_legend_handles_labels()
axes[1].legend(flip(handles, 2), flip(labels, 2), bbox_to_anchor=[0.5, 0.8], loc='center', fontsize=10, ncol=2)
axes[1].set_ylim(y_min, y_max)
axes[1].set_title('Rational optimization, fixed entry fee = 0', fontsize=10)
axes[1].tick_params(axis='y', labelsize=8)
axes[1].spines['bottom'].set_visible(False)
axes[1].yaxis.get_offset_text().set_size(8)
axes[1].set_xlabel('time', fontsize=10)
axes[1].set_ylabel('Share of total revenue', fontsize=10)


fig.set_tight_layout(True)
# plt.show()

fig_name = fig_dir + "RO_final_welfare_dist.pdf"
plt.savefig(fig_name, type="pdf")

print('Plot 07/10 - finished')




print('Plot 08/10 - 1/2'),
plt.clf()
# ylim_max = max(max(trans_fee_b_av_RO_p01_ef0_upper), max(trans_fee_b_av_RO_p01_efm200_upper), max(trans_fee_b_av_RO_p01_efm200_upper), max(trans_fee_s_av_RO_p01_ef0_upper), max(trans_fee_s_av_RO_p01_efm200_upper), max(trans_fee_s_av_RO_p01_efm200_upper)) + 5
ylim_max = 300
ylim_min = min(min(trans_fee_b_av_RO_p01_ef0_upper), min(trans_fee_b_av_RO_p01_efm200_upper), min(trans_fee_b_av_RO_p01_efm200_upper), min(trans_fee_s_av_RO_p01_ef0_upper), min(trans_fee_s_av_RO_p01_efm200_upper), min(trans_fee_s_av_RO_p01_efm200_upper))


fig, axes = plt.subplots(2, figsize=(5, 8))
axes[0].plot(time_RO, trans_fee_b_av_RO_p01_ef0_mean, label='Prices buyer', linewidth=1.0)
axes[0].plot(time_RO, trans_fee_s_av_RO_p01_ef0_mean, label='Prices seller', linewidth=1.0)
axes[0].legend(loc='best', fontsize=10)
axes[0].set_ylim(ylim_min, ylim_max)
axes[0].set_title('Rational optimization, fixed entry fee = 0', fontsize=10)
axes[0].tick_params(axis='y', labelsize=8)
axes[0].set_xlabel('time', fontsize=10)
axes[0].set_ylabel('Price', fontsize=10)
print('Plot 08/10 - 2/2'),
axes[1].plot(time_RO, trans_fee_b_av_RO_p01_efm200_mean, label='Prices buyer', linewidth=1.0)
axes[1].plot(time_RO, trans_fee_s_av_RO_p01_efm200_mean, label='Prices seller', linewidth=1.0)
axes[1].legend(loc='best', fontsize=10)
axes[1].set_ylim(ylim_min, ylim_max)
axes[1].set_title('Rational optimization, fixed entry fee = -200', fontsize=10)
axes[1].tick_params(axis='y', labelsize=8)
axes[1].set_xlabel('time', fontsize=10)
axes[1].set_ylabel('Price', fontsize=10)
fig.set_tight_layout(True)
# plt.show()

fig_name = fig_dir + "RO_prices_direct_customers.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 08/10 - finished')



plt.clf()

grey_3_types = ["-","-","-"]

ylim_max = max(max(prov_rev_av_RO_p01_ef0_mean), max(prov_rev_av_RO_p01_efm200_mean), max(pb_rev_av_RO_p01_ef0_mean), max(pb_rev_av_RO_p01_efm200_mean), max(pbs_rev_av_RO_p01_ef0_mean), max(pbs_rev_av_RO_p01_efm200_mean))
ylim_min = min(min(prov_rev_av_RO_p01_ef0_mean), min(prov_rev_av_RO_p01_efm200_mean), min(pb_rev_av_RO_p01_ef0_mean), min(pb_rev_av_RO_p01_efm200_mean), min(pbs_rev_av_RO_p01_ef0_mean), min(pbs_rev_av_RO_p01_efm200_mean))
print('Plot 09/10 - 1/2'),
fig, axes = plt.subplots(2, figsize=(5, 8))
axes[0].plot(time_RO, prov_rev_av_RO_p01_ef0_mean, label='Provider revenue',  linestyle=grey_3_types[0], linewidth=1.0)
axes[0].plot(time_RO, pb_rev_av_RO_p01_ef0_mean, label='Provider+Buyer revenue', linestyle=grey_3_types[1], linewidth=1.0)
axes[0].plot(time_RO, pbs_rev_av_RO_p01_ef0_mean, label='Total revenue', linestyle=grey_3_types[2], linewidth=1.0)

axes[0].fill_between(time_RO, prov_rev_av_RO_p01_ef0_mean, np.zeros(len(time_RO)),  alpha=0.25)
axes[0].fill_between(time_RO, pb_rev_av_RO_p01_ef0_mean, prov_rev_av_RO_p01_ef0_mean, alpha=0.25)
axes[0].fill_between(time_RO, pbs_rev_av_RO_p01_ef0_mean, pb_rev_av_RO_p01_ef0_mean, alpha=0.25)
axes[0].legend(loc='best', fontsize=10)
axes[0].set_ylim(ylim_min, ylim_max)
axes[0].tick_params(axis='y', labelsize=8)
axes[0].yaxis.get_offset_text().set_size(8)
axes[0].set_title('Rational optimization, fixed entry fee = 0', fontsize=10)
axes[0].set_xlabel('time', fontsize=10)
axes[0].set_ylabel('Revenue')

print('Plot 09/10 - 2/2'),
axes[1].plot(time_RO, prov_rev_av_RO_p01_efm200_mean, label='Provider revenue', linestyle=grey_3_types[0], linewidth=1.0)
axes[1].plot(time_RO, pb_rev_av_RO_p01_efm200_mean, label='Provider+Buyer revenue', linestyle=grey_3_types[1], linewidth=1.0)
axes[1].plot(time_RO, pbs_rev_av_RO_p01_efm200_mean, label='Total revenue', linestyle=grey_3_types[2], linewidth=1.0)
axes[1].fill_between(time_RO, prov_rev_av_RO_p01_efm200_mean, np.zeros(len(time_RO)), alpha=0.25)
axes[1].fill_between(time_RO, pb_rev_av_RO_p01_efm200_mean, prov_rev_av_RO_p01_efm200_mean, alpha=0.25)
axes[1].fill_between(time_RO, pbs_rev_av_RO_p01_efm200_mean, pb_rev_av_RO_p01_efm200_mean, alpha=0.25)
axes[1].legend(loc='best', fontsize=10)
axes[1].set_ylim(ylim_min, ylim_max)
axes[1].tick_params(axis='y', labelsize=8)
axes[1].yaxis.get_offset_text().set_size(8)
axes[1].set_title('Rational optimization, fixed entry fee = -200', fontsize=10)
axes[1].set_xlabel('time', fontsize=10)
axes[1].set_ylabel('Revenue')

fig.set_tight_layout(True)

# plt.show()

fig_name = fig_dir + "RO_final_welfare.pdf"
plt.savefig(fig_name, type="pdf")
print('Plot 09/10 - finished')


print('Plot 10/10 - 1/1'),
nbuyers = [125, 250, 500, 1000, 2000, 4000, 8000, 16000, 32000]

plt.clf()


ylim_max = max(max(bs_trans_fee_b_mean), max(bs_trans_fee_s_mean)) + 10
ylim_min = min(min(bs_trans_fee_b_mean), min(bs_trans_fee_s_mean)) - 10

fig, axes = plt.subplots(figsize=(15, 9))
axes.plot(nbuyers,bs_trans_fee_b_mean, label='Buyer transaction price')
axes.plot(nbuyers,bs_trans_fee_s_mean, label='Seller transaction price')
axes.legend(loc='best')
axes.set_ylim(ylim_min, ylim_max)
axes.set_xlim(125, 32000)
axes.set_xscale('log')
#axes.set_title('')
axes.set_xlabel('Number of buyers')
axes.set_ylabel('Max nb of customers')

fig_name = fig_dir + "BST_comparison_RO_noq.pdf"
plt.savefig(fig_name, type="pdf")

print('Plot 10/10 - finished')

print('Plotting finished. Please find the figures in', fig_dir)
