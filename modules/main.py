#!/usr/bin/env python3
import numpy as np
#from data import take_data
from models import VerhulstModel, GompertzModel, RichardModel

def take_data():
    data = []
    with open("western_data.dat","r") as file:
        for i in file:
            part = i.strip().split()
            data.append(part[1])
    refdata =[int(x) for x in data]
    return (refdata)

def write_data(data1=None,data2=None,data3=None):
    input_data = take_data()
    years = [1960,1970,1984,2000,2010]
    with open("output.dat","w") as file:
        file.write(f"#Year\t#Actual\t#Verh\tGomptz\tRichard\n")
        for  a,b,c,d,e in zip(years, input_data, data1, data2,data3):
            file.write(f"{a}\t{b}\t{c}\t{d}\t{e}\n")
    print("Data written Successfully!")

def MSE(data1=None, data2=None):
    if data1 is None or data2 is None:
        raise ValueError("Data cannot be None")
    return np.mean((data1 - data2) ** 2)
def RMSE(actual=None, estimated=None):
    if actual is None or estimated is None:
        raise ValueError("Data cannot be None")
    return np.sqrt(np.mean((actual - estimated) ** 2))
def RelativeRMSE(actual=None, estimated=None):
    if actual is None or estimated is None:
        raise ValueError("Data cannot be None")
    mean = np.mean(actual)
    return (RMSE(actual, estimated) / mean) * 100
def main():
    p = np.array(take_data())
    t = np.arange(len(p))
    p0 = p[0]
    k0 = 5_000_000.0

    r_init = 0.1

    model = VerhulstModel(p, p0, k0, r_init, t)
    model.fit()
    model2 = GompertzModel(p, p0, k0, r_init, t)
    model2.fit()
    model3 = RichardModel(p,p0, k0, r_init, t, theta=1.0)
    model3.fit()
    data1 = model.predict()
    data2 = model2.predict()
    data3 = model3.predict()
    write_data(data1,data2,data3)

if __name__ == "__main__":
    main()
