int_list = [2, 1, 3, 5, 4]


def int_strings():
    yield from (str(value) for value in sorted(int_list))


iter = int_strings()
string_list = list(iter)

print(iter)

print(", ".join(string_list))
