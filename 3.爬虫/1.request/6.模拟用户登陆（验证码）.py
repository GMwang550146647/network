import requests
from lxml import etree


"""
1.验证码
brew install imagemagick
brew install tesseract
pip install tesserocr pillow
"""

"""
1.方法1： 百度接口
"""


def parse_check_code(img_file):
    import base64
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(img_file, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()


"""
2.方法2：
"""


def parse_check_code1(file):
    from PIL import Image, ImageFilter
    import pytesseract
    captcha = Image.open(file)
    result = pytesseract.image_to_string(captcha)
    return result


if __name__ == '__main__':
    url = 'https://so.gushiwen.org/user/login.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
        'Referer': 'https://so.gushiwen.org/user/login.aspx?from='
    }
    response = requests.get(url, headers=headers)
    tree = etree.HTML(response.text)
    check_code_url = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    check_code = requests.get(check_code_url, headers=headers).content
    check_code_file = '6.checkcode.jpg'
    with open(check_code_file, 'wb') as f:
        f.write(check_code)
    img = open(check_code_file, 'rb')
    result = input("please input check_code: ")
    data = {
        'email': '550146647@qq.com',
        'pwd': '550146647',
        'code': result
    }
    result=requests.post(url=url,headers=headers,data=data).text
    with open('login_detail.html','w') as f:
        f.write(result)