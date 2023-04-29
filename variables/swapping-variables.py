"""
Problem:
Write a program that switches the values stored in two inputted variables a and b. Print results.
"""

# 1.  Using a temporary variable (any type of value):

a = input("Enter value for a: ")
b = input("Enter value for b: ")

temp = a
a = b
b = temp

print("After swapping using temporary variable: a =", a, "and b =", b)



# 2.  Using a tuple (any type of value):

a, b = b, a

print("After swapping using a tuple: a =", a, "and b =", b)

"""Note 2: This solution uses [Python Tuple Unpacking](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/), a Python feature that allows us to assign multiple variables in a single line. We create a tuple containing `a` and `b`, and then unpack the tuple into variables `b` and `a`, respectively. This effectively swaps the values of `a` and `b`."""


# 3.  Using arithmetic operations (it works only for integer values):

a = int(a)
b = int(b)

a = a + b
b = a - b
a = a - b
print("After swapping using arithmetic operations: a =", a, "and b =", b)


"""Note 3: This solution relies on arithmetic operations to swap the values of a and b. We add a and b, and store the result in a. Then we subtract b from the new value of a to get the original value of a, and store it in b. Finally, we subtract the original value of b from the new value of a to get the original value of b, and store it in a. The values of a and b are swapped."""

# 4.  Using XOR bitwise operation:

a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping Using XOR bitwise operation: a =", a, "and b =", b)

""" Note 4: This solution uses the XOR bitwise operator (^) to swap the values of a and b. We perform the XOR operation on a and b, and store the result in a. Then we perform the XOR operation again on the new value of a and the original value of b, and store the result in b. Finally, we perform the XOR operation again on the new value of b and the original value of a, and store the result in a. The values of a and b are swapped.
 """

"""Warning!
Please keep in mind that some of these solutions may not be suitable for certain scenarios, and it's always important to consider the limitations and edge cases of each approach before implementing them."""
