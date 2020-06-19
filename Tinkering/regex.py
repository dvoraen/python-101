import re


# @check
# <ID>|<stat>+<skill> at <diff>=<rcvr>


check_pattern = r"""
(?P<id>[0-9]+)?\|?                 # retainer ID
(?P<stat>[a-zA-Z]+\b)              # stat
(\s*[+]\s*)?
(?P<skill>[a-zA-Z]+\b)?            # skill
(\s*at\s*)?
(?P<diff>[0-9]+)?                  # difficulty
([=])?
(?P<rcvrs>[a-zA-Z,]+)?              # rcvrs
"""

def check_match(test_str: str, regex):
    r = regex.match(test_str)
    if r is None:
        print("Did not match (%s)" % test_str)
    else:
        print("Matched %s" % test_str)
        print(r.groupdict())
        print(r.groups())


result = re.compile(check_pattern, re.VERBOSE)

test = "strength"
check_match(test, result)

test = "strength at 15=Bhandn"
check_match(test,result)

test = "str+ath"
check_match(test, result)

test = "str+ath=Bhandn"
check_match(test, result)

test = "str+ ath"
check_match(test, result)

test = "str + ath"
check_match(test, result)

test = "str +ath"
check_match(test, result)

test = "str+ath at 20"
check_match(test, result)

test = "1384|strength+dexterity at 40=self"
check_match(test, result)

test = "1221|int+riddles at25=Bhandn,Aleksei"
check_match(test,result)