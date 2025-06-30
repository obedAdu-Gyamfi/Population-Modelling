#!/usr/bin/env python3
import numpy as np
from data import take_data

pis = np.array(take_data())    # flatten list, not a nested array
t = np.arange(len(pis))
p0 = pis[0]                    # initial population (scalar)
k = 3_000_000.0               # starting guess for carrying capacity
r = 0.1                        # better initial guess for r

def model(p0, k, r, t):
    A = (k - p0) / p0
    return (k * p0) / (p0 + (k - p0) * np.exp(-r * t))

def residuals(pis, t, k, r):
    return pis - model(p0, k, r, t)

def dk_drivative(p0, k, r, t):
    A = (k - p0) / p0
    exp_term = np.exp(-r * t)
    D = 1 + A * exp_term
    # df/dk
    return 1.0 / D - (k * exp_term / p0) / (D ** 2)

def dr_derivative(p0, k, r, t):
    A = (k - p0) / p0
    exp_term = np.exp(-r * t)
    D = 1 + A * exp_term
    # df/dr
    return (k * A * t * exp_term) / (D ** 2)

def jacobian(p0, k, r, t):
    return np.column_stack((dk_drivative(p0, k, r, t),
                            dr_derivative(p0, k, r, t)))

def mse(pis, t, k, r):
    res = residuals(pis, t, k, r)
    return np.mean(res**2)

max_iter = 100
for _ in range(max_iter):
    R = residuals(pis, t, k, r)
    J = jacobian(p0, k, r, t)
    A = J.T @ J
    lamb = 1e-3 * np.max(np.diag(A))  # adaptive damping
    B = J.T @ R

    # Solve (JᵀJ + λI) Δ = Jᵀ R
    delta = np.linalg.solve(A + lamb * np.eye(2), B)

    S = mse(pis, t, k, r)
    k_try, r_try = k + delta[0], r + delta[1]
    S_try = mse(pis, t, k_try, r_try)

    if S_try < S:
        k, r = k_try, r_try
        lamb /= 10
    else:
        lamb *= 10

    if abs(S - S_try) < 1e-6:
        break

print(f"Estimated carrying capacity (k): {k}")
print(f"Estimated growth rate (r): {r}")
