def encrypt(stringe,shft):
    cyp =''
    for char in stringe:
        if char ==' ':
            cyp = cyp+char
        elif char.isupper():
            cyp= cyp+chr((ord(char)+shft-65)%26+65)
        else:
            cyp= cyp+chr((ord(char)+shft-97)%26+97)
    return cyp

def decrypt(stringd,shift):
    cyp =''
    for char in stringe:
        if char ==' ':
            cyp = cyp+char
        elif char.isupper():
            cyp= cyp+chr((ord(char)+shft-65)%26+65)
        else:
            cyp= cyp+chr((ord(char)+shft-97)%26+97)
    return cyp

text = input("enter the message to be encrypted")
n=int(input("enter the shift value "))
print("encypted text is ",encrypt(text,n))
enc = encrypt(text,n)
decry = input("enter the decrpyted message")
x=int(input("enter the shift back value")
print("decrpyted message is ",decrypt(decry,x))             
