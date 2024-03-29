import pyqrcode
import png
from tkinter import *
from tkinter import messagebox, filedialog

# Function to generate the QR code and save it
def get_code():
    try:
        data_var = data.get()
        qr = pyqrcode.create(str(data_var))
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], title="Save QR Code")
        if save_path:
            qr.png(save_path, scale=6)
            messagebox.showinfo("Success", "QR Code generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {str(e)}")

# Create Tkinter window
base = Tk()
base.geometry("400x200")
base.title("QR Code Generator")

# Variable to store text for QR Code
data = StringVar()

# Field to input text
dataEntry = Entry(textvariable=data, width="30")
dataEntry.place(x=80, y=50)

# Call get_code() on click
button = Button(base, text="Get Code", command=get_code, width="30", height="2", bg="grey")
button.place(x=80, y=100)

base.mainloop()
