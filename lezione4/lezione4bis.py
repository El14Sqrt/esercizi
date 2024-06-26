#dato un intero x, restituisce True se x è palindromo, e False altrimenti.

#senza usare "return s == s[::-1]"

def is_pal(x: int) -> bool:
    s:str = str(x)
    i:int = 0
    s_length = len(s)
    while i < (s_length // 2): #for i in range(len(s))
        j = s_length - (i+1)
        if s[i] != s[j]:
            return False
        i += 1
    return True

#data una stringa s che contiene parole e spazi, restituire la lunghezza dell'ultima parola in s.
#una parola è una sottostringa che contiene caratteri contugui diversi dallo spazio.

s: str = "oggi è lunedì"

#modo 1
"""
l: list[str] = s.split()
return len(1[-1])
"""

#modo 2
"""
i: int = 0
curr_len: int = 0
while i < len(s):
    if s[i] != " ":
        curr_len += 1
    else:
        break
"""

#dato un intero col_number, restituire il suo corrispondente titolo di colonna come su un foglio  excel

def convert_to_title(col_number: int) ->str:
    #curr_char = chr(ord("A") + (col_number-1))

    result: str = ""
    while col_number > 0:
        resto: int = (col_number - 1) % 26 
        result = chr(resto + ord("A")) + result
        col_number = (col_number - 1) // 26
    return result


#data una lista nums di n elementi, restituire l'elemento che compare più di n/2 volte.

def majority_element(nums: list[int]) -> int:
    d: dict[int, int] = {}
    for i in nums:
        d[i] = nums.count(i)

    length = len(nums)
    for key in d:
        d[key] /= length
        if d[key] > 0.5:
            return key
    
    return None

#la prima parte può essere sostituita da d: dict[int, int] = dict(Counter(nums))

#oppure ancora:
"""
for i in nums:
    if nums.count(i) > len(nums) /2:
        return i
return None
"""

#data una lista nums  di int , spostare gli zeri alla fine di questa lista 
#mantenendo l'ordine originale dei numeri che nn sono zeri

def move_zeroes(nums_list: list[int]):
    for i in nums_list:
        if i == 0:
            x = nums_list.remove(i)
            nums_list.append(x)
    
    return nums_list

#restituisci l'intersezione

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1_s = set(nums1)
    nums2_s = set (nums2)
    common_numbers = []
    for el in nums1_s:
        if el in nums2_s:
            common_numbers.append(el)
    return common_numbers
