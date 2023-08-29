from pytube import YouTube

a = input()      # 輸入 YouTube 連結
yt = YouTube(a)     # 取得 YouTube 物件
print(yt.streams.get_highest_resolution())  #印出最高畫質
yt.streams.get_highest_resolution().download()      #下載最高畫質影片