def reverse_word(input_text):
	output = ""
	length = len(input_text)
	for c in input_text:
		output = c + output
	return output

def reverse(input_text):
	output = ""
	a_word, input_text = get_first_word(input_text)
	while(a_word or input_text):
		output = concat(output, reverse_word(a_word))
		a_word, input_text = get_first_word(input_text)
	return output

def get_first_word(input_text):
	output = ""
	i = 0
	for c in input_text:
		i = i + 1
		if(c == " "):
			return output, input_text[i:]
		output = output + c
	return output, input_text[i:]


def concat(sentence, word):
	if(sentence):
		return sentence + " " + word
	else:
		return word


input_text = raw_input("Enter String: ")
print reverse(input_text)
# Input: Hello W World! Vee   Vee
# Output: olleH W !dlroW eeV   eeV