import numpy as np
from modules.materials.material import Material

#https://www.mit.edu/~6.777/matprops/aluminum.htm
class Aluminium(Material):
    young_modulus = 70 # GPa
    poisson_ratio = 0.33
    density = 2700 # kg/m^3
    # isotropic - https://www.efunda.com/formulae/solid_mechanics/mat_mechanics/hooke_isotropic.cfm
    elasticity_matrix = (young_modulus / ((1 + poisson_ratio) * (1 - 2 * poisson_ratio))) * np.array([
        [(1 - poisson_ratio), poisson_ratio, poisson_ratio, 0, 0, 0],
        [poisson_ratio, (1 - poisson_ratio), poisson_ratio, 0, 0, 0],
        [poisson_ratio, poisson_ratio, (1 - poisson_ratio), 0, 0, 0],
        [0, 0, 0, 1 / 2 * (1 - 2 * poisson_ratio), 0, 0],
        [0, 0, 0, 0, 1 / 2 * (1 - 2 * poisson_ratio), 0],
        [0, 0, 0, 0, 0, 1 / 2 * (1 - 2 * poisson_ratio)],
    ])