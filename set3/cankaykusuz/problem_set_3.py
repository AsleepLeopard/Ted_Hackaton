
# PROBLEM SET 3
# For this task students will be asked to draw a star  with turtle library.
# The users of the program shall be able to adjust the size of the star from the console.
# The star should have 5 corners.
# The star should be red.

# Used for both Procedure

setup(100, 100)
size_factor = int(input("Size 1(bigest)-3(smallest): "))

reset()
pencolor(red)

# Procedure for drawing the star: (Fixed size)

# Starting point:
setx(15)
sety(75)

pendown()
goto(85, 75) 
# düz çizgi

goto(30 ,15)

goto(50, 100)
# üst nokta

goto(30 ,15)

goto(15, 75)

# Changable size:

# Procedure for drawing the star: (Fixed size)

# Starting point:
setx(15 * size_factor)
sety(100 - 15 * size_factor)

pendown()
goto(100 - 15 * size_factor, 100 - 25 * size_factor) 
# düz çizgi

goto(30 * size_factor , 15 * size_factor)

goto(50, 100 - 10 * size_factor) 
# üst nokta

goto(30 * size_factor, 15 * size_factor)

goto(15 * size_factor, 100 - 25 * size_factor)

