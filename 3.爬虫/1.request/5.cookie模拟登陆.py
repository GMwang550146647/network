import requests

# 1.自己复制cookie过来 header填充
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    "Cookie": 'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1614420193; Hm_lvt_1db88642e346389874251b5a1eded6e3=1614420009; device_id=24700f9f1986800ab4fcc880530dd0ed; u=851614420008663; xq_a_token=62effc1d6e7ddef281d52c4ea32f6800ce2c7473; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxNTYwMzIxNSwiY3RtIjoxNjE0NDE5OTUyNjI2LCJjaWQiOiJkOWQwbjRBWnVwIn0.pEFYi0l-CVd5fwyBCJUeCu5OjaQ3QE13nrAqxYJmkzF4XdOquH6x-vdhdyVqvhW4fxbC851-GR7eD_qmm1rA06TaqARI93CEU9G7TRlSF7cuaUPpbljO-1i5ndruzSUYX3kdo6DRYkJrw9aQaO-eu_rsczpJcdYp0kUERkUiutmbrmrptGZmel7qtDuKnisQ4nO9Jpfk6yQaNyJgn0t3OSi15OiMTnndzhhn_2gFtZTK1wYwishrPe5QzC6JdOccc7Yi_426_Wqrm4OdNgCyxluKQKmKqlpVasguw_IJvhcBhmWqG_I8XLV8aoisANhWEXQA18grM6f4Sk2B_ynB5w; xq_r_token=53a0f79d5bae795fb7abc6814dc0fc0410413016; xqat=62effc1d6e7ddef281d52c4ea32f6800ce2c7473; acw_tc=2760820916144200086617294e4eb49045961f758d9a7bfd8467476be769f4'
}
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=174586&size=15'
data = requests.get(url, headers=headers).json()
print(data)

# 2.创建cookie对象并自动保存(一般需要先访问首页)
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
}
session.get('https://xueqiu.com',headers=headers)
data=session.get(url,headers=headers).json()
print(data)