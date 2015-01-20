def cal(input):
	original = int(input)
	num = original
	n = len(str(num))
	number_array = []
	maxx = -1
	maxx_index = -1
	for i in range(0,n) :
		temp = (num/10)*10
		x = num-temp
		number_array.append(x)
		if(x > maxx):
			maxx = x
			maxx_index = i
		num = num/10
	# print number_array
	if(maxx_index == n-1):
		output_max = str(original)
	else:
		output_max = ""
		for i in range(n-1,-1,-1):
			if maxx_index == i:
				output_max = output_max+str(number_array[n-1])
			elif i == n-1:
				output_max = output_max+str(number_array[maxx_index])
			else:
				output_max = output_max+str(number_array[i])
		print output_max

n = input('number of test cases:')
for i in range(0, int(n)):
	cal(input())