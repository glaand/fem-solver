import numpy as np
from abc import ABC, abstractmethod, abstractproperty

class Element(ABC):
    material = None
    triangles = []
    local_nodes = []
    global_nodes = []
    node_map = []
    element_stiffness_matrix = []
    
    def __init__(self, global_nodes, node_map, material):
        self.global_nodes = global_nodes
        self.node_map = node_map
        self.material = material

    def get_local_nodes(self):
        return self.local_nodes
    
    def get_mapped_global_nodes(self):
        mapped_global_nodes = []
        for node_index in self.node_map:
            mapped_global_nodes.append(self.global_nodes[node_index])
        return mapped_global_nodes
    
    def get_mapped_triangles(self):
        triangles = []
        for triangle in self.triangles:
            mapped_triangle = []
            for node_index in triangle:
                mapped_triangle.append(self.node_map[node_index])
            triangles.append(mapped_triangle)
        return triangles
    
    def assemble_jacobian(self, dN):
        J = dN @ self.get_mapped_global_nodes()
        return J.T
    
    def assemble_local_stiffness_matrix(self):
        for gauss_point in self.gauss_points:
            xi, eta, zeta = gauss_point
            dN_math = self.shape_function_derivative(xi, eta, zeta)
            jacobian = self.assemble_jacobian(dN_math)
            dN_physical = np.linalg.inv(jacobian) @ dN_math
            B = self.assemble_B_matrix(dN_physical)
            self.element_stiffness_matrix += ((B.T @ self.material.elasticity_matrix) @ B) * np.linalg.det(jacobian)
        return self.element_stiffness_matrix
    
    @abstractmethod
    def shape_function(self, xi, eta, zeta):
        pass
    