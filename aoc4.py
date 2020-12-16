import re

def has_all_fields(passport):
	required_keys = "byr iyr eyr hgt hcl ecl pid".split()
	passport = passport.split()
	for entry in required_keys:
		found_entry = False
		for data in passport:
			if data.split(":")[0] == entry:
				found_entry = True
				break
		if not found_entry:
			return False
	return True

def validate_string_in_yr_range(year_str, min_yr, max_yr):
	try:
		year = int(year_str)
		if year < min_yr or year > max_yr:
			return False
	except ValueError:
		return False
	return True

def is_valid_passport(passport):
	if not has_all_fields(passport):
		return False
	required_keys = "byr iyr eyr hgt hcl ecl pid".split()
	passport = passport.split()
	for data in passport:
		entry = data.split(":")
		entry[1] = entry[1].strip()
		if entry[0] == "byr":
			if not validate_string_in_yr_range(entry[1], 1920, 2002):
				return False
		if entry[0] == "iyr":
			if not validate_string_in_yr_range(entry[1], 2010, 2020):
				return False
		if entry[0] == "eyr":
			if not validate_string_in_yr_range(entry[1], 2020, 2030):
				return False
		if entry[0] == "hgt":
			unit =  entry[1][-2:]
			if unit == "in":
				try:
					num = int(entry[1][0:-2])
					if num < 59 or num > 76:
						return False
				except ValueError:
					return False
			elif unit == "cm":
				try:
					num = int(entry[1][0:-2])
					if num < 150 or num > 193:
						return False
				except ValueError:
					return False
			else:
				return False
		if entry[0] == "hcl":
			if not re.search("#([a-f]|[0-9]){6}", entry[1]) or len(entry[1]) != 7:
				return False
		if entry[0] == "pid":
			if not re.search("[0-9]{9}", entry[1]) or len(entry[1]) != 9:
				return False
		if entry[0] == "ecl":
			if entry[1] not in "amb blu brn gry grn hzl oth".split():
				return False
	return True



num_valid_passports = 0
with open("input/aoc4_input.txt", "r") as f:
	passport_file_string = ""
	check_last_line = False
	for line in f:
		line = line.strip()
		if len(line) == 0:
			if is_valid_passport(passport_file_string):
				num_valid_passports += 1
			passport_file_string = ""
			check_last_line = False
		else:
			passport_file_string += " " + line.strip()
			check_last_line = True
	if check_last_line:
		if is_valid_passport(passport_file_string):
			num_valid_passports += 1
		

print(num_valid_passports)