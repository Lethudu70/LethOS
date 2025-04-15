import os
import time
import winsound
import threading
import subprocess
import socket
import tkinter as tk
from tkinter import simpledialog
import sys
import random

# Path to audio files
startup_sound_path = "C:\\sound for LethOS\\Windows XP Startup.wav"
shutdown_sound_path = "C:\\sound for LethOS\\Windows XP Shutdown.wav"
error_sound_path = "C:\\sound for LethOS\\Windows XP Error.wav"

# Path to the virtual disk
disk_path = "C:/LethOS/VirtualDisk"

# Function to convert temperature to °W
def convert_temperature(temp, unit):
    if unit == 'C':
        converted_temp = temp * 1.8
        return f"{temp}°C = {converted_temp}°W"
    elif unit == 'F':
        converted_temp = (temp - 32) * 5 / 9 * 1.8
        return f"{temp}°F = {converted_temp}°W"
    elif unit == 'K':
        converted_temp = (temp - 273.15) * 1.8
        return f"{temp}K = {converted_temp}°W"
    else:
        return "Unsupported temperature unit!"

def wedo_converter():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Enter the temperature unit (C, F, K): ").upper()
        result = convert_temperature(temp, unit)
        print(f"\033[92m{result}\033[0m")
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid number.\033[0m")

def create_virtual_disk():
    if not os.path.exists(disk_path):
        os.makedirs(disk_path)
        print("\033[92mVirtual Disk created successfully!\033[0m")

def copy_explorer_exe_to_virtual_disk():
    source_exe = "Leth_Exploro.exe"
    destination = os.path.join(disk_path, source_exe)
    if os.path.exists(source_exe):
        try:
            if not os.path.exists(destination):
                with open(source_exe, 'rb') as src, open(destination, 'wb') as dst:
                    dst.write(src.read())
                print("\033[92mLeth_Exploro.exe copied to VirtualDisk.\033[0m")
        except Exception as e:
            print(f"\033[91mError copying Leth_Exploro.exe: {e}\033[0m")
    else:
        print("\033[91mLeth_Exploro.exe not found in current directory!\033[0m")

def play_startup_sound():
    try:
        winsound.PlaySound(startup_sound_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"\033[91mError playing startup sound: {e}\033[0m")

def play_shutdown_sound():
    try:
        winsound.PlaySound(shutdown_sound_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"\033[91mError playing shutdown sound: {e}\033[0m")

def play_error_sound():
    try:
        winsound.PlaySound(error_sound_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"\033[91mError playing error sound: {e}\033[0m")

def boot_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m")
    print(" " * 40 + "****************************************")
    print(" " * 40 + "**                                    **")
    print(" " * 40 + "**         LethOS Booting...          **")
    print(" " * 40 + "**                                    **")
    print(" " * 40 + "****************************************")
    print("\033[0m")
    play_startup_sound()
    print("\033[94mLoading LethOS...\033[0m")
    bar_length = 50
    for i in range(bar_length + 1):
        bar = "=" * i + " " * (bar_length - i)
        percent = (i / bar_length) * 100
        print(f"\r[{bar}] {percent:.2f}%", end="", flush=True)
        time.sleep(0.1)
    print("\n\033[92mSystem initializing...\033[0m")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def shutdown():
    while True:
        print("\033[93mShutdown Options:\033[0m")
        print("1: Shutdown")
        print("2: Restart")
        print("3: Return to Shell")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\033[92mThank you for using LethOS!\033[0m")
            play_shutdown_sound()
            print("\033[92mShutting down...\033[0m")
            exit()
        elif choice == "2":
            print("\033[92mRestarting...\033[0m")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            shell()
        elif choice == "3":
            return
        else:
            play_error_sound()
            print("\033[91mInvalid option. Please try again.\033[0m")

def shell():
    create_virtual_disk()
    copy_explorer_exe_to_virtual_disk()
    boot_screen()
    print("\033[92mLethOS Shell - Type 'help' for commands\033[0m")
    while True:
        try:
            command = input("\033[92mLethOS> \033[0m").strip()
            if command == "shutdown":
                shutdown()
            elif command == "help":
                print("\033[92mAvailable commands: clear, echo [text], ls, shutdown, explorer, wedo_converter, info, play, date, random_fact, joke, calculator\033[0m")
            elif command.startswith("echo"):
                print(" ".join(command.split()[1:]))
            elif command == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
            elif command == "ls":
                list_files()
            elif command == "explorer":
                open_explorer()
            elif command == "wedo_converter":
                wedo_converter()
            elif command == "info":
                show_info()
            elif command == "play":
                play_sound_or_video()
            elif command == "date":
                display_date()
            elif command == "random_fact":
                display_random_fact()
            elif command == "joke":
                tell_joke()
            elif command == "calculator":
                start_calculator()
            else:
                play_error_sound()
                print("\033[91mUnknown command.\033[0m")
        except Exception as e:
            print(f"\033[91mAn error occurred: {e}\033[0m")
            input("Press Enter to continue...")

def display_date():
    try:
        current_date = os.popen('date /t').read().strip()
        print(f"\033[92mToday's date: {current_date}\033[0m")
    except Exception as e:
        print(f"\033[91mError displaying the date: {e}\033[0m")

def display_random_fact():
    print("\033[92mDid you know? The Eiffel Tower can be 15 cm taller during the summer.\033[0m")

def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why can't you give Elsa a balloon? Because she will let it go.",
        "What did one ocean say to the other ocean? Nothing, they just waved.",
        "Why don't some couples go to the gym? Because some relationships don't work out.",
        "Why did the scarecrow win an award? Because he was outstanding in his field."
    ]
    print("\033[92m" + random.choice(jokes) + "\033[0m")

def play_sound_or_video():
    while True:
        file_path = input("\033[92mEnter the audio or video file path (or type 'exit' to return to the shell): \033[0m").strip()
        if file_path.lower() == 'exit':
            print("\033[92mReturning to the shell...\033[0m")
            break
        if os.path.exists(file_path):
            if file_path.endswith(('.mp3', '.wav', '.mp4', '.avi')):
                try:
                    os.startfile(file_path)
                    print(f"\033[92mPlaying {file_path}...\033[0m")
                except Exception as e:
                    print(f"\033[91mError playing the file: {e}\033[0m")
            else:
                print("\033[91mThe file must be an audio (.mp3, .wav) or video (.mp4, .avi) file.\033[0m")
        else:
            print(f"\033[91mFile {file_path} not found.\033[0m")

def list_files():
    try:
        current_dir = os.getcwd()
        files = os.listdir(current_dir)
        print("\033[92mListing files in:", current_dir, "\033[0m")
        for file in files:
            print(file)
    except Exception as e:
        print(f"\033[91mError listing files: {e}\033[0m")

def open_explorer():
    exe_path = os.path.join(disk_path, "Leth_Exploro.exe")
    if os.path.exists(exe_path):
        try:
            os.startfile(exe_path)
            print("\033[92mLaunching LethOS File Explorer...\033[0m")
        except Exception as e:
            print(f"\033[91mError launching File Explorer: {e}\033[0m")
    else:
        print("\033[91mLeth_Exploro.exe not found in VirtualDisk!\033[0m")

def show_info():
    print("\033[92m")
    print("****************************************")
    print("**                                    **")
    print("**            LethOS 4.0              **")
    print("**         Developed by Leth          **")
    print("**      A basic operating system      **")
    print("**            Version 4.0             **")
    print("**                                    **")
    print("****************************************")
    print("\033[0m")

def start_calculator():
    calc_window = tk.Tk()
    calc_window.title("Calculator")
    entry = tk.Entry(calc_window, width=25, font=('Arial', 14), borderwidth=2, relief="solid")
    entry.grid(row=0, column=0, columnspan=4)
    def button_click(value):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + value)
    def clear():
        entry.delete(0, tk.END)
    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0),
    ]
    for (text, row, col) in buttons:
        button = tk.Button(calc_window, text=text, width=5, height=2, font=('Arial', 12),
                           command=lambda t=text: button_click(t) if t != "=" and t != "C" else (calculate() if t == "=" else clear()))
        button.grid(row=row, column=col)
    calc_window.mainloop()

if __name__ == "__main__":
    shell()
