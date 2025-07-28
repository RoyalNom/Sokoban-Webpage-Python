let columns = 15; let rows = 15; let colSize; let rowSize;
const size = 35; let board = [];
let timerStarted = false; let startingTime; let elapsedTime = 0;
let player; let cardboardbox; let goal;
let playerPos = [0, 0];
let canMove = true; let moves_amount = 0
let goals = Array(columns + 2).fill().map(() => Array(rows + 2).fill(false)); // Goals uses an Array of the coordinates, which is kept seperately from the board as goals layer under everything else
let completed_goals = 0; let total_goals = 0;
let json_config = {
  "boxes": [
    [1, 1],
    [3, 1],
    [1, 3],
    [3, 3],
  ],
  "goals": [
    [3, 12],
    [12, 3],
    [11, 11],
    [13, 13],
  ],
  "paths": [
  [
    0,
    0
  ],
  [
    0,
    1
  ],
  [
    0,
    2
  ],
  [
    0,
    3
  ],
  [
    0,
    4
  ],
  [
    0,
    5
  ],
  [
    0,
    6
  ],
  [
    0,
    8
  ],
  [
    0,
    9
  ],
  [
    0,
    10
  ],
  [
    0,
    11
  ],
  [
    0,
    12
  ],
  [
    0,
    13
  ],
  [
    0,
    14
  ],
  [
    1,
    0
  ],
  [
    1,
    1
  ],
  [
    1,
    2
  ],
  [
    1,
    3
  ],
  [
    1,
    4
  ],
  [
    1,
    5
  ],
  [
    1,
    6
  ],
  [
    1,
    8
  ],
  [
    1,
    9
  ],
  [
    1,
    10
  ],
  [
    1,
    11
  ],
  [
    1,
    12
  ],
  [
    1,
    13
  ],
  [
    1,
    14
  ],
  [
    2,
    0
  ],
  [
    2,
    1
  ],
  [
    2,
    2
  ],
  [
    2,
    3
  ],
  [
    2,
    4
  ],
  [
    2,
    5
  ],
  [
    2,
    6
  ],
  [
    2,
    8
  ],
  [
    2,
    9
  ],
  [
    2,
    10
  ],
  [
    2,
    11
  ],
  [
    2,
    12
  ],
  [
    2,
    13
  ],
  [
    2,
    14
  ],
  [
    3,
    0
  ],
  [
    3,
    1
  ],
  [
    3,
    2
  ],
  [
    3,
    3
  ],
  [
    3,
    4
  ],
  [
    3,
    5
  ],
  [
    3,
    6
  ],
  [
    3,
    7
  ],
  [
    3,
    8
  ],
  [
    3,
    9
  ],
  [
    3,
    10
  ],
  [
    3,
    11
  ],
  [
    3,
    12
  ],
  [
    3,
    13
  ],
  [
    3,
    14
  ],
  [
    4,
    0
  ],
  [
    4,
    1
  ],
  [
    4,
    2
  ],
  [
    4,
    3
  ],
  [
    4,
    4
  ],
  [
    4,
    5
  ],
  [
    4,
    6
  ],
  [
    4,
    8
  ],
  [
    4,
    9
  ],
  [
    4,
    10
  ],
  [
    4,
    11
  ],
  [
    4,
    12
  ],
  [
    4,
    13
  ],
  [
    4,
    14
  ],
  [
    5,
    0
  ],
  [
    5,
    1
  ],
  [
    5,
    2
  ],
  [
    5,
    3
  ],
  [
    5,
    4
  ],
  [
    5,
    5
  ],
  [
    5,
    6
  ],
  [
    5,
    8
  ],
  [
    5,
    9
  ],
  [
    5,
    10
  ],
  [
    5,
    11
  ],
  [
    5,
    12
  ],
  [
    5,
    13
  ],
  [
    5,
    14
  ],
  [
    6,
    0
  ],
  [
    6,
    1
  ],
  [
    6,
    2
  ],
  [
    6,
    3
  ],
  [
    6,
    4
  ],
  [
    6,
    5
  ],
  [
    6,
    6
  ],
  [
    6,
    8
  ],
  [
    6,
    9
  ],
  [
    6,
    10
  ],
  [
    6,
    11
  ],
  [
    6,
    12
  ],
  [
    6,
    13
  ],
  [
    6,
    14
  ],
  [
    7,
    3
  ],
  [
    7,
    12
  ],
  [
    8,
    0
  ],
  [
    8,
    1
  ],
  [
    8,
    2
  ],
  [
    8,
    3
  ],
  [
    8,
    4
  ],
  [
    8,
    5
  ],
  [
    8,
    6
  ],
  [
    8,
    8
  ],
  [
    8,
    9
  ],
  [
    8,
    10
  ],
  [
    8,
    11
  ],
  [
    8,
    12
  ],
  [
    8,
    13
  ],
  [
    8,
    14
  ],
  [
    9,
    0
  ],
  [
    9,
    1
  ],
  [
    9,
    2
  ],
  [
    9,
    3
  ],
  [
    9,
    4
  ],
  [
    9,
    5
  ],
  [
    9,
    6
  ],
  [
    9,
    8
  ],
  [
    9,
    9
  ],
  [
    9,
    10
  ],
  [
    9,
    11
  ],
  [
    9,
    12
  ],
  [
    9,
    13
  ],
  [
    9,
    14
  ],
  [
    10,
    0
  ],
  [
    10,
    1
  ],
  [
    10,
    2
  ],
  [
    10,
    3
  ],
  [
    10,
    4
  ],
  [
    10,
    5
  ],
  [
    10,
    6
  ],
  [
    10,
    8
  ],
  [
    10,
    9
  ],
  [
    10,
    10
  ],
  [
    10,
    11
  ],
  [
    10,
    12
  ],
  [
    10,
    13
  ],
  [
    10,
    14
  ],
  [
    11,
    0
  ],
  [
    11,
    1
  ],
  [
    11,
    2
  ],
  [
    11,
    3
  ],
  [
    11,
    4
  ],
  [
    11,
    5
  ],
  [
    11,
    6
  ],
  [
    11,
    8
  ],
  [
    11,
    9
  ],
  [
    11,
    10
  ],
  [
    11,
    11
  ],
  [
    11,
    12
  ],
  [
    11,
    13
  ],
  [
    11,
    14
  ],
  [
    12,
    0
  ],
  [
    12,
    1
  ],
  [
    12,
    2
  ],
  [
    12,
    3
  ],
  [
    12,
    4
  ],
  [
    12,
    5
  ],
  [
    12,
    6
  ],
  [
    12,
    7
  ],
  [
    12,
    8
  ],
  [
    12,
    9
  ],
  [
    12,
    10
  ],
  [
    12,
    11
  ],
  [
    12,
    12
  ],
  [
    12,
    13
  ],
  [
    12,
    14
  ],
  [
    13,
    0
  ],
  [
    13,
    1
  ],
  [
    13,
    2
  ],
  [
    13,
    3
  ],
  [
    13,
    4
  ],
  [
    13,
    5
  ],
  [
    13,
    6
  ],
  [
    13,
    8
  ],
  [
    13,
    9
  ],
  [
    13,
    10
  ],
  [
    13,
    11
  ],
  [
    13,
    12
  ],
  [
    13,
    13
  ],
  [
    13,
    14
  ],
  [
    14,
    0
  ],
  [
    14,
    1
  ],
  [
    14,
    2
  ],
  [
    14,
    3
  ],
  [
    14,
    4
  ],
  [
    14,
    5
  ],
  [
    14,
    6
  ],
  [
    14,
    8
  ],
  [
    14,
    9
  ],
  [
    14,
    10
  ],
  [
    14,
    11
  ],
  [
    14,
    12
  ],
  [
    14,
    13
  ],
  [
    14,
    14
  ]
],
  "player": [0, 0]
}
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