import pandas as pd
from pandas import DataFrame
import sys
import csv

def _mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)


def normalizeElem(list, elem):
    return (elem - min(list)) / (max(list) - min(list))


def denormalizeElem(list, elem):
    return (elem * (max(list) - min(list))) + min(list)


def error_exit(string):
    print(string)
    sys.exit(0)

#normalizasyon
def normalisation(s):
    return [((_ - min(s)) / (max(s) - min(s))) for _ in s]

#tahmini fiyat
def raw_estimated_price(t0, x, t1):
    return t0 + x * t1


def estimated_price(t0, t1, x, X, Y):
    # print(f'({x} - {min(X)}) / ({max(X)} - {min(X)}) == { (x - min(X)) / (max(X) - min(X))}')
    price_ranged = raw_estimated_price(t0, (x - min(X)) / (max(X) - min(X)), t1)
    # print(price_ranged)
    # print(f"(max(Y) - min(Y)) == {(max(Y) - min(Y))}")
    return price_ranged * (max(Y) - min(Y)) + min(Y)


def cost(X, Y, th):
    return ((th[1] * X + th[0] - Y) ** 2).mean()



def getData(file):
    data = pd.read_csv(file)
    mileages = data['km'].tolist()
    prices = data['price'].tolist()
    return (mileages, prices)



def get_gradient_csv(input):
    try:
        with open(input, 'r') as file:
            return {line.split(':')[0].strip(): float(line.split(':')[1].strip()) for line in file}
    except:
        return {'T0': 0, 'T1': 0}


def set_gradient_csv(output, t0, t1):
    try:
        with open(output, "w+") as f:
            f.write(f'T0:{t0}\nT1:{t1}\n')
    except:
        error_exit('Wrong file')



def normal(message):
    """
        Verbosity for normal msg
    """
    print(message)


def prRed(skk): return "\033[91m{}\033[00m".format(skk)
def prGreen(skk): return "\033[92m{}\033[00m".format(skk)
def prYellow(skk): return "\033[33m{}\033[0m".format(skk)
def prLightPurple(skk): return "\033[94m{}\033[00m".format(skk)
def prPurple(skk): return "\033[95m{}\033[00m".format(skk)
def prCyan(skk): return "\033[96m{}\033[00m".format(skk)
def prLightGray(skk): return "\033[97m{}\033[00m".format(skk)
def prBlack(skk): return "\033[98m {}\033[00m".format(skk)