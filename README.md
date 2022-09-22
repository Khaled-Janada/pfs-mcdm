# pfs-mcdm  

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--6522--8482-green)](https://orcid.org/0000-0002-6522-8482)

  
Python implementation of multi-criteria decision-making (MCDM) algorithms using pythagorean fuzzy sets (PFSs).  
  
**Implemented Algorithms:**  
  
- Simple Aggregation  
- TOPSIS  
- PROMETHEE  
  
**Future Work:**  
  
- Electre  
- COPRAS  
  
For more information about PFSs and the implemented algorithms see:  
  
- Yager, R.R., & Abbasov, A.M. (2013). Pythagorean Membership Grades, Complex Numbers, and Decision Making. International Journal of Intelligent  
  Systems, 28, doi:[10.1002/int.21584](https://doi.org/10.1002/int.21584).  
- Yager, R.R. (2014). Pythagorean Membership Grades in Multicriteria Decision Making. IEEE Transactions on Fuzzy Systems, 22, 958-965,  
  doi:[10.1109/TFUZZ.2013.2278989](https://doi.org/10.1109/TFUZZ.2013.2278989).  
- Zhang, X., & Xu, Z. (2014). Extension of TOPSIS to Multiple Criteria Decision Making with Pythagorean Fuzzy Sets. International Journal of  
  Intelligent Systems, 29, doi:[10.1002/int.21676](https://doi.org/10.1002/int.21676).  
- Molla, M.U., Giri, B.C., & Biswas, P. (2021). Extended PROMETHEE method with Pythagorean fuzzy sets for medical diagnosis problems. Soft Comput.,  
  25, 4503-4512, doi:[10.1007/s00500-020-05458-7](https://doi.org/10.1007/s00500-020-05458-7).  
- Ye, J., & Chen, T. (2022). Pythagorean Fuzzy Sets Combined with the PROMETHEE Method for the Selection of Cotton Woven Fabric. Journal of Natural  
  Fibers, doi:[10.1080/15440478.2022.2072993](https://doi.org/10.1080/15440478.2022.2072993).  
  
***  
  
## Installation  
  
The `pfs-mcdm` package can be installed from PyPI using pip for Python 3  
  
```
$ pip install pfs-mcdm
``` 
  
***
## How to use?  
  
The decision matrix can be provided as a 2D array-like of tuples. Each tuple represents a pythagorean fuzzy number $(\mu, \nu)$.
The weights of the  criteria are provided as an 1D array-like of floats.
Weights are normalized to sum to 1.
Optionally, the `aternatives` argument can be used to provide alternatives' names.
  
The output solution is a pandas `DataFrame`

    import pfs-mcdm as pfs  
      
    matrix = [ 
    [(0.9, 0.3), (0.7, 0.6), (0.5, 0.8), (0.6, 0.3)],
    [(0.4, 0.7), (0.9, 0.2), (0.8, 0.1), (0.5, 0.3)],  
    [(0.8, 0.4), (0.7, 0.5), (0.6, 0.2), (0.7, 0.4)], 
    [(0.7, 0.2), (0.8, 0.2), (0.8, 0.4), (0.6, 0.6)]] 
      
    weights = [0.15, 0.25, 0.35, 0.25]  
      
    alternatives = ['UNI AIR', 'Transasia', 'Mandarin', 'Daily Air']

#### Simple Aggregation:

    from pfs-mcdm import simple_aggregation

    simple_aggregation_sol = simple_aggregation(matrix, weights, alternatives=alternatives)  
      
    print(simple_aggregation_sol)

<blockquote><blockquote>

|           | Aggregated    | Score | Rank |
|-----------|---------------|-------|------|
| UNI AIR   | (0.635, 0.55) | 0.101 | 4    |
| Transasia | (0.69, 0.265) | 0.406 | 1    |
| Mandarin  | (0.68, 0.355) | 0.336 | 3    |
| Daily Air | (0.735, 0.37) | 0.403 | 2    |

</blockquote></blockquote>

#### TOPSIS:

    from pfs-mcdm import topsis

    topsis_sol = topsis(matrix, weights, alternatives=alternatives)  
       
    print(topsis_sol)

<blockquote><blockquote>

|           | D+    | D-    | Revised Closeness | Rank |
|-----------|-------|-------|-------------------|------|
| UNI AIR   | 0.351 | 0.165 | -1.586            | 4    |
| Transasia | 0.175 | 0.396 | 0.000             | 1    |
| Mandarin  | 0.204 | 0.359 | -0.254            | 3    |
| Daily Air | 0.201 | 0.316 | -0.348            | 2    |

</blockquote></blockquote>

#### PROMETHEE:
The `promethee` function takes an optional argument `preference_func` to determine the preference function to be used. Available functions are `usual`, `ushape`, `vshape`, `level`, and `gaussian`; default is `usual`.  
&nbsp; For `ushape` preference function, an additional argument `q` can be passed to determine the indifference threshold; default is zero. For `vshape` and `level` preference function, additional arguments `q` and `p` can be passed to determine the indifference and preference thresholds, respectively; default is zero. For the `gaussian` preference function, an additional argument `s` can be passed to determine the Gaussian threshold; default is 0.5.

    from pfs-mcdm import promethee

    promethee_sol = promethee(matrix, weights, alternatives=alternatives, preference_func='vshape', q=0.1, p=0.8)  
      
    print(promethee_sol)

|           | Positive Outranking | Negative Outranking | Net Outranking | Rank |
|-----------|---------------------|---------------------|----------------|------|
| UNI AIR   | 0.094               | 0.445               | -0.351         | 4    |
| Transasia | 0.291               | 0.158               | 0.133          | 1    |
| Mandarin  | 0.189               | 0.137               | 0.051          | 3    |
| Daily Air | 0.250               | 0.084               | 0.167          | 2    |

# License  
MIT