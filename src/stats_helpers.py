import pandas as pd
import scipy.stats as ss
def ChiSquare(x,y, verbose=True):
    confusion_matrix = pd.crosstab(x,y)
    chi2, p, dof, ex = ss.chi2_contingency(confusion_matrix)
    if verbose:
        print("\n=====================================")
        print(confusion_matrix)
        print("-------------------------------------")
        print("p-value: %.4f" % p)
        print("=====================================\n\n")
    return p
