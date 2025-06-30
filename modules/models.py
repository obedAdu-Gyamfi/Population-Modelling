#!/usr/bin/env python3
import numpy as np

class VerhulstModel:

    def __init__(self, pis, p0, k, r, t):
        self.pis = pis
        self.p0 = p0
        self.k = float(k)
        self.r = float(r)
        self.t = t

    def model(self, k=None, r=None):
        k = self.k if k is None else k
        r = self.r if r is None else r
        A = (k - self.p0) / self.p0
        exp_term = np.exp(-r * self.t)
        return k / (1 + A * exp_term)

    def residuals(self, k=None, r=None):
        return self.pis - self.model(k, r)

    def dk_derivative(self):
        A = (self.k - self.p0) / self.p0
        exp_term = np.exp(-self.r * self.t)
        D = 1 + A * exp_term
        return 1.0 / D - (self.k * exp_term / self.p0) / (D ** 2)

    def dr_derivative(self):
        A = (self.k - self.p0) / self.p0
        exp_term = np.exp(-self.r * self.t)
        D = 1 + A * exp_term
        return (self.k * A * self.t * exp_term) / (D ** 2)

    def jacobian(self):
        return np.column_stack((self.dk_derivative(), self.dr_derivative()))

    def mse(self, k=None, r=None):
        res = self.residuals(k, r)
        return np.mean(res**2)

    def fit(self, max_iter=100, tol=1e-6):
        for _ in range(max_iter):
            R = self.residuals()
            J = self.jacobian()
            A_mat = J.T @ J
            lamb = 1e-3 * np.max(np.diag(A_mat))
            B = J.T @ R

            delta = np.linalg.solve(A_mat + lamb * np.eye(2), B)
            S_old = self.mse()
            k_trial = self.k + delta[0]
            r_trial = self.r + delta[1]
            S_new = self.mse(k_trial, r_trial)

            if S_new < S_old:
                self.k, self.r = k_trial, r_trial
                lamb /= 10
            else:
                lamb *= 10

            if abs(S_new - S_old) < tol:
                break

    def predict(self):
        est_p = self.model()
        return est_p.astype(int).tolist()
    

class GompertzModel:

    def __init__(self, pis, p0, k, r, t):
        self.pis = pis
        self.p0 = p0
        self.k = float(k)
        self.r = float(r)
        self.t = t

    def model(self, k=None, r=None):
        k = self.k if k is None else k
        r = self.r if r is None else r
        return (k*np.exp(np.exp(-r * self.t)*np.log(self.p0/k)))

    def residuals(self, k=None, r=None):
        return self.pis - self.model(k, r)

    def dk_derivative(self):
        exp_term = np.exp(np.log(self.p0/self.k)*np.exp(-self.r * self.t))
        other_term = (1 - np.exp(-self.r * self.t))
        return (exp_term * other_term)
    def dr_derivative(self):
        exp_term = (-self.k*self.t*np.exp(-self.r * self.t)*np.log(self.p0/self.k))
        other_term = np.exp(np.log(self.p0/self.k)*np.exp(-self.r * self.t))
        return (exp_term * other_term)
    def jacobian(self):
        return np.column_stack((self.dk_derivative(), self.dr_derivative()))

    def mse(self, k=None, r=None):
        res = self.residuals(k, r)
        return np.mean(res**2)

    def fit(self, max_iter=100, tol=1e-6):
        for _ in range(max_iter):
            R = self.residuals()
            J = self.jacobian()
            A_mat = J.T @ J
            lamb = 1e-3 * np.max(np.diag(A_mat))
            B = J.T @ R

            delta = np.linalg.solve(A_mat + lamb * np.eye(2), B)
            S_old = self.mse()
            k_trial = self.k + delta[0]
            r_trial = self.r + delta[1]
            S_new = self.mse(k_trial, r_trial)

            if S_new < S_old:
                self.k, self.r = k_trial, r_trial
                lamb /= 10
            else:
                lamb *= 10

            if abs(S_new - S_old) < tol:
                break

    def predict(self):
        est_p = self.model()
        return est_p.astype(int).tolist()
import numpy as np

class RichardModel:
    def __init__(self, pis, p0, k, r, t, theta):
        self.pis = np.array(pis, dtype=float)
        self.p0 = float(p0)
        self.k = float(k)
        self.r = float(r)
        self.t = np.array(t, dtype=float)
        self.theta = float(theta)

    def model(self, k=None, r=None, theta=None):
        # Allow trial values for fitting
        K = self.k if k is None else k
        R = self.r if r is None else r
        TH = self.theta if theta is None else theta

        Q = (K / self.p0)**TH - 1
        return K / (1 + Q * np.exp(-R * TH * self.t))**(1/TH)

    def dk_derivative(self):
        K, R, T = self.k, self.r, self.theta
        t = self.t; p0 = self.p0
        Q = (K/p0)**T - 1
        E = np.exp(-R*T*t)
        B = (1 + Q*E)
        D = B**(1/T)
        # Partial derivative wrt K
        dQ_dK = T*(K/p0)**(T-1) / p0
        dB_dK = dQ_dK * E
        dD_dK = (1/T) * B**(1/T - 1) * dB_dK
        return (1 / D) - K * dD_dK / D**2

    def dr_derivative(self):
        K, R, T = self.k, self.r, self.theta
        t = self.t; p0 = self.p0
        Q = (K/p0)**T - 1
        E = np.exp(-R*T*t)
        B = (1 + Q*E)
        D = B**(1/T)
        dB_dR = -Q * T * t * E
        dD_dR = (1/T) * B**(1/T - 1) * dB_dR
        return -K * dD_dR / D**2

    def dtheta(self):
        K, R, T = self.k, self.r, self.theta
        t = self.t; p0 = self.p0
        Q = (K/p0)**T - 1
        E = np.exp(-R*T*t)
        B = 1 + Q * E
        D = B**(1/T)
        p = K / D

        # Partial derivatives
        dQ_dT = (K/p0)**T * np.log(K/p0)
        dB_dT = dQ_dT*E - Q*R*t*E

        # dD/dT terms:
        term1 = -np.log(B) / T**2
        term2 = (1/T)*(dB_dT / B)
        dD_dT = D * (term1 + term2)

        return -K * dD_dT / D**2

    def residuals(self, k=None, r=None, theta=None):
        return self.pis - self.model(k, r, theta)

    def jacobian(self):
        return np.column_stack((
            self.dk_derivative(),
            self.dr_derivative(),
            self.dtheta()
        ))

    def mse(self, k=None, r=None, theta=None):
        return np.mean(self.residuals(k, r, theta)**2)

    def fit(self, max_iter=100, tol=1e-6):
        for _ in range(max_iter):
            R = self.residuals()
            J = self.jacobian()
            A = J.T @ J
            lamb = 1e-3 * np.max(np.diag(A))
            Bv = J.T @ R
            delta = np.linalg.solve(A + lamb * np.eye(3), Bv)

            old_mse = self.mse()
            k_t, r_t, th_t = self.k + delta[0], self.r + delta[1], self.theta + delta[2]
            new_mse = self.mse(k_t, r_t, th_t)

            if new_mse < old_mse:
                self.k, self.r, self.theta = k_t, r_t, th_t
            lamb *= 0.1 if new_mse < old_mse else 10.0

            if abs(old_mse - new_mse) < tol:
                break

    def predict(self):
        est = self.model()
        return est.astype(int).tolist()
