'''def f1(a):#定义了一个方法/函数
	print(a,"方法f1被执行了")



f1("666")#调用方法/函数'''

'''def add(a,b,c,d):
	e=a+b+c+d#add(a,b,c,d)的函数表达式
	return e#e==函数值/add(1,2,3,4)


#result=add(1,3,4,5)#把函数值赋给变量
print("本次相加的结果:",add(1,2,3,4))'''
while 1==1:
	p=input("请添加原料:(1.苹果 2.梨子 3.樱桃)")

	def zzj(p):
		if p=="苹果" or p=="梨子" or p=="樱桃":
			
			print("正在榨汁")
			print("两分钟以后")
			s="这是您的"+p+"汁"
			return s
		else:
			print("榨汁机毁坏")
	print(zzj(p))
	continue