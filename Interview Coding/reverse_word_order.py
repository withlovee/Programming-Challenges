def reverse_order(input_text):
	output = ""
	a_word, input_text = get_first_word(input_text)
	while(a_word or input_text):
		output = concat(output, a_word)
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
		return word + " " + sentence
	else:
		return word


input_text = raw_input("Enter String: ")
print reverse_order(input_text)
# Input: Hello W World! Vee   Vee
# Output: Vee   Vee World! W Hello