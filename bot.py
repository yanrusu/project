import discord  
from discord.ext import commands, tasks  
import json  
import datetime  # datetime 模組，處理日期和時間
from searchweather import status  

# 從 TOKEN.json 讀取 Token，token 是機器人的鑰匙，要有 token 才能控制機器人
with open('TOKEN.json', "r", encoding="utf8") as jsonf:
    jdata = json.load(jsonf)

# 創建權限，允許機器人訪問所有功能
intents = discord.Intents.all()

# 指定命令前綴為 '!'，並指定使用的權限
bot = commands.Bot(command_prefix='!', intents=intents)

# 指定天氣信息發送的 Discord 頻道 ID
weatherchannel = 1140835388815061072

# 當機器人上線時的事件處理函數
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")  # 輸出機器人的身份
    print('Bot 已經上線！')  # 輸出上線信息
    print(status)  # 輸出天氣資訊 
    getweather.start()  # 開始 getweather 循環任務

# 當機器人重新連接時的事件處理函數
@bot.event
async def on_resumed():
    print('Bot 已經重新連接！')  # 輸出重新連接信息

# 創建名為 todayweather 的命令，使用 !todayweather 可獲取天氣
@bot.command()
async def todayweather(ctx):
    await ctx.send(status)  # 發送天氣資訊至發送指令的頻道

# 設定每 60 秒運行一次的循環任務 getweather
@tasks.loop(seconds=60)
async def getweather():
    now = datetime.datetime.now().strftime("%H%M")  # 取得當前時間的小時和分鐘
    specified_time = "0600"  # 指定特定的時間為 "0600"
    
    if now == specified_time:  # 如果當前時間等於指定的時間，運行下方程式
        infweather = status  # 獲取天氣資訊
        channel = bot.get_channel(weatherchannel)  # 獲取指定的 Discord 頻道
        await channel.send(infweather)  # 發送天氣資訊至指定的頻道

# 使用 Token 啟動機器人
bot.run(jdata['token'])  # 使用從 JSON 文件讀取的 Token 啟動機器人
