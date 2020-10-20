#!/usr/bin/python3

#	How to use a class statement in Python

"""
	Definition of a simple class.
"""
class ASimpleClass:
	myOwnObject = None																	#	define a class attribute (which is public by default)

	"""
		Our own constructor.
	"""
	def __init__(self, arg = tuple()):
		self.myOwnObject = arg
	# end constructor

	def thisIsMyObject(self):															#	define a class method
		return self.myOwnObject
	# end function
# end class

print(ASimpleClass.myOwnObject)
#print(ASimpleClass.thisIsMyObject())

"""
	Using objects.
"""
print("-----------------------")
useThis = ASimpleClass("Hello World!")
print(useThis.myOwnObject)
print(useThis.thisIsMyObject())
print(useThis.thisIsMyObject)

"""
	Deleting objects.
"""
del useThis
#print(useThis.thisIsMyObject())														#	since here our object does no longer exist

"""
	Deriving a class.
"""
class DerivedClass(ASimpleClass):
	def thisIsMyObject(self):															#	define an another class method
		return 123
	# end function
# end class

useThis = DerivedClass()
print(useThis.thisIsMyObject())

"""
	Multiple inheritance.
"""
class AnAnotherDerivedClass(ASimpleClass):												#	derive an another class from ASimpleClass
	def thisIsMyObject(self):
		return bool(123 == 321)
	# end function
# end class

class MultipleInheritance(DerivedClass, AnAnotherDerivedClass):							#	using multiple inheritance
	def thisIsMyObject(self):
		return dict()
	# end function
# end class

useThis = MultipleInheritance()															#	create an object for our class
print(useThis.thisIsMyObject())															#	What will printed out?
del useThis
print("-----------------------")
#-------------------------------------------------------
"""
	Modify access.
"""
class Point:
	__x = 0																				#	__ -> private access
	__y = 0																				#	_ -> protected access

	def __init__(self, x = 0, y = 0):
		self.__x = x
		self.__y = y
	# end constructor

	def getX(self):
		return self.__x
	# end method

	def getY(self):
		return self.__y
	# end method

	def onEqualPosition(self, otherPoint):
		return (self.__x == otherPoint.getX() and self.__y == otherPoint.getY())
	#end method

	def __add__(self, otherPoint):														#	overload "+" for this class only
		tmpX = self.__x + otherPoint.getX()
		tmpY = self.__y + otherPoint.getY()

		return Point(tmpX, tmpY)
	# end overloaded operator
# end class

point01 = Point(10,20)																	#	point01 = {10,20}
point02 = Point()																		#	point02 = {0,0}

print(point01.onEqualPosition(point02))
point02.__x = 10
point02.__y = 20
print(point01.onEqualPosition(point02))

print(point02.getX())
print(point02.getY())

point03 = point01 + point02
print("point03 = ({0},{1})".format(point03.getX(), point03.getY()))