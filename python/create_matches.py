import json
import random

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


f = open("relationships.json", "r")
people_json = f.read()
f.close()
people_rela = json.loads(people_json)["people"]

# Reshuffle until no invalid matches are created
while True:
	new_order = new_index_order(people_rela)
	matches = {}
	done = True
	for i, rela in enumerate(people_rela):
		person = list(rela.keys())[0]
		match = list(people_rela[new_order[i]].keys())[0]
		if match in rela[person]:
			print(person, match)
			done = False
			break
		matches[person] = match
	if done:
		break
print(matches)