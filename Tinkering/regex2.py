import re

regex = r"(?P<names>(?:[a-zA-Z]+\s*/?\s*)+)"
string = "Bhandn /Apostate/Tehom"

match = re.match(regex, string)

if match:
    print("Matched")
    print(match.groupdict())
    matchstr = match.string
    namelist = [name for name in matchstr.split(",") if name]
else:
    print("No match")
    namelist = "Boo"


print(namelist)