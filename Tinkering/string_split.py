manyString = "Aendal,Bhandn,Apostate,Puffin,Herja"
singleString = "Bhandn"

testString = "material,qty"

manyList = manyString.split(",")
singleList = singleString.split(",")

try:
    mq_str, inform_msg = testString.split("/")
except ValueError:
    mq_str = testString
    inform_msg = None

print(manyList)
print(singleList)
print(f"{mq_str} and {inform_msg}")