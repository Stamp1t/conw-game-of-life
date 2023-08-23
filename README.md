# Game of Life

This project is a variation of Game of Life


## Technologies used
Language:
- Python
  
Libraries:
- Pygame
- Numpy

## Rules

The game follows some very simple rules:


    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

    Any live cell with two or three live neighbours lives on to the next generation.

    Any live cell with more than three live neighbours dies, as if by overpopulation.

    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Source: https://rustwasm.github.io/docs/book/game-of-life/rules.html

Game of Life simulates the development of cells over multiple generations



## Description
When starting the Project, you can start editing the Edit-Field:
- "Mode" tells you which mode you are currently in
- The white highlighted cell at your mouse curser indicates which cell you are hovering over at the moment



pic

Now you can start creating custom cell patterns by hovering over a dead (black) cell and left-clicking it in order to revitalize it

pic

Apart from that, you can draw one of the precasted cell patterns
- Click on the pattern you want to see 
- Your indicator will turn red
- You can now choose a location to draw the pattern

pic

In order to
- start the game, press "start"
- pause the development of the cells, press "pause"
- clear the screen and restart the game, press "clear"
