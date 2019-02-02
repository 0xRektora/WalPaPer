# WalPaPer
A simple python script than can download wallpapers and change the current one.
It'll only works with windows.
I use it myself with Windows automatic task, and basically call the script once the user log in.

## Requierments
```
beautifulsoup4==4.7.1
requests==2.21.0
```

## Usage
Call the script as below :
  ```python wallpaper.py config.cfg images log.txt```

You can tweak the names and the path for these files if you feel it to.

## Automatisation
You can call the script **as an administrator** `addTask.bat` to automatically add a new task that'll be called once the user logon.

## Config
You can change the `config.cgf` if you feel it to, i use [Wallhaven](https://alpha.wallhaven.cc/) to gather the images, it'll only work with it, you can check the website and add query parameters based on the GET URL, e.i: https://alpha.wallhaven.cc/search?q=universe+space&categories=111&purity=100&resolutions=1920x1080&sorting=random&order=desc
Would be :
```
[config]
resolutions=1920x1080
categories=111
purity=100
sorting=relevance
order=desc
[search]
keyword=universe+space
```
You can try to mess with the site and the research function and use the parameters you need, just make sure you don't misspell it.

## Demo

![demo.gif](https://github.com/Bloodyline/WalPaPer/blob/master/demo.gif)
