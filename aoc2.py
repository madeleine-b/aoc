
def part_one():
	num_valid_pws = 0
	with open("input/aoc2_input.txt", "r") as f:
		for line in f:
			policy, pw = line.split(":")
			letter = policy[-1]
			min_times = int(policy.split("-")[0])
			max_times = int(policy.split("-")[1].split()[0])
			if pw.count(letter) >= min_times and pw.count(letter) <= max_times:
				num_valid_pws += 1

	print(num_valid_pws)

def part_two():
	num_valid_pws = 0
	with open("input/aoc2_input.txt", "r") as f:
		for line in f:
			policy, pw = line.split(":")
			pw = pw.strip()
			letter = policy[-1]
			first_pos = int(policy.split("-")[0])
			second_pos = int(policy.split("-")[1].split()[0])
			if (pw[first_pos - 1] == letter) ^  (pw[second_pos - 1] == letter):
				num_valid_pws += 1

	print(num_valid_pws)

part_two()