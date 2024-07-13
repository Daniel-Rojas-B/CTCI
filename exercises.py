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


        