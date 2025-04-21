
# PROBLEM SET 4 - DONE
# For this task the students will be asked to code an algorithm that prints a sand clock to the console.

# Canvas width: 7 char
canvas_width = 7
width = 7

print("\n")
print("\n")

while width >= 3:
    print((" " * ((canvas_width - width) // 2)) + "#" * width + (" " * ((canvas_width - width) // 2)))
    width -= 2
else:
    while width <= 7:
        print((" " * ((canvas_width - width) // 2)) + "#" * width + (" " * ((canvas_width - width) // 2)))
        width += 2

