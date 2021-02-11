class dog(object):
	"""docstring for dog"""
	#初始化方法
	def __init__(self, name,age,color):#self表示当前对象，定义类的属性
		self.name=name
		self.age=age
		self.color=color

	def eat(self):  #普通方法
		print(self.name,"正在啃骨头")
	def run(self,speed):
		print(self.name,"正在飞快的跑!速度:",speed)

#实例化对象
dog=dog("小黑",3,"白色")#dog隐式传递给self，传递参数

print(dog.color)
dog.eat()
dog.run("3m/s")