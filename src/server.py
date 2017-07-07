from lib.game import Game

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.debug=True
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
        global game
        game = Game(request.form['letter'])
        return request.form['letter']


@app.route('/play')
def play():
    turn = game.getInitialMove()
    if turn == 'Bot':
        game.makeMove(game.getBotMove(), game.getBotSymbol())
    return jsonify({'board': game.getBoard()})


@app.route('/playerMove',methods=['GET','POST'])
def takePlayerMove():
    if request.method == 'POST':
        game.makeMove(int(request.form['move']),game.getUserSymbol())
        game.makeMove(game.getBotMove(), game.getBotSymbol())
        res = {'over' : False,'board' : game.getBoard()}
        if game.isWinner(game.getBotSymbol()):
            res['over'] = True
            res['winner'] = 'computer'
        if game.isWinner(game.getUserSymbol()):
            res['over'] = True
            res['winner'] = 'player'
        if game.isBoardFull():
            res['over'] = True
            res['tie'] = True
        return jsonify(res)


if __name__ == '__main__':
    app.run()
