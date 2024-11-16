from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import time

class AudioProcessingHandler(FileSystemEventHandler):
    def __init__(self, script1_path, script2_path):
        self.script1_path = script1_path
        self.script2_path = script2_path

    def on_created(self, event):
        if event.is_directory:
            return
            
        # Check if the new file is an audio file
        if event.src_path.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
            print(f"New audio file detected: {event.src_path}")
            
            # Wait for file to be completely written
            self._wait_for_file_ready(event.src_path)
            
            # Run scripts in sequence
            print("Running first script...")
            subprocess.run(["python", self.script1_path])
            
            print("Running second script...")
            subprocess.run(["python", self.script2_path])

    def _wait_for_file_ready(self, filepath, timeout=60):
        """Wait until file is completely written"""
        previous_size = -1
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            current_size = os.path.getsize(filepath)
            if current_size == previous_size:
                return
            previous_size = current_size
            time.sleep(1)

def start_monitoring(directory_path, script1_path, script2_path):
    event_handler = AudioProcessingHandler(script1_path, script2_path)
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    # Configure these paths according to your setup
    WATCH_DIRECTORY = "/path/to/watch/directory"
    SCRIPT1_PATH = "/path/to/first_script.py"
    SCRIPT2_PATH = "/path/to/second_script.py"
    
    start_monitoring(WATCH_DIRECTORY, SCRIPT1_PATH, SCRIPT2_PATH)