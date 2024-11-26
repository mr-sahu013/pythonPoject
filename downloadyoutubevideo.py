from pytube import YouTube
import time

def download_youtube_video(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the stream for 1080p resolution
        video_stream = yt.streams.filter(res="1080p", file_extension='mp4').first()

        if video_stream is None:
            print("1080p video stream is not available.")
            return

        # Define a callback function to show progress
        def progress_callback(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percent_complete = (bytes_downloaded / total_size) * 100
            elapsed_time = time.time() - start_time
            print(f'Download progress: {percent_complete:.2f}% | Time elapsed: {elapsed_time:.2f} seconds', end='\r')

        # Set the callback function
        yt.register_on_progress_callback(progress_callback)

        print(f'Starting download for: {yt.title}')
        start_time = time.time()

        # Download the video
        video_stream.download()

        print(f'\nDownload completed: {yt.title}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Replace the URL with the desired YouTube video URL
video_url = "https://youtu.be/aZb0iu4uGwA?si=QKG867M5nEqdlQ0V"
download_youtube_video(video_url)