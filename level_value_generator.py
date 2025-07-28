# Python version with json import of some P5JS code
# Mainly used to generate level values
import json

def generate_path_positions(columns, rows):
    return [[i, j] for i in range(columns) for j in range(rows)]

def remove_coords_from_paths(paths_array, removable_coords_list):
    return [coord for coord in paths_array if coord not in removable_coords_list]

# Grid size
columns = 15
rows = 15

# Coordinates to remove
removed_coords = [
  [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
  [0,1],[14,1],
  [0,2],[2,2],[3,2],[5,2],[7,2],[8,2],[10,2],[12,2],[14,2],
  [0,3],[4,3],[6,3],[9,3],[11,3],[13,3],[14,3],
  [0,4],[1,4],[2,4],[3,4],[4,4],[6,4],[7,4],[8,4],[10,4],[12,4],[13,4],[14,4],
  [6,5],[10,5],
  [0,6],[1,6],[2,6],[3,6],[5,6],[7,6],[8,6],[9,6],[11,6],[13,6],[14,6],
  [0,7],[4,7],[6,7],[12,7],[14,7],
  [0,8],[2,8],[3,8],[4,8],[5,8],[6,8],[8,8],[9,8],[10,8],[11,8],[13,8],[14,8],
  [0,9],[7,9],
  [0,10],[1,10],[2,10],[3,10],[4,10],[6,10],[8,10],[10,10],[12,10],[13,10],[14,10],
  [4,11],[10,11],
  [0,12],[1,12],[3,12],[5,12],[6,12],[8,12],[9,12],[11,12],[13,12],[14,12],
  [0,13],[2,13],[4,13],[7,13],[12,13],[14,13],
  [0,14],[1,14],[2,14],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14],[9,14],[10,14],[11,14],[12,14],[13,14],[14,14]
]  # Example: these won't appear in the final output

# Generate and filter paths
path_positions = generate_path_positions(columns, rows)
filtered_positions = remove_coords_from_paths(path_positions, removed_coords)

# Format as JSON string with square brackets and indentation
paths_json_snippet = json.dumps(filtered_positions, indent=2)

# Print the result
print('"paths": ' + paths_json_snippet)
