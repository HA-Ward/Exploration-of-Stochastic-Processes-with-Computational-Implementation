import numpy as np

def gamblers_ruin(start, p, m, batch_size=1000):
    q = 1 - p
    step_set = np.array([-1, 1])
    probs = np.array([q, p])

    position = start
    walk_chunks = [np.array([start])]

    while True:
        steps = np.random.choice(step_set, size=batch_size, p=probs)
        path = position + np.cumsum(steps)

        hit = np.where((path == 0) | (path == m))[0]

        if hit.size > 0:
            first_hit = hit[0]
            walk_chunks.append(path[:first_hit + 1])
            break
        else:
            walk_chunks.append(path)
            position = path[-1]

    random_walk = np.concatenate(walk_chunks)
    return random_walk, random_walk[-1], len(random_walk) - 1

def simulate_gamblers_ruin(n_paths, start, p, m):
    paths = []
    final_positions = []
    steps_taken = []
    for i in range(n_paths):
        walk, finalp, steps = gamblers_ruin(start, p, m)
        paths.append(walk)
        final_positions.append(finalp)
        steps_taken.append(steps)
    return paths, final_positions, steps_taken

def run_for_n(args):
    n, start, p, m = args
    final_positions = simulate_gamblers_ruin(n, start, p, m)[1]
    ratio = np.sum(np.array(final_positions) == 0) / n
    return ratio

def exact_duration_pmf(a, m, p, n_max):
    q = 1 - p
    probs = np.zeros(m+1)      # probability of being at each position
    probs[a] = 1.0
    pmf = np.zeros(n_max)      # P(absorbed at exactly step n)

    for n in range(1, n_max+1):
        new_probs = np.zeros(m+1)
        for i in range(1, m):          # only transient states move
            new_probs[i+1] += probs[i]*p
            new_probs[i-1] += probs[i]*q
        # mass that just landed on 0 or m this step = newly absorbed
        pmf[n-1] = new_probs[0] + new_probs[m]
        new_probs[0] = 0     # remove absorbed mass so it doesn't move again
        new_probs[m] = 0
        probs = new_probs

    return pmf

