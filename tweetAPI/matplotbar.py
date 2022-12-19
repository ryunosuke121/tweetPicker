import matplotlib.pyplot as plt


def negaPosiBar(scores):
    a = range(-1.0,1.0)
    b=scores

    plt.bar(a,b)
    plt.show()