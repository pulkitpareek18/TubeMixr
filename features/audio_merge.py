from pydub import AudioSegment
import time

def merge_audio(list_of_audio_files):
    # Load the audio files
    audio_files = []
    for audio_file in list_of_audio_files:
        audio_files.append(AudioSegment.from_file(audio_file, format="mp3"))
    
    # Combine the audio files
    combined_audio = AudioSegment.empty()
    for audio in audio_files:
        combined_audio += audio
    
    # Save the combined audio
    combined_audio.export(f"output/combined_audio_{time.time()}.mp3", format="mp3")
    print("Audio combined successfully!")