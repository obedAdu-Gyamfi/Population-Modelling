#!/usr/bin/env python3
import numpy as np
from models import VerhulstModel, GompertzModel, RichardModel

class Western:
    def __init__(self, wp,k0,r_init):
        self.wp = wp
        self.k0 = k0
        self.r_init = r_init

        self.t = np.arange(len(wp))

    def verhulst_model(self):
        p0 = self.wp[0]
        model = VerhulstModel(self.wp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz_model(self):
        p0 = self.wp[0]
        model = GompertzModel(self.wp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard_model(self):
        p0 = self.wp[0]
        model = RichardModel(self.wp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class Central:
    def __init__(self, cp,k0,r_init):
        self.cp = cp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(cp))
    def verhulst(self):
        p0 = self.cp[0]
        model = VerhulstModel(self.cp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.cp[0]
        model = GompertzModel(self.cp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.cp[0]
        model = RichardModel(self.cp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class GreatAccra:
    def __init__(self, gp,k0,r_init):
        self.gp = gp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(gp))
    def verhulst(self):
        p0 = self.gp[0]
        model = VerhulstModel(self.gp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.gp[0]
        model = GompertzModel(self.gp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.gp[0]
        model = RichardModel(self.gp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class Volta:
    def __init__(self, vp,k0,r_init):
        self.vp = vp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(vp))
    def verhulst(self):
        p0 = self.vp[0]
        model = VerhulstModel(self.vp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.vp[0]
        model = GompertzModel(self.vp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.vp[0]
        model = RichardModel(self.vp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class Eastern:
    def __init__(self, ep,k0,r_init):
        self.ep = ep
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(ep))
    def verhulst(self):
        p0 = self.ep[0]
        model = VerhulstModel(self.ep, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.ep[0]
        model = GompertzModel(self.ep, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.ep[0]
        model = RichardModel(self.ep, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class Ashanti:
    def __init__(self, ap,k0,r_init):
        self.ap = ap
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(ap))
    def verhulst(self):
        p0 = self.ap[0]
        model = VerhulstModel(self.ap, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.ap[0]
        model = GompertzModel(self.ap, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.ap[0]
        model = RichardModel(self.ap, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class BrongAhafo:
    def __init__(self, bp,k0,r_init):
        self.bp = bp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(bp))
    def verhulst(self):
        p0 = self.bp[0]
        model = VerhulstModel(self.bp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.bp[0]
        model = GompertzModel(self.bp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.bp[0]
        model = RichardModel(self.bp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class Northern:
    def __init__(self, northp,k0,r_init):
        self.np = northp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(northp))

    def verhulst(self):
        p0 = self.np[0]
        model = VerhulstModel(self.np, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.np[0]
        model = GompertzModel(self.np, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.np[0]
        model = RichardModel(self.np, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class UpperEast:
    def __init__(self, uep,k0,r_init):
        self.uep = uep
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(uep))
    def verhulst(self):
        p0 = self.uep[0]
        model = VerhulstModel(self.uep, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.uep[0]
        model = GompertzModel(self.uep, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.uep[0]
        model = RichardModel(self.uep, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
class UpperWest:
    def __init__(self, uwp,k0,r_init):
        self.uwp = uwp
        self.k0 = k0
        self.r_init = r_init
        self.t = np.arange(len(uwp))
    def verhulst(self):
        p0 = self.uwp[0]
        model = VerhulstModel(self.uwp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def gompertz(self):
        p0 = self.uwp[0]
        model = GompertzModel(self.uwp, p0, self.k0, self.r_init, self.t)
        model.fit()
        data = model.predict()
        return data
    def richard(self):
        p0 = self.uwp[0]
        model = RichardModel(self.uwp, p0, self.k0, self.r_init, self.t, theta=1.0)
        model.fit()
        data = model.predict()
        return data
