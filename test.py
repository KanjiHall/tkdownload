import requests

burp0_url = "https://api.tkdown.net:443/v2/download?post_id=7200184250677644587&type=nowm"
burp0_cookies = {"_ga": "GA1.1.349337245.1733669127", "_clck": "z3rnxe%7C2%7Cfrj%7C0%7C1803", "_clsk": "1u8px38%7C1733669147213%7C1%7C1%7Cw.clarity.ms%2Fcollect", "__gads": "ID=c985beb2e69f3282:T=1733669170:RT=1733669170:S=ALNI_MYKtqgjA3xVnVGWa7OLJT8o280e7g", "__gpi": "UID=00000f87a0454341:T=1733669170:RT=1733669170:S=ALNI_MY22_R80qdiE0KRth_hSwC62H1_rQ", "__eoi": "ID=c8972596963ad2d7:T=1733669170:RT=1733669170:S=AA-AfjZNVvIR1u1_ShlOYGSp1PrG", "_ga_2XBNWN4QFK": "GS1.1.1733669127.1.1.1733669174.0.0.0", "FCNEC": "%5B%5B%22AKsRol8diImBvxzpzjInncf5cVzPKfuSXPPvD7sYIVtek0vhpFUG85OpPH_7PPd4ajnoH-rXWUVgEU9nSk22vTpYAYGy1zZ8n6vLqkJRLwSrRgJWUMQ6t54dOv1fb91A8mb6HBR9wf2iO0fe1YhLAm5jv19oyVG-kQ%3D%3D%22%5D%5D"}
burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept-Language": "en-US,en;q=0.9", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "iframe", "Referer": "https://tkdown.net/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=0, i", "Connection": "keep-alive"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)