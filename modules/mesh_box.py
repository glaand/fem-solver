import numpy as np
from .elements.C3D8 import C3D8
from .materials.aluminium import Aluminium
from collections import OrderedDict

class Mesh:
    nodes = []

    elements = []

    # Nodal forces boundary conditions
    boundary_conditions = []
    GRID_SIZE_X = 21
    GRID_SIZE_Y = 21
    GRID_SIZE_Z = 21


    def __init__(self):
        i = 0
        for z in range(self.GRID_SIZE_X):
            for y in range(self.GRID_SIZE_Y):
                for x in range(self.GRID_SIZE_Z):
                    #if not (x == 0 or x == self.GRID_SIZE_X - 2 or y == 0 or y == self.GRID_SIZE_X - 2):
                    #    continue
                    self.nodes.append([x, y, z])

        self.nodes = np.array(self.nodes)
        
        for z in range(self.GRID_SIZE_X-1):
            for y in range(self.GRID_SIZE_Y-1):
                for x in range(self.GRID_SIZE_Z-1):
                    node_down_top_left = x + y * self.GRID_SIZE_X + z * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_down_top_right = x + 1 + y * self.GRID_SIZE_X + z * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_down_bottom_left = x + (y + 1) * self.GRID_SIZE_X + z * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_down_bottom_right = x + 1 + (y + 1) * self.GRID_SIZE_X + z * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_up_top_left = x + y * self.GRID_SIZE_X + (z + 1) * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_up_top_right = x + 1 + y * self.GRID_SIZE_X + (z + 1) * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_up_bottom_left = x + (y + 1) * self.GRID_SIZE_X + (z + 1) * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    node_up_bottom_right = x + 1 + (y + 1) * self.GRID_SIZE_X + (z + 1) * self.GRID_SIZE_X * self.GRID_SIZE_Y
                    #if not (x == 0 or x == self.GRID_SIZE_X - 2 or y == 0 or y == self.GRID_SIZE_X - 2):
                    #    continue
                    self.elements.append(
                        C3D8(
                        self.nodes,
                        [
                            node_down_top_left,
                            node_down_top_right,
                            node_down_bottom_left,
                            node_down_bottom_right,
                            node_up_top_left,
                            node_up_top_right,
                            node_up_bottom_left,
                            node_up_bottom_right
                        ], 
                        Aluminium())
                    )

                    if x == 0:
                        self.boundary_conditions.append((node_down_top_left, False, False, False, 0))
                        self.boundary_conditions.append((node_down_bottom_left, False, False, False, 0))
                        self.boundary_conditions.append((node_up_top_left, False, False, False, 0))
                        self.boundary_conditions.append((node_up_bottom_left, False, False, False, 0))
                    if x == self.GRID_SIZE_X - 2:
                        self.boundary_conditions.append((node_down_top_right, True, False, False, -5))
                        self.boundary_conditions.append((node_down_bottom_right, True, False, False, -5))
                        self.boundary_conditions.append((node_up_top_right, True, False, False, -5))
                        self.boundary_conditions.append((node_up_bottom_right, True, False, False, -5))

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
    
    def get_faces(self):
        faces = []
        for triangle in self.get_triangles():
            faces.append([3, triangle[0], triangle[1], triangle[2]])
        return faces
    
    def set_displacements(self, displacements):
        self.displacements = displacements

    def get_displaced_nodes(self):
        return self.nodes + self.displacements
