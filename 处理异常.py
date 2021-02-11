'''a=[12,23,34,45,56,0,"a",78]
for i in a:
	print("-----",i)
	try:  #可能会报错或出现异常
		print(3/i)	
	except Exception as e:#捕获try语句里面的异常Exception就是捕获的异常对象
		print("出现错误，错误是：",e)#出现异常时执行的语句
	else:
		print("_____正常")
	finally:
		print("==本次结束")#无论是否异常，都会执行语句'''

#自定义异常
pwd="10001"		
if len(pwd)<8:
	e=Exception("密码不能低于8位数")#自定义异常
	raise e#抛出异常
else:
	print("密码设置成功")