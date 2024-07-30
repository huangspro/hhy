k='''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<p>您有一分钟的输入时间</p>
'''
m='''
<form name="frm1">
<input name="h" id="k" type="text"></input>
<input type="submit" value="发送/刷新"></input>
</form>
<script>
setTimeout("frm1.submit();",60000);
</script>
</body>
</html>
'''
def g(a):
    return(k+'<div style="background-color:lightblue;">'+a+'</div>'+m)
from flask import Flask,request
app = Flask(__name__)
n=[]
@app.route('/')
def uploader():
    a=request.args.get('h')
    if request.method=="GET":
       if a!=None and a!="":
          n.append('消息'+':'+a+'<br>')
       return(g(''.join(n)))
    else:
       return(g(''))
app.run(debug=True,host="0.0.0.0",port=3000)