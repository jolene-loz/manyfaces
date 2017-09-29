# pylint: disable=c
# Problem Set 2, Part II
# Name: Lozano,Jolene
# Collaborators: --

import Tkinter

# Please put all your function definitions here (if you have any).
# need help with defining functions
#FINAL updated manyfaces


def draw_excited_eyes(canvas):
    # This one draws the left eye.
    canvas.create_arc(120, 300, 250, 160, start=0, extent=180, fill='white')
    canvas.create_arc(145, 300, 225, 160, start=0, extent=180, fill='black')
    # And this call draws the right eye
    canvas.create_arc(240, 300, 380, 160, start=0, extent=180, fill='white')
    canvas.create_arc(270, 300, 350, 160, start=0, extent=180, fill='black')


def draw_hat(canvas):
    canvas.create_polygon(150, 100, 160, 20, 250, 100, fill='purple')
    canvas.create_oval(150, 10, 175, 35, fill='deep pink')


def draw_happy_eyes(canvas2):
    #Calls left eye
    canvas2.create_arc(
        165, 235, 225, 175, start=0, extent=180, style=Tkinter.ARC)
    #Calls right eye
    canvas2.create_arc(
        255, 235, 315, 175, start=0, extent=180, style=Tkinter.ARC)


def draw_sun_rays(canvas2):
    canvas2.create_polygon((130, 180, 50, 60, 180, 120), fill="yellow")
    canvas2.create_polygon((180, 200, 250, 10, 340, 200), fill="yellow")
    canvas2.create_polygon((250, 180, 460, 60, 400, 240), fill="yellow")
    canvas2.create_polygon((120, 200, 15, 300, 180, 350), fill="yellow")
    canvas2.create_polygon((170, 310, 120, 465, 350, 350), fill="yellow")
    canvas2.create_polygon((280, 390, 440, 465, 350, 350), fill="yellow")
    canvas2.create_polygon((350, 350, 480, 340, 380, 255), fill="yellow")


def draw_sad_eyes(canvas3):
    #draws eyes
    canvas3.create_oval(150, 150, 250, 250, fill='white')
    canvas3.create_oval(250, 150, 350, 250, fill='white')
    #draws pupils
    canvas3.create_oval(210, 210, 240, 230, fill='black')
    canvas3.create_oval(260, 210, 290, 230, fill='black')


def draw_sad_body(canvas3):
    canvas3.create_arc(120, 400, 350, 500, start=0, extent=180, fill='black')
    canvas3.create_rectangle(120, 450, 160, 500, fill='black')
    canvas3.create_rectangle(310, 450, 350, 500, fill='black')
    canvas3.create_rectangle(170, 420, 300, 500, fill='black')


def draw_surprised_eyes(canvas4):
    #draws eyes
    canvas4.create_oval(150, 150, 250, 250, fill='white')
    canvas4.create_oval(250, 150, 350, 250, fill='white')
    #draws pupils
    canvas4.create_oval(190, 180, 220, 220, fill='black')
    canvas4.create_oval(280, 180, 310, 220, fill='black')


def draw_surprised_brows(canvas4):
    #draws left eyebrow
    canvas4.create_arc(
        140, 135, 200, 190, start=50, extent=150, style=Tkinter.ARC)
    #draws right brow
    canvas4.create_arc(
        350, 135, 300, 200, start=0, extent=100, style=Tkinter.ARC)


def draw_angry_eyes(canvas5):
    #draws eyes
    canvas5.create_oval(170, 210, 210, 270, fill='black')
    canvas5.create_oval(280, 210, 320, 270, fill='black')
    #draws pupils
    canvas5.create_oval(190, 210, 200, 270, fill='red')
    canvas5.create_oval(300, 210, 310, 270, fill='red')


