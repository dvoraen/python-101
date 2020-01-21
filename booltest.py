

#boolean test!


test_value = 8  # in binary, 1000
bit_mask = 4    # in binary, 0100

print("Test value (bool): %s" % bool(test_value))
print("Test value (xor with mask): %s" % (test_value ^ bit_mask))

test_value ^= bit_mask
print("Test value (xor mask as bool): %s" % bool(test_value))

test_value ^= True
print("Test value (xor with True): %s" % test_value)

print("Test value (not test_value): %s" % (not test_value))

test_value = 2
print("Test value (= not test_value): %s/%d (original value %d)" % (not test_value, not test_value, test_value))

test_value = not(not test_value)
print("Test value (= not not test_value): %s/%d" % (test_value, test_value))

test_value = 1
print("Test value (xor 1 with True): %s -- Bool: %s" % (test_value ^ True, (test_value ^ True)==True))

print("Test value (false ^ false): %s" % (False ^ False))

test_value ^= True
print("Bool test: %s (value: %s)" % (test_value==True, test_value))

test_value ^= True
print("Bool test 2: %s (value: %s)" % (test_value==True, test_value))

test_value = 2
test_value ^= True
print("Test value (2 ^ True): %s -- Result: %s" % (test_value, 2 ^ True == True))
test_value ^= True
print("Test value ((2 ^ True) ^ True): %s " % test_value)

test_value = 2
print("Test value (~ test_value): %s" % (bool(~test_value)))