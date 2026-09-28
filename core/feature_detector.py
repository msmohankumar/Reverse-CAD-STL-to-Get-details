def detect_features(mesh):

    features = {}

    features["Vertices"] = len(mesh.vertices)
    features["Faces"] = len(mesh.faces)

    if len(mesh.faces) > 1000:
        complexity = "High"
    elif len(mesh.faces) > 300:
        complexity = "Medium"
    else:
        complexity = "Low"

    features["Complexity"] = complexity

    return features