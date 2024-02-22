import tkinter as tk
from walker import Walker


def draw(walker: Walker, canvas: tk.Canvas):
    # Walker takes a step
    walker.step()
    walker.show(canvas)
    canvas.update()

    # Schedule the next call to draw after a delay (milliseconds)
    canvas.after(0, draw, walker, canvas)


def main():
    # Create a window
    window = tk.Tk()
    window.title("Random Walker")
    window.resizable(False, False)

    # Create a canvas
    canvas = tk.Canvas(window, width=640, height=320)
    canvas.pack()

    # Set the background color
    canvas.config(bg="white")

    # Create a walker
    walker = Walker(width=640, height=320)
    draw(walker, canvas)

    # Run the Tkinter event loop
    window.mainloop()


if __name__ == '__main__':
    main()
