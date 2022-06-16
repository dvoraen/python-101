str_list = [
    '"Hi!"',
    '"Hello!"',
    '"How are you?"',
    '"I\'m fine, thanks."',
    '"Good to hear!"',
]

num_list = range(5)


def generate():
    yield from (entry.lower() for entry in str_list)


def num_generate():
    yield from (num_list)


for msg in generate():
    print(msg)

for num in num_generate():
    print(num)