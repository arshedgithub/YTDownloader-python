from tkinter import *
from tkinter import filedialog
from pytube import YouTube

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

screen = Tk()
title = screen.title("UTube Downloader")
canvas = Canvas(screen, width=500, height=400)

# logo_img = PhotoImage(file='yt.png')
# logo_img = logo_img.subsample(2,2)
# canvas.create_image(250, 80, image=logo_img)
canvas.pack()

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter the URL",font=('Arial', 12))

path_label = Label(screen, text="Select Path for download",font=('Arial', 12))
select_btn = Button(screen,text="Select", command=select_path)

download_btn = Button(screen,text="Download File")

canvas.create_window(250, 150, window=link_label)
canvas.create_window(250, 175, window=link_field)
canvas.create_window(250, 220, window=path_label)
canvas.create_window(250, 245, window=select_btn)
canvas.create_window(250, 290, window=download_btn)


screen.mainloop()






# url = input("Enter URL : ")

# video = YouTube(url)

# print(video.title)
# print(video.thumbnail_url)
# video.streams.get_highest_resolution().download()
# print('downloaded')
