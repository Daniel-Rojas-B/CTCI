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