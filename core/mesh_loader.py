import trimesh

def load_mesh(file_path):
    mesh = trimesh.load(file_path)

    if isinstance(mesh, trimesh.Scene):
        mesh = mesh.dump(concatenate=True)

    return mesh