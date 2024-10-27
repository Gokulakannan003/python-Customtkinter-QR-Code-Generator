import customtkinter
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import qrcode
import sys

customtkinter.set_appearance_mode("light")
root = CTk()
root.title("QR Code Generator")
root.geometry("500x500")
root.resizable(False, False)

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, 'qr.ico')
else:
    icon_path = 'qr.ico'

root.iconbitmap(icon_path)

enter_frame = CTkFrame(root, height=50, width=300)
enter_frame.place(x=100, y=50)

userinput = CTkEntry(enter_frame,
                     height=50,
                     width=300,
                     font=("arial black", 15, "bold"),
                     bg_color="azure2",
                     border_color="red",
                     corner_radius=4)
userinput.place(x=0, y=0)

work_frame = CTkFrame(root,
                      height=300,
                      width=300,
                      border_color="red",
                      border_width=2,
                      corner_radius=4,
                      fg_color="azure")
work_frame.place(x=100, y=115)


def generate_qr():
    data = userinput.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text or URL.")
        return
    qr = qrcode.QRCode(version=1, box_size=12, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='azure')
    img = img.convert('RGB')
    img.save("qr_code.png")
    display_qr_code("qr_code.png")


def display_qr_code(a):
    img = Image.open(a)
    img = img.resize((work_frame.winfo_width(), work_frame.winfo_height()), Image.LANCZOS)

    qr_image = CTkImage(light_image=img, size=(290, 290))
    qr_code_image.configure(image=qr_image)


label = CTkLabel(root, text="Enter text or URL", font=("arial black", 15, "bold"))
label.pack(pady=10)


button_frame = CTkFrame(root,
                        height=50,
                        width=300,
                        corner_radius=4)
button_frame.place(x=100, y=420)

generate_button = CTkButton(button_frame,
                            text="Generate QR Code",
                            command=generate_qr,
                            corner_radius=4,
                            height=50,
                            width=300,
                            font=("Arial black", 15, "bold"),
                            border_width=2,
                            border_color="red",
                            hover_color="red",
                            fg_color="ivory4",
                            text_color="black")
generate_button.place(x=0, y=0)

qr_code_image = CTkLabel(work_frame, text="")
qr_code_image.place(x=5, y=5)

root.mainloop()
