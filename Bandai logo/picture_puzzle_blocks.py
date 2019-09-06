

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()


#--------------------------------------------------------------------#

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up']]
arrangement_02 = [['Block B', 'Bottom right', 'Up']]
arrangement_03 = [['Block C', 'Bottom left', 'Up']]
arrangement_04 = [['Block D', 'Bottom right', 'Up']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down']]
arrangement_11 = [['Block A', 'Bottom right', 'Left']]
arrangement_12 = [['Block A', 'Bottom left', 'Right']]

arrangement_13 = [['Block B', 'Bottom left', 'Down']]
arrangement_14 = [['Block B', 'Bottom right', 'Left']]
arrangement_15 = [['Block B', 'Bottom left', 'Right']]

arrangement_16 = [['Block C', 'Bottom left', 'Down']]
arrangement_17 = [['Block C', 'Bottom right', 'Left']]
arrangement_18 = [['Block C', 'Bottom left', 'Right']]

arrangement_19 = [['Block D', 'Bottom left', 'Down']]
arrangement_20 = [['Block D', 'Bottom right', 'Left']]
arrangement_21 = [['Block D', 'Bottom left', 'Right']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up'],
                  ['Block D', 'Top right', 'Up']]
arrangement_31 = [['Block A', 'Top left', 'Up'],
                  ['Block C', 'Bottom left', 'Up']]

arrangement_32 = [['Block B', 'Bottom right', 'Up'],
                  ['Block D', 'Bottom left', 'Up'],
                  ['Block C', 'Top right', 'Up']]
arrangement_33 = [['Block B', 'Bottom right', 'Up'],
                  ['Block D', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up']]
arrangement_34 = [['Block B', 'Bottom left', 'Up'],
                  ['Block A', 'Bottom right', 'Up'],
                  ['Block D', 'Top left', 'Up'],
                  ['Block C', 'Top right', 'Up']]

arrangement_40 = [['Block C', 'Bottom right', 'Left'],
                  ['Block D', 'Top right', 'Right']]
arrangement_41 = [['Block A', 'Top left', 'Down'],
                  ['Block C', 'Bottom left', 'Up']]

arrangement_42 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_43 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_44 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

arrangement_50 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_51 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_52 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

arrangement_60 = [['Block B', 'Bottom right', 'Left'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block C', 'Top right', 'Down']]
arrangement_61 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Left'],
                  ['Block A', 'Top left', 'Right']]
arrangement_62 = [['Block B', 'Bottom left', 'Down'],
                  ['Block A', 'Bottom right', 'Left'],
                  ['Block D', 'Top left', 'Right'],
                  ['Block C', 'Top right', 'Up']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left'],
                  ['Block D', 'Top right', 'Left'],
                  ['Block A', 'Bottom left', 'Left'],
                  ['Block B', 'Top left', 'Left']]

arrangement_81 = [['Block B', 'Bottom right', 'Right'],
                  ['Block D', 'Bottom left', 'Right'],
                  ['Block A', 'Top right', 'Right'],
                  ['Block C', 'Top left', 'Right']]

arrangement_89 = [['Block A', 'Bottom right', 'Down'],
                  ['Block C', 'Top right', 'Down'],
                  ['Block B', 'Bottom left', 'Down'],
                  ['Block D', 'Top left', 'Down']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up'],
                  ['Block D', 'Bottom right', 'Up'],
                  ['Block B', 'Top right', 'Up'],
                  ['Block A', 'Top left', 'Up']]

arrangement_91 = [['Block D', 'Bottom right', 'Up'],
                  ['Block C', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up'],
                  ['Block B', 'Top right', 'Up']]

arrangement_92 = [[ 'Bottom right', 'Up'],
                  ['Block B', 'Top right', 'Up'],
                  ['Block C', 'Bottom left', 'Up'],
                  ['Block A', 'Top left', 'Up']]

arrangement_99 = [['Block C', 'Bottom left', 'Up'],
                  ['Block D', 'Bottom right', 'Up'],
                  ['Block A', 'Top left', 'Up'],
                  ['Block B', 'Top right', 'Up']]

#
#--------------------------------------------------------------------#



#draw Block A
def draw_Block_A(x_cor, y_cor, rotation):
    # draw a square and fill it with 'firebrick1' color
    penup()
    goto(x_cor - 125, y_cor + 125)
    pendown()
    setheading(0)
    pencolor('white')
    pensize(3)
    fillcolor('firebrick1')
    begin_fill()
    for _ in range(4):
        forward(250)
        right(90)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 110, y_cor - 115)
    elif rotation == 90:
        goto(x_cor + 115, y_cor - 110)
    elif rotation == 180:
        goto(x_cor + 115, y_cor + 110)
    else:
        goto(x_cor - 110, y_cor + 115)

    # draw the letter B and fill it with white color
    pendown()
    setheading(rotation)
    pencolor('white')
    fillcolor('white')
    begin_fill()
    forward(95)
    circle(45,180)
    setheading(rotation)
    circle(40,180)
    setheading(rotation + 180)
    forward(95)
    left(90)
    forward(170)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 65, y_cor - 85)
    elif rotation == 90:
        goto(x_cor + 85, y_cor - 65)
    elif rotation == 180:
        goto(x_cor + 75, y_cor + 80)
    else:
        goto(x_cor - 80, y_cor + 85)

    # draw the center of the letter B and fill it with 'firebrick' color
    setheading(rotation)
    pendown()
    pencolor('firebrick1')
    fillcolor('firebrick1')
    begin_fill()
    forward(30)
    circle(20,180)
    setheading(rotation + 180)
    forward(10)
    right(90)
    forward(35)
    right(90)
    forward(10)
    circle(15,180)
    setheading(rotation + 180)
    forward(30)
    left(90)
    forward(105)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor + 125, y_cor - 115)
    elif rotation == 90:
        goto(x_cor + 115, y_cor + 125)
    elif rotation == 180:
        goto(x_cor - 125, y_cor + 110)
    else:
        goto(x_cor - 115, y_cor - 125)

    # Draw half of the letter A and fill it with white color
    pendown()
    pencolor('white')
    fillcolor('white')
    setheading(rotation + 180)
    begin_fill()
    forward(80)
    right(105)
    forward(175)
    right(75)
    forward(35)
    right(90)
    forward(30)
    right(15)
    forward(114)
    left(105)
    forward(29)
    right(90)
    forward(30)
    end_fill()


# draw Block B
def draw_Block_B(x_cor, y_cor, rotation):
    # draw a square and fill it with 'firebrick1' color
    penup()
    goto(x_cor - 125, y_cor + 125)
    setheading(0)
    pencolor('white')
    pensize(3)
    fillcolor('firebrick1')
    begin_fill()
    pendown()
    for _ in range(4):
        forward(250)
        right(90)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 125, y_cor + 54)
    elif rotation == 90:
        goto(x_cor - 54, y_cor - 125)
    elif rotation == 180:
        goto(x_cor + 125, y_cor - 59)
    else:
        goto(x_cor + 54, y_cor + 125)

    # draw the other half of the letter A and fill it with white color
    begin_fill()
    setheading(rotation)
    pencolor('white')
    fillcolor('white')
    pendown()
    forward(30)
    right(75)
    forward(175)
    right(105)
    forward(40)
    right(75)
    forward(137)
    right(15)
    forward(37)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 125, y_cor - 115)
    elif rotation == 90:
        goto(x_cor + 115, y_cor - 125)
    elif rotation == 180:
        goto(x_cor + 125, y_cor + 110)
    else:
        goto(x_cor - 115, y_cor + 125)

    # draw the last part of Block A and fill it with white
    pendown()
    setheading(rotation)
    begin_fill()
    forward(15)
    left(90)
    forward(29)
    left(90)
    forward(15)
    left(90)
    forward(29)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 35, y_cor - 115)
    elif rotation == 90:
        goto(x_cor + 115, y_cor - 35)
    elif rotation == 180:
        goto(x_cor + 35, y_cor + 110)
    else:
        goto(x_cor - 115, y_cor + 35)

    # draw letter N and fill it with white color
    pendown()
    setheading(rotation)
    begin_fill()
    forward(38)
    left(90)
    forward(110)
    right(145)
    forward(133)
    left(55)
    forward(38)
    left(90)
    forward(170)
    left(90)
    forward(38)
    left(90)
    forward(105)
    right(145)
    forward(125)
    left(55)
    forward(42)
    left(90)
    forward(169)
    end_fill()


