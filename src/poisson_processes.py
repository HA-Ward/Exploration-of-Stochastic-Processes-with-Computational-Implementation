import numpy as np

def simulate_poisson_process(rate, T_max):
    t = 0
    p = 0
    position = [p]
    arrival_times = [t]
    while t < T_max:
        gap = np.random.exponential(scale=1/rate)  # exponential holding time
        t += gap
        if t < T_max:
            position.append(position[-1])
            arrival_times.append(t)

            position.append(position[-1]+1)
            arrival_times.append(t)
    position.append(position[-1])
    arrival_times.append(T_max)
    return (arrival_times, position)

def simulate_multi_processes(npaths, rate, T_max):
    paths = []
    for i in range(npaths):
        paths.append(simulate_poisson_process(rate, T_max))
    return paths