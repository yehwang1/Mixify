# A Spotify playlist Application developed by Brian Hwang, 2021. 
# Copyright © 2021 Brian Hwang. All rights reserved.
import tkinter as tk
from playlist_generate import *
window = tk.Tk() #Main window
window.title("Mixify - A Spotify Playlist Generator")
window.configure(background="#343434")
#Top main label
label = tk.Label(text="Welcome to Mixify!",font=("Helvetica Nueue",45))
label.configure(background="#343434",fg='#E5E4E2')
label.grid(row=0)
#Spotify Logo
logo = tk.PhotoImage(file="Spotify-logo.png")
smaller_image = logo.subsample(20,20)
w1 = tk.Label(window, image=smaller_image).grid(row=2)
#Small description label
description = tk.Label(text="\nA Spotify playlist generating application designed to seamlessly mix and blend playlists together into one.",font=("Helvetica Nueue",15))
description.configure(background="#343434",fg='#E5E4E2')
description.grid(row=3)
#space filler
space = tk.Label(text="",font=("Helvetica Nueue",10))
space.configure(background="#343434",fg='#E5E4E2')
space.grid(row=4)
#Inputs
#number of playlists
playlist_num_label = tk.Label(text="How many playlists would you like to incorporate? (maximum of 5)",font=("Helvetica Nueue",20))
playlist_num_label.configure(background="#343434",fg='#E5E4E2')
playlist_num_label.grid(row=7)
num_playlists_entry = tk.Entry(window,width=3)
num_playlists_entry.grid(row=8)
#number of songs in desired playlist
song_num_label = tk.Label(text="How many songs would you like in your playlist? (minimum of 1, maximum of 100)",font=("Helvetica Nueue",20))
song_num_label.configure(background="#343434",fg='#E5E4E2')
song_num_label.grid(row=10)
num_songs_entry = tk.Entry(window,width=3)
num_songs_entry.grid(row=11)
#Playlist URLs
url_label = tk.Label(text="Enter your playlists' URLs, separated by a space between each URL.",font=("Helvetica Nueue",20))
url_label.configure(background="#343434",fg='#E5E4E2')
url_label.grid(row=12)
url_entry = tk.Entry(window,width=70)
url_entry.grid(row=13)
#Playlist Name
name_label = tk.Label(text="What would you like to name your playlist?",font=("Helvetica Nueue",20))
name_label.configure(background="#343434",fg='#E5E4E2')
name_label.grid(row=14)
name_entry = tk.Entry(window,width=20)
name_entry.grid(row=15)
#space filler
space = tk.Label(text="",font=("Helvetica Nueue",20))
space.configure(background="#343434",fg='#E5E4E2')
space.grid(row=16)
#Make playlist function using Spotify API
def make_playlist():
    num_playlists = num_playlists_entry.get()
    num_tracks = num_songs_entry.get()
    urls_input = url_entry.get()
    url_list = urls_input.split()
    playlist_name = name_entry.get()
    create_playlist(num_tracks=num_tracks,num_playlists=num_playlists,url_list=url_list,playlist_name=playlist_name)
    congrats = tk.Label(text="Happy listening!",font=("Helvetica Nueue",20))
    congrats.configure(background="#343434",fg='#E5E4E2')
    congrats.grid(row=19)
#Make playlist button
make_playlist_button = tk.Button(window,text = 'Make my playlist!',command=make_playlist)
make_playlist_button.grid(row=17)
#space filler
space = tk.Label(text="",font=("Helvetica Nueue",40))
space.configure(background="#343434",fg='#E5E4E2')
space.grid(row=18)
#Copyright
copyright = tk.Label(text="Developed by Brian Hwang, 2021. Copyright © 2021 Brian Hwang. All rights reserved.",font=("Helvetica Nueue",12))
copyright.configure(background="#343434",fg='#E5E4E2')
copyright.grid(row=20)

window.mainloop()
