# 임의의 수신자에게 전자메일을 보내는 간단한 메일 클라이언트
# (i) 메일 서버(로컬서버, '127.0.0.1')와 TCP 연결을 설정
# (ii) SMTP 프로토콜을 이용하여 대화를 나누고 (강의자료 2장 53페이지 참조, 최소 sample SMTP interaction 내용은 반드시 포함) 
# (iii) 메일 서버를 통해 수신자에게 전자메일을 보내고 (메일 서버 코드(파이썬)는 첨부 파일 확인)
# (iv) 마지막으로 메일 서버와의 TCP 연결을 종료함

from socket import*

serverPort = 12000 # 포트번호
serverName = "127.0.0.1" # 서버의 주소
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP socket 생성
clientSocket.connect((serverName,serverPort)) # 서버와 TCP 연결

# <SMTP interaction>
# HELO DESKTOP-QFBCA5B
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '220':
        msg = input('C: ')
        clientSocket.send(msg.encode())
except:
    print('220 error.')

# MAIL FROM: <alice@crepes.fr>
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '250':
        msg = input('C: ')
        clientSocket.send(msg.encode())
except:
    print('250 error.')
    
# RCPT TO: <bob@hamburger.edu>
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '250':
        msg = input('C: ')
        clientSocket.send(msg.encode())
except:
    print('250 error.')    
    
# DATA
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '250':
        msg = input('C: ')
        clientSocket.send(msg.encode())
except:
    print('250 error.')

# persistent DATA & .
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '354':
        while True:
            msg = input('C: ')
            clientSocket.send(msg.encode())
            if (msg=='.'):
                break
            replymsg = clientSocket.recv(1024).decode()
except:
    print('354 error.')
    
# QUIT
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '250':
        msg = input('C: ')
        clientSocket.send(msg.encode())
except:
    print('250 error.')

# 221 msg -> connection close
try:
    replymsg = clientSocket.recv(1024).decode()
    if replymsg[:3] == '221':
        clientSocket.close() # TCP 연결 종료
except:
    print('221 error.')
