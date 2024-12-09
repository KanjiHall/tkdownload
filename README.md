# tkdownload
This tool automates downloading TikTok videos using the tkdown.net API. It processes multiple URLs from a file, extracts video IDs, and saves videos directly to your local storage in bulk. Simplify retrieving and saving TikTok videos without manually interacting with the website.

### User Guide for Video Download Program

#### 1. System Requirements
- Python 3.6 or later
- Internet connection for downloading videos
- Operating system that supports Python (Windows, macOS, Linux)

---

#### 2. Install Dependencies

Download Python from here: https://www.python.org/downloads/

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

#### 3. Configure the URL List File
1. Create a text file named `urls.txt` in the same directory as the program.
2. Add video URLs to the `urls.txt` file, one URL per line. For example:
   ```
    https://www.tiktok.com/@ikeahacksandideas/video/7290635561692450080?is_from_webapp=1&sender_device=pc&web_id=7413327064453072426
    https://www.tiktok.com/@what.bb.built/video/7200184250677644587?is_from_webapp=1&sender_device=pc&web_id=7413327064453072426
    https://www.tiktok.com/@sues_daily/video/7201952794197101830?is_from_webapp=1&sender_device=pc&web_id=7413327064453072426
   ```

---

#### 4. Run the Program
1. Open a terminal or command prompt.
2. Execute the program with the following command:
   ```bash
   python script_name.py
   ```
   (Replace `script_name.py` with the name of your Python script.)

---

#### 5. Check the Results
- After the program finishes downloading, videos will be saved in the current directory with the format `video_id.mp4`.
- Example: If the video ID is `123456`, the downloaded file will be named `123456.mp4`.

---

#### 6. Notes
- If any errors occur (e.g., video ID not found or download failed), the program will display a specific error message.
- Ensure that the `urls.txt` file does not contain blank lines or invalid URLs.

---

#### 7. Contact for Support
If you encounter issues or need assistance, please reach out via email or the developer's GitHub.
