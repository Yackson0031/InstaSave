from datetime import datetime
from tqdm import tqdm
import requests
import re
import sys

# Banner
print(''' 
 
                        [Coded Edited By Yackson0031]

''')


# Function to download an instagram photo or video
def download_image_video():
    url = input("Please enter image/video URL: ")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                # print("\nDownloading the image...")
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                download_link = final + '&dl=1'
                print(download_link)

            if final == "video":
                extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                video_link = extract_video_link.group()
                final = re.sub('meta property="og:video" content="', '', video_link)
                downloadable_link = final + '&dl=1'
                print(downloadable_link)

        else:
            print("Entered URL is not an instagram.com URL.")
    except AttributeError:
        print("Unknown URL")


download_image_video()