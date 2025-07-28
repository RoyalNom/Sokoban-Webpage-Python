// Placement functions
function placeCardboardBoxes(boxCoords) {
  for (let coord of boxCoords) { // coord instead of box since that is already a function in JS
    let x = coord[0] + 1;
    let y = coord[1] + 1;
    board[x][y] = -1;
  }
}
function createGoals(goalCoords) {
  for (let goal of goalCoords) {
    let x = goal[0] + 1;
    let y = goal[1] + 1;
    goals[x][y] = true;
    total_goals++;
  }
}
function placePlayer(playerCoords) {
  for (let Player of playerCoords) {
    let x = Player[0] + 1;
    let y = Player[1] + 1;
    playerPos = [x, y];
    board[x][y] = -3;
  }
}
function placePaths(pathCoords) {
  for (let Path of pathCoords) {
    let x = Path[0] + 1;
    let y = Path[1] + 1;
    board[x][y] = 0
  }
}

function displayBoard(){
  for (let i=0; i< columns + 2; i++){
    for (let j=0; j< rows + 2; j++){
      
      if (board[i][j] === -1 && goals[i][j]) {
        fill(0, 255, 0); // Box on goal = green
      } else if (board[i][j] === -1) {
        fill(0, 0, 255); // Box
      } else if (goals[i][j]) {
        fill(255, 0, 0); // Goal tile
      } else if (board[i][j] === -3 && goals[i][j]) {
        fill(255, 0, 0); // Player on red background
      } else if (board[i][j] === 0 || board[i][j] === -3) {
        fill(255)// White
      } else {
        fill(0); // Black
      }
      
      rect(i * colSize, j * rowSize, colSize, rowSize)
      
      if (board[i][j] == -3) {
        fill(0, 255, 0); // Player
        let x = i * colSize;
        let y = j * rowSize;
        triangle(
          x + colSize / 2, y + rowSize / 4,         // Top point
          x + colSize / 4, y + rowSize * 3 / 4,      // Bottom left
          x + colSize * 3 / 4, y + rowSize * 3 / 4   // Bottom right
        );
      } 
    }
  }
}

// Win condition function
function checkgoals() {
  if (gameWon) return;
  completed_goals = 0;
  
  // Check grid and array for a completed goal
  for (let i = 0; i < columns; i++) {
    for (let j = 0; j < rows; j++) {
      if (goals[i][j] && board[i][j] === -1) {
        completed_goals++;
      }
    }
  }
  // Check for win condition
  if (completed_goals === total_goals) {
    gameWon = true;
    noLoop(); // Stop the draw loop
    console.log(" You win!");
    const winMsg = document.getElementById("winMessage");
    if (winMsg) winMsg.textContent = " Score Has Been Saved to database...";
  }
}

// Functions for redoing and undoing moves
function undoMove() {
  if (moveStack.length === 0) return;
  let lastState = moveStack.pop();
  
  // Clear the current player
  let [currX, currY] = playerPos;
  board[currX][currY] = 0;
  
  // Restore player to the old position
  let [oldX, oldY] = lastState.playerPos;
  board[oldX][oldY] = -3;
  playerPos = [oldX, oldY];
  
  // if a box was moved, move it back
  if (lastState.boxPositions) {
    let [oldBoxPos, newBoxPos] = lastState.boxPositions;
    board[newBoxPos[0]][newBoxPos[1]] = 0;
    board[oldBoxPos[0]][oldBoxPos[1]] = -1;
    redoStack.push({
            playerPos: [currX, currY],
            boxPositions: [[newBoxPos[0], newBoxPos[1]], [oldBoxPos[0], oldBoxPos[1]]]
    }); 
  } else {
    redoStack.push({
    playerPos: [currX, currY],
    boxPositions: null
  });
  }
  
  moves_amount--;
}
function redoMove(){
  if (redoStack.length === 0) return;
  let nextState = redoStack.pop();
  let undoBoxPositions = null;
  
  // if a box was moved, move it back
  // happens in reverse order from undo, since a box needs to move 
  // before the player can go to that spot
  if (nextState.boxPositions) {
    let [oldBoxPos, newBoxPos] = nextState.boxPositions;
    board[oldBoxPos[0]][oldBoxPos[1]] = -1;
    board[newBoxPos[0]][newBoxPos[1]] = 0;
    
    undoBoxPositions = [[newBoxPos[0], newBoxPos[1]], [oldBoxPos[0], oldBoxPos[1]]];
  }
  
  // Clear the current player
  let [currX, currY] = playerPos;
  board[currX][currY] = 0;

  // Restore player to the old position
  let [newX, newY] = nextState.playerPos;
  board[newX][newY] = -3;
  playerPos = [newX, newY];
  
  moveStack.push({
    playerPos: [currX, currY],
    boxPositions: undoBoxPositions
  })

  moves_amount++;
}