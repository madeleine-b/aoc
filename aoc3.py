tree_map = []
with open("input/aoc3_input.txt", "r") as f:
	for line in f:
		line = line.strip()
		row = [1 if line[i] == "#" else 0 for i in range(len(line))]
		tree_map.append(row)

num_cols = len(tree_map[0])
prod = 1
for pair in iter([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]):
	col_increment = pair[0]
	row_increment = pair[1]
	num_trees = 0
	row_coord = 0
	col_coord = 0
	for row_coord in range(row_increment, len(tree_map), row_increment):
		col_coord = (col_coord + col_increment) % num_cols
		num_trees += tree_map[row_coord][col_coord]
	prod *= num_trees

print(prod)