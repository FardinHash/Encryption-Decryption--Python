
word=input('Enter the text: ')
key=int(input('Enter the key: '))

nword=''

ascii=nwa=0

for i in word:
    if i.isupper():
        ascii=ord(i)
        nwa=(ascii-key-65)%26+65
    if i.islower():
        ascii=ord(i)
        nwa=(ascii-key-97)%26+97
    nword+=chr(nwa)
    
print('Decrypted code: ',nword)
