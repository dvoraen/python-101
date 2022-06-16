class StringHolder:
    def __init__(self):
        self.value = 0
        self.string = f"Value is {self.value}"
        self.format_string = "Value is {value}"

    def printme(self, value: int):
        self.value = value
        print(self.string)

    def printformat(self, value: int):
        self.value = value
        print(self.format_string.format(value=self.value))


names = sorted(["Abacus", "Dael", "Vindaen"])
msgs = [
    "Bhandn performs an assisted check of strength and athletics.",
    f"Assisting: {', '.join(names)}",
]

print(f"{names}")
print(f"{*names,}")
print()

for msg in msgs:
    print(msg)

print()

sh = StringHolder()
sh.printme(3)
sh.printformat(4)
