"""
	Time Complexity  : O(N)
	Space Complexity : O(1)

	Where 'N' is the number given in the problem.
"""
## BRUTE FORCE
import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
	# Declare a variable to store our result and initialize it with 1.
	answer = 1

	# Iterating 'N' times.
	for i in range(1, n + 1):
		# Multiply answer with 'X' and then do modulo with 'M'.
		answer = (answer * x) % m
	
	# Return the answer.
	return answer

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1
 
 
## RECURSIVE APPROACH

"""
	Time Complexity  : O(log N)
	Space Complexity : O(log N)

	Where 'N' is the number given in the problem.
"""

def modularExponentiation(x, n, m):
	# Base case.
	if (n == 0):
		return 1
	
	# Calculate 'X' ^ ('N' / 2) recursively and store it in ans variable.
	answer = modularExponentiation(x, n // 2, m)

	# If 'N' is even then return the square of answer.
	if (n % 2 == 0):
		return (answer * answer) % m
	# Else return the square of answer multiplied with 'X.
	else:
		return ((((answer * answer) % m) * x) % m) % m
	
# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1
 
 
 ### Iterative Approach


"""
	Time Complexity  : O(log N)
	Space Complexity : O(1)

	Where 'N' is the number given in the problem.
"""

def modularExponentiation(x, n, m):
	# Declare a variable to store our result and initialize it with 1.
	answer = 1

	# Run a loop until 'N' > 0.
	while (n > 0):
		# If bitwise and of 'N' with 1 is 1 then multiply answer with 'X'.
		if (n & 1): 
			answer = (answer * x) % m
		
		# Do modular squaring of 'X'.
		x = (x * x ) % m

		# Right shift 'N' by 1 bit for next iteration.
		n >>= 1

	# Return the answer.
	return answer

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1