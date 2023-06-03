import numpy as np
from modules.mesh_bar import Mesh

class Assembly:
    node_shape = ()
    nodes = 0
    dof = 0
    stiffness_matrix = []
    nodal_forces = []

    def __init__(self, mesh: Mesh):
        self.mesh = mesh
        self.nodes, self.dof = mesh.get_nodes().shape
        self.stiffness_matrix = np.zeros((self.nodes * self.dof, self.nodes * self.dof))
        self.nodal_forces = np.zeros((self.nodes * self.dof, 1))

    def assemble_global_stiffness_matrix(self):
        print(f"Assembling global stiffness matrix...")
        for element in self.mesh.get_elements():
            Ke = element.assemble_local_stiffness_matrix()
            for i,I in enumerate(element.node_map):
                for j,J in enumerate(element.node_map):
                    self.stiffness_matrix[self.dof*I,self.dof*J]     += Ke[self.dof*i,self.dof*j]
                    self.stiffness_matrix[self.dof*I+1,self.dof*J]   += Ke[self.dof*i+1,self.dof*j]
                    self.stiffness_matrix[self.dof*I+2,self.dof*J]   += Ke[self.dof*i+2,self.dof*j]
                    self.stiffness_matrix[self.dof*I+2,self.dof*J+1] += Ke[self.dof*i+2,self.dof*j+1]
                    self.stiffness_matrix[self.dof*I+2,self.dof*J+2] += Ke[self.dof*i+2,self.dof*j+2]
                    self.stiffness_matrix[self.dof*I+1,self.dof*J+2] += Ke[self.dof*i+1,self.dof*j+2]
                    self.stiffness_matrix[self.dof*I+1,self.dof*J+1] += Ke[self.dof*i+1,self.dof*j+1]
                    self.stiffness_matrix[self.dof*I,self.dof*J+1]   += Ke[self.dof*i,self.dof*j+1]

        return self.stiffness_matrix
    
    def apply_boundary_conditions(self):
        print(f"Applying boundary conditions to {self.stiffness_matrix.shape[0]}x{self.stiffness_matrix.shape[1]} matrix")
        for boundary in self.mesh.boundary_conditions:
            node_index, dof1, dof2, dof3, value = boundary
            j = self.dof * node_index
            self.stiffness_matrix[j, :] = 0
            self.stiffness_matrix[j, j] = 1
            self.stiffness_matrix[j+1, :] = 0
            self.stiffness_matrix[j+1, j+1] = 1
            self.stiffness_matrix[j+2, :] = 0
            self.stiffness_matrix[j+2, j+2] = 1
            self.nodal_forces[j] = 0
            
            if dof1:
                self.nodal_forces[j] = value
            if dof2:
                self.nodal_forces[j+1] = value
            if dof3:
                self.nodal_forces[j+2] = value
            


    def solution_tensor_to_matrix(self, U):
        return np.reshape(U, (self.nodes, self.dof))
            