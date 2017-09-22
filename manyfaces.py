# pylint: disable=c
# Problem Set 2, Part II
# Name:
# Collaborators:

import Tkinter

# Please put all your function definitions here (if you have any).


def main():
    """The main function. Please complete this function definition.

    Of course, you probably want to define several other functions and call
    them inside this function definition.
    """
    # We need the following three lines to create a Tkinter window and have a
    # canvas created in that window. We name that canvas ps2_canvas.
    # Please keep these three lines at the very top of your function definition.
    # Everything else in the body of your function should appear after these
    # lines. Thank you.
    window = Tkinter.Tk()
    ps2_canvas = Tkinter.Canvas(window, width=500, height=500)
    ps2_canvas.grid(row=0, column=0)

    # These next four function calls are the ones that draw the face, eyes, and
    # mouth. You should modify these for your program.

    # This draws the face.
    ps2_canvas.create_oval(100, 100, 400, 400, fill='yellow')

    # This call draws the mouth.
    ps2_canvas.create_arc(
        175, 175, 325, 325, start=225, extent=90, style=Tkinter.ARC)

    # This one draws the left eye.
    ps2_canvas.create_oval(200, 205, 202, 207, fill='black')

    # And this call draws the right eye.
    ps2_canvas.create_oval(298, 205, 300, 207, fill='black')

    # Don't remove the next two lines (they have to stay inside the function
    # definition at the very end of the body).
    window.mainloop()
    return None


# The main program.
# Please do not remove this function call. This call to the main function
# should run your whole program.
main()
