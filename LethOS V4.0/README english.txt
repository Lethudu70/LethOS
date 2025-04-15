Description:
LethOS is a simulated operating system designed to provide an interactive experience through a command line interface. This program simulates various functionalities such as temperature conversion, file exploration, virtual disk management, and more.




Key Features:

Temperature Conversion: Convert temperature between different units (Celsius, Fahrenheit, Kelvin) to the custom unit °W.

Virtual Disk: Create a virtual disk and copy executable files to this disk.

Startup and Shutdown Sounds: Upon startup, a Windows XP startup sound is played. The same sound plays during shutdown.

Boot Screen: A progress bar is displayed during system startup.

System Management Options: You can shut down, restart, or return to the shell via an interactive menu.

Date and Time Display: Commands to display the current date and real-time clock.

Random Facts: A command to display interesting and random facts with every call.

Real-time Clock: Displays the current time with live updates on the console.

Equipped with the latest Leth Exploro: A program-specific file explorer.

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Available Commands:

help: Displays a list of available commands.

clear: Clears the screen.

echo [text]: Displays the specified text.

ls: Lists files and folders in the current directory.

shutdown: Opens shutdown options (Shutdown, Restart, Return to Shell).

explorer: Opens the file explorer.

wedo_converter: Launches the temperature converter to the °W unit.

info: Displays system information.

play: Plays a sound or video file.

date: Displays the current date.

random_fact: Displays a random fact.

clock: Displays the current time in real-time.

joke: Displays a random joke.

calculator: Launches a simple calculator.

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Installation Instructions:

Ensure Python 3.x is installed on your machine.

Place this program in a directory of your choice.

Place the necessary sound files (Windows XP Startup, Shutdown, and Error) in the C:\sound for LethOS\ directory for the sounds to play correctly.

Run the program using the command python lethos.py or python3 lethos.py in your terminal.

Warnings:

This program is designed to work only on Windows systems due to the use of specific file paths and the winsound library for sound management.

The required sound files and other necessary files must be in the specified paths to avoid errors during execution.

Author: Developed by Leth.

License:

This program is provided under the MIT License.