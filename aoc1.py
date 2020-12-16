data = []
with open("input/aoc1_input", "r") as f:
	data = f.readlines()
	data = [int(d.strip()) for d in data]

def part_one():
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			if data[i] + data[j] == 2020:
				print(data[i]*data[j])
				return

def part_two():
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			for k in range(j + 1, len(data)):
				if data[i] + data[j] + data[k]== 2020:
					print(data[i]*data[j]*data[k])
					return 