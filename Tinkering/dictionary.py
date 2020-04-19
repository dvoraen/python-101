dict1 = {"hi":1, "hello":2, "how goes?":3}
dict2 = {"me":1, "myself":2, "Irene":3}


def func(data:dict = {}) -> int:
    fdict = data

    # This is what I want: the paired data.
    for value in fdict:
        print(fdict[value])



func()
func(dict1)
func(dict2)