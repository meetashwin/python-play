# Program to count the set bits in an integer
# Examples:
# n=6, binary=110 => Set bits = 2 (number of 1's)
# n=12, binary=1100 => Set bits = 2
# n=7, binary=111 => Set bits = 3 

def countsetbits(n):
	count = 0

	while(n):
		count += n & 1
		n >>= 1
	
	return count

print("Enter the number to find set bits for:")
n = int(input())
print("Set bits for {0} is {1}".format(n, countsetbits(n)))