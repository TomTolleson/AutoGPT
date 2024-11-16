from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio_on_silence(input_file, output_dir, min_silence_len=1000, silence_thresh=-16, keep_silence=200):
    """
    Splits an audio file into smaller files based on silence.

    Args:
        input_file (str): Path to the input audio file.
        output_dir (str): Directory to save the output files.
        min_silence_len (int): Minimum length of silence in milliseconds to split on.
        silence_thresh (int): Silence threshold in dBFS.
        keep_silence (int): Amount of silence to keep at the beginning and end of each chunk.
    """

    sound = AudioSegment.from_file(input_file)
    chunks = split_on_silence(
        sound,
        min_silence_len=500,
        silence_thresh=-60,
        keep_silence=100
    )

    for i, chunk in enumerate(chunks):
        output_file = f"{output_dir}/chunk_{i}.wav"
        chunk.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = "/Users/tomtolleson/AutoGPT/autogpt_platform/shared/gosubcoda/audio/notebook.wav"  # Replace with your file
    output_dir = "/Users/tomtolleson/AutoGPT/autogpt_platform/shared/gosubcoda/audio/processed"  # Replace with desired output directory
    split_audio_on_silence(input_file, output_dir)