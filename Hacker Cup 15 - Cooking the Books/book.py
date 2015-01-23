class Book:

	def __init__(self, number):
		self.input_number = str(number) # e.g. '12345'
		self.length = len(self.input_number) # e.g. 5
		self.digit_array = self.convert_to_digit_array() # e.g. [1, 2, 3, 4, 5]
		self.max_digit, self.max_digit_index = self.get_max_digit() # e.g. 5, 4
		self.output_digit_array = self.cook_it() # e.g. [5, 2, 3, 4, 1]
		self.output_number = self.merge() # e.g. 52341
		print self.output_number

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

	def cook_it(self):
		output = list(self.digit_array)
		if(self.max_digit != self.digit_array[0]):
			output[0], output[self.max_digit_index] = self.digit_array[self.max_digit_index], self.digit_array[0]
		return output

	def merge(self):
		return ''.join(str(x) for x in self.output_digit_array)


n = input('number of test cases: ')
for i in range(0, int(n)):
	num = input()
	print 'Case #'+str(i+1)+':',
	Book(num)
