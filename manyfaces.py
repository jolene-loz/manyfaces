# pylint: disable=c
# Problem Set 2, Part II
# Name:
# Collaborators:

import Tkinter

# Please put all your function definitions here (if you have any).
# need help with defining functions


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
    user_input = raw_input(
        "Hello there. I'm a robot that understands emotions: happy, sad, mad, annoyed, and excited"
    )
    if user_input == 'excited':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='yellow')
        # This call draws the mouth.
        ps2_canvas.create_arc(
            165, 105, 350, 390, start=180, extent=180, fill='purple')
        # This one draws the left eye.
        ps2_canvas.create_arc(
            120, 300, 250, 160, start=0, extent=180, fill='white')
        ps2_canvas.create_arc(
            150, 300, 200, 160, start=0, extent=180, fill='black')
        # And this call draws the right eye.
        ps2_canvas.create_arc(
            240, 300, 380, 160, start=0, extent=180, fill='white')
        ps2_canvas.create_arc(
            270, 300, 350, 160, start=0, extent=180, fill='black')
        # ps2_canvas.create_oval(298, 210, 300, 257, fill='black')
    elif user_input == 'happy':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='pink')
        #create smile
        ps2_canvas.create_arc(
            175, 175, 325, 325, start=225, extent=90, style=Tkinter.ARC)
        #create eyes
        ps2_canvas.create_arc(
            155, 275, 225, 125, start=0, extent=180, style=Tkinter.ARC)
        ps2_canvas.create_arc(
            255, 175, 305, 325, start=0, extent=180, style=Tkinter.ARC)

    elif user_input == 'sad':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='blue')
        ps2_canvas.create_arc(
            165, 305, 355, 405, start=0, extent=180, style=Tkinter.ARC)
        #create eyes
        ps2_canvas.create_oval(150, 150, 250, 250, fill='white')
        ps2_canvas.create_oval(210, 210, 240, 230, fill='black')

        ps2_canvas.create_oval(250, 150, 350, 250, fill='white')
        ps2_canvas.create_oval(280, 210, 260, 230, fill='black')

        ps2_canvas.create_oval(150, 270, 160, 320, fill='cyan')
    # elif user_input == 'annoyed':
    # elif user_input == 'mad':
    #

    # Don't remove the next two lines (they have to stay inside the function
    # definition at the very end of the body).
    window.mainloop()
    return None


main()

# The main program.
# Please do not remove this function call. This call to the main function
# should run your whole program.
