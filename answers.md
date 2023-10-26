# CMPS 2200 Reciation 5
## Answers

**Name:**__Simon Yung_____


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
- Random:
        
|      n |   qsort-fixed-pivot |   qsort-random-pivot |   selection sort |   timsort |
|--------|---------------------|----------------------|------------------|-----------|
|    100 |               0.150 |                0.190 |            0.297 |     0.002 |
|    200 |               0.300 |                0.395 |            1.076 |     0.004 |
|    500 |               0.842 |                1.087 |            6.347 |     0.007 |
|   1000 |               1.790 |                2.448 |           24.669 |     0.011 |
|   2000 |               3.713 |                4.974 |           99.043 |     0.037 |
|   5000 |              10.691 |               13.713 |          618.345 |     0.060 |
|  10000 |              22.869 |               28.575 |         2534.304 |     0.112 |
|  20000 |              46.730 |               57.424 |         10943.332|     4.234 |
|  50000 |             127.178 |              151.873 |         42391.629|    12.043 |
| 100000 |             273.210 |              340.926 |       160235.623 |    26.064 |

- Fixed:

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   selection sort |   timsort |
|--------|---------------------|----------------------|------------------|-----------|
|    100 |               0.116 |                0.220 |            0.258 |     0.003 |
|    200 |               0.232 |                0.437 |            0.913 |     0.003 |
|    500 |               0.588 |                1.102 |            5.285 |     0.008 |
|   1000 |               1.258 |                2.321 |           20.961 |     0.022 |
|   2000 |               2.697 |                4.938 |           80.234 |     0.023 |
|   5000 |               7.567 |               12.653 |          504.161 |     0.057 |
|  10000 |              16.054 |               26.607 |         2017.726 |     0.113 |
|  20000 |              33.886 |               57.257 |         8203.332 |     0.213 |
|  50000 |              93.560 |              150.567 |       324451.937 |     0.554 |
| 100000 |             196.882 |              323.855 |       127893.124 |     1.115 |

Running these tests match up with the asymptoptic expectations with selections sort around O(n^2), quicksort around O(nlogn). the change form randon to fixed does not change selection sort or random pivot but seems to slightly improve fixed-pivot. 



- **1c.**
As seen above none of the functions made can even come close to maching timsort in terms of speed.
