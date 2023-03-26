import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from tkinter import ttk


def download_video():
    url = url_entry.get()
    save_path = path_entry.get()
    filename = filename_entry.get()

    try:
        yt = YouTube(url)
        video = yt.streams.filter(res="720p").first()
        size = video.filesize
        print(f"Title: {yt.title}")
        print(f"URL: {url}")
        print(f"Save Path: {save_path}")
        print(f"Filename: {filename}")
        print(f"Resolution: 720p")
        print(f"Size: {size / 1024 / 1024:.2f} MB")

        video.download(output_path=save_path, filename=filename + '.mp4')
                       # progress_callback=progress_callback)

        messagebox.showinfo(title="Download Completed", message="Video download completed!")
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        messagebox.showerror(title="Download Failed", message=error_message)


def update_progressbar(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded / total_size * 100
    progress_bar["value"] = percent
    root.update_idletasks()


root = tk.Tk()
root.title("YT Video Downloader")

url_label = tk.Label(root, text="Video URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

path_label = tk.Label(root, text="Save Path:")
path_label.pack()
path_entry = tk.Entry(root)
path_entry.pack()

filename_label = tk.Label(root, text="Filename:")
filename_label.pack()
filename_entry = tk.Entry(root)
filename_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

log_text = tk.Text(root)
log_text.pack()

root.mainloop()
