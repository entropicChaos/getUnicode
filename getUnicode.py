#this program uses python built in functions ord(c)||chr(i) in order to get a unicode #character from an integer or a unicode integer from character


question = input('are you looking for an Integer or a Character (i/c)? : ')

def _to_character(number):
	fromNumberToChar= chr(number)
	print('%d is equal to %s' %(number,fromNumberToChar))

def _to_number(character):
	fromCharacterToInt=ord(character)
	print('%s is equal to %d ' %(character,fromCharacterToInt))
	

if (question.lower() == 'c'):
	intToTranslate = int(input('Enter integer '))
	_to_character(intToTranslate)
elif(question.lower()=='i'):
	charToTranslate = str(input('Enter character '))
	_to_number(charToTranslate)
