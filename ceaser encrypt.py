word=input('Enter the text: ')
key=int(input('Enter the key:"))
no_word=''

ascii=no_word=0

for i in word:
    if i.isupper():
        ascii=ord(i)
        nowa=(ascii+key-65)%26+65
        
    if i.islower():
        ascii=ord(i)
        nowa=(ascii+key-97)%26+97
        
    no_word+=chr(nowa)
    
 print('Encrypted code: ',no_word)
