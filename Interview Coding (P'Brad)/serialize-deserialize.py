def serialize(input_array):
	output = ""
	for word in input_words:
		for c in word:
			if(c == "%"):
				output = output + "%5"
			elif(c == "&"):
				output = output + "%4"
			else:
				output = output + c
		output = output + "&"
	return output

def deserialize(input_str):
	output_array = []
	word = ""
	skip_one = False
	for i,c in enumerate(input_str):
		if(skip_one):
			skip_one = False
		elif(c == "&"):
			output_array.append(word)
			word = ""
		elif(c == "%" and input_str[i+1] == "4"):
			word = word + "&"
			skip_one = True
		elif(c == "%" and input_str[i+1] == "5"):
			word = word + "%"
			skip_one = True
		else:
			word = word + c
	return output_array


input_words = []
input_text = raw_input()

while(input_text != 'end'):
	input_words.append(input_text)
	input_text = raw_input()

# print input_words

serialized_text = serialize(input_words)
# print serialized_text

print deserialize(serialized_text)

# input:
# vee
# v&v
# v%%v
# %5%5
# abc
# %4%5%%4%5&%455%%&&&
# end