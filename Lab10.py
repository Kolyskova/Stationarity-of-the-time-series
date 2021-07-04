import numpy as np
from scipy import stats
import random

n1 = []
n2 = []
M1 = 0
M2 = 0
S1 = 0
S2 = 0
T = 0
"""
n1 = np.loadtxt("data11.txt", delimiter='\t', dtype=np.int)
n2 = np.loadtxt("data12.txt", delimiter='\t', dtype=np.int)
"""
for i in range(25):
    n1.append(random.uniform(0, 10))
    n2.append(random.uniform(0, 10))

for i in range(20):
    M1 += n1[i] / 25
    M2 += n2[i] / 25
for i in range(25):
    S1 += ((n1[i] - M1)**2) / 25
    S2 += ((n2[i] - M2)**2) / 25
for i in range(25):
    print(n1[i])
print("Среднее: ", M1, " Дисперсия: ", S1)
for i in range(25):
    print(n2[i])
print("Среднее: ", M2, " Дисперсия: ", S2)
T = abs(M1 - M2) / ((S1 / 25)**0.5 + (S2 / 25)**0.5)
print("Критерий сдвига:")
print("Выборочное значение: ", T)
t = stats.t.ppf(1 - 0.05 / 2, 2 * 25 - 2)
f = stats.f.cdf(1 - 0.05 / 2, 24, 24)
print("Критическое значение: ", t)
if t > T:
    print("Ряд стационарен")
else:
    print("Ряд нестационарен")
print("Критерий рассеяний:")
print("Выборочное значение: ", S1 / S2)
print("Критическое значение: ", f)
if S1 / S2 < f:
    print("Ряд стационарен")
else:
    print("Ряд нестационарен")
