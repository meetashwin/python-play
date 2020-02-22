def square(value):
	"""Returns the square of a value (docstring)"""
	new_value = value ** 2
	return new_value

print(square(2))
print(square(5))

def raise_to_power(value1, value2):
	"""Raise value1 to the power of value2"""
	new_value = value1 ** value2
	return new_value

print(raise_to_power(3,2))
print(raise_to_power(2,3))

def raise_both(value1, value2):
	"""Raise both values respectively"""
	new_value_1 = value1 ** value2
	new_value_2 = value2 ** value1

	new_value = (new_value_1, new_value_2)

	return new_value

print(raise_both(2,3))