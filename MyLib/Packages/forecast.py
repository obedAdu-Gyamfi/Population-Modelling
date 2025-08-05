#!/usr/bin/python3

from .models import *
'''
def forecast(p0, k0, r0, theta, t, mode):
    mode = mode.lower()
    if mode == "verhulst":
        cast = VerhulstModel.model(p0, k0, r0, t)
    elif mode == "gompertz":
        cast = GompertzModel(p0, k0, r0, t)
    elif mode == "richard":
        cast = RichardModel(p0, k0, r0, t, theta)
    pass

'''
def forecast(**kwargs):
    for key , value in kwargs:
        print(f"{key} --> {value}")