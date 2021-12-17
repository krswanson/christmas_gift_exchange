import json
import os
from create_matches import create_matches

def save_matches(year, matches):
    filename = "matches_" + str(year) + ".json"
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, filename)
    ans = "y"
    if os.path.exists(file):
        print("The year", year, "already has a file with match data!")
        ans = input("Are you sure you want to over-write this year? (y/n) ")
    if ans == "y":
        with open(file, 'w') as f:
            json.dump(matches, f, indent=4)
            print("Matches saved to:", file)
    else:
        print("Aborted. No matches saved.")

year = input("Which Christmas year is this for? ")
matches = create_matches("matches_" + str(int(year) - 1) + ".json")
#matches = create_matches("matches_2021.json")
save_matches(year, matches)
