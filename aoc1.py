data = []
with open("input/aoc1_input", "r") as f:
	data = f.readlines()
	data = [int(d.strip()) for d in data]

for i in range(len(data)):
	for j in range(i + 1, len(data)):
		if data[i] + data[j] == 2020:
			print(data[i]*data[j])
			quit()