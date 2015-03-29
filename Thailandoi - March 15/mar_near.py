f = open('2.txt', 'w')
# input_f = open('mar_hindex-verifying-input.txt.txt', 'r')

def do():
	k = raw_input('')
	k1 = k.split(' ')
	k10 = int(k1[0])
	data = [0] * k10

	H = raw_input('')
	H = H.split(' ')
	for h in H:
		h = int(h)
		data[h] = 1

	K = raw_input('')
	K = K.split(' ')
	output = []
	for k in K:
		# print 'in ', int(k)
		k = int(k)
		count = 0
		for i in range(0, k10-k):
			if data[i] == 1 and data[i+k] == 1:
				count = count + 1
		output.append(count)
	output2 = ' '.join([str(x) for x in output])
	print output2
	# f.write(output2 + "\n")



	# for k in text[1:]:
	# 	# k = raw_input('')
	# 	k = int(k)
	# 	data[k] = data[k] + 1
	# 	# f.write(x)
	# 	# f.write('\n')
	# # print data
	# for i in range(9999,-1,-1):
	# 	count1[i] = count1[i+1] + data[i]
	# 	if count1[i] >= i and count1[i+1] <= i:
	# 		# print count1[i], i, count1[i+1], data[i]
	# 		# print i
	# 		f.write(str(i))
	# 		f.write('\n')
	# 		break

n = raw_input('')
n = int(n)
for i in range(0,n) :
	do()
f.close()