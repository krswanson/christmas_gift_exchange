import json
import os
from create_matches import create_matches, get_json_file

def matchfile(year):
    filename = "matches_" + str(year) + ".json"
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, filename)

def write_matches(file, matches):
    with open(file, 'w') as f:
        json.dump(matches, f, indent=4)

def save_matches(year, matches):
    file = matchfile(year)
    ans = "y"
    if os.path.exists(file):
        print("The year", year, "already has a file with match data!")
        ans = input("Are you sure you want to over-write this year? (y/n) ")
    if ans == "y":
        write_matches(file, matches)
        print("Matches saved to:", file)
    else:
        print("Aborted. No matches saved.")

if __name__ == "__main__":
    settings = get_json_file('settings.json')
    year = settings["year"]
    back = int(settings["years_back"])
    rela_file = settings["relationships_file"]
    old_matches = [rela_file]
    for i in range(back):
        old_year = int(year) - 1 - i
        old_matches.append(matchfile(old_year))
    try:
        matches = create_matches(rela_file, old_matches)
        save_matches(year, matches)
    except FileNotFoundError as e:
        print(e)
        if "matches_" in str(e):
            print("Make sure you have previous year files if years_back is greater than 0")


