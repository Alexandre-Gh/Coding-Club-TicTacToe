# ❌⭕ Tic-Tac-Toe Workshop Documentation

## 📌 Description
In this workshop, you will build the classic **Tic-Tac-Toe game** using Python and run it directly on your computer.  
Along the way, you’ll learn core programming concepts such as variables, functions, arrays, conditions, and game logic.

By the end, you’ll have:
- A fully playable game  
- A better understanding of how interactive programs work  

**Language used:** Python

---

## 🧰 Prerequisites
- A laptop *(can be provided during offline sessions)*
- A code editor such as [Visual Studio Code](https://code.visualstudio.com/Download) or similar
- [Python 3.13](https://www.python.org/ftp/python/3.13.13/python-3.13.13-amd64.exe) installed on your computer
- PyGame installed on your computer (see `install-pygame.bat` script in repository)
- The project repository downloaded and ready

---

## ⚠️ Before you start
At the end of this document, you will see a list of functions already set up for you to use in this project, don’t forget to use them!

## 🚀 Steps

### 1. Change Window Size  
**Concept:** Variables & running a file  

When you launch the project, you will see the window is very small. This is not ideal...

Modify the variables controlling the game window size and execute the Python file.

**You’ll learn:**
- How to change variable values  
- How to run a Python program  

---

### 2. Draw Grid  
**Concept:** Functions & global variables  

Draw the Tic-Tac-Toe grid on the screen.

**You’ll learn:**
- How to call functions  
- How global variables can be reused throughout the program  

---

### 3. Detect Click  
**Concept:** Function arguments  

Detect where the player clicks on the grid.

**You’ll learn:**
- How functions receive arguments  
- How mouse positions can be used in a game  

---

### 4. Track Turns  
**Concept:** `if` / `else` conditions  

Switch between players after each turn.

**You’ll learn:**
- How conditional statements work  
- How to control game flow  

---

### 5. Modify Field  
**Concept:** Arrays (lists)  

Store and update the game board values.

**You’ll learn:**
- How to use arrays/lists  
- How to modify values inside a list  

---

### 6. Draw Field  
**Concept:** Writing functions  

Display the current game state visually.

**You’ll learn:**
- How to create reusable functions  
- How to separate logic from rendering  

---

### 7. Check for Win  

Detect when a player has won the game.

**You’ll learn:**
- How to compare multiple values  
- How win conditions are checked in games  

---

### 8. Check for Draw  

Detect when no more moves are possible.

**You’ll learn:**
- How to detect special game states  
- How to combine multiple conditions  

---

### 9. Draw End Screen and End Game  

Display the result screen and stop the game.

**You’ll learn:**
- How to end a game loop  
- How to display final results to the player  

---

## 🧩 Available Functions

These functions are provided to allow you to perform certain actions, such as drawing visuals or handling game logic.

You are free to use them.

```python
# Drawing functions

drawGrid(screen, colour, windowSize, horizontalLines, verticalLines, lineWidth)
# Draws the Tic-Tac-Toe grid

drawCircle(screen, colour, positionX, positionY, radius)
# Draws a circle symbol

drawCross(screen, colour, positionX, positionY, sideLength, lineWidth)
# Draws a cross symbol

drawEndScreen(screen, text, bgColour, winSize)
# Displays the end screen with the game result


# Game logic functions

createEndScreenText(text, colour)
# Creates styled text for the end screen

noMoreSpace(field)
# Returns True if no empty spaces remain on the board

printField(field)
# Prints the current game field in the console
```

## 💡 Don’t worry if everything doesn’t work immediately, debugging is part of programming.
