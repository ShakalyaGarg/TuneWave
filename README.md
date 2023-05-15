# MP3 Player
The MP3 Player project is a feature-rich music player application developed using Python and the tkinter library. It provides a user-friendly graphical user interface (GUI) that allows users to play, pause, stop, and navigate between songs in a specified directory.

## Features
**Play**: Users can select a song from the available list and click the "Play" button to start playing the selected song. The player supports playback of MP3 files.  

**Pause**: The "Pause" button allows users to pause the currently playing song. Clicking the "Pause" button again resumes playback from where it was paused.  

**Stop**: Clicking the "Stop" button stops the currently playing song and resets the player to the beginning of the song.

**Next/Previous**: Users can easily navigate between songs by clicking the "Next" and "Previous" buttons. The player automatically loads and plays the next or previous song in the list.  

**Song List**: The application displays a list of available songs in a specified directory. Users can browse through the list and select the desired song to play.  

**Song Information**: The currently playing song's information, including the name of the song, is displayed on the GUI. This allows users to easily identify the song being played.

## Usage
1. Launch the MP3 Player application.
2. Browse the available list of songs displayed on the GUI.
3. Select a song by clicking on it.
4. Click the "Play" button to start playing the selected song.
5. While playing, the "Pause" button can be used to pause the song at any point. Clicking the "Pause" button again resumes playback from where it was paused.
6. To stop playback, click the "Stop" button. This stops the song and resets the player to the beginning of the song.
7. To navigate to the next song, click the "Next" button. The player loads and automatically starts playing the next song in the list.
8. To go back to the previous song, click the "Previous" button. The player loads and automatically starts playing the previous song in the list.

## Preview of the User Interface
![ScreenSnap](https://github.com/ShakalyaGarg/TuneWave/assets/129611852/b5c3b6e6-7a0e-4e69-8f35-0324b35bbef0)



## Customization
The MP3 Player can be customized to suit your preferences:

**Song Directory**: Modify the rootpath variable in the code to specify the directory where your music files are located. This allows you to use the player with your own collection of songs.  

**GUI Customization**: The player's GUI can be customized by replacing the provided images (*prev_img.png, stop_img.png, play_img.png, pause_img.png, next_img.png*) with your own images. Make sure to update the image paths in the code accordingly.

## Prerequisites
Before running the MP3 Player, ensure you have the following:

* *Python 3.0* installed on your system.
* The pygame library installed. You can install it using the command *pip install pygame*.
