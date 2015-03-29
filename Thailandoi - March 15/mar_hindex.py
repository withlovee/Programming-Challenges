f = open('1.txt', 'w')
# input_f = open('mar_hindex-verifying-input.txt.txt', 'r')

def do():
	data = [0] * 10001
	count1 = [0] * 10001
	# count2 = [0] * 10001
	k = raw_input('')
	text = k.split(' ')
	for k in text[1:]:
		# k = raw_input('')
		k = int(k)
		data[k] = data[k] + 1
		# f.write(x)
		# f.write('\n')
	# print data
	for i in range(9999,-1,-1):
		count1[i] = count1[i+1] + data[i]
		if count1[i] >= i and count1[i+1] <= i:
			# print count1[i], i, count1[i+1], data[i]
			# print i
			f.write(str(i))
			f.write('\n')
			break

n = raw_input('')
n = int(n)
for i in range(0,n) :
	do()
f.close()