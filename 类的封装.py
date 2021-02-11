
class card(object):

	def __init__(self, num,pwd,ban):

		self.num = num#卡号
		self.pwd = pwd#密码
		self.__ban = ban#余额 私有属性（只能在类的内部被访问）
	def cun(self):
		print("存款！")
	def getban(self,num,pwd):
		if num==self.num and pwd==self.pwd:
			return self.__ban
		else:
			return "输入错误"


card=card("1001","2345","5000")
print(card.getban("1001","2345"))