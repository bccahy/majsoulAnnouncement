import json
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.maj-soul.com/homepage/scripts/NewsList.json"

# 发送GET请求获取JSON数据
with urllib.request.urlopen(url) as response:
    json_data = json.loads(response.read())

# 找出id值最大的数据
max_id_item = max(json_data['data'], key=lambda x: x['id'])
# 使用BeautifulSoup去除HTML标签
soup = BeautifulSoup(max_id_item['editorContent'], 'html.parser')
text_content = soup.get_text()

# 读取上一次发送的内容
try:
    with open('last_news.txt', 'r') as f:
        last_news = f.read()
except FileNotFoundError:
    last_news = ""
    
if last_news != text_content:
    # 如果内容不同，更新news.txt
    with open('news.txt', 'w') as file:
        file.write(text_content)
else:
    # 如果内容相同，确保news.txt为空
    with open('news.txt', 'w') as file:
        file.write('')
        
# 如果内容不同,则写入文件并输出
if text_content != last_news:
    with open('last_news.txt', 'w') as f:
        f.write(text_content)
    
