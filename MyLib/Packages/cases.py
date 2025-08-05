#!/usr/bin/env python3
"""
This is a class that contains the model for fitting the data
for each region
"""


import numpy as np
from .models import VerhulstModel, GompertzModel, RichardModel

class RegionClass:

    def __init__(self, p, k0=0, r_init=0, theta=1, model=""):
        self.p0 = p[0]
        self.p = p
        self.k0 = k0
        self.r_init = r_init
        self.theta = theta
        #self.t = np.arange(len(self.p))
        self.t = np.array((0,1,2.4,4,5))
        self.model = model
        

    def lmodel(self):
        try:
            if self.model == "verhulst":
                mymodel = VerhulstModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t
                    )
                mymodel.theta = 0
                #path = self.region + "_" + "verhulst.json"
            elif self.model == "gompertz":
                mymodel = GompertzModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t
                    )
                mymodel.theta = 0

                #path = self.region + " - " + "gompertz.json"
            elif self.model == "richard":
                mymodel = RichardModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t,
                    self.theta
                    )
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        mymodel.fit()
        data = mymodel.predict()
        params = {"k": mymodel.k, "r": mymodel.r, "theta": mymodel.theta}
        #p = np.array((self.p))
        return (data, params)
    
    def forecast(self, years):
        try:
            if self.model == "verhulst":
                mymodel = VerhulstModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t
                    )
                mymodel.theta = 0
            elif self.model == "gompertz":
                mymodel = GompertzModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t
                    )
                mymodel.theta = 0
            elif self.model == "richard":
                mymodel = RichardModel(
                    self.p,
                    self.p0,
                    self.k0,
                    self.r_init,
                    self.t,
                    self.theta
                    )
            mymodel.fit()
            return mymodel.fcast(years)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        