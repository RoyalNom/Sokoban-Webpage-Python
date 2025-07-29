let columns = 15; let rows = 15; let colSize; let rowSize;
const size = 35; let board = [];
let timerStarted = false; let startingTime; let elapsedTime = 0;
let player; let cardboardbox; let goal;
let playerPos = [0, 0];
let canMove = true; let moves_amount = 0
let goals = Array(columns + 2).fill().map(() => Array(rows + 2).fill(false)); // Goals uses an Array of the coordinates, which is kept seperately from the board as goals layer under everything else
let completed_goals = 0; let total_goals = 0;

let gameWon = false;
// Undo Redo Logic
let moveStack = [];
let redoStack = [];

// Some abstractions to concider
//WALL = 1;
//EMPTY = 0;
//BOX = -1;
//PLAYER = -3;
//GOAL = -2;

function setup() {
  console.log(json_config);
  createCanvas((columns + 2) * size, (rows + 2) * size);
  colSize = width/ (columns + 2);
  rowSize = height/(rows + 2);
  for (let i = 0; i<columns + 2; i++){
    board[i] = [];
    for (let j=0; j<rows + 2; j++){
      board[i][j] = 1;
    }
  }
  let pathPositions = json_config.paths;
  let boxPositions = json_config.boxes;
  let goalPositions = json_config.goals;
  let PlayerPosition = [json_config.player];
  placePaths(pathPositions);
  placeCardboardBoxes(boxPositions);
  createGoals(goalPositions);
  placePlayer(PlayerPosition);
  startingTime = millis();
}

function draw() {
  background(220);
  displayBoard();
  document.getElementById("moveCounter").textContent = `Moves: ${moves_amount}`;
  if (timerStarted) {
    elapsedTime = (millis() - startTime) / 1000;
    document.getElementById("timer").textContent = `Time: ${elapsedTime.toFixed(1)}s`;
  }
  checkgoals()
  if (gameWon) {
    fill(0, 255, 0);
    textSize(48);
    textAlign(CENTER, CENTER)
    text("YOU WON!", width / 2, height / 2);
  }
  if (
    !keyIsDown(LEFT_ARROW) &&
    !keyIsDown(RIGHT_ARROW) &&
    !keyIsDown(UP_ARROW) &&
    !keyIsDown(DOWN_ARROW)
  ) {
    canMove = true;
  }
} 

//function displayBoard()

//function placeCardboardBoxes(boxCoords)

//function checkgoals()

function resetGame(){
  location.reload();
}

function keyPressed(){
  if (!canMove) return;
  let dx = 0;
  let dy = 0;
  
  // Key detection
  if (keyCode === LEFT_ARROW) dx = -1;
  else if (keyCode === RIGHT_ARROW) dx = 1;
  else if (keyCode === UP_ARROW) dy = -1;
  else if (keyCode === DOWN_ARROW) dy = 1;
  else if (key === 'z' || key === 'Z') {
    undoMove();
    return;
  }
  else if (key === 'x' || key === 'X') {
    redoMove();
    return;
  }
  
  if (dx !== 0 || dy !== 0) {
    let [x, y] = playerPos;
    let newX = x + dx;
    let newY = y+ dy;
    
    // Out of bounds check
    if (newX < 1 || newX >= columns + 1 || newY < 1 || newY >= rows + 1) return;
    
    // Move if the cell is empty
    if (board[newX][newY] === 0 || board[newX][newY] === -2) {
      if (goals[x][y]) {
        board[x][y] = 0; // Leave goal tile empty
      } else {
        board[x][y] = 0;
      }
      board[newX][newY] = -3;
      playerPos = [newX, newY];
      moveStack.push({
        playerPos: [x, y],
        boxPositions: null
      });
      redoStack = [];
      if (!timerStarted) {
        timerStarted = true;
        startTime = millis();
      }
      moves_amount++;
      canMove = false;
    } 
    // Box logic
    else if (board[newX][newY] === -1) {
      let boxNewX = newX + dx;
      let boxNewY = newY + dy;
      if (
        boxNewX >= 0 && boxNewX < columns &&
        boxNewY >= 0 && boxNewY < rows &&
        (board[boxNewX][boxNewY] === 0 || board[boxNewX][boxNewY] === -2)
      ) {
        board[boxNewX][boxNewY] = -1;
        board[newX][newY] = -3;
        board[x][y] = 0;
        playerPos = [newX, newY];
        moveStack.push({
          playerPos: [x, y],
          boxPositions: [[newX, newY], [boxNewX, boxNewY]],
        });
        redoStack = [];
        if (!timerStarted) {
          timerStarted = true;
          startTime = millis();
        }
        moves_amount++;
        canMove = false;
      }
  }
}

//function undoMove() {

}