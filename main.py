import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # converting height to meters
        bmi = weight / (height ** 2)
        bmi_result.set(f'Your BMI: {bmi:.2f}')

        if bmi < 18.5:
            status.set('Underweight')
        elif 18.5 <= bmi < 25:
            status.set('Normal weight')
        elif 25 <= bmi < 30:
            status.set('Overweight')
        else:
            status.set('Obese')

    except ValueError:
        bmi_result.set('Please enter valid values')

# Create the main window
window = tk.Tk()
window.title('BMI Calculator')

# Set background image
bg_image = Image.open('bmi.jpg')  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place widgets
frame = ttk.Frame(window, padding='10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels
weight_label = ttk.Label(frame, text='Weight (kg):')
weight_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

height_label = ttk.Label(frame, text='Height (cm):')
height_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

bmi_label = ttk.Label(frame, textvariable='BMI:')
bmi_label.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

# Entry widgets
weight_entry = ttk.Entry(frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_entry = ttk.Entry(frame)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Button
calculate_button = ttk.Button(frame, text='Calculate BMI', command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result display
bmi_result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=bmi_result, font=('Helvetica', 12), background='white')
result_label.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

# Status display
status = tk.StringVar()
status_label = ttk.Label(frame, textvariable=status, font=('Helvetica', 12), foreground='blue', background='white')
status_label.grid(row=4, column=0, columnspan=2, pady=10)

# Adjust text size based on screen size
window.option_add('*TButton*Font', ('Helvetica', int(window.winfo_screenwidth() / 40)))
window.option_add('*TLabel*Font', ('Helvetica', int(window.winfo_screenwidth() / 50)))

# Center the window
window.eval('tk::PlaceWindow . center')

# Run the application
window.mainloop()
