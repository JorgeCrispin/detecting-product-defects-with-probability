import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7
## Task 2:
print(stats.poisson.pmf(lam, 7))
## Task 3:
print(stats.poisson.cdf(4,lam))
## Task 4:
print(1-stats.poisson.cdf(10,lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)
## Task 6:
print(year_defects[0:20])

## Task 7:
print(lam*365)
## Task 8:
print(sum(year_defects))
## Task 9:
print(year_defects.mean())
## Task 10:
print(year_defects.max())
## Task 11:
print(1-stats.poisson.cdf(14,lam))

### Extra Bonus ###
# Task 12
nintieth = stats.poisson.ppf(0.90,lam)
print(nintieth)
# Task 13
print(sum(year_defects >= nintieth)/len(year_defects))