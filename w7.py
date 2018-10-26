# 導入 Flask 類別
from flask import Flask
'''
If you are using a single module (as in this
example), you should use __name__ because depending on if it’s started as application
or imported as module the name will be different ('__main__' versus
the actual import name). This is needed so that Flask knows where to look for
templates, static files, and so on. For more information have a look at the Flask
documentation.
'''
# 利用 Flask 類別建立 app 案例
app = Flask(__name__)
 
'''
The route decorator is used to register a view function for a given URL rule.
This does the same thing as add_url_rule() but is intended for decorator.
'''
# 利用 decorator 設定 URL 連結
@app.route('/')
def hello_world():
    # 傳回字串
    return 'W7, Hello, World!'

@app.route('/w8')
def hello_world8():
    # 傳回字串
    return 'W8, Hello, World!'
 
 
# app 在本機埠號 5000 執行, 且開啟 debug 模式
app.run(host='127.0.0.1', port=5000, debug=True)