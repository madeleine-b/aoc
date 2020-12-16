highest_id = 818
seats_taken = [0] * (highest_id + 1)
num_rows = 128

with open ("input/aoc5_input.txt", "r") as f:
	for boarding_pass in f:
		row = int(''.join(["0" if boarding_pass[i] == "F" else "1" for i in range(0, 7)]), 2)
		col = int(''.join(["0" if boarding_pass[i] == "L" else "1" for i in range(7, 10)]), 2)
		seat_id = row * 8 + col
		seats_taken[seat_id] = 1
		
for i in range(0, len(seats_taken) - 2):
	if seats_taken[i] == 1 and seats_taken[i + 1] == 0 and seats_taken[i + 2] == 1:
		print("candidate id", i + 1)
