#!/usr/bin/env python3
"""
This module provides functions for reading and writing population data,
as well as for writing error metrics to json files.
"""
from .Error_Analysis import MSE, RMSE, RelativeRMSE


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

'''
def write_data(org = None, vdata=None, gdata=None, rdata=None, region=""):
    years = [1960,1970,1984,2000,2010]
    if region == "":
        raise ValueError("<Region> cannot be None")
    if region == "Western":
        filename = "Western_output.dat"
    elif region == "Central":
        filename = "Central_output.dat"
    elif region == "Greater Accra":
        filename = "GreaterAccra_output.dat"
    elif region == "Volta":
        filename = "Volta_output.dat"
    elif region == "Eastern":
        filename = "Eastern_output.dat"
    elif region == "Ashanti":
        filename = "Ashanti_output.dat"
    elif region == "Brong Ahafo":
        filename = "BrongAhafo_output.dat"
    elif region == "Northern":
        filename = "Northern_output.dat"
    elif region == "Upper West":
        filename = "UpperWest_output.dat"
    elif region == "Upper East":
        filename = "UpperEast_output.dat"
    try:
        with open(filename, "wt", encoding="utf-8") as file:
            file.write(f"#Year\t#Actual\t#Verh\t#Gomptz\t#Richard\n")
            for  a,b,c,d,e in zip(years, org, vdata, gdata, rdata):
                file.write(f"{a}\t{b}\t{c}\t{d}\t{e}\n")

    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
'''

def write_error(orig=None, predicted=None, model=""):
    try:
        if model is None:
            raise ValueError("<Model> cannot be None")
        if orig is None or predicted is None:
            raise ValueError("<orig> and <predicted> cannot be None")
    
        m = MSE(orig, predicted)
        rm = RMSE(orig, predicted)
        rrm = RelativeRMSE(orig, predicted)
        metrics = {
                "MSE": m,
                "RMSE": rm,
                "Relative RMSE": rrm
            }
        return metrics
    except ValueError as ve:
        print("[{}] {}".format(ve.__class__.__name__, ve))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


def write_data(*args, filename):
    try:
        year = [1960, 1970, 1984, 2000, 2010]
        with open(filename, "wt", encoding="utf-8") as file:
            file.write(f"#Year \t #Popl \t #Verh \t #Gmpz \t #Rich\n")
            for rows in zip(year, *args):
                line = "\t".join(str(x) for x in rows)
                #if line.strip():  # Check if the line is not empty
                file.write(line + '\n')
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))