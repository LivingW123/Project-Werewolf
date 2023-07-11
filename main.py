import geocoder
import ephem

import customtkinter


import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
root.title("Project Werewolf")
root.geometry("400x300")
# Define the function to open another window
def open_another_window():
    new_window = tk.Tk()
    new_window.title("Another Window")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="This is another window.")
    label.pack()

# Create a button to open another window
button = customtkinter.CTkButton(root, command=open_another_window)
# button.configure(width=100, height=50, bd=0, relief="raised", highlightthickness=0)
button.pack()

# Create a smooth button
smooth_button = tk.Button(root, text="Smooth Button", relief="flat", bd=0, bg="lightblue", fg="black")
smooth_button.pack()
smooth_button.config(padx=10, pady=10)

# Add some background image
# image = Image.open("background.png")
# background_image = ImageTk.PhotoImage(image)
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
# canvas.create_image(0, 0, image=background_image)

# Add a border around the page
root.config(borderwidth=5)



def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        return g.latlng
    else:
        return None

location = get_current_location()
if location:
    ulatitude, ulongitude = location
    print(f"Latitude: {ulatitude}, Longitude: {ulongitude}")
else:
    print("Unable to retrieve current location.")


root.mainloop()