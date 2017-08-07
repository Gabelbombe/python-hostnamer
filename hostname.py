import socket
import SocketServer

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 8080


class TheHandler(BaseHTTPRequestHandler):

    def do_get(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(socket.gethostname())
        return


try:
    httpd = SocketServer.TCPServer(("", PORT), TheHandler)
    print "serving at port", PORT
    httpd.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    httpd.socket.close()
