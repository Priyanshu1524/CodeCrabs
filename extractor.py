import os
import json


def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url
    }


def extract_video_data_from_url(url):
    command = f'yt-dlp "{url}" -j --no-playlist'
    output = os.popen(command).read()
    if not output.strip():
        raise ValueError("Failed to get video info. Is yt-dlp installed? Is the URL valid?")
    try:
        video_data = json.loads(output)
    except json.JSONDecodeError:
        print("Command output:\n", output)
        raise

    title = video_data["title"]
    formats = video_data["formats"]
    thumbnail = video_data.get("thumbnail", "")
    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title": title,
        "formats": formats,
        "thumbnail": thumbnail
    }
