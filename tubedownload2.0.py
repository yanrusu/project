from pytube import YouTube
import os
from moviepy.editor import *

a = input()    # 輸入 YouTube 連結 
r = input('res:')       # 輸入畫質
ress = r+'p'        # 畫質更改格式
yt = YouTube(a)     # 取得 YouTube 物件


tvideo = yt.streams.filter(res=ress,type='video').first()   # 搜尋指定畫質影像
tvideo_filename = 'video'   # 影像檔案名稱
tvideo.download(filename=tvideo_filename)   # 下載
taudio = yt.streams.filter(type='audio').first()    # 搜尋聲音檔
taudio_filename = 'audio'   #聲音檔案名稱
taudio.download(filename=taudio_filename)   # 下載
filename_ = tvideo.default_filename     #取得原影片名稱

os.system(f'ffmpeg -i "{tvideo_filename}" -i "{taudio_filename}" -c copy "{tvideo.default_filename[:-4]}.mp4"')     # 合併影音
os.remove(tvideo_filename)      # 刪除原影像檔 
os.remove(taudio_filename)      # 刪除原聲音檔 
