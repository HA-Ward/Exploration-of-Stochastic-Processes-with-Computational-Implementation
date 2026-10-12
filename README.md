# Exploration of Stochastic Processes with Computational Implementation

This project explores a sequence of stochastic processes, comparing analytical results with Monte Carlo simulation in Python. Each section derives the theory, implements it computationally, and checks that the two agree.

Random walks. I derive the expectation and variance of a simple random walk and test them against simulations of different sizes. The mean converges quickly, while the variance is far more sensitive to extreme paths at small sample sizes.

Gambler’s ruin. I solve for the probability of ruin and the expected duration using difference equations, then validate both by simulation. Two findings stood out. First, the simulated ruin ratio fluctuates around the true value at a scale set by the standard error, which shrinks only like 1/√n. Second, expected duration can be a misleading summary: by computing the exact duration distribution, I show cases where the mean falls in a region where the game rarely ends.

Markov chains. I reformulate gambler’s ruin using transition matrices, which gives the full duration distribution directly. I also verify convergence to the stationary distribution of a three-state chain.

Poisson processes. I simulate Poisson processes from both of their definitions (exponential waiting times and Poisson increments) and verify the distribution of counts and the superposition property.

Brownian motion. I simulate Brownian motion as a Gaussian random walk on a discretised time grid, validate its mean, variance and density over time, and connect the spreading of the density to the diffusion equation. I then solve the continuous gambler’s ruin problem using martingales and optional stopping, and confirm the results by simulation.

The full write-up is in the PDF, and the code used to generate every figure is in this repository.
