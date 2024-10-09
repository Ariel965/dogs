"""
Module Docstring: main.py
=======================

This is the main module of the read/write to text file project.
"""

__author__ = "Ariel Whittington"
__version__ = "0.1"
__license__ = "None"
__date__ = "October 9, 2024"

def read_file(file_name) -> None:
    """
    Reads a text file and prints it to the console.
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line, end = "")
    
def new_file(file_name) -> None:
    """
    Creates a new text file and writes date to it, OR overwites an existing file.
    """
    with open(file_name, "w") as f:
        f.write("Maine Coon")

def append_file(file_name, data) -> None:
    """
    Appends new data to an existing text file.
    """
    with open(file_name,  "r") as f:
        lines = f.readlines()
    
    with open(file_name, "a") as f:
        last_line = lines[-1].strip()
        if lines and last_line != "":
            f.write("\n")
        f.write(data)
def main():
    """
    Main entry point of application.
    """
    append_file("cats.txt", "Siamese" + "\n")
    with open("cats.txt", 'a') as file:
        user_submission = input("Enter a new cat: ")
        file.write(user_submission + "\n")
        
if __name__ == "__main__":
    """
    Starts the program.
    """
    main()