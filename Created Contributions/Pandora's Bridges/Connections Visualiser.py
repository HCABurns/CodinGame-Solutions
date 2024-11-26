# Relevant imports.
import matplotlib.pyplot as plt
import tests

# Select coordinates and connections from the 'tests.py' file.
#coordinates , connections = tests.test1()
coordinates , connections = tests.valid1()

# Extract x, y, z coordinates.
x, y, z = zip(*coordinates)

# Create a 3D plot.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot points.
ax.scatter(x, y, z, c='red', s=50, label='Points')

# Plot connections.
for connection in connections:
    u, v = connection
    x_vals = [coordinates[u][0], coordinates[v][0]]
    y_vals = [coordinates[u][1], coordinates[v][1]]
    z_vals = [coordinates[u][2], coordinates[v][2]]
    ax.plot(x_vals, y_vals, z_vals, c='blue', linewidth=1)

# Add labels to each point.
for idx, (px, py, pz) in enumerate(coordinates):
    ax.text(px, py, pz, idx, color='black')

# Set labels and title.
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_title('Minimum Spanning Tree Visual')

# Show plot.
plt.show()
