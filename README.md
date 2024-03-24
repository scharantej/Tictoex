## Flask Application Design for Tic Tac Toe Website

### HTML Files

1. **index.html:** The main page of the website, containing the HTML structure and JavaScript for the tic tac toe game.
2. **game.html:** The page that displays the game board and handles player moves.

### Routes

1. **@app.route('/')**: The route for the index page.
2. **@app.route('/game')**: The route for the game page.
3. **@app.route('/move', methods=['POST'])**: The route to handle player moves and update the game state.
4. **@app.route('/check_winner', methods=['POST'])**: The route to check for a winner and return the appropriate message.