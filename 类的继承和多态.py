class animal(object):
	def __init__(self, color):
		self.color=color
	def eat(self):
		print("动物正在吃")
	def run(self):
		print("动物正在跑")


class cat(animal):
	def eat(self):
			print("猫在吃鱼")	

class dog(animal):#父类和子类含同名方法，优先使用子类的方法
	def __init__(self, name,age,color):
		super(dog, self).__init__(color)#调用父类的初始化方法
		self.age=age
		self.name=name

	def eat(self):
			print("狗在啃骨头")	

#多态(定义一个普通方法，以达到调用所有类所共含的方法)
def feed(obj):
	obj.eat()

a=animal("褐色")
b=cat("黑色")
c=dog("xihu",6,"白色")
feed(a)#不需重复调用方法
