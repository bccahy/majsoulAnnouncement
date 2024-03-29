import json
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.maj-soul.com/homepage/scripts/NewsList.json"

# 發送GET請求獲取JSON數據
with urllib.request.urlopen(url) as response:
   json_data = json.loads(response.read())

# 找出id值最大的數據
max_id_item = max(json_data['data'], key=lambda x: x['id'])
# 使用BeautifulSoup去除HTML標籤
soup = BeautifulSoup(max_id_item['editorContent'], 'html.parser')
text_content = soup.get_text()
print(text_content)

