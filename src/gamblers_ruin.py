import numpy as np

def gamblers_ruin(start, p, m):
    q = 1-p
    boundaryReached = False
    step_set = np.array([-1, 1])
    probs = np.array([q,p])
    random_walk = [start]
    while not boundaryReached:
        random_step = np.random.choice(step_set, p=probs)
        random_walk = np.append(random_walk, random_walk[-1] + random_step)
        if random_walk[-1] == 0 or random_walk[-1] == m:
            boundaryReached = True
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

