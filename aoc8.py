program = []
with open("input/aoc8_input.txt", "r") as f:
	for line in f:
		instr = line.split()
		if instr[1][0] == "+":
			instr[1] = int(instr[1][1:])
		else:
			instr[1] = int(instr[1])
		program.append(instr)

pc = 0
acc = 0
execution_hit_count = [0] * len(program)
while pc < len(program) and pc >= 0:
	execution_hit_count[pc] += 1
	if execution_hit_count[pc] > 1:
		print(acc)
		break
	current_instr = program[pc]
	if current_instr[0] == "nop":
		pc += 1
		pass
	elif current_instr[0] == "acc":
		acc += current_instr[1]
		pc += 1
	else:
		pc += current_instr[1]