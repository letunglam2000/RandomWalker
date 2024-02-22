import random
from tkinter import Canvas


class Walker:
    def __init__(self, width: int, height: int):
        # Location of the walker on the canvas
        self.x = width // 2
        self.y = height // 2

    def step(self) -> None:
        """
        The walker moves in a random direction.

        :return: None
        """
        choice: int = random.randint(0, 3)
        steps = 1
        if choice == 0:  # move right
            self.x += steps
        elif choice == 1:  # move left
            self.x -= steps
        elif choice == 2:  # move down
            self.y += steps
        else:  # move up
            self.y -= steps

    def show(self, canvas: Canvas) -> None:
        # Draw a point at coordinates (self.x, self.y)
        canvas.create_oval(self.x, self.y, self.x+1, self.y+1, fill="black")
