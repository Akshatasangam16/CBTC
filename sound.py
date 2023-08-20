import sounddevice as sd
import wavio

def record_audio(filename, duration, sample_rate):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio_data, sample_rate, sampwidth=2)  # Save recorded audio as WAV file
    print(f"Audio saved as '{filename}'")

def main():
    filename = input("Enter the name of the audio file to save (e.g., recording.wav): ")
    duration = float(input("Enter the duration of the recording (in seconds): "))
    sample_rate = 44100  # You can adjust the sample rate as needed
    
    record_audio(filename, duration, sample_rate)

if _name_ == "_main_":
    main()