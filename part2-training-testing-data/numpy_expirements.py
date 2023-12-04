'''import tkinter as tk

# Function to draw a simple graph on the canvas
def draw_graph():
    # Clear previous drawings
    canvas.delete("all")

    # Graph data (you can replace this with your own data)
    data = [10, 50, 30, 40, 70]

    # Calculate the scaling factors
    max_value = max(data)
    scale_x = 30  # X-axis scaling factor
    scale_y = 5   # Y-axis scaling factor

    # Draw the graph lines
    for i in range(len(data) - 1):
        x1 = i * scale_x
        y1 = canvas_height - data[i] * scale_y
        x2 = (i + 1) * scale_x
        y2 = canvas_height - data[i + 1] * scale_y
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

# Create the main window
window = tk.Tk()
window.title("Tkinter Graph")

# Set the dimensions of the window
canvas_width = 200
canvas_height = 150

# Create a canvas to draw on
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create a button to trigger the graph drawing
button = tk.Button(window, text="Draw Graph", command=draw_graph)
button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("part2-training-testing-data/Fitness - Data.csv")

Array = np.array(data)
Array.reshape(263, 24)
#print(Array)
x = 0
for i in Array:
    if 225 in i:
        x+=1
        
#print(x)

lst = []
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


newarr = arr.reshape(6, 2)

y = 0
import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("RESULTS GUI")
sentence = "The quick brown fox jumped over the lazy dog"
#display the result
result_label = tk.Label(root, text=sentence)
result_label.pack(pady=10)
tk.Label(root, text="HI").pack(pady=5
# Start the Tkinter event loop

'''
def add_text(x):
    text_label = tk.Label(root, text=x)
    text_label.pack(pady=5)

#Function
def button_click():
    print("Button clicked!")
    add_text("Hello")
def up_one():
    y = y + 1
    print(y)

add_text("hello")
#Create a button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack(pady=20)
button2 = tk.Button(root, text="Plus one", command=up_one)
button2.pack()
# Set the dimensions of the window
root.geometry("400x300")
root.mainloop()
print(newarr)
for i in newarr:
    #print(newarr[i])
    if 3 not in i:
        lst.append(i)

print(lst)

dataset = data
df = pd.DataFrame(dataset)
cols = [1,2,3,4]
df = df[df.columns[cols]]
print(cols[1])
#print(df)

x = 3.48484
print(np.around(x, 2))
'''