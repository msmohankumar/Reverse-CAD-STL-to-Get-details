import plotly.graph_objects as go

def show_mesh(mesh):

    vertices = mesh.vertices
    faces = mesh.faces

    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=vertices[:,0],
                y=vertices[:,1],
                z=vertices[:,2],
                i=faces[:,0],
                j=faces[:,1],
                k=faces[:,2]
            )
        ]
    )

    return fig