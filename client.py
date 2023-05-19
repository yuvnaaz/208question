import socket
import tkinter as tk

IP_ADDRESS = "127.0.0.1"
PORT = 1234

def setup():
    global IP_ADDRESS, PORT
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP_ADDRESS, PORT))

def musicWindow():
    window = tk.Tk()
    window.title("Music Player")
    window.geometry("300x300")
    window.configure(bg = "blue")
    # Create the Select Song label
    selectSongLabel = tk.Label(window, text="Select Song")
    selectSongLabel.place(x = 2, y = 1)

    # Create the Listbox for displaying songs
    Listbox = tk.Listbox(window, height = 10, width = 39,activestyle = 'dotbox', bg = 'lightbluesky')
    Listbox.place(x=10,y=10)

    # Create the Scrollbar for the Listbox
    Scrollbar = tk.Scrollbar(Listbox)
    Scrollbar.place(relheight = 1, relx = 1)
    Scrollbar.config(command = Listbox.yview)

    # Create the Play button
    playButton = tk.Button(window, text="Play")
    playButton.place(x = 30, y = 200)

    # Create the Stop button
    stopButton = tk.Button(window, text="Stop")
    stopButton.place(x = 200, y = 200)

    # Create the Upload button
    uploadButton = tk.Button(window, text="Upload")
    uploadButton.place(x = 30, y = 250)

    # Create the Download button
    downloadButton = tk.Button(window, text="Download")
    downloadButton.place(x = 200, y = 250)

    # Create the Info label for displaying status messages
    infoLabel = tk.Label(window, text="")
    infoLabel.place(x = 4, y = 280)

    window.mainloop()

if __name__ == '__main__':
    setup()
    musicWindow()
