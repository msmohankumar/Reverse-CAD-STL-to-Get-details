def analyze_geometry(mesh):

    bbox = mesh.bounding_box.extents

    return {
        "Vertices": len(mesh.vertices),
        "Faces": len(mesh.faces),
        "Volume_mm3": round(mesh.volume, 2),
        "Surface_Area_mm2": round(mesh.area, 2),
        "Length_mm": round(bbox[0], 2),
        "Width_mm": round(bbox[1], 2),
        "Height_mm": round(bbox[2], 2)
    }