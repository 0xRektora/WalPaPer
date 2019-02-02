__author__ = "Bloodyline01"
__copyright__ = "No copyright followed"
__credits__ = ["Bloodyline01"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Bloodyline01"
__email__ = "Bloodyline01@gmail.com"
__status__ = "Production"

import requests, configparser
from bs4 import BeautifulSoup
import random, datetime
import os, ctypes, sys
import argparse


parser = argparse.ArgumentParser(description='Download and change you current windows wallpaper easily with your settings.')
parser.add_argument('config', type=str,
                    help='The path to the config file.')
parser.add_argument('images', type=str,
                    help='The path to the images file.')
parser.add_argument('log', type=str,
                    help='The path to the logs file.')

args = parser.parse_args()
print(args.config)

def log(text=""):
    with open(args.log, "a") as f:
        toPrint = "\n\t[+] " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "   [ " + text + " ]"
        f.writelines(toPrint)
        print(toPrint)

with open(args.log, "a") as f:
    f.writelines("------ Initializing ------\n")

config = configparser.ConfigParser()
config.read(args.config)

query = "https://alpha.wallhaven.cc"
query += "/search?q="

query += config.get("search", "keyword")

for item in config.items("config"):
    query += "&" + item[0] + "=" + item[1]

query += "&page=" + str(random.randint(0, 10)) # Choose a random page

headers = {'Accept-Encoding': 'identity', "User-Agent": "Mozilla/532.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}
log("Requesting : " + query)

r = requests.get(query, headers=headers)
if r.status_code == 200:
    soup = BeautifulSoup(r.text, features="html.parser")

    links = soup.find_all('a', {"class":"preview"})

    randLink = random.choice(links).get("href")

    log("Requesting : " + randLink)

    r = requests.get(randLink, headers=headers)

    if r.status_code == 200:

        soup = BeautifulSoup(r.text, features="html.parser")

        links = soup.find_all('img', {"id":"wallpaper"})

        img = random.choice(links).get("src")
        link = "https:"+img

        log("Requesting : " + link)
    

        r = requests.get(link, headers=headers)

        if r.status_code == 200:

            path = args.images + "\\" + config.get("search", "keyword")
            try:
                if not os.path.exists(path):
                    os.mkdir(path)
            except:
                path = args.images + "\\" + "Others"
                if not os.path.exists(path):
                    os.mkdir(path)
                

            path += "\\" +img.split("/")[-1]
            
            try:
                log("Writing to : " + path)
                with open(path, 'wb') as f:
                    f.write(r.content)
            except:
                log("Can't write content to destination : " + path)
            
            try:
                path = os.path.abspath(path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
                log("New wallpaper added " + path)
            except:
                log("Can't change the wallpaper")

        else:
            log("Error getting datas step 3")
    
    else:
        log("Error getting datas step 2")

else:
    log("Error getting datas step 1")

with open(args.log , "a") as f:
    f.writelines("\n\n------ END ------\n\n")
