"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	if n >= 0:
		pass
	else:
		n = n * (-1)

	if n < 10:
		return n
	else:
		n1 = n % 10
		n2 = (n - (n % 10)) // 10
		if n1 > find_largest_digit(n2):
			return n1
		else:
			return find_largest_digit(n2)

if __name__ == '__main__':
	main()
