# from os import getcwd
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#
# PORT_NUMBER = 8080
#
#
# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/":
#             self.path = "templates/index.html"
#         elif self.path == "/game":
#             self.path = "templates/game.html"
#         else:
#             self.path =""+ self.path
#
#         try:
#             file = open(getcwd() + '/' + self.path)
#             self.send_response(200)
#             self.end_headers()
#             self.wfile.write(file.read())
#             file.close()
#             return
#
#         except IOError:
#             self.send_error(404, 'File Not Found: %s' % self.path)
#
#
# server = HTTPServer(('', PORT_NUMBER), MyHandler)
# print 'Started httpserver on port ', PORT_NUMBER
# server.serve_forever();

from src.lib.game import Game
from flask import Flask, url_for, render_template, request

app = Flask(__name__)
game = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def show_game():
    return render_template('game.html')


@app.route('/letter', methods=['GET', 'POST'])
def giveCommentResponse():
    if request.method == 'POST':
        game = Game(request.form['letter'])
        return request.form['letter']


if __name__ == '__main__':
    app.run()
