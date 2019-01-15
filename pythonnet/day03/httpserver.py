from socket import *

#接收request 发送response
def handleClient(connfd):
    request = connfd.recv(4096)
    #将request按行分割
    request_lines = request.splitlines()
    #查看请求的每一行
    for line in request_lines:
        print(line)
    try:
        f = open('index.html')
    except Exception:
        response="HTTP/1.1 404 Not Found\r\n"
        response+="Content-Type: text/html\r\n"
        response+='\r\n'
        response+="<h1>Sorry the page not found!</h1>"
    else:
        response="HTTP/1.1 200 OK\r\n"
        response+="Content-Type: text/html\r\n"
        response+='\r\n'
        response+=f.read()
    finally:
        #将结果给客户端
        connfd.send(response.encode())

#创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(\
    SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(5)
    print("Listen the port 8000...")
    while True:
        connfd,addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()

main()