import numpy as np
from scipy import stats

bm25 = np.loadtxt('bm25.avg_p.txt')
inl2 = np.loadtxt('inl2.avg_p.txt')

pvalue = stats.ttest_rel(bm25, inl2, axis=0, nan_policy='propagate').pvalue


with open('significance.txt', 'w') as f:
    print(pvalue, file=f)