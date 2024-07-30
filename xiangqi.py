k='''
<DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js">
</script>
<script> 
$(document).ready(function(){
$('#i').click(function(){
var i=0;    
$(document).click(function(e){
var x=e.pageX;
var y=e.pageY;
$('p').html(x+"   "+y);
$('#i').animate({left:x-25,top:y-25},50);
i++;
if(i==2){
$(document).unbind();}
});});


$('#o').click(function(){
var kk=0;    
$(document).click(function(e){
var x=e.pageX;
var y=e.pageY;
$('p').html(x+"   "+y);
$('#o').animate({left:x-25,top:y-25},50);
kk++;
if(kk==2){
$(document).unbind();}
});});
});
</script>
<img src="https://img2.baidu.com/it/u=2284219779,2043610498&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=542"></img>
<img id="i" width="50" height="50" src="https://img.88tph.com/production/20180123/12482266-1.jpg!/watermark/url/L3BhdGgvbG9nby5wbmc/align/center/fw/640/quality/70" style="position:absolute;">
</img><br><br><br>
<img id="o" width="50" height="50" src="https://img.88tph.com/production/20180123/12482266-1.jpg!/watermark/url/L3BhdGgvbG9nby5wbmc/align/center/fw/640/quality/70" style="position:absolute;">
</img>
</body>
</html>
'''
from flask import *
app = Flask(__name__)

@app.route('/')
def uploader():
    return k
app.run(debug=True,host="0.0.0.0",port=4000)