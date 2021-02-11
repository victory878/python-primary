'''class xiong(object):

	def __init__(self, kind,name,color,hobby):

		self.kind=kind
		self.name=name
		self.color=color
		self.hobby=hobby
	def ha(self):
		print("种类:",self.kind,",名字:",self.name,",颜色:",self.color,",爱好:",self.hobby,"。")

xiong=xiong("灰熊","大壮","黑色","睡觉")		
print(xiong.ha())'''

class animal(object):#animal类继承object类，object为父类
	def __init__(self, color):
		self.color = color
	def eat(self):
		print("动物在吃")
	def run(self):
		print("动物在跑")
class cat(animal):#cat继承animal类的属性和方法
	pass

cat=cat("黑色")
print(cat.color)
cat.run()
cat.eat(）





