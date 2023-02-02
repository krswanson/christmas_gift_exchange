import json
import random
import os

def index_shuffle(l):
	indexes = list(range(len(l)))
	random.shuffle(indexes)
	return indexes

# Indexes in random order, none in same position
def new_index_order(l):
	good = False
	new_order = index_shuffle(l)
	while not good:
		good = True
		for (i, val) in enumerate(new_order):
			if val == i:
				good = False
				new_order = index_shuffle(l)
	return new_order

def get_json_file(filename):
	dirname = os.path.dirname(__file__)
	file = os.path.join(dirname, filename)
	f = open(file, "r")
	json_str = f.read()
	f.close()
	json_dict = json.loads(json_str)
	return json_dict

def create_matches(relationships_file, dont_match_files):
	rela_dict = get_json_file(relationships_file)
	original_names_list = list(rela_dict.keys())
	# Add any number of previous years' people to not match with
	for file in dont_match_files:
		old_matches = get_json_file(file)
		for name in original_names_list:
			rela_dict[name].append(old_matches[name])

	# Reshuffle until no invalid matches are created
	while True:
		new_order = new_index_order(original_names_list)
		matches = {}
		done = True
		for i, name in enumerate(original_names_list):
			match = original_names_list[new_order[i]]
			if match in rela_dict[name]:
				#print(name, match, rela_dict[name])
				done = False
				break
			matches[name] = match
		if done:
			break
	return matches

#matches = create_matches("Relationships.json", ["matches_2021.json", "matches_2022.json"])
#print(matches)