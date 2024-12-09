import re
import requests
from threading import Thread

def extract_video_id(url):
    """Trích xuất video ID từ URL."""
    match = re.search(r'/video/(\d+)', url)
    return match.group(1) if match else None

def download_video(video_id, download_api, headers):
    """Tải video từ URL và lưu vào file."""
    response = requests.get(download_api, headers=headers, stream=True)
    if response.status_code == 200:
        file_name = f"{video_id}.mp4"
        with open(file_name, "wb") as video_file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    video_file.write(chunk)
        print(f"Tải video thành công! Video đã được lưu với tên {file_name}")
    else:
        print(f"Không thể tải video {video_id}. Mã trạng thái: {response.status_code}")

def process_url(url, headers):
    """Xử lý một URL, trích xuất video ID và tải video."""
    url = url.strip()
    video_id = extract_video_id(url)
    if video_id:
        print(f"Đang xử lý video ID: {video_id}")
        download_api = f"https://api.tkdown.net:443/v2/download?post_id={video_id}&type=nowm"
        download_video(video_id, download_api, headers)
    else:
        print(f"Không tìm thấy video ID trong URL: {url}")

def process_urls(file_path):
    """Đọc file và xử lý từng URL với đa luồng."""
    with open(file_path, "r") as file:
        urls = file.readlines()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://tkdown.net/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    threads = []
    for url in urls:
        thread = Thread(target=process_url, args=(url, headers))
        threads.append(thread)
        thread.start()

    # Đợi tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

# Đường dẫn tới file urls.txt
file_path = "urls.txt"
process_urls(file_path)