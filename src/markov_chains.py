import numpy as np

def markov_chain(n_steps, states, transition_matrix, start_distribution):
    current_position = np.random.choice(states, p=start_distribution)
    path = np.array([current_position])
    for i in range(n_steps):
        current_position = np.random.choice(states, p=transition_matrix[current_position])
        path = np.append(path, current_position)
    return path

def generate_paths(n_chains, n_steps, states, transition_matrix, start_distribution):
    paths = []
    for i in range(n_chains):
        paths.append(markov_chain(n_steps, states, transition_matrix, start_distribution))
    return np.array(paths)

