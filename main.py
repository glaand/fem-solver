from modules.mesh_cube import Mesh as CubeMesh
from modules.mesh_bar import Mesh as BarMesh
from modules.mesh_pyramid import Mesh as PyramidMesh
from modules.assembly import Assembly
from modules.solver import Solver

print("Linear, Simple 3D FEM Solver by André Glatzl")

mesh = PyramidMesh()
assembly = Assembly(mesh)
assembly.assemble_global_stiffness_matrix()
assembly.apply_boundary_conditions()
solver = Solver(assembly)
U = solver.solve()
U = assembly.solution_tensor_to_matrix(U)
print(U)