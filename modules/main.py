#!/usr/bin/env python3
import numpy as np
from data import take_data, write_data
#from models import VerhulstModel, GompertzModel, RichardModel
from region import Western, Central, GreatAccra, Volta, Eastern, Ashanti, BrongAhafo, Northern, UpperEast, UpperWest


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
    wp,cp,gp,vp,ep,ap,bp,northp,uep,uwp = np.array(take_data())

    k0 = 5_000_000.0
    r_init = 0.1

    wmodel = Western(wp, k0, r_init)
    WestVerhulstData = wmodel.verhulst_model()
    WestGompertzData = wmodel.gompertz_model()
    WestRichadData = wmodel.richard_model()
    write_data(wp,WestVerhulstData,WestGompertzData,WestRichadData,"Western")

    cmodel = Central(cp, k0, r_init)
    CentVerhulstData = cmodel.verhulst()
    CentGompertzData = cmodel.gompertz()
    CentRichardData = cmodel.richard()
    write_data(cp,CentVerhulstData,CentGompertzData,CentRichardData,"Central")

    gmodel = GreatAccra(gp, 6_000_000.00, r_init)
    GreatVerhulstData = gmodel.verhulst()
    GreatGompertzData = gmodel.gompertz()
    GreatRichardData = gmodel.richard()
    write_data(gp,GreatVerhulstData,GreatGompertzData,GreatRichardData,"GreaterAccra")

    vmodel = Volta(vp, k0, r_init)
    VoltaVerhulstData = vmodel.verhulst()
    VoltaGompertzData = vmodel.gompertz()
    VoltaRichardData = vmodel.richard()
    write_data(vp,VoltaVerhulstData,VoltaGompertzData,VoltaRichardData,"Volta")

    emodel = Eastern(ep, k0, r_init)
    EastVerhulstData = emodel.verhulst()
    EastGompertzData = emodel.gompertz()
    EastRichardData = emodel.richard()
    write_data(ep,EastVerhulstData,EastGompertzData,EastRichardData,"Eastern")

    amodel = Ashanti(ap, 6_000_000.00, r_init)
    AshVerhulstData = amodel.verhulst()
    AshGompertzData = amodel.gompertz()
    AshRichardData = amodel.richard()
    write_data(ap,AshVerhulstData,AshGompertzData,AshRichardData,"Ashanti")

    bmodel = BrongAhafo(bp, k0, r_init)
    BraVerhulstData = bmodel.verhulst()
    BraGompertzData = bmodel.gompertz()
    BraRichardData = bmodel.richard()
    write_data(bp,BraVerhulstData,BraGompertzData,BraRichardData,"BrongAhafo")

    nmodel = Northern(northp, k0, r_init)
    NorthVerhulstData = nmodel.verhulst()
    NorthGompertzData = nmodel.gompertz()
    NorthRichardData = nmodel.richard()
    write_data(northp, NorthVerhulstData,NorthGompertzData,NorthRichardData,"Northern")

    uemodel = UpperEast(uep, k0, r_init)
    UEDVerhulstData = uemodel.verhulst()
    UEDGompertzData = uemodel.gompertz()
    UEDRichardData = uemodel.richard()
    write_data(uep,UEDVerhulstData,UEDGompertzData,UEDRichardData,"UpperEast")

    uwmodel = UpperWest(uwp, k0, r_init)
    UWDVerhulstData = uwmodel.verhulst()
    UWDGompertzData = uwmodel.gompertz()
    UWDRichardData = uwmodel.richard()
    write_data(uwp,UWDVerhulstData,UWDGompertzData,UWDRichardData,"UpperWest")

if __name__ == "__main__":
    main()
