import numpy as np
from .elements.C3D8 import C3D8
from .materials.aluminium import Aluminium

class Mesh:
    nodes = np.array([
        (0, 0, 0), # 0
        (1, 0, 0), # 1
        (2, 0, 0), # 2
        (0, 1, 0), # 3
        (1, 1, 0), # 4
        (2, 1, 0), # 5
        (0, 2, 0), # 6
        (1, 2, 0), # 7
        (2, 2, 0), # 8
        (0, 3, 0), # 9
        (1, 3, 0), # 10
        (2, 3, 0), # 11
        (0, 0, 1), # 12
        (1, 0, 1), # 13
        (2, 0, 1), # 14
        (0, 1, 1), # 15
        (1, 1, 1), # 16
        (2, 1, 1), # 17
        (0, 2, 1), # 18
        (1, 2, 1), # 19
        (2, 2, 1), # 20
        (0, 3, 1), # 21
        (1, 3, 1), # 22
        (2, 3, 1), # 23
        (0, 0, 2), # 24
        (1, 0, 2), # 25
        (2, 0, 2), # 26
        (0, 1, 2), # 27
        (1, 1, 2), # 28
        (2, 1, 2), # 29
        (0, 2, 2), # 30
        (1, 2, 2), # 31
        (2, 2, 2), # 32
        (0, 3, 2), # 33
        (1, 3, 2), # 34
        (2, 3, 2), # 35
    ])

    elements = [
        C3D8(nodes, [0, 1, 3, 4, 12, 13, 15, 16], Aluminium()),
        C3D8(nodes, [1, 2, 4, 5, 13, 14, 16, 17], Aluminium()),
        C3D8(nodes, [3, 4, 6, 7, 15, 16, 18, 19], Aluminium()),
        C3D8(nodes, [4, 5, 7, 8, 16, 17, 19, 20], Aluminium()),
        C3D8(nodes, [6, 7, 9, 10, 18, 19, 21, 22], Aluminium()),
        C3D8(nodes, [7, 8, 10, 11, 19, 20, 22, 23], Aluminium()),
        C3D8(nodes, [12, 13, 15, 16, 24, 25, 27, 28], Aluminium()),
        C3D8(nodes, [13, 14, 16, 17, 25, 26, 28, 29], Aluminium()),
        C3D8(nodes, [15, 16, 18, 19, 27, 28, 30, 31], Aluminium()),
        C3D8(nodes, [16, 17, 19, 20, 28, 29, 31, 32], Aluminium()),
        C3D8(nodes, [18, 19, 21, 22, 30, 31, 33, 34], Aluminium()),
        C3D8(nodes, [19, 20, 22, 23, 31, 32, 34, 35], Aluminium()),
    ]

    # Nodal forces boundary conditions
    boundary_conditions = [
        # node, dof1, dof2, dof3, value
        (0, False, False, False, 0),  # Fixed at wall
        (1, False, False, False, 0),  # Fixed at wall
        (2, False, False, False, 0),  # Fixed at wall
        (12, False, False, False, 0), # Fixed at wall
        (13, False, False, False, 0), # Fixed at wall
        (14, False, False, False, 0), # Fixed at wall
        (24, False, False, False, 0), # Fixed at wall
        (25, False, False, False, 0), # Fixed at wall
        (26, False, False, False, 0), # Fixed at wall
        (9, False, True, False, 1),  # Being pulled here (only in y-direction)
        (10, False, True, False, 1), # Being pulled here (only in y-direction)
        (11, False, True, False, 1), # Being pulled here (only in y-direction)
        (21, False, True, False, 1), # Being pulled here (only in y-direction)
        (22, False, True, False, 1), # Being pulled here (only in y-direction)
        (23, False, True, False, 1), # Being pulled here (only in y-direction)
        (33, False, True, False, 1), # Being pulled here (only in y-direction)
        (34, False, True, False, 1), # Being pulled here (only in y-direction)
        (35, False, True, False, 1), # Being pulled here (only in y-direction)
    ]

    displacements = []

    def get_nodes(self):
        return self.nodes
    
    def get_elements(self):
        return self.elements

    def get_triangles(self):
        triangles = []
        for element in self.elements:
            triangles.append(element.get_mapped_triangles())
        return np.array(triangles).reshape(-1, 3)
    
    def set_displacements(self, displacements):
        self.displacements = displacements

    def get_displaced_nodes(self):
        return self.nodes + self.displacements
