from pytube import YouTube
import os
from moviepy.editor import *





while True:
    a = input('請輸入欲下載影片連結 : ')
    if  'https://www.youtube.com' in a: break
    else: print('請輸入正確連結')

reslist = [144 , 240 , 360 , 480 , 720 , 1080 , 1440 , 2160 , 4320]

while True:
    r = input('請輸入畫質 : ')
    if int(r) in reslist:
            break
    else:
        print('無此畫質選項')

ress = r+'p' 

try:
    yt = YouTube(a)
except:
    print('連結有誤，無法下載')
    os._exit(0) 


n = True ; i=0

while (n):
    i+=1
    try:
        mb_ = yt.streams.filter(res=ress).first().filesize_mb #大小
        mb_+= yt.streams.filter(type="audio").first().filesize_mb
        mb_=round(mb_,2)
        if i == 1:
            print(f"下載中，共 {mb_} MB")
            n = 0
        else: 
            print(f'無 {firstress[:-1]}P 畫質，自動調至 {ress[:-1]}P 大小{mb_} MB')
            n = 0
        

    except: 
        if i == 1 : firstress = ress
        if int(ress[:-1]) > 720:
            ress = int(ress[:-1])
            ress -= 360
            ress = str(ress)+'p'
        elif ress == '720p':
            ress = '480p'
        elif ress == '480p':
            ress = '360p'
        elif ress == '360p':
            ress = '240p'
        elif ress == '240p':
            ress = '144p'
            


tvideo = yt.streams.filter(res=ress,type='video').first()
tvideo_filename = 'video'
tvideo.download(filename=tvideo_filename)
taudio = yt.streams.filter(type='audio').first()
taudio_filename = 'audio'
taudio.download(filename=taudio_filename)
filename_ = tvideo.default_filename

os.system(f'ffmpeg -i "{tvideo_filename}" -i "{taudio_filename}" -c copy "{tvideo.default_filename[:-4]}.mp4"')
os.remove(tvideo_filename)
os.remove(taudio_filename)