# draw Block_C
def draw_Block_C(x_cor, y_cor, rotation):
    # draw a square and fill it with 'firebrick1' color
    penup()
    goto(x_cor - 125, y_cor + 125)
    setheading(0)
    pendown()
    pencolor('white')
    pensize(3)
    fillcolor('firebrick1')
    begin_fill()
    for _ in range(4):
        forward(250)
        right(90)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 110, y_cor - 55)
    elif rotation == 90:
        goto(x_cor + 55, y_cor - 110)
    elif rotation == 180:
        goto(x_cor + 115, y_cor + 55)
    else:
        goto(x_cor - 55,y_cor + 115)

    # draw letter 'D' and fill it with white color,
    # fill the center with 'firebrick1' color
    setheading(rotation)
    pencolor('white')
    fillcolor('white')
    begin_fill()
    pendown()
    forward(70)
    circle(85,180)
    forward(70)
    left(90)
    forward(170)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 75, y_cor - 15)
    elif rotation == 90:
        goto(x_cor + 20, y_cor - 70)
    elif rotation == 180:
        goto(x_cor + 80, y_cor + 15)
    else:
        goto(x_cor - 15,y_cor + 80)

    #draw the center of Block 'D' and fill it with 'firebrick1' color
    pendown()
    setheading(rotation)
    pencolor('firebrick1')
    fillcolor('firebrick1')
    begin_fill()
    forward(30)
    circle(45,180)
    forward(30)
    left(90)
    forward(90)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor + 125, y_cor - 55)
    elif rotation == 90:
        goto(x_cor + 55, y_cor + 125)
    elif rotation == 180:
        goto(x_cor - 125, y_cor + 55)
    else:
        goto(x_cor - 55, y_cor - 125)

    # draw half of the letter 'A' and fill it with white color
    pendown()
    setheading(rotation + 180)
    pencolor('white')
    fillcolor('white')
    begin_fill()
    forward(80)
    right(105)
    forward(175)
    right(75)
    forward(35)
    right(90)
    forward(30)
    right(15)
    forward(114)
    left(105)
    forward(29)
    right(90)
    forward(30)
    end_fill()


