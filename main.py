import tkinter as tk                 # Graphical User Interface (GUI)
import fnmatch                       # Used to compare filenames
import os                            # Used for basic interactions with operating system
from pygame import mixer             # Module Used for number of channels for playback of Sounds

canvas = tk.Tk()                     # Object canvas initialized by tkinter
canvas.title("MP3_Player")           # Title of the MP3_Player
canvas.geometry("500x450")           # Dimensions of the App
canvas.config(bg="Black")            # Basic Background color of the App (bg)

rootpath = "D:\\SONGS"               # The location of the folder where the songs are stored
pattern = "*.mp3"                    # Pattern of the song files which we want in our music player

mixer.init()                         # Used to initialize the mixer module from pygame

# Defining variables to their respective photos using the tk.PhotoImage function
prev_img = tk.PhotoImage(file = 'prev_img.png')
stop_img = tk.PhotoImage(file = 'stop_img.png')
play_img = tk.PhotoImage(file = 'play_img.png')
pause_img = tk.PhotoImage(file = 'pause_img.png')
next_img = tk.PhotoImage(file = 'next_img.png')

# select function is used to select a particular song and play it
# label.config is used to display the selected song by passing the song name as text in it
# mixer.music.load is used to select the song by passing the rootpath and adding the song name to it
# mixer.music.play function plays that song
# if the text of play_Button is Play then the role of the play button will be to play the song from start but if the
# play_Button text is Unpause then the play button will just resumed the pause song and change the text of play_Button
# to Play
def select():
    if play_Button['text'] == 'Play':
        label.config(text = listbox.get('anchor'))
        mixer.music.load(rootpath + "\\" + listbox.get('anchor'))
        mixer.music.play()
    else:
        mixer.music.unpause()
        play_Button['text'] = 'Play'

# stops the currently playing song
# mixer.music.stop function stops the song
def stop():
    mixer.music.stop()
    listbox.select_clear('active')

# Use of pause button to pause the songs
# if the text of the pause_button is Pause then we pause the song (using music.mixer.pause) and change the text of
# play_Button to Unpause
def pause():
    if pause_Button['text'] == 'Pause':
        mixer.music.pause()
        play_Button['text'] = 'Unpause'

# Changes the name to the next song's name and after that uses the body of select function to play the next song
# listbox.curselection gives the current song's index
def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    # till now the function has successfully changed the name to the next song in queue but now we have to change
    # the song and by using the select function it can be easily done
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    # We changed the song to the next one but will have to change the selection too to the next song otherwise the
    # same song will be keep on playing even after hitting the next button
    # select_clear is used to clear selection
    # listbox.activate is used to select the next_song and select_set is used to set the next_song as default
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

# changes the name to the prev song's name and after that uses the body of the select function to play the previous song
def play_prev():
    prev_song = listbox.curselection()
    prev_song = prev_song[0]-1
    prev_song_name = listbox.get(prev_song)
    label.config(text = prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

# tk.Listbox is used to make a list where we can store the required songs in our MP3_Player
# foreground color (fg) and background color (bg) are initialized with a width of 100
# listbox.pack here is used to close our listbox (here listbox is the initialized variable)
listbox = tk.Listbox(canvas, fg = 'cyan', bg='black', width=100, font=('PatrickHandSC-Regular',10))
listbox.pack(padx = 15, pady = 15)

# tk.Label is used to make a display box where on can place text or images
# here the variable label is defined to display the currently selected song
label = tk.Label(canvas, text = '', bg='black', fg='yellow', font=('PatrickHandSC-Regular',12))
label.pack(pady = 15)

# tk.Frame is used to grp and organize other widgets in this case buttons like play and stop
# anchor in top.pack is used to define the position of the frame in this case centre
top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')

prev_Button = tk.Button(canvas, text='Prev', image=prev_img, bg='black', borderwidth=0, command=play_prev)
prev_Button.pack(pady=15, in_=top, side='left')

stop_Button = tk.Button(canvas, text='Stop', image=stop_img, bg='black', borderwidth=0, command=stop)
stop_Button.pack(pady=15, in_=top, side='left')

play_Button = tk.Button(canvas, text='Play', image=play_img, bg='black', borderwidth=0, command=select)
play_Button.pack(pady=15, in_=top, side='left')

pause_Button = tk.Button(canvas, text='Pause', image=pause_img, bg='black', borderwidth=0, command=pause)
pause_Button.pack(pady=15, in_=top, side='left')

next_Button = tk.Button(canvas, text='Next', image=next_img, bg='black', borderwidth=0, command=play_next)
next_Button.pack(pady=15, in_=top, side='left')


# os.walk is basically used to track the rootpath by using top to bottom approach by first going through root followed
# by the directories and finally coming down files
# fnmatch.filter here basically compares the filename in that directory to the pattern of files required by us
# listbox.insert here inserts all the files in the end of the listbox
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end',filename)

canvas.mainloop()