import copy

original_program = []
with open("input/aoc8_input.txt", "r") as f:
	for line in f:
		instr = line.split()
		if instr[1][0] == "+":
			instr[1] = int(instr[1][1:])
		else:
			instr[1] = int(instr[1])
		original_program.append(instr)

# Returns the value of |acc| iff it terminated normally
# Else -1
def execute_modified_program(program):
	pc = 0
	acc = 0
	execution_hit_count = [0] * len(program)
	while pc < len(program) and pc >= 0:
		execution_hit_count[pc] += 1
		if execution_hit_count[pc] > 1:
			return -1
		current_instr = program[pc]
		if current_instr[0] == "nop":
			pc += 1
		elif current_instr[0] == "acc":
			acc += current_instr[1]
			pc += 1
		else:
			pc += current_instr[1]
	return acc


for i in range(len(original_program)):
	if original_program[i][0] == "acc":
		continue
	modified_program = copy.deepcopy(original_program)
	modified_program[i][0] = "jmp" if modified_program[i][0] == "nop" else "nop"
	ret = execute_modified_program(modified_program)
	if ret != -1:
		print(ret)
		break
