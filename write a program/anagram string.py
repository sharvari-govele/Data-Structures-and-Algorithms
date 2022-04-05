
 
def anagramcheck(str1,str2) :
    if(sorted(str1)==sorted(str2)) :
        print ('strings are an anagram') 
    else:
        print('strings are not an angram')

str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
anagramcheck(str1,str2)
    