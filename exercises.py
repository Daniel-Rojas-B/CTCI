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


