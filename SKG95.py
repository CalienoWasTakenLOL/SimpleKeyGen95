import tkinter as tk
import random
import webbrowser

# Function to generate a valid key
def generate_key():
    # XXX: Number between 001 and 366, padded to 3 digits
    xxx = f"{random.randint(1, 366):03}"
    
    # YY: Number between 95 and 99
    yy = str(random.randint(95, 99))
    
    oem = "OEM"
    
    # 00: Remains unchanged
    zero_zero = "00"
    
    # SSSSS: Sum of digits divisible by 7
    while True:
        sssss = f"{random.randint(0, 99999):05}"
        if sum(int(digit) for digit in sssss) % 7 == 0:
            break
    
    # ZZZZZ: Random 5-digit number
    zzzzz = f"{random.randint(0, 99999):05}"
    
    # Combine to form the key
    key = f"{xxx}{yy}-{oem}-{zero_zero}{sssss}-{zzzzz}"
    
    # Display the generated key in the entry field
    result_var.set(key)

# Function to open Google
def open_support():
    webbrowser.open("https://github.com/CalienoWasTakenLOL")

# Create the main window
root = tk.Tk()
root.title("SimpleKeyGen95")
root.geometry("400x250")
root.configure(bg="black")  # Set background color to black

# Add a label above the key generator text field with Comic Sans font
title_label = tk.Label(root, text="SImpleKeyGen for windows 95 by bizzero", font=('Comic Sans MS', 12, 'bold'), fg="cyan", bg="black")
title_label.pack(pady=(20, 10))

# Define a variable to hold the result
result_var = tk.StringVar()

# Create a text field to display the result
result_entry = tk.Entry(root, textvariable=result_var, justify='center', font=('Arial', 14), width=30, bg="black", fg="green")
result_entry.pack(pady=10)

# Create a frame to hold both buttons side by side, with background set to black
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

# Create the "Support Me" button with customized colors
support_button = tk.Button(button_frame, text="My Github", command=open_support, bg="gray", fg="black")
support_button.pack(side='left', padx=10)

# Create the "Generate" button next to the "Support Me" button with customized colors
generate_button = tk.Button(button_frame, text="Generate key", command=generate_key, bg="gray", fg="black")
generate_button.pack(side='left', padx=10)

# Run the application
root.mainloop()
