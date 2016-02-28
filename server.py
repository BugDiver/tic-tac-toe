from os import getcwd
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		if self.path=="/":
			self.path="public/index.html"
		else:
			self.path = "public/"+self.path

		try:
			file = open(getcwd() +'/'+self.path) 
			self.send_response(200)
			self.end_headers()
			self.wfile.write(file.read())
			file.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)


server = HTTPServer(('', PORT_NUMBER), myHandler)
print 'Started httpserver on port ' , PORT_NUMBER	
server.serve_forever();