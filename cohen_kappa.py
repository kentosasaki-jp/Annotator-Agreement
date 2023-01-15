# compute cohen's kappa
from sklearn.metrics import cohen_kappa_score

a = []
b = []
    
def main():
    cohen_kappa = cohen_kappa_score(a, b)
    print("Cohen's Kappa: ",cohen_kappa)
    
if __name__ == '__main__':
    main()
    