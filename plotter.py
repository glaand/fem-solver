import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from modules.mesh_cube import Mesh as CubeMesh
from modules.mesh_bar import Mesh as BarMesh
from modules.assembly import Assembly
from modules.solver import Solver

mesh = BarMesh()
x, y, z = mesh.get_nodes().T
i, j, k = mesh.get_triangles().T

mesh_data_without_displacements = go.Mesh3d(x=x, y=y, z=z, alphahull=5, opacity=0.2, color='cyan', i=i, j=j, k=k)

# Displacement figure
assembly = Assembly(mesh)
assembly.assemble_global_stiffness_matrix()
assembly.apply_boundary_conditions()
solver = Solver(assembly)
U = solver.solve()
U = assembly.solution_tensor_to_matrix(U)
mesh.set_displacements(U)

nx, ny, nz = mesh.get_displaced_nodes().T
mesh_data_with_displacements = go.Mesh3d(x=nx, y=ny, z=nz, alphahull=5, opacity=1, color='red', i=i, j=j, k=k)

# Boundary figure
boundary_points = []
force_points = []
for boundary in mesh.boundary_conditions:
    node = mesh.get_nodes()[boundary[0]]
    if boundary[4] == 0:
        boundary_points.append(node)
    else:
        force_points.append(node)

boundary_points = np.array(boundary_points)
force_points = np.array(force_points)

bx, by, bz = boundary_points.T
boundary_data = go.Scatter3d(x=bx, y=by, z=bz, mode='markers', marker=dict(size=15, color='black'))
fx, fy, fz = force_points.T
force_data = go.Scatter3d(x=fx, y=fy, z=fz, mode='markers', marker=dict(size=15, color='red'))

data = [
    mesh_data_without_displacements,
    boundary_data,
    force_data,
    mesh_data_with_displacements
]

fig = go.Figure(
    data=data,
    layout=go.Layout(
        scene=dict(
            aspectmode="data",  # Keep aspect ratio based on data values
            aspectratio=dict(x=1, y=1, z=1)  # Adjust aspect ratio as needed
        )
    )
)

fig.show()
