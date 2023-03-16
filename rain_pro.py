import requests
from bs4 import BeautifulSoup
import re

def find_rain_pro(location):
    if "台北市" in location or "新北市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa'
    elif "基隆市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/2d7ad0763322f8f204948bab69b8437cc74e2cb1fddc0b11261dc6666360749e'
    elif "桃園市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/efbf308224729b20c95ff9150f731657639bc63cce74c8c098357587b7bbc9c4'
    elif "新竹市" in location or "新竹縣" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/9d98eb3f97a83330c0599a7548c3c7b47163615858673cfee2406e208ce20604'
    elif "苗栗縣" in location or "苗栗市"in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/b994c89cc0ff3b6b56814e2730a58c821d2585ce6d3f190ea6a8c502c82268c2'
    elif "台中市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/8e095973cc14ab3966eab1a0c6a1b04f5291e61049bff4cb42a510b3881afec9'
    elif "彰化縣" in location or "彰化市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/50f0afa948f93e0309ee2f37a6d34beaf66a79e423e4dec6b9bc063ce8d993c8'
    elif "南投市" in location or "南投縣" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/a1591900149ce2866eb985058411182aaa98152e9e4493653298b56f28532459'
    elif "雲林縣" in location or "雲林市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/4c111547644f519c2e670ace56437d0797a696d86193269d05a1de8f6196dfbf'
    elif "嘉義縣" in location or "嘉義市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/083ec430bd75b8e34579f93ce7c6c033e47d58eca20302a4ede6e3914cd1150a'
    elif "台南縣" in location or "台南市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/cb9a4442e9bf7da0ece89bd21a5161210e79cccc0ec2647b3565977e7a278c31'
    elif "高雄縣" in location or "高雄市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/48697cc4c9743031df643ebe553fc08fd83bf2e96d7c7f58c0db435d5888131f'
    elif "屏東縣" in location or "屏東市" in location:
        url = 'https://weather.com/zh-TW/weather/hourbyhour/l/2303e8481a2d2f9b32e5343dc3661a921123f3ccdd277563e4b6d7771d53a244'
    else:
        return "目前還未開發到此地區"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    percentage = soup.find('span', {'data-testid': 'PercentageValue'}).text
    return ("降雨機率為"+percentage)


print(find_rain_pro("台中市造下棒「好"))