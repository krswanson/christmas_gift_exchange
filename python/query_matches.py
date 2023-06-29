from create_matches import get_json_file
from save_matches import matchfile, write_matches
class QueryMatches():

	def __init__(self, year):
		self.year = year
		self.file = file = matchfile(year)

	def find_match_person_has(self, person):
		matches = get_json_file(self.file)
		return matches[person]
	
	def find_person_who_has_match(self, match):
		matches = get_json_file(self.file)
		for name, cur_match in matches.items():
			if match == cur_match:
				return name
		return ""

	def add_person(self, new_person, swap_person):
		matches = get_json_file(self.file)
		if new_person in matches.keys():
			return False
		matches[new_person] = new_person
		write_matches(self.file, matches)
		self.swap_matches(new_person, swap_person)
		return True

	def swap_matches(self, person1, person2):
		matches = get_json_file(self.file)
		match1 = matches[person1]
		match2 = matches[person2]
		matches[person1] = match2
		matches[person2] = match1
		write_matches(self.file, matches)

	def get_match_dict(self):
		return get_json_file(self.file)

year = input("Type year you want or press enter for settings.json year: ")
if not year:
	year = get_json_file("settings.json")["year"]
query = QueryMatches(year)
option = ""
while True:
	print("1. See who a person has")
	print("2. See whw has a certain person")
	print("3. Add a new person")
	print("4. Swap two existing matches")
	print("5. See list of name options")
	print("6. Exit")
	option = input("What would you like to do? ")
	match option:
		case "1":
			person = input("Whose match do you want to see? ")
			try:
				match = query.find_match_person_has(person)
				print("\n", person, "has", match)
			except KeyError:
				print("\n", "'" + person + "'", "was not found")
		case "2":
			match = input("See whe has: ")
			person = query.find_person_who_has_match(match)
			if person:
				print("\n", person, "has", match)
			else:
				print("\n No one has '" + match + "'. Check your spelling or add them.")
		case "3":
			new_person = input("who would you like to add? ")
			swap_person = input("Who should get " + new_person + " as their match (and give " + new_person + " their match)? ")
			try:
				if query.add_person(new_person, swap_person):
					print("\n Success!", new_person, "has", swap_person + "'s match and", swap_person, "has", new_person, "as their match.")
				else:
					print("\n", "Failed to add. Make sure", new_person, "doesn't already exist for", year + ".")	
			except:
				print("\n", "Failed to add. Make sure", swap_person, "exists and is spelled correctly.")
		case "4":
			person1 = input("Type person who needs their match swapped: ")
			person2 = input("Type person " + person1 + "'s match should be swapped with: ")
			try:
				query.swap_matches(person1, person2)
				print("\n Success! The matches of", person1, "and", person2, "bave been swapped.")
			except KeyError:
				print("\n", "Failed to swap. Make sure both people exist and are spelled correctly.")
		case "5":
			print()
			for name in query.get_match_dict():
				print(name)
		case "6":
			print("Exiting...")
			break
		case _:
			print("\n Please type a number from the menu.")
	print()
	