# draw block D
def draw_Block_D(x_cor, y_cor, rotation):
    # draw a square and fill it with 'firebrick1' color
    penup()
    pencolor('white')
    pensize(3)
    fillcolor('firebrick1')
    goto(x_cor - 125, y_cor + 125)
    setheading(0)
    pendown()
    begin_fill()
    for _ in range(4):
        forward(250)
        right(90)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 125, y_cor + 114)
    elif rotation == 90:
        goto(x_cor - 114, y_cor - 125)
    elif rotation == 180:
        goto(x_cor + 125, y_cor - 114)
    else:
        goto(x_cor + 115, y_cor + 125)

    # draw the other half of the letter 'A' and fill it with white color
    pencolor('white')
    fillcolor('white')
    setheading(rotation)
    begin_fill()
    pendown()
    forward(30)
    right(75)
    forward(175)
    right(105)
    forward(40)
    right(75)
    forward(137)
    right(15)
    forward(37)
    right(90)
    forward(30)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 125, y_cor - 55)
    elif rotation == 90:
        goto(x_cor + 55, y_cor - 125)
    elif rotation == 180:
        goto(x_cor + 125, y_cor + 55)
    else:
        goto(x_cor - 55, y_cor + 125)

    # draw the last part of letter 'A' and fill it with white color
    pendown()
    setheading(rotation)
    begin_fill()
    forward(15)
    left(90)
    forward(29)
    left(90)
    forward(15)
    end_fill()

    # goto different coordinates when the orientation is different
    penup()
    if rotation == 0:
        goto(x_cor - 35, y_cor + 115)
    elif rotation == 90:
        goto(x_cor - 115, y_cor - 35)
    elif rotation == 180:
        goto(x_cor + 35,y_cor - 115)
    else:
        goto(x_cor + 115, y_cor + 35)

    # draw letter 'I' and fill it with white
    fillcolor('white')
    setheading(rotation)
    begin_fill()
    forward(41)
    right(90)
    forward(170)
    right(90)
    forward(41)
    right(90)
    forward(170)
    end_fill()


#executes the instructions in 'arrangement'
def execute_instructions(instruction):
    block = instruction[0]
    position = instruction[1]
    rotation = instruction[2]

    # Give string'Top left', 'Top right', 'Bottom left', 'Bottom right'  two integer values for coordinates
    if position == 'Top left':
        x_cor, y_cor = -125,375
    elif position == 'Top right':
        x_cor, y_cor = 125,375
    elif position == 'Bottom left':
        x_cor, y_cor = -125,125
    else:
        x_cor,y_cor = 125,125

    # Give string'Up', 'Down', 'Left', 'Right'  one integer value for rotation.
    if rotation == 'Up':
        rotation = 0
    elif rotation == 'Left':
        rotation = 90
    elif rotation == 'Down':
        rotation = 180
    else:
        rotation = 270

    # Decide which Block to call.
    if block == 'Block A':
        draw_Block_A(x_cor, y_cor, rotation)
    elif block == 'Block B':
        draw_Block_B(x_cor, y_cor, rotation)
    elif block == 'Block C':
        draw_Block_C(x_cor, y_cor, rotation)
    else:
        draw_Block_D(x_cor, y_cor, rotation)

#draw Blocks in the given arrangements
# in different locations and orientations.
def stack_blocks(arrangement):
    for instruction in arrangement:
        execute_instructions(instruction)

create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('BANDAI logo')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(True, True)

#############################################################################
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)  # see the available arrangement lists above
#############################################################################

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#
