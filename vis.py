import numpy as np
import open3d as o3d

# Load the original PLY file
ply_file = "3dgs_pc.ply"
point_cloud = o3d.io.read_point_cloud(ply_file)

# Convert the points to a NumPy array
points = np.asarray(point_cloud.points)
print(points.shape)

k = 10000000
subset_points = points[:k, :]

subset_point_cloud = o3d.geometry.PointCloud()
subset_point_cloud.points = o3d.utility.Vector3dVector(subset_points)

if point_cloud.has_colors():
    colors = np.asarray(point_cloud.colors)
    subset_colors = colors[:k, :]  # Modify to match the sampling method
    subset_point_cloud.colors = o3d.utility.Vector3dVector(subset_colors)

if point_cloud.has_normals():
    normals = np.asarray(point_cloud.normals)
    subset_normals = normals[:k, :]  # Modify to match the sampling method
    subset_point_cloud.normals = o3d.utility.Vector3dVector(subset_normals)

vis = o3d.visualization.Visualizer()
vis.create_window()

vis.add_geometry(subset_point_cloud)

render_option = vis.get_render_option()
render_option.background_color = [0, 0, 0]  # Black background

vis.run()
vis.destroy_window()
