def part_one():
	sum_yeses = 0
	with open("input/aoc6_input.txt", "r") as f:
		group = ""
		check_last_line = False
		for line in f:
			line = line.strip()
			if len(line) == 0:
				sum_yeses += len(set([c for c in group]))
				group = ""
				check_last_line = False
			else:
				group += line.strip()
				check_last_line = True
		if check_last_line:
			sum_yeses += len(set([c for c in group]))
	print(sum_yeses)

def part_two():
	sum_yeses = 0
	with open("input/aoc6_input.txt", "r") as f:
		group = []
		check_last_line = False
		for line in f:
			line = line.strip()
			if len(line) == 0:
				if len(group) == 1:
					sum_yeses += len(group[0])
				else:
					sum_yeses += len(group[0].intersection(*group[1:]))
				group = []
				check_last_line = False
			else:
				group.append(set([c for c in line.strip()]))
				check_last_line = True
		if check_last_line:
			sum_yeses += len(group[0].intersection(*group[1:]))

	print(sum_yeses)

