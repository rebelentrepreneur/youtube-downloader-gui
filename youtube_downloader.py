import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from pytube import YouTube
import os

def download_video(url, save_path):
    try:
        yt = YouTube(url)  # creating a YouTube object
        streams = yt.streams.filter(progressive=True, file_extension="mp4")  # filtering streams to get progressive streams in mp4 format
        highest_res_stream = streams.get_highest_resolution()  # getting the highest resolution stream
        highest_res_stream.download(output_path=save_path)  # downloading the highest resolution stream to the specified path
        messagebox.showinfo("Success", "Video downloaded successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_directory():
    directory = filedialog.askdirectory(title="Please select the directory you want to save")
    if directory:
        directory_entry.delete(0, tk.END)  # Clear the entry
        directory_entry.insert(0, directory)  # Insert the selected directory
    return directory

def start_download():
    url = url_entry.get()
    save_path = directory_entry.get()
    if url and save_path:
        download_video(url, save_path)
    else:
        messagebox.showwarning("Input Error", "Please enter a URL and select a directory")

# Create the main window
root = ctk.CTk()
root.title("YouTube Downloader")

# URL Entry
url_label = ctk.CTkLabel(root, text="Enter YouTube URL:")
url_label.pack(pady=5)
url_entry = ctk.CTkEntry(root, width=400)
url_entry.pack(pady=5)

# Directory selection
directory_label = ctk.CTkLabel(root, text="Enter the path or Select the Download Directory:")
directory_label.pack(pady=5)
directory_entry = ctk.CTkEntry(root, width=400)
directory_entry.pack(pady=5)
select_button = ctk.CTkButton(root, text="Select Directory", command=select_directory)
select_button.pack(pady=5)

# Download button
download_button = ctk.CTkButton(root, text="Download", command=start_download)
download_button.pack(pady=20)

# Run the application
root.mainloop()
