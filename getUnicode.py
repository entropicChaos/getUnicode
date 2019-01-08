#this program uses python built in functions ord(c)||chr(i) in order to get a unicode #character from an integer or a unicode integer from character


question = input('what are you looking for :')


	

if (question.lower() == 'i'):
	intToTranslate = int(input('Enter integer '))
	intTranslated= chr(intToTranslate)
	print('%d is equal to %s' %(intToTranslate,intTranslated))
elif(question.lower()=='c'):
	charToTranslate = str(input('Enter character '))
	charTranslated= ord(charToTranslate)
	print('%s is equal to %d '%(charToTranslate,charTranslated))
