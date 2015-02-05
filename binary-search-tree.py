# FROM @nuttt
# https://gist.github.com/nuttt/67003b5e7c7eba133bd7
# build a binary tree class (with no repeat element in tree)
# with following APIs
# - new()
# - addnode(int a)
# --- return true if a is not already in binary tree
# --- otherwise return false
# - removenode(int a)
# --- return true if a is removed in binary tree
# --- return false if otherwise
# - depth(int a)
# --- return integer repesents depth of a in binary tree
# --- return null if a is not in binary tree
# - isInBinaryTree(int a)
# - preorder()
# --- return array of integer representing preorder traversal of tree
# - inorder()
# - postorder()

class Node:
	def __init__(self, val):
		self.value = val
		self.left_child = None
		self.right_child = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, val):
		if(self.root == None):
			self.root = Node(val)
			return True
		return self.insert_recursive(self.root, val)

	def insert_recursive(self, root, val):
		if(val < root.value):
			if(root.left_child == None):
				root.left_child = Node(val)
				return True
			else:
				return self.insert_recursive(root.left_child, val)
		elif(val > root.value):
			if(root.right_child == None):
				root.right_child = Node(val)
				return True
			else:
				return self.insert_recursive(root.right_child, val)
		else:
			return False

	def get_node(self, val):
		return self.get_node_recursive(self.root, val)

	def get_node_recursive(self, root, val):
		if(root == None):
			return None
		if(root.value == val):
			return root
		if(val < root.value):
			return self.get_node_recursive(root.left_child, val)
		else:
			return self.get_node_recursive(root.right_child, val)

	def get_parent_node(self, val):
		if(self.root.value == val):
			pass
		return self.get_parent_node_recursive(self.root, val)

	def get_parent_node_recursive(self, root, val):
		if(root == None):
			return None
		if(root.left_child != None and root.left_child.value == val):
			return root
		if(root.right_child != None and root.right_child.value == val):
			return root
		if(val < root.value):
			return self.get_node_recursive(root.left_child, val)
		else:
			return self.get_node_recursive(root.right_child, val)

	def remove(self, val):
		parent_node = self.get_parent_node(val)
		if(parent_node == None):
			return False
		if(parent_node.left_child != None and parent_node.left_child.value == val):
			parent_node.left_child = self.remove_node(parent_node.left_child)
		if(parent_node.right_child != None and parent_node.right_child.value == val):
			parent_node.right_child = self.remove_node(parent_node.right_child)
		print self.inorder()

	def remove_node(self, node):
		if(node == None):
			return None
		if(node.right_child == None and node.left_child == None):
			return None
		if(node.right_child == None and node.left_child != None):
			return node.left_child
		if(node.right_child != None and node.left_child == None):
			return node.right_child
		return self.get_replace_node(node.left_child)

	def get_replace_node(self, node):
		if(node == None):
			return None
		replace_node = self.get_replace_node(node.right_child)
		if(replace_node == None):
			return node
		else:
			return replace_node

	def inorder(self):
		output = []
		self.inorder_recursive(output, self.root)
		return output

	def inorder_recursive(self, output, root):
		if(root == None):
			return True
		self.inorder_recursive(output, root.left_child)
		output.append(root.value)
		self.inorder_recursive(output, root.right_child)

	def preorder(self):
		output = []
		self.preorder_recursive(output, self.root)
		return output

	def preorder_recursive(self, output, root):
		if(root == None):
			return True
		output.append(root.value)
		self.preorder_recursive(output, root.left_child)
		self.preorder_recursive(output, root.right_child)

	def postorder(self):
		output = []
		self.postorder_recursive(output, self.root)
		return output

	def postorder_recursive(self, output, root):
		if(root == None):
			return True
		self.postorder_recursive(output, root.left_child)
		self.postorder_recursive(output, root.right_child)
		output.append(root.value)

bst = BST()
bst.insert(33)
bst.insert(10)
bst.insert(12)
bst.insert(310)
bst.insert(20)
bst.insert(40)
bst.insert(210)
bst.insert(0)
bst.insert(510)
bst.insert(10)
bst.insert(3120)
#            33
#    10             310
# 0     12      40      510
#         20      210      3120
print bst.inorder()
print bst.preorder()
print bst.postorder()
bst.remove(3120)