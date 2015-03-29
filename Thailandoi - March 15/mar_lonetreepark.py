f = open('3.txt', 'w')
# input_f = open('mar_hindex-verifying-input.txt.txt', 'r')
class Solution:

	data = []
	k1row = 0
	k1col = 0

	def __init__(self):
		self.data = []
		self.k1row = 0
		self.k1col = 0

	def do(self):
		data = []
		k = raw_input('')
		k1 = k.split(' ')
		self.k1row = int(k1[0])
		self.k1col = int(k1[1])
		for i in range(0,self.k1row):
			row = raw_input('')
			self.data.append(row)

		max_area = 0
		for i in range(0, self.k1row):
			for j in range(0, self.k1col):
				max_area = max(max_area, self.find(i,j))
		print max_area

	def find(self, start_row, start_col):
		n = min(self.k1row - start_row, self.k1col - start_col)
		# print start_row, start_col, n
		max_n = 1
		for i in range(1,n+1):
			x = self.count_tree(start_row, start_col, i)
			if(x == -1):
				# print 'return ', str(i-1)
				return i-1
		return n

	def count_tree(self, start_row, start_col, k):
		n_tree = 0
		# print "> ",start_row,start_col,k
		for i in range(start_row, start_row + k):
			for j in range(start_col, start_col + k):
				# print ">>",i,j
				if(self.data[i][j] == '#'):
					n_tree = n_tree + 1
					if(n_tree > 1):
						return -1
		# print start_row, start_col, i, n_tree
		return n_tree


	# H = raw_input('')
	# H = H.split(' ')
	# for h in H:
	# 	h = int(h)
	# 	data[h] = 1

	# K = raw_input('')
	# K = K.split(' ')
	# output = []
	# for k in K:
	# 	# print 'in ', int(k)
	# 	k = int(k)
	# 	count = 0
	# 	for i in range(0, k10-k):
	# 		if data[i] == 1 and data[i+k] == 1:
	# 			count = count + 1
	# 	output.append(count)
	# output2 = ' '.join([str(x) for x in output])
	# print output2
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
	Solution().do()
f.close()