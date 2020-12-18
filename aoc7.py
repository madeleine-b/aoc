total_containments = 0

def num_subbags_contain_gold_bag(outer_bag, rule_dict, sum_so_far):
	if rule_dict[outer_bag] == 0:
		return sum_so_far
	sub_sum = sum_so_far
	for rule in rule_dict[outer_bag]:
		if rule[1] == "shiny gold":
			#print(outer_bag, " holds shiny gold")
			sub_sum += 1
		else:
			#print("making subcall for", rule[1])
			ret = num_subbags_contain_gold_bag(rule[1], rule_dict, 0)
			#print("\t", rule[1], " indirectly holds %d bags that hold shiny gold" % ret)
			sub_sum += ret
	return sub_sum

def set_up_rule_dict():
	rule_dict = {}
	with open("input/aoc7_input.txt", "r") as f:
		for rule in f:
			rule = rule.split("contain")
			bag_kind = rule[0][0:-5].strip()
			rule[1] = rule[1].strip()
			if bag_kind not in rule_dict:
				rule_dict[bag_kind] = []
			if rule[1] == "no other bags.":
				rule_dict[bag_kind] = 0
			else:
				containments = rule[1].split(",")
				# strip off the period
				containments[-1] = containments[-1][0:-1]
				for r in containments:
					num = int(r.split()[0])
					if num == 1:
						kind = ' '.join(r.split()[1:])[0:-4]
					else:
						kind = ' '.join(r.split()[1:])[0:-5]
					rule_dict[bag_kind].append((num, kind))
	return rule_dict

rule_dict = set_up_rule_dict()
total_outer = 0
for k, v in rule_dict.items():
	ret = num_subbags_contain_gold_bag(k, rule_dict, 0)
	if ret > 0:
		total_outer += 1

print(total_outer)
