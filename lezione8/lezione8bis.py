#ESERCITAZIONE

#ESERCIZIO 2

#Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest 
#palindrome that can be built with those letters. 
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

def longest_palindrome(s: str) -> int:
    s = s.lower()
    s_rev = s[::-1]
    palindrome_string: list = []
    all_palindrome: list = []
            


print(longest_palindrome("abccccdd"))
print(longest_palindrome("Aa"))

#ESERCIZIO 3

#Implement a last-in-first-out (LIFO) stack using only two queues. 
#The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

#Implement the MyStack class:

#- push(x: int) -> None: Pushes element x to the top of the stack.
#- Top() -> None: Removes the element on the top of the stack and returns it.
#- pop() -> None: Returns the element on the top of the stack.
#- empty() -> None: Returns true if the stack is empty, false otherwise.

class Queue:
    pass


class MyStack:
    pass



#ESERCIZIO 5

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

#An input string is valid if: 

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.

def is_valid_parenthesis(s: str) -> bool:
    if "()" in s:
        return True
    elif "[]" in s:
        return True
    elif "{}" in s:
        return True
    elif s == "":
        return True
    else:
        return False


print(is_valid_parenthesis("()"))
print(is_valid_parenthesis("(]"))
print(is_valid_parenthesis("{}"))
print(is_valid_parenthesis("{[]}"))
print(is_valid_parenthesis("()[]{}"))


#ESERCIZIO 6

#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
#representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 
#into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    pass

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  
