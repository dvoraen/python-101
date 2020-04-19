

try:
    raise ValueError("This is a test.")
except ValueError as err:
    msg = str(err)
    print(msg)