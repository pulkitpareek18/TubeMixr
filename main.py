import os
from features.audio_download import download_audio
from features.audio_split import split_audio
from features.audio_merge import merge_audio
from features.read_csv import read_csv

# Clear the temp directory and its subfolders
temp_dir = os.path.join(os.getcwd(), "temp")
for root, dirs, files in os.walk(temp_dir):
    for file in files:
        os.remove(os.path.join(root, file))


# List of URLs with start and end times
url_start_end = []


def command_line_input():
    no_tracks = int(input("Enter the number of tracks: "))
    print("-----------------------------------\n")
    for i in range(no_tracks):
        url = input(f"Enter the URL for track {i+1}: ")
        start = int(input(f"Enter the start time for track {i+1} in seconds: "))
        end = int(input(f"Enter the end time for track {i+1} in seconds: "))
        url_start_end.append([url, start, end])
        print("-----------------------------------\n")

def csv_input():
    global url_start_end
    url_start_end = read_csv("csv/tubemixr.csv")

# User Input
print("Welcome to TubeMixr!")
print("Please select the input method: ")
print("1. Command Line Input")
print("2. CSV File Input")
choice = int(input("Enter your choice: "))
if choice == 1:
    command_line_input()
elif choice == 2:
    csv_input()
else:
    print("Invalid choice. Exiting...")
    exit()


# Download audio and store filenames
names = []
for data in url_start_end:
    url = data[0]
    download_audio(url, name=str(url_start_end.index(data)))
    names.append(str(url_start_end.index(data)))

print(names)

# Split audio files based on start and end times
for name in names:
    index = int(name)
    start = url_start_end[index][1]
    end = url_start_end[index][2]
    split_audio(f"temp/{name}.m4a", start, end)

merge_audio([f"temp/split/{name}.mp3" for name in names])