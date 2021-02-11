'''def show(name,age,sex,hobby):#形参
	print("我叫:",name,"年龄:",int(age),"性别:",sex,"爱好:",hobby)
#show("张三","18","男","打球")#实参（顺序传入）
show(name="张三",hobby="打球",sex="男",age="18")#关键词传入'''

'''def show(name,age,sex,hobby="打球"):#hobby="打球"为默认参数
	print("我叫:",name,"年龄:",int(age),"性别:",sex,"爱好:",hobby)
show(name="张三",sex="男",age="18")'''

'''def show(name,age,sex,hobby="打球"):#hobby="打球"为默认参数
	print("我叫:",name,"年龄:",int(age),"性别:",sex,"爱好:",hobby)
show(name="张三",sex="男",age="18",hobby="看书")#优先输入手动传入参数'''
def add(*args):
	
	s=0
	for i in args:
		
		s=s+i
	return s
d=add(1,2,3,4,56,8,7)#不定长参数
print(d)



