
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the game state
board = [["", "", ""], ["", "", ""], ["", "", ""]]
turn = "X"
winner = None

# Main page route
@app.route('/')
def index():
    return render_template('index.html')

# Game page route
@app.route('/game')
def game():
    global board, turn
    return render_template('game.html', board=board, turn=turn)

# Move handling route
@app.route('/move', methods=['POST'])
def move():
    global board, turn, winner

    # Get the move data from the request
    row = int(request.form['row'])
    col = int(request.form['col'])

    # Check if the move is valid
    if board[row][col] == "":
        board[row][col] = turn
        
        # Check for a winner
        winner = check_winner()
        
        # Switch turns
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    # Redirect to the game page
    return redirect(url_for('game'))

# Winner checking function
def check_winner():
    global board

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    # Check for a tie
    if all(all(row) for row in board):
        return "Tie"

    # No winner yet
    return None

if __name__ == '__main__':
    app.run(debug=True)
