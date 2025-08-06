import tkinter as tk
import customtkinter as ctk
import subprocess
import sys
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🎙️ Alexa Voice Assistant")
app.geometry("500x350")

title_label = ctk.CTkLabel(app, text="Alexa AI Assistant", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

output_text = tk.StringVar()
output_label = ctk.CTkLabel(app, textvariable=output_text, wraplength=450, justify="center", font=("Arial", 16))
output_label.pack(pady=20)

def run_voice_assistant():
    output_text.set("🎧 Alexa is listening...")

    if sys.platform == "win32":
        subprocess.Popen(["start", "cmd", "/k", "python main.py"], shell=True)
    else:
        subprocess.Popen(["python3", "main.py"])

start_button = ctk.CTkButton(app, text="🎙️ Start Listening", command=run_voice_assistant, font=("Arial", 16))
start_button.pack(pady=30)

app.mainloop()
