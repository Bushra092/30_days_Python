from http.server import HTTPServer, BaseHTTPRequestHandler
import time
HOST = 'localhost'
PORT = 9999


class firstHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes('<html><body><h1>HELLO WORLD</h1></body></html>','utf-8'))

def do_POST(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    self.wfile.write(bytes('{"Time" :"' + date + '"}','utf-8'))


server = HTTPServer ((HOST, PORT), firstHTTP)
print('Server now running......')
server.serve_forever()
server.server_close()
print('Server Stopped!')