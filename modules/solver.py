import numpy as np

class Solver:
    assembly = None
    def __init__(self, assembly):
        self.assembly = assembly

    def solve(self):
        print("Solving system of equations")
        print(f"K = {self.assembly.stiffness_matrix.shape}")
        print(f"F = {self.assembly.nodal_forces.shape}")
        K = self.assembly.stiffness_matrix
        F = self.assembly.nodal_forces
        U = np.linalg.solve(K, F)
        return U