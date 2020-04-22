dict1 = {"hi":1, "hello":2, "how goes?":3}
dict2 = {}

def func(data:dict = None):
    fdict = data or {}

    # This is what I want: the paired data.
    for value in fdict:
        print(fdict[value])



func()
func(dict1)
func(dict2)