def draw_angry_arms(canvas5):

    #draws arms
    canvas5.create_rectangle(150, 420, 350, 450, fill='red2')
    #draws hands
    canvas5.create_oval(320, 400, 390, 470, fill='red2')
    canvas5.create_oval(120, 400, 190, 470, fill='red2')


def draw_angry_horns(canvas5):
    canvas5.create_polygon(150, 170, 100, 100, 250, 150, fill='red2')
    canvas5.create_polygon(230, 170, 400, 100, 330, 180, fill='red2')


def draw_angry_brows(canvas5):
    canvas5.create_line(150, 150, 235, 205)
    canvas5.create_line(250, 205, 335, 150)


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
    window = Tkinter.Tk()
    ps2_canvas = Tkinter.Canvas(window, width=500, height=500)
    ps2_canvas.grid(row=0, column=0)

    #asks user to input an emotion
    user_input = raw_input(
        "Hello there. I'm a robot that understands emotions: happy, sad, mad, surprised, and excited. How are you doing today?"
    )

    if user_input == 'excited':
        #draws hat
        draw_hat(ps2_canvas)
        #draws hair
        ps2_canvas.create_arc(
            120, 50, 370, 300, start=0, extent=340, fill='black')
        #draws face
        ps2_canvas.create_oval(100, 100, 400, 400, fill='yellow')
        # This call draws the mouth.
        ps2_canvas.create_arc(
            165, 105, 350, 390, start=180, extent=180, fill='VioletRed4')
<<<<<<< HEAD
        #calls eyes
        draw_excited_eyes(ps2_canvas)

    elif user_input == 'happy':
        #calls sun rays
        draw_sun_rays(ps2_canvas)
=======
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

        #creates face
        ps2_canvas.create_oval(100, 100, 400, 400, fill='blue')
        #create sad mouth
        ps2_canvas.create_arc(
            165, 305, 350, 405, start=0, extent=180, style=Tkinter.ARC)
        #create teardrops
        ps2_canvas.create_oval(150, 270, 170, 320, fill='cyan')
        ps2_canvas.create_oval(320, 240, 350, 300, fill='cyan')
        #create eyes
        draw_sad_eyes(ps2_canvas)
<<<<<<< HEAD
        #creates body
        draw_sad_body(ps2_canvas)

    elif user_input == 'surprised':
        #creates face
        ps2_canvas.create_oval(100, 100, 400, 400, fill='gold')
        #creates eyes
        draw_surprised_eyes(ps2_canvas)
        #creates brows
        draw_surprised_brows(ps2_canvas)
        #creates outh
        ps2_canvas.create_oval(200, 300, 300, 330, fill='black')

    else:
        #creates arms
        draw_angry_arms(ps2_canvas)
        #creates body
        ps2_canvas.create_polygon(170, 500, 250, 300, 330, 500, fill='red2')
        #creates horns
        draw_angry_horns(ps2_canvas)
        #creates face
        ps2_canvas.create_oval(100, 100, 400, 400, fill='red4')
        #calls eyes
        draw_angry_eyes(ps2_canvas)
        #calls brows
        draw_angry_brows(ps2_canvas)
        #creates mouth
=======

    elif user_input == 'surprised':
        ps2_canvas.create_oval(100, 100, 400, 400, fill='gold')
        draw_surprised_eyes(ps2_canvas)
        draw_surprised_brows(ps2_canvas)
        ps2_canvas.create_oval(200, 300, 300, 330, fill='black')

    else:
        ps2_canvas.create_oval(100, 100, 400, 400, fill='red4')
        draw_angry_eyes(ps2_canvas)
        draw_angry_brows(ps2_canvas)
>>>>>>> 4094bdc6188adc4686edf4ee6233e763df8a0c7e
        ps2_canvas.create_arc(
            185, 285, 320, 395, start=0, extent=180, fill='black')

    window.mainloop()
    return None


#outside function definition
# calls main method
main()

# The main program.
# Please do not remove this function call. This call to the main function
# should run your whole program.
