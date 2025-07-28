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
removed_coords = [[7, 0], [7, 1], [7, 2], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 13], [7, 14], [0, 7], [1, 7], [2, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [10, 7], [11, 7], [13, 7], [14, 7],]  # Example: these won't appear in the final output

# Generate and filter paths
path_positions = generate_path_positions(columns, rows)
filtered_positions = remove_coords_from_paths(path_positions, removed_coords)

# Format as JSON string with square brackets and indentation
paths_json_snippet = json.dumps(filtered_positions, indent=2)

# Print the result
print('"paths": ' + paths_json_snippet)
