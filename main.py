# ===== Modules =====
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import random
import os

# === Jarvis ===
class jarvis:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""

    def run(self):
        self.say("Hello Bhai! I am Jarvis. How can I help you?")
        while True:
            command = self.listen()
            if "exit" in command:
                self.say("Exiting Jarvis.")
                break
            elif "open youtube" in command:
                webbrowser.open("youtube.com")
                self.say("Opening YouTube")

# === Task Manager ===
class taskManager:
    def __init__(self):
        self.task_list = []
        self.next_id = 1

    def add_task(self):
        task = input("Enter a task> ")
        self.task_list.append({"id": self.next_id, "task": task})
        print(f"Task added with ID {self.next_id}")
        self.next_id += 1

    def view_task(self):
        if not self.task_list:
            print("No tasks found.")
        else:
            for t in self.task_list:
                print(f"{t['id']}. {t['task']}\n")

    def remove_task(self):
        self.view_task()
        try:
            task_id = int(input("Enter the ID of task to remove> "))
            for t in self.task_list:
                if t["id"] == task_id:
                    self.task_list.remove(t)
                    print(f"Task {task_id} removed.")
                    return
            print("Task ID not found.")
        except ValueError:
            print("Invalid input, enter a number.")

    def run(self):
        while True:
            choice = input("1-Add task\n2-View Task\n3-Remove Task\n4-Exit\nEnter your choice> ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

# === NotePad ===
class notePad:
    def __init__(self):
        self.note_list = []
        self.next_id = 1

    def add_note(self):
        note = input("Write your note> ")
        self.note_list.append({"id": self.next_id, "note": note})
        print(f"Note added with ID {self.next_id}")
        self.next_id += 1

    def view_note(self):
        if not self.note_list:
            print("No notes found.")
        else:
            for n in self.note_list:
                print(f"{n['id']}. {n['note']}")

    def remove_note(self):
        self.view_note()
        try:
            note_id = int(input("Enter the ID of note to remove> "))
            for n in self.note_list:
                if n["id"] == note_id:
                    self.note_list.remove(n)
                    print(f"Note {note_id} removed.")
                    return
            print("Note ID not found.")
        except ValueError:
            print("Invalid input, enter a number.")

    def run(self):
        while True:
            choice = input("1-Add note\n2-View note\n3-Remove note\n4-Exit\nEnter your choice> ")
            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.view_note()
            elif choice == "3":
                self.remove_note()
            elif choice == "4":
                break
            else:
                print("Invalid Input.")

# === Games ===
class games:
    def __init__(self):
        self.choices = list(range(1, 10))

    def guessTheNumber(self):
        random_num = random.choice(self.choices)
        try:
            user_num = int(input("Guess the number> "))
            if user_num == random_num:
                print("You guessed the correct number!")
            else:
                print(f"Wrong! The number was {random_num}.")
        except ValueError:
            print("Invalid input! Enter a number.")

    def rockPaperScissors(self):
        options = ["rock", "paper", "scissors"]
        user = input("Choose rock, paper, or scissors> ").lower()
        comp = random.choice(options)
        print(f"Computer chose: {comp}")
        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("You lose!")

    def diceRoll(self):
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")

    def run(self):
        while True:
            choice = input("Choose game (guess/rps/dice/exit)> ").lower()
            if choice == "guess":
                self.guessTheNumber()
            elif choice == "rps":
                self.rockPaperScissors()
            elif choice == "dice":
                self.diceRoll()
            elif choice == "exit":
                break
            else:
                print("No game available with this name.")

# ===== Code Editor =====
class codeEditor:
    def __init__(self, folder="code_files"):
        self.folder = folder
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    # Create new file
    def create_file(self):
        filename = input("Enter file name> ")
        filepath = os.path.join(self.folder, filename)
        if os.path.exists(filepath):
            print("File already exists!")
            return
        content = input("Enter your code (type 'END' in new line to finish):\n")
        lines = []
        while content != "END":
            lines.append(content)
            content = input()
        with open(filepath, "w") as f:
            f.write("\n".join(lines))
        print(f"{filename} created successfully!")

    # View file
    def view_file(self):
        self.list_files()
        filename = input("Enter file name to view> ")
        filepath = os.path.join(self.folder, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                print("\n--- FILE CONTENT ---")
                print(f.read())
                print("--- END OF FILE ---\n")
        else:
            print("File not found!")

    # Edit file
    def edit_file(self):
        self.list_files()
        filename = input("Enter file name to edit> ")
        filepath = os.path.join(self.folder, filename)
        if os.path.exists(filepath):
            with open(filepath, "a") as f:
                print("Enter code to append (type 'END' in new line to finish):")
                line = input()
                while line != "END":
                    f.write(line + "\n")
                    line = input()
            print(f"{filename} edited successfully!")
        else:
            print("File not found!")

    # Delete file
    def delete_file(self):
        self.list_files()
        filename = input("Enter file name to delete> ")
        filepath = os.path.join(self.folder, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"{filename} deleted successfully!")
        else:
            print("File not found!")

    # List all files
    def list_files(self):
        files = os.listdir(self.folder)
        if files:
            print("Files in editor:")
            for f in files:
                print("-", f)
        else:
            print("No files found.")

    # Main editor loop
    def run(self):
        while True:
            choice = input("\n1-Create file\n2-View file\n3-Edit file\n4-Delete file\n5-List files\n6-Exit\nEnter choice> ")
            if choice == "1":
                self.create_file()
            elif choice == "2":
                self.view_file()
            elif choice == "3":
                self.edit_file()
            elif choice == "4":
                self.delete_file()
            elif choice == "5":
                self.list_files()
            elif choice == "6":
                break
            else:
                print("Invalid choice")



# === Alarm ===
def alarm():
    try:
        choice_time = int(input("Set reminder time (seconds)> "))
        print(f"Alarm set for {choice_time} seconds...")
        time.sleep(choice_time)
        print("Times up!")
    except ValueError:
        print("Invalid Input. Enter a number.")

# === Calculator ===
def calculator():
    while True:
        a = input("Enter first number> ")
        if a == "exit":
            break
        b = input("Enter second number> ")
        if b == "exit":
            break
        try:
            result = eval(a + "+" + b)
            print("Result:", result)
        except:
            print("Invalid input, try numbers or type 'exit' to quit.")

# === MINIOS Main Loop ===
if __name__ == "__main__":
    print("Welcome to MINIOS! Type 'help' to view all commands.")

    while True:
        cmd = input("MINIOS> ").lower()

        if cmd == "help":
            print("Commands:")
            print("help")
            print("calculator")
            print("jarvis")
            print("task manager")
            print("notepad")
            print("games")
            print("alarm")
            print("code editor")
            print("exit")

        elif cmd == "jarvis":
            jarvis().run()

        elif cmd == "calculator":
            calculator()

        elif cmd == "task manager":
            taskManager().run()

        elif cmd == "notepad":
            notePad().run()

        elif cmd == "alarm":
            alarm()

        elif cmd == "games":
            games().run()
        
        elif cmd == "code editor":
            codeEditor().run()

        elif cmd == "exit":
            print("Exiting MINIOS...")
            break

        else:
            print("Unknown command, type 'help' to see commands")
