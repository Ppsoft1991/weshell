import itchat,time
import os


def comm_pwd():
    return os.popen('pwd', mode='r').read()

def exit():
    time.sleep(3)
    os._exit(0)

def wrong(cmd):
    return f'bash: {cmd}: command not found'

def sendMessage(message,id):
    itchat.send(msg=message,toUserName=id)

@itchat.msg_register(itchat.content.TEXT)
def do_shell(msg):
    text = msg.text
    if text == 'exit':
        #exit()
        sendMessage('Bye',msg['FromUserName'])
    elif text[:2] == 'cd':
        os.chdir(text[3:])
        sendMessage(comm_pwd(), msg['FromUserName'])
    elif 'cat' in text:
        sendMessage('Access Denied', msg['FromUserName'])
    elif 'tac' in text:
        sendMessage('Access Denied', msg['FromUserName'])
    else:
        response = os.popen(text, mode='r').read()
        if response == '' or response == None:
            sendMessage(wrong(text), msg['FromUserName'])
        else:
            sendMessage(response, msg['FromUserName'])


itchat.auto_login(True,enableCmdQR=True)
itchat.run()