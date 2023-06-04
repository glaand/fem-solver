import numpy as np
from .elements.C3D8 import C3D8
from .materials.aluminium import Aluminium

class Mesh:
    nodes = np.array([])

    elements = []

    # Nodal forces boundary conditions
    boundary_conditions = []

    def __init__(self):
        # Create 10x100x2 global nodes and connect them with local nodes inside elements
        global_nodes = []
        for i in range(10):
            for j in range(100):
                for k in range(2):
                    global_nodes.append([i, j, k])
        self.nodes = np.array(global_nodes)
        cubes = 1000
        print(global_nodes)

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
