# Introduction to Programming in Python and Project Tutorial

This project is the starting point of a small Tic-Tac-Toe game. Some parts of the game are already handled for you, such as the methods used to draw on the screen.

This document presents how variables, lists, conditions, and functions work in Python in order to get started.

It is highly encouraged to search for resources online or tutorials about Python and programming in general.

---

## Variables: storing data

A **variable** is used to store data that your program can use later.

In Python, variables are created by assigning a value with `=`.

```python
size = 30
```

This line can be separated into multiple parts:

- `size` is the name of the variable
- `=` assigns a value to the variable
- `30` is the stored value

---

### Choosing a variable name

Variable names should describe what the value represents.

Example:

```python
status = 'playing'
endScreenText = None
turn = 'Player1'
```

A clear variable name makes code easier to read and understand.

---

### Variables can change

Variables can be modified later.

```python
turn = 'Player1'

turn = 'Player2'
```

Here, the value stored in `turn` changes over time.

---

## Lists: storing multiple values

A variable can also store multiple values using a **list**.

```python
field = [0, 0, 0]
```

You can modify values inside the list:
```python
field[0] = 1


You can even store lists inside of lists!

```python
field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

field[0][0] = 1

```


---

## Conditions: making decisions

Games often need to make decisions depending on what happens.

Python uses `if` and `else` statements for this.

Example:

```python
if (a == 1):
    print("Hello")
else:
    print("Goodbye")
```

---

## Functions: reusable blocks of code

A **function** is a reusable block of code that performs a task.

Functions are useful because they allow the same code to run multiple times without rewriting it.

Here is a complete example:

```python
result = 0  # External variable for this example

def addNumbers(a, b):
    global result
    result = a + b
```

This function can be separated into several parts:

- `def` tells Python that a function is being created
- `addNumbers` is the name of the function
- `a` and `b` are called **parameters**
- `:` starts the function block
- Indented lines contain the code that runs when the function is called

The parameters (`a` and `b`) receive values when the function is called.

Example:

```python
addNumbers(5, 3)
```

When this function call happens:

- `a` receives the value `5`
- `b` receives the value `3`

So inside the function, the code becomes:

```python
result = 5 + 3
```

After the calculation, `result` will contain `8`.

This allows the same function to work with different values without rewriting the logic every time.

For example:

```python
addNumbers(10, 2)
addNumbers(7, 1)
addNumbers(100, 50)
```

Each function call uses different values while reusing the same code structure.

---

## Functions in this project

Some functions are already provided for you and can be used during the project:

```python
drawGrid(screen, colour, windowSize, horizontalLines, verticalLines, lineWidth)

drawCircle(screen, colour, positionX, positionY, radius)

drawCross(screen, colour, positionX, positionY, sideLength, lineWidth)

drawEndScreen(screen, text, bgColour, winSize)

createEndScreenText(text, colour)

noMoreSpace(field)

printField(field)
```

Each function has a specific purpose:

- `drawGrid(...)` draws the Tic-Tac-Toe grid
- `drawCircle(...)` draws a circle symbol
- `drawCross(...)` draws a cross symbol
- `drawEndScreen(...)` displays the end screen
- `createEndScreenText(...)` creates text for the end screen
- `noMoreSpace(field)` checks if the board is full
- `printField(field)` prints the board in the console

⚠️ Check the provided documentation to see how and when to use these functions.