import numpy as np

def random_walk(start, steps, p):
    q = 1-p
    step_set = np.array([-1,1])
    probs = np.array([q,p])
    random_steps = np.random.choice(step_set, steps, p=probs)

    return np.concatenate([[start], [start] + np.cumsum(random_steps)])

def simulate_random_walks(n_paths, start, steps, p):
    paths = []
    final_positions = []
    for i in range(n_paths):
        path = random_walk(start, steps, p)
        final_positions.append(path[-1])
        paths.append(path)
    return paths, final_positions


