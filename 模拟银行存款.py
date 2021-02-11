card1="1001"
psd1="123456"
yue1=10000

card2="1002"
psd2="12345"
yue2=20000

card3="1003"
psd3="1234"
yue3=30000

times=0
while True:
	print("欢迎进入我的银行")

	card=input("请输入您的银行卡号:")
	psd=input("请输入您的密码:")
	yue=0#余额
	
	if card==card1 and psd==psd1:
		yue=yue1
	elif card==card2 and psd==psd2:	
		yue=yue2
	elif card==card3 and psd==psd3:
		yue=yue3
	else:
		times=times+1
		if times>=3:
			print("您已经3次输入错误,请联系柜台!")
			break
		else:
			print("卡号密码输入错误!请重新输入!")
			continue
		




	while True:
		num=input("请选择您要办理的业务:1.存款 2.取款 3.退卡")
		if num=="1":
			inn=float(input("请输入存款金额:"))
			if inn<=0:
				print("存款金额请大于0!")
			elif inn>0:
				yue=yue+inn
				print("存款成功!存入:",inn,"余额:",yue)
				continue
		elif num=="2":
			out=float(input("请输入取款金额"))
			if out>yue:
				print("余额不足,赶紧去赚钱!")
				continue
			else:
				yue=yue-out
				print("取款成功!取出:",out,"余额",yue)
		elif num=="3":
			print("请收好您的卡片，欢迎下次再来!")
			break
		
		else:
			print("输入有误,请重新输入")
			continue


























