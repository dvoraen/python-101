

def func(data:dict = {}) -> int:
    fdict = data

    for value in fdict:
        print(value[0])

    for value in fdict:
        print(value[1])


dict1 = {"hi":1, "hello":2, "how goes?":3}
dict2 = {"me":1, "myself":2, "Irene":3}


func()
func(dict1)
func(dict2)