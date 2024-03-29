import os
import requests
from bs4 import BeautifulSoup
import time

def get_page_content():
    url = 'https://www.maj-soul.com/#/news'
    response = requests.get(url)
    return response.text

def parse_page_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    news_items = soup.select('.news-item')
    return [item.get_text(strip=True) for item in news_items]

def send_feishu_message(message):
    webhook_url = os.environ.get('FEISHU_WEBHOOK')
    if webhook_url:
        data = {
            "msg_type": "text",
            "content": {
                "text": message
            }
        }
        requests.post(webhook_url, json=data)
    else:
        print("未设置飞书Webhook环境变量")

def main():
    prev_content = None
    while True:
        content = get_page_content()
        current_content = parse_page_content(content)
        
        if prev_content is None:
            prev_content = current_content
        elif current_content != prev_content:
            send_feishu_message("检测到页面内容发生变化")
            prev_content = current_content
        
        time.sleep(300)  # 每5分钟检查一次

if __name__ == '__main__':
    main()