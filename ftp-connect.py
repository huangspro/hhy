from ftplib import FTP
import time
i=input("请输入需要链接的计算机的ip地址")
d=int(input("请输入端口号（默认为21）："))
u=input("请输入用户名")
p=input("请输入密码")
ftp=FTP()                   
ftp.connect(i,d)   
ftp.login(u,p)
print("与目标计算机连接成功")

print('FTP服务器指定目录中有如下文件')
print(ftp.dir()) 
n=input('请输入要上传的文件路径')
m=input('请输入需要上传的文件名')
k="STOR "+m
with open(n, "rb") as f:
     print("正在上传")
     ftp.storbinary(k, f)
print("上传成功")
time.sleep(10)
