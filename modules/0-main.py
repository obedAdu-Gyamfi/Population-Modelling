#!/usr/bin/env python3
import numpy as np
from data import take_data
from models import VerhulstModel

def write_data(data=None):
    #recv_data = verhulst()
    input_data = take_data()
    years = [1960,1970,1984,2000,2010]
    with open("output.dat","w") as file:
        file.write(f"#Year\t#Actual\t#Est \n")
        for  a,b,c in zip(years, input_data, data):
            file.write(f"{a}\t{b}\t{c}\n")
    print("Data written Successfully!")

def main():
    pis = np.array(take_data())
    t = np.arange(len(pis))
    p0 = pis[0]
    k_init = 3_000_000.0
    r_init = 0.1

    model = VerhulstModel(pis, p0, k_init, r_init, t)
    model.fit()
    data = model.predict()
    write_data(data)
    print(f"Estimated carrying capacity (k): {model.k:.4f}")
    print(f"Estimated growth rate (r): {model.r:.6f}")
    print("Predicted values:", model.predict())




if __name__ == "__main__":
    main()
