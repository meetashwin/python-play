#This program counts the number of zerod in array

# Here's the test array
binary_array = [1, 1, 1, 1, 0, 0, 0, 0]
zero_count = {"count":0}

for i in range(len(binary_array)):
	if (binary_array[i] == 0):
		zero_count["count"] = zero_count["count"] + 1

print(zero_count["count"])