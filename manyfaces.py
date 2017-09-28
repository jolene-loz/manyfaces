# pylint: disable=c
# Problem Set 2, Part II
# Name:
# Collaborators:

import Tkinter

# Please put all your function definitions here (if you have any).
# need help with defining functions


def draw_excited_eyes(canvas):
    # This one draws the left eye.
    canvas.create_arc(120, 300, 250, 160, start=0, extent=180, fill='white')
    canvas.create_arc(145, 300, 225, 160, start=0, extent=180, fill='black')

    # And this call draws the right eye.
    canvas.create_arc(240, 300, 380, 160, start=0, extent=180, fill='white')
    canvas.create_arc(270, 300, 350, 160, start=0, extent=180, fill='black')


def draw_happy_eyes(canvas2):
    canvas2.create_arc(
        165, 235, 225, 175, start=0, extent=180, style=Tkinter.ARC)
    canvas2.create_arc(
        255, 235, 315, 175, start=0, extent=180, style=Tkinter.ARC)


def draw_sad_eyes(canvas3):
    #draws eyes
    canvas3.create_oval(150, 150, 250, 250, fill='white')
    canvas3.create_oval(250, 150, 350, 250, fill='white')
    #draws pupils
    canvas3.create_oval(210, 210, 240, 230, fill='black')
    canvas3.create_oval(260, 210, 290, 230, fill='black')


def draw_surprised_eyes(canvas4):
    canvas4.create_oval(150, 150, 250, 250, fill='white')
    canvas4.create_oval(250, 150, 350, 250, fill='white')
    canvas4.create_oval(190, 180, 220, 220, fill='black')
    canvas4.create_oval(280, 180, 310, 220, fill='black')


def draw_surprised_brows(canvas4):
    canvas4.create_arc(
        145, 125, 230, 180, start=50, extent=150, style=Tkinter.ARC)
    canvas4.create_arc(
        350, 135, 300, 200, start=0, extent=100, style=Tkinter.ARC)


def draw_angry_eyes(canvas5):
    canvas5.create_oval(170, 210, 210, 270, fill='black')
    canvas5.create_oval(280, 210, 320, 270, fill='black')
    canvas5.create_oval(190, 210, 200, 270, fill='red')
    canvas5.create_oval(300, 210, 310, 270, fill='red')


def draw_angry_brows(canvas5):
    canvas5.create_line(150, 150, 235, 205)
    canvas5.create_line(250, 205, 335, 150)


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
        "Hello there. I'm a robot that understands emotions: happy, sad, mad, surprised, and excited. How are you doing today?"
    )
    if user_input == 'excited':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='yellow')
        # This call draws the mouth.
        ps2_canvas.create_arc(
            165, 105, 350, 390, start=180, extent=180, fill='VioletRed4')
        # ps2_canvas.create_arc(
        #     230, 400, 380, 290, start=30, extent=180, fill='PaleVioletRed1')
        draw_excited_eyes(ps2_canvas)

    elif user_input == 'happy':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='DarkOrange1')
        #create smile
        ps2_canvas.create_arc(
            175, 175, 325, 325, start=180, extent=180, fill='white')
        ps2_canvas.create_line(180, 275, 320, 275)
        #create eyes
        draw_happy_eyes(ps2_canvas)

    elif user_input == 'sad':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='blue')
        #create sad mouth
        ps2_canvas.create_arc(
            165, 305, 350, 405, start=0, extent=180, style=Tkinter.ARC)
        #create teardrops
        ps2_canvas.create_oval(150, 270, 170, 320, fill='cyan')
        ps2_canvas.create_oval(320, 240, 350, 300, fill='cyan')
        #create eyes
        draw_sad_eyes(ps2_canvas)

    elif user_input == 'surprised':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='gold')
        draw_surprised_eyes(ps2_canvas)
        draw_surprised_brows(ps2_canvas)
        ps2_canvas.create_oval(200, 300, 300, 330, fill='black')

    else:
        ps2_canvas.create_oval(100, 100, 400, 400, fill='red4')
        draw_angry_eyes(ps2_canvas)
        draw_angry_brows(ps2_canvas)
        ps2_canvas.create_arc(
            185, 285, 320, 395, start=0, extent=180, fill='black')

    # Don't remove the next two lines (they have to stay inside the function
    # definition at the very end of the body).
    window.mainloop()
    return None


main()

# The main program.
# Please do not remove this function call. This call to the main function
# should run your whole program.
