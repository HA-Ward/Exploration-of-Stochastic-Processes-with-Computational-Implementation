import numpy as np

def brownian_motion(N, T, sigma = 1.0):
    dt = T/N
    Z = np.random.normal(0, 1, N)
    dB = sigma * np.sqrt(dt) * Z
    B = np.concatenate(([0], np.cumsum(dB)))   # B[0] = 0, B[i] = B(t_i)
    t = np.linspace(0, T, N + 1)
    return B, t