#!/usr/bin/env python3
import numpy as np

def take_data():
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []
    with open("data.dat","r") as file:
        for i in file:
            part = i.strip().split()
            data1.append(part[1])
            data2.append(part[2])
            data3.append(part[3])   
            data4.append(part[4])
            data5.append(part[5])
            data6.append(part[6])
            data7.append(part[7])
            data8.append(part[8])
            data9.append(part[9])
            data10.append(part[10])
    Wdata =[int(x) for x in data1]
    Cdata =[int(x) for x in data2]
    GAdata =[int(x) for x in data3]
    Vdata =[int(x) for x in data4]
    Edata =[int(x) for x in data5]
    Adata =[int(x) for x in data6]
    Bdata =[int(x) for x in data7]
    Ndata =[int(x) for x in data8]
    UEdata =[int(x) for x in data9]
    UWdata =[int(x) for x in data10]
    return (Wdata, Cdata, GAdata, Vdata, Edata, Adata, Bdata, Ndata, UEdata, UWdata)


def write_data(input = None, data1=None,data2=None,data3=None, region=None):
    years = [1960,1970,1984,2000,2010]
    if region is None:
        raise ValueError("<Region> cannot be None")
    if region == "Western":
        filename = "Western_output.dat"
    elif region == "Central":
        filename = "Central_output.dat"
    elif region == "GreaterAccra":
        filename = "GreaterAccra_output.dat"
    elif region == "Volta":
        filename = "Volta_output.dat"
    elif region == "Eastern":
        filename = "Eastern_output.dat"
    elif region == "Ashanti":
        filename = "Ashanti_output.dat"
    elif region == "BrongAhafo":
        filename = "BrongAhafo_output.dat"
    elif region == "Northern":
        filename = "Northern_output.dat"
    elif region == "UpperWest":
        filename = "UpperWest_output.dat"
    elif region == "UpperEast":
        filename = "UpperEast_output.dat"
    else:
        filename = "output.dat"
    with open(filename,"w") as file:
        file.write(f"#Year\t#Actual\t#Verh\t#Gomptz\t#Richard\n")
        for  a,b,c,d,e in zip(years, input, data1, data2,data3):
            file.write(f"{a}\t{b}\t{c}\t{d}\t{e}\n")
    #print(f"Data written Successfully! for {region}")