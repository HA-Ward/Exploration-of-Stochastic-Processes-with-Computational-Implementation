import numpy as np

def brownian_motion(N, T, sigma = 1.0):
    dt = T/N
    Z = np.random.normal(0, 1, N)
    dB = sigma * np.sqrt(dt) * Z
    B = np.concatenate(([0], np.cumsum(dB)))   # B[0] = 0, B[i] = B(t_i)
    t = np.linspace(0, T, N + 1)
    return B, t

def simulate_brownian_paths(n_paths, n_steps, T, sigma = 1.0):
    dt = T/n_steps
    Z = np.random.normal(0, 1, size=(n_paths  ,n_steps))
    dB = sigma * np.sqrt(dt) * Z
    B = np.cumsum(dB, axis= 1)
    B = np.hstack([np.zeros((n_paths, 1)), B])
    t = np.linspace(0, T, n_steps + 1)
    return B, t

def simulate_brownian_ruin(dt, start, m, batch_size =1000, sigma = 1.0):
    walk_chunks = []
    first_chunk = True

    while True:
        Z = np.random.normal(0, 1, size=batch_size)
        dB = sigma * np.sqrt(dt) * Z
        B = np.concatenate(([0], np.cumsum(dB))) + start

        hit = np.where((B <= 0) | (B >= m))[0]

        chunk = B if first_chunk else B[1:]
        offset = 0 if first_chunk else 1

        if hit.size > 0:
            first_hit = hit[0]
            walk_chunks.append(B[: first_hit + 1][offset:])
            break
        else:
            walk_chunks.append(chunk)
            start = B[-1]
            first_chunk = False

    path = np.concatenate(walk_chunks)
    n = len(path)
    t = np.arange(n, dtype=float) * dt

    if n >= 2:
        x0, x1 = path[-2], path[-1]
        boundary = 0.0 if x1 <= 0 else m
        f = (boundary - x0) / (x1 - x0)
        path[-1] = boundary
        t[-1] = t[-2] + f * dt

    T = t[-1]
    return path, path[-1], T, t

def estimate_brownian_ruin(npaths, dt, start, m, batch_size =1000, sigma = 1.0):
    final_positions = []
    durations = []
    for i in range(npaths):
        path, finalp, T, t = simulate_brownian_ruin(dt, start, m, batch_size, sigma)
        final_positions.append(finalp)
        durations.append(T)
    return final_positions, durations

def run_for_n(args):
    n, dt, start, m = args
    final_positions, durations = estimate_brownian_ruin(n, dt, start, m)
    ratio = np.sum(np.array(final_positions) == 0) / n
    estimated_duration = np.mean(np.array(durations))
    return ratio, estimated_duration