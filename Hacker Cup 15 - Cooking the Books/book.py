class Book:

	def __init__(self, number):
		self.input_number = str(number) # e.g. '12345'
		self.length = len(self.input_number) # e.g. 5
		self.digit_array = self.convert_to_digit_array() # e.g. [1, 2, 3, 4, 5]
		self.cooked_max_number = self.cook_max() # e.g. 52341
		print self.cooked_max_number

	def convert_to_digit_array(self):
		output = []
		for i in range(0, self.length):
			output.append(int(self.input_number[i]))
		return output

	def get_max_digit(self):
		maxx = -1
		maxx_index = -1
		for i, number in enumerate(self.digit_array):
			if(number > maxx):
				maxx = number
				maxx_index = i
		return maxx, maxx_index

	def cook_max(self):
		max_digit, max_digit_index = self.get_max_digit() # e.g. 5, 4
		output_digit_array = self.swap_max_digit(max_digit, max_digit_index) # e.g. [5, 2, 3, 4, 1]
		return self.merge(output_digit_array) # e.g. 52341

	def swap_max_digit(self, max_digit, max_digit_index):
		output = list(self.digit_array)
		if(max_digit != self.digit_array[0]):
			output[0], output[max_digit_index] = self.digit_array[max_digit_index], self.digit_array[0]
		return output

	def merge(self, digit_array):
		return ''.join(str(x) for x in digit_array)


n = input('number of test cases: ')
for i in range(0, int(n)):
	num = input()
	print 'Case #'+str(i+1)+':',
	Book(num)
