from functions import BigDataSolver

solver = BigDataSolver()
subject_coefficients = [0.1, 0.01, 0.5]
constraint_coefficients = [[0.05, 0.01, 0.15], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
constraint_bias = [1, 10, 25, 2]
solver.linear_programming(subject_coefficients, constraint_coefficients, constraint_bias)

