def reverse(input_text):
	output = ""
	length = len(input_text)
	for c in input_text:
		output = c + output
	return output

input_text = raw_input("Enter String: ")
print reverse(input_text)