from sklearn.preprocessing import LabelBinarizer
import argparse

"""
example: 
number of annotators: 5, 
number of annotations: 4, 
number of categories: 3

rate_list = 
      [1, 2, 2],
      [0, 4, 1],
      [0, 3, 2], 
      [5, 0, 0],   
    ]
"""
def one_hot(label):
    label_binary = LabelBinarizer().fit_transform(label)
    return label_binary

def compute_fleiss_kappa(rate_list: list, n: int) -> float:
    N = len(rate_list) 
    k = len(rate_list[0]) 

    print('Number of Annotators: {}'.format(n))
    print('Number of Annotations: {}'.format(N))
    print('Number of Categories: {}'.format(k))

    P_bar = sum([(sum([el**2 for el in row]) - n) / (n * (n - 1)) for row in rate_list]) / N
    print('P_bar: {}'.format(P_bar))

    Pe_bar = sum([(sum([row[j] for row in rate_list]) / (N * n)) ** 2 for j in range(k)])
    print('Pe_bar: {}'.format(Pe_bar))

    kappa = float(0)
    try:
        kappa = (P_bar - Pe_bar) / (1 - Pe_bar)
    except ZeroDivisionError:
        kappa = float(1)

    return kappa

def main(rate_list, n):
    print('Fleiss kappa: {}'.format(compute_fleiss_kappa(rate_list, n)))
    
if __name__ == '__main__':
    main()
    