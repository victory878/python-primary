before=float(input("请输入你的税前工资:"))
m1=float(input("请输入社保扣除金额:"))

ss=0#纳税金额
ys=before-m1-5000#应纳税所得额

if ys<=36000 and ys>0:
	ss=ys*0.03-0
elif ys<=144000:
	ss=ys*0.1-2520
elif ys<=300000:
	ss=ys*0.2-16920
elif ys<=420000:
	ss=ys*0.25-31920
elif ys<=660000:
	ss=ys*0.3-52920
elif ys<=960000:
	ss=ys*0.35-85920
elif ys>960000:
	ss=ys*0.45-181920

print("您应缴纳税额:",ss,"到手工资",before-m1-ss)




