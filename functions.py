class BigDataSolver:

    def linear_programming(self, subject_coefficients, constraint_coefficients, constraint_bias, method="max"):
        import numpy as np
        import cvxpy as cp
        # variable numbers
        n = len(subject_coefficients)
        subject_coefficients = np.array(subject_coefficients)
        constraint_coefficients = np.array(constraint_coefficients)
        constraint_bias = np.array(constraint_bias)

        variables = cp.Variable(n, integer=True)
        if method == "max":
            objective = cp.Maximize(cp.sum(subject_coefficients * variables))

        # if all x > 0 then
        constraints = [0 <= variables, constraint_coefficients * variables <= constraint_bias]
        # else
        # constraints = [constraint_coefficients*variables <= constraint_bias]
        prob = cp.Problem(objective, constraints)

        results = prob.solve(solver=cp.CPLEX)

        print(prob.value)
        print(variables.value)


