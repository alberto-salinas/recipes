class BiNode:
	def __init__(self, data, left = None, right = None):
		self.__data = data
		self.__left = left
		self.__right = right

	def getData(self):
		return self.__data

	def setData(data):
		self.__data = data

	def getLeft(self):
		return self.__left

	def setLeft(self, left):
		self.__left = left

	def getRight(self):
		return self.__right

	def setRight(self, right):
		self.__right = right

class Node:
	def __init__(self, data, nextLink = None):
		self.__data = data
		self.__nextLink = nextLink

	def getData(self):
		return self.__data

	def setData(self, data):
		self.__data = data

	def getNext(self):
		return self.__nextLink

	def setNext(self, nextLink):
		self.__nextLink = nextLink
