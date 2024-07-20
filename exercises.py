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

#1.5 One Way: given two strings determine if they are one edit or zero edits away to be equal

def oneEditAway(s1:str,s2:str):
    if(len(s1)==len(s2)):
        return oneEditReplace(s1,s2)
    elif(len(s1)+1==len(s2)):
        return oneEditInsert(s1,s2)
    elif(len(s1)-1==len(s2)):
        return oneEditInsert(s1,s2)
    return False

def oneEditReplace(s1:str,s2:str):
    foundDifference = False
    for i in range(len(s1)):
        
        if(s1[i]!=s2[i]):
            if (foundDifference):
                return False
            foundDifference= True
    return True

def oneEditInsert(s1:str,s2:str):
    index1=0
    index2=0
    while(index2<len(s2) and index1<len(s1)):
        if(s1[index1]!=s2[index2]):
            if(index1!=index2):
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    return True         
        

print(oneEditReplace("pale","ple"))
print(oneEditInsert("pale","ple"))
print(oneEditAway("pale","ple"))

#1.6 Compressed String

def compressed_string(s:str):
    compressed_string=''
    counter = 1
    s_length=len(s)
    print(s_length)
    for i in range(s_length-1):
        if s[i]==s[i+1]:
            counter+=1
        else:
            compressed_string+=s[i]+str(counter)
            print(s[i])
            counter = 1
        
    return compressed_string

print(compressed_string('abbbc'))