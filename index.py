from flask import Flask, request
import requests
import json
import re

app = Flask(__name__)

@app.route("/c/r", methods=["GET"])
def randomMail():
    login = requests.get("https://randomuser.me/api?nat=US")
    first = json.loads(login.text)["results"][0]["name"]["first"]
    last = json.loads(login.text)["results"][0]["name"]["last"]
    name = str(first)+str(last)
    getDomain = requests.get("https://api.mail.tm/domains").text
    domain = json.loads(getDomain)['hydra:member'][0]['domain']
    create_req = requests.post("https://api.mail.tm/accounts", json={"address": str(name)+'@'+domain,"password": "Cc14024578f214@"})

    if '201' in str(create_req):
        created_mail = json.loads(create_req.text)['address']
        result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/> <meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: -apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif; font-size: 20px;}body{background-color: #F3F4F6;}.sep{height: 5px; background-color: #d4d6d8; margin-top: 10px; border-radius: 6px;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.h{color: red;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.button-9{appearance: button; backface-visibility: hidden; background-color: #405cf5; border-radius: 6px; border-width: 0; box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0; box-sizing: border-box; color: #fff; cursor: pointer; font-family: -apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif; font-size: 100%; height: 44px; line-height: 1.15; margin: 12px 0 0; outline: none; overflow: hidden; padding: 0 25px; position: relative; text-align: center; text-transform: none; transform: translateZ(0); transition: all .2s,box-shadow .08s ease-in; user-select: none; -webkit-user-select: none; touch-action: manipulation;}.button-9:disabled{cursor: default;}.button-9:focus{box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset, rgba(50, 50, 93, .2) 0 6px 15px 0, rgba(0, 0, 0, .1) 0 2px 2px 0, rgba(50, 151, 211, .3) 0 0 0 4px;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="banner" role="banner"> <p>Reload this page to create new email address <br>Tải lại trang này để tạo email mới</p></div><div class="container"> <div class="email"> <p>Email: '''+created_mail+'''</p><a href="https://nqdung.com/m/'''+created_mail+'''" target="_blank"> <button class="button-9" role="button">View Message here!</button> </a> </div><div class="sep"></div><br><div class="notice" id="en"> <p class="h">Notice</p><p>There is no way you can get your email back. Your email is being generated during your browsing and it is being stored encrypted. You must save the email before closing the browser. There will be no way to get your email back if you don't save it. We are not responsible for this issue.</p></div><div class="notice" id="vi"> <p class="h">Lưu ý: </p><p>Không có cách nào bạn có thể lấy lại email của bạn. Email của bạn đang được tạo ra trong quá trình duyệt của bạn và nó đang được lưu trữ mã hóa. Bạn phải lưu email trước khi tắt trình duyệt. Sẽ không có cách nào lấy lại email của bạn nếu bạn không lưu. Chúng tôi không chịu trách nhiệm về vấn đề này.</p></div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
        result = result
    elif '200' not in str(create_req):
        catch_err = json.loads(create_req.text)["hydra:description"]
        if 'This value is already used.' in str(catch_err) or '422' in str(create_req):
            result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif;}body{background-color: #F3F4F6;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.res{height: 30vmax; position: relative;}.res h2{margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #0FFF50; font-size: 5em; line-height: 1em;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="banner" role="banner"> <p>Reload this page to create new email address <br>Tải lại trang này để tạo email mới</p></div><div class="container"> <div class="res"> <h2>This value is already used.</h2> </div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
        else:
            result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif;}body{background-color: #F3F4F6;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.res{height: 40vmax; position: relative;}.res h2{margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #0FFF50; font-size: 5em; line-height: 1em;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="banner" role="banner"> <p>Reload this page to create new email address <br>Tải lại trang này để tạo email mới</p></div><div class="container"> <div class="res"> <h2>An error occurred.</h2> </div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
    else:
        result = create_req.text
    return result

@app.route("/c/<user>", methods=["GET"])
def createMail(user):
    getDomain = requests.get("https://api.mail.tm/domains").text
    domain = json.loads(getDomain)['hydra:member'][0]['domain']
    create_req = requests.post("https://api.mail.tm/accounts", json={"address": user+'@'+domain,"password": "Cc14024578f214@"})

    if '201' in str(create_req):
        created_mail = json.loads(create_req.text)['address']
        result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif; font-size: 20px;}body{background-color: #F3F4F6;}.sep{height: 5px; background-color: #d4d6d8; margin-top: 10px; border-radius: 6px;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.h{color: red;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="banner" role="banner"> <p>Reload this page to create new email address <br>Tải lại trang này để tạo email mới</p></div><div class="container"> <div class="email"> <p>Email: '''+created_mail+'''</p></div><div class="sep"></div><br><div class="notice" id="en"> <p class="h">Notice: </p><p>There is no way you can get your email back. Your email is being generated during your browsing and it is being stored encrypted. You must save the email before closing the browser. There will be no way to get your email back if you don't save it. We are not responsible for this issue.</p></div><div class="notice" id="vi"> <p class="h">Lưu ý: </p><p>Không có cách nào bạn có thể lấy lại email của bạn. Email của bạn đang được tạo ra trong quá trình duyệt của bạn và nó đang được lưu trữ mã hóa. Bạn phải lưu email trước khi tắt trình duyệt. Sẽ không có cách nào lấy lại email của bạn nếu bạn không lưu. Chúng tôi không chịu trách nhiệm về vấn đề này.</p></div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
    elif '200' not in str(create_req):
        catch_err = json.loads(create_req.text)["hydra:description"]
        if 'This value is already used.' in str(catch_err) or '422' in str(create_req):
            result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif;}body{background-color: #F3F4F6;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.res{height: 30vmax; position: relative;}.res h2{margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #0FFF50; font-size: 5em; line-height: 1em;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="container"> <div class="res"> <h2>This value is already used.</h2> </div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
        else:
            result = '''<!DOCTYPE html><html lang="en"><head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif;}body{background-color: #F3F4F6;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.res{height: 30vmax; position: relative;}.res h2{margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #0FFF50; font-size: 5em; line-height: 1em;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style></head><body> <div class="banner" role="banner"> <p>Reload this page to create new email address <br>Tải lại trang này để tạo email mới</p></div><div class="container"> <div class="res"> <h2>An error occurred.</h2> </div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>'''
    else:
        result = create_req.text
    return result

@app.route("/s", methods=["GET"])
def getstock():
    code = request.args.get("t", default="", type=str)
    res = requests.get("https://api.hotmailbox.me/mail/currentstock").text
    sum_hotmail = json.loads(res)["Data"][0]['Instock']
    sum_outlook = json.loads(res)["Data"][1]['Instock']
    if 'hotmail' in code:
        stock = {
            "hotmail_instock": sum_hotmail
        }
    elif 'outlook' in code:
        stock = {
            "outlook_instock": sum_outlook
        }
    return json.dumps(stock)

@app.route("/hm/input", methods=["GET"])
def hm():
    key = request.args.get("key", default="", type=str)
    if key == "32dabd13-a5c4-41ae-8862-f9275ea3b8cf":
        res = requests.get("https://api.hotmailbox.me/mail/currentstock").text
        hm = json.loads(res)["Data"][0]['Instock']
        result = {
            "sum": int(hm)
        }
    return result

@app.route("/ol/input", methods=["GET"])
def ol():
    key = request.args.get("key", default="", type=str)
    if key == "32dabd13-a5c4-41ae-8862-f9275ea3b8cf":
        res = requests.get("https://api.hotmailbox.me/mail/currentstock").text
        ol = json.loads(res)["Data"][1]['Instock']
        result = {
            "sum":int(ol)
        }
    return result

@app.route("/m/<mail>", methods=["GET"])
def getCode(mail):
    try:
        res = requests.Session()
        res.headers.update({'Content-Type': 'application/json'})
        res.headers.update({'Connection': 'keep-alive'})
        login = res.post("https://api.mail.tm/token", json={"address":str(mail),"password":"Cc14024578f214@"})
        token = json.loads(login.text)["token"]
        res.headers.update({'Authorization': 'Bearer ' + str(token)})
        getMessages = res.get("https://api.mail.tm/messages")
        id0 = json.loads(getMessages.text)["hydra:member"][0]["id"]
        getText = res.get('https://api.mail.tm/messages/'+ id0)
        content = json.loads(getText.text)["text"]
        fromAdress = json.loads(getText.text)["from"]['address']
        fromName = json.loads(getText.text)["from"]['name']
        toAdress = json.loads(getText.text)["to"][0]['address']
        toName = json.loads(getText.text)["to"][0]['name']
        subject = json.loads(getText.text)["subject"]
        content = json.loads(getText.text)["text"]
        
        content = content.split('\n')
        for i, value in enumerate(content):
            if "http" in value:
                web = re.search("(?P<url>https?://[^\s]+)", value).group("url")
                new_content = f'<a href="{web}" target="_blank">{web}</a>'
                content[i] = re.sub("(|)|[|].|]|{|}", "", new_content)
        content ="<br>".join(content)

        result = """<!DOCTYPE html><html lang="en"> <head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/><meta charset="UTF-8"> <title>ND Shop</title> <style>*{font-family: 'Roboto',sans-serif;}a{word-wrap: break-word;}body{background-color: #F3F4F6;}.content br{ content: ""; margin: 0.75em; display: block; font-size: 100%;}.sep{height: 5px; background-color: #d4d6d8; margin-top: 10px; border-radius: 6px;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.info-table{color:#4f46e5; font-size:18px; font-weight:500; line-height:24px; font-weight: 600; text-align: left;}.content{line-height:24px; padding:20px 24px; font-size: 18px;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style> </head> <body> <div class="banner" role="banner"> <p>Reload this page to get the latest messages <br>Tải lại trang này để nhận tin nhắn mới nhất</p></div><div class="container"> <div class="mailbox"> <table class="info-table"> <tr> <th>From: </th> <td>"""+fromName +" ["+ fromAdress +"]" +"""</td></tr><tr> <th>To: </th> <td>"""+toName+" ["+toAdress+ "]"+"""</td></tr><tr> <th>Subject: </th> <td>"""+subject+"""</td></tr></table> <div class="sep"></div><p class="content">"""+content+"""</p></div></div><footer> &copy; 2023 ND Shop | nqdung.com </footer></body></html>"""
    except:
        result = '''<!DOCTYPE html><html lang="en"> <head> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/> <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/pEvk/ndshop/main/favicon.ico"/> <meta charset="UTF-8"/> <title>ND Shop</title> <style>*{font-family: "Roboto", sans-serif;}body{background-color: #f3f4f6;}.container{background-color: #ffffff; border-radius: 6px; box-shadow:#000000 0px 0px 0px 0px; line-height: 24px; margin: 10px 30px 30px 30px; padding: 20px 24px}.res{height: 30vmax; position: relative;}.res h2{margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #0fff50; font-size: 5em; line-height: 1em;}footer{margin-right: auto !important; color: #adb5bd !important; text-align: center !important;}.banner{display: block; background-color: #A9A9A9; border-radius: 6px; /* margin: 0px 30px 0px 30px; */ width: fit-content; position: relative; margin: 0 auto;}.banner p{padding: 5px; color: #0fff50; font-weight: bold; position: relative; text-align: center; text-transform: none; font-size: 20px;}</style> </head> <body> <div class="banner" role="banner"> <p>Reload this page to get the latest messages <br>Tải lại trang này để nhận tin nhắn mới nhất</p></div><div class="container"> <div class="res"><h2>No Message.</h2></div></div><footer>&copy; 2023 ND Shop | nqdung.com</footer> </body></html>'''
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0")
