#所有文件分两大类：1.文本文件 2.二进制文件
#实现复制粘贴
fh1=open(r"C:\Users\ASUS\Pictures\Saved Pictures\002.png","rb")#rb表示读取非文本文件
data1=fh1.read()
print(data1)
fh2=open(r"C:\Users\ASUS\Pictures\Camera Roll\666.png","wb")#wb表示写入文件
fh2.write(data1)
fh1.close()
fh2.close()
