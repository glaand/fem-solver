import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from modules.mesh_cube import Mesh as CubeMesh
from modules.mesh_bar import Mesh as BarMesh
from modules.mesh_pyramid import Mesh as PyramidMesh
from modules.assembly import Assembly
from modules.solver import Solver

mesh = PyramidMesh()
x, y, z = mesh.get_nodes().T
i, j, k = mesh.get_triangles().T

mesh_data_without_displacements = go.Mesh3d(x=x, y=y, z=z, alphahull=5, opacity=1, color='cyan', i=i, j=j, k=k)

data = [
    mesh_data_without_displacements
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
