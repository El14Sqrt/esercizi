#ESERCITAZIONE

#ESERCIZIO 2

#Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest 
#palindrome that can be built with those letters. 
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

def longest_palindrome(s: str) -> int:
    length = 0
    odd_found = False
    

    for char in set(s):  
        count = s.count(char)
        length += count // 2 * 2  
        if count % 2 == 1:
            odd_found = True
    
    if odd_found:
        length += 1
    
    return length


print(longest_palindrome("abccccdd"))
print(longest_palindrome("Aa"))

#ESERCIZIO 3

#Implement a last-in-first-out (LIFO) stack using only two queues. 
#The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

#Implement the MyStack class:

#- Push(x: int) -> None: Pushes element x to the top of the stack.
#- Top() -> None: Removes the element on the top of the stack and returns it.
#- Pop() -> None: Returns the element on the top of the stack.
#- Empty() -> None: Returns true if the stack is empty, false otherwise.

class Queue:
    def __init__(self) -> None:
        self.items = []

    def in_queue(self, item):
        if item not in self.items:
            self.items.append(item)
    
    def out_queue(self, item):
        if item in self.items:
            return self.items.pop(0)
    
    def is_empty(self):
        if len(self.items) == 0:
            return "empty queue"
         
class MyStack:
    def __init__(self) -> None:
        self.queue1 = Queue()
        self.queue2 = Queue()

    def Push(self, x: int) -> None:
        self.queue1.in_queue(x)

    def Top(self) -> None:
        while len(self.queue1.items) > 1:
            self.queue2.in_queue(self.queue1.out_queue())
        top_element = self.queue1.out_queue()
        
        self.queue2.in_queue(top_element)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element
    
    
    def Pop(self) -> None:
        while len(self.queue1.items) > 1:
            self.queue2.in_queue(self.queue1.out_queue())
        
        pop_element = self.queue1.out_queue()
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return pop_element
    

    def Empty(self) -> None:
        return self.queue1.is_empty() and self.queue2.is_empty()



    
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
    p1,p2 =m-1,n-1
    p=m+n-1
    while p1 >=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[p] = nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2 -=1
        p -=1
    while p2 >=0:
        nums1[p] = nums2[p2]
        p2-=1
        p-=1
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  
