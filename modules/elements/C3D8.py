# https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node26.html
import numpy as np
from .element import Element

class C3D8(Element):
    local_nodes = np.array([
        (-1, -1, -1), # 0
        ( 1, -1, -1), # 1
        (-1,  1, -1), # 2
        ( 1,  1, -1), # 3
        (-1, -1,  1), # 4
        ( 1, -1,  1), # 5
        (-1,  1,  1), # 6
        ( 1,  1,  1)  # 7
    ])

    triangles = np.array([
        (0,1,2), #1
        (1,3,2), #2
        (4,6,7), #3
        (4,5,7), #4
        (3,5,7), #5
        (3,1,5), #6
        (0,1,4), #7
        (1,4,5), #8
        (2,6,7), #9
        (2,3,7), #10
        (0,2,6), #11
        (0,4,6)  #12
    ])

    gauss_points = np.array([
        (-0.577350269189626, -0.577350269189626, -0.577350269189626),
        ( 0.577350269189626, -0.577350269189626, -0.577350269189626),
        (-0.577350269189626,  0.577350269189626, -0.577350269189626),
        ( 0.577350269189626,  0.577350269189626, -0.577350269189626),
        (-0.577350269189626, -0.577350269189626,  0.577350269189626),
        ( 0.577350269189626, -0.577350269189626,  0.577350269189626),
        (-0.577350269189626,  0.577350269189626,  0.577350269189626),
        ( 0.577350269189626,  0.577350269189626,  0.577350269189626)
    ])

    element_stiffness_matrix = np.zeros((24, 24))

    def shape_function(self, xi, eta, zeta):
        # Grenzen -1 bis 1, damit Gauss-Quadratur funktioniert
        N = 1/8 * np.array([
            (1-xi)*(1-eta)*(1-zeta),
            (1+xi)*(1-eta)*(1-zeta),
            (1-xi)*(1+eta)*(1-zeta),
            (1+xi)*(1+eta)*(1-zeta),
            (1-xi)*(1-eta)*(1+zeta),
            (1+xi)*(1-eta)*(1+zeta),
            (1-xi)*(1+eta)*(1+zeta),
            (1+xi)*(1+eta)*(1+zeta)
        ])
        return N
    
    def shape_function_derivative(self, xi, eta, zeta):
        dNdxi = np.array([
            -(1-eta)*(1-zeta),
            (1-eta)*(1-zeta),
            -(1+eta)*(1-zeta),
            (1+eta)*(1-zeta),
            -(1-eta)*(1+zeta),
            (1-eta)*(1+zeta),
            -(1+eta)*(1+zeta),
            (1+eta)*(1+zeta)
        ])
        dNdeta = np.array([
            -(1-xi)*(1-zeta),
            -(1+xi)*(1-zeta),
            (1-xi)*(1-zeta),
            (1+xi)*(1-zeta),
            -(1-xi)*(1+zeta),
            -(1+xi)*(1+zeta),
            (1-xi)*(1+zeta),
            (1+xi)*(1+zeta)
        ])
        dNdzeta = np.array([
            -(1-xi)*(1-eta),
            -(1+xi)*(1-eta),
            -(1-xi)*(1+eta),
            -(1+xi)*(1+eta),
            (1-xi)*(1-eta),
            (1+xi)*(1-eta),
            (1-xi)*(1+eta),
            (1+xi)*(1+eta)
        ])

        dN = np.array([dNdxi, dNdeta, dNdzeta])

        return (1/8) * dN
    
    def assemble_B_matrix(self, dN):
        B = np.zeros((6, 24))
        for i in range(len(self.local_nodes)):
            B[0, 3*i] = dN[0, i]
            B[1, 3*i+1] = dN[1, i]
            B[2, 3*i+2] = dN[2, i]
            B[3, 3*i] = dN[1, i]
            B[3, 3*i+1] = dN[0, i]
            B[4, 3*i+1] = dN[2, i]
            B[4, 3*i+2] = dN[1, i]
            B[5, 3*i] = dN[2, i]
            B[5, 3*i+2] = dN[0, i]
        return B