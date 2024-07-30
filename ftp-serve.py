from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

a=int(input('是否要创建服务器(是：1,不是:2)'))
if a==1:
   b=input('请输入客户端需要填写的用户名')
   c=input('请输入客户端需要填写的密码')
   o=input('请输入本机局域网IP')
   p=int(input('请输入一个两位数的端口号,如21'))
   print('正在创建服务器')
   authorizer = DummyAuthorizer()
   authorizer.add_user(b,c,r"C:\Users\Administrator\Desktop",perm="elradfmw")
   handler = FTPHandler
   handler.authorizer = authorizer
   server = FTPServer((o,p), handler)
   print('服务器创建成功')
   print('已默认允许客户端访问桌面文件')
   server.serve_forever() 
