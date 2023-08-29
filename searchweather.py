from bs4 import BeautifulSoup  # 匯入 BeautifulSoup 模組，用於解析 HTML
from selenium import webdriver  # 匯入 webdriver 模組，用於模擬瀏覽器行為


# 使用 Chrome 瀏覽器驅動程式
driver = webdriver.Chrome()

# 使用瀏覽器訪問指定的網址
driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000203")

# 獲取網頁源碼
web = driver.page_source

# 關閉瀏覽器
driver.quit()

# 使用 BeautifulSoup 模組解析網頁源碼
soup = BeautifulSoup(web, 'html.parser')

# 尋找特定的 HTML 元素和屬性以取得資料
table = soup.find('div', accesskey="K")
table1 = table.find('div',id="PC_week")
table2 = table1.find('div',class_="table-responsive report-table pc grid_open")
table3 = table2.find('table',id="TableId3hr")
table4 = table3.findAll('td',headers = "PC3_Po")

# 創建一個空列表，以存放降雨機率
w = []

# 逐一處理 table4 中的元素
for i in range(len(table4)):
    # 取得文字
    hrwt = table4[i].get_text() 
    # 取得特定資料
    if i == 0 or i == 1:
        if hrwt != '0%':
            w.append(int(hrwt[:2]))
        else:
            w.append(0)

# 用於判斷降雨情況
rain5 = False  ; rain7 = False ; rain3 = False; norain = False

# 根據降雨率判斷標誌
for i in range(len(w)):
    if w[i]>=70:
        rain7 = True
    elif w[i]>=50:
        rain5 = True
    elif w[i]>=30:
        rain3 = True
    else: 
        norain = True

# 用於儲存天氣狀況
status = ''

# 根據降雨情況設定天氣狀況
if rain7:
    status = '降雨率 70% 以上，記得帶拖鞋'
elif rain5:
    status = '降雨率 50% 以上，可能要帶拖鞋'
elif rain3:
    status = '降雨率 30% 以上，應該不用帶鞋'
elif norain:
    status = '今日不會下雨'
