from sympy import *
q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m=symbols('q w e r t y u i o p a s d f g h j k l z x c v b n m')
def hj(A):
    if A!="":
        a=expand(A)
        a=str(a)
        return(a.replace('⋅',''))
    else:
        return('None')
def ysfj(A):
    if A!="":
        a=factor(A)
        a=str(a)
        return(a.replace('⋅',''))
    else:
        return('None')
k='''
<!DOCTYPE html>
<html>
<head>
<style>
div{background-color:lightgreen;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div>
乘方:如x**2
乘法:如x*y
根号:如sqrt(x)
</div><br>
<p></p>
<div>
<form>
<p>化简,如(x+y)**2</p>
<input type="text" name="hj"></input>
</div>
<div>
<p>因式分解,如x**2-y**2</p>
<input type="text" name="ysfj"></input>
</div>
<div>
<input type="submit" value="开始"></input>
</form>
</div>
</body>
</html>
'''
from flask import *
import os
app = Flask(__name__)
d='''

'''
@app.route('/')
def uploader():
    a=request.args.get('hj')
    b=request.args.get('ysfj')
    if a!=None or b!=None:
       os.system('clear')
       return '<meta name="viewport" content="width=device-width, initial-scale=1">'+'已化简：'+hj(a)+'<br>'+'已因式分解：'+ysfj(b)+d
    return k
app.run(debug=True,host="0.0.0.0",port=4000)