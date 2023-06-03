import numpy as np
from .elements.C3D8 import C3D8
from .materials.aluminium import Aluminium

class Mesh:
    nodes = np.array([
        #cube
        (0, 0, 0), # 0
        (1, 0, 0), # 1
        (0, 1, 0), # 2
        (1, 1, 0), # 3
        (0, 0, 1), # 4
        (1, 0, 1), # 5
        (0, 1, 1), # 6
        (1, 1, 1), # 7
    ])

    elements = [
        C3D8(nodes, [0, 1, 2, 3, 4, 5, 6, 7], Aluminium()),
    ]

    # Nodal forces boundary conditions
    boundary_conditions = [
        (0, 2, 0),  # Fixed at wall
        (1, 2, 0),  # Fixed at wall
        (3, 2, 0),  # Fixed at wall
        (4, 2, 0),  # Fixed at wall
        (2, 1, 200),  # Being pulled here
        (3, 1, 200), # Being pulled here
        (6, 1, 200), # Being pulled here 
        (7, 1, 200), # Being pulled here
    ]

    def get_nodes(self):
        return self.nodes
    
    def get_elements(self):
        return self.elements

    def get_triangles(self):
        triangles = []
        for element in self.elements:
            triangles.append(element.get_mapped_triangles())
        return np.array(triangles).reshape(-1, 3)
