from collections import Counter

#1.1 Is unique
def unique_characters(s:str) -> bool:
    length = len(s)
    for i in range(length):
        for j in range(i+1,length):
            if s[i]==s[j]:
                return False
    return True

print(unique_characters("Futbol"))
print(unique_characters("Soccer"))

#1.2 Is permutation
def is_permutation(str1:str,str2:str) ->bool:
    if len(str1)!=len(str2):
        return False
    if sorted(str1)==sorted(str2):
        return True
    
print(is_permutation("dog","god"))
print(is_permutation("cow","wocc"))

#1.3 Option 1: Replace with 20%
def replace_with_20(s:str) ->str:
    
    return s.replace(' ','%20')    

print(replace_with_20("tomorrow soccer"))

#1.3 Option 2: Replace with %20 pending 
# def replace_with_20v2(s:str)->str:

#1.4 is_palindrome_permutation

def is_palindrome_permutation(s:str)->bool:
    #String without spaces
    basic_string = ''.join(s.split()).lower()
    #Count the frequency of each character
    count_characters=Counter(basic_string)

    #It can only be one character with count 1 or 0
    less_or_equals_one = sum(1 for count in count_characters.values() if count %2!=0)

    return less_or_equals_one<=1
    
print(is_palindrome_permutation("tact coa"))
print(is_palindrome_permutation("am layi la m"))




