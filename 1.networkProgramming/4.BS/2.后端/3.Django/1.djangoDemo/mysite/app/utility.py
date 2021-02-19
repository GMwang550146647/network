import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import re
import logging
import json
import numpy as np

def filter(value, target_value, keep_if_match=True, match_type='any', regex=False):
    """
    To tell 'value' match target_value or not !
    :param value:           The value to be tested,it can be list, tuple or string
    :param target_value:    target value, list of items or regex(if regex=True)
    :param keep_if_match:   keep if 'value' match the conditions in 'target_value'
    :param match_type:      all-> all of the patterns in target_value should be match; any-> at least one match
    :param regex:           if the items in target_value should be regarded as regex expression
    :return:
    """
    if type(value) == str and value.strip()[0] in ['(', '[']:
        try:
            value = json.loads(value)
        except Exception as err:
            logging.error(f"Filter Error ->  Value: {value}  Details : {err}")
    if type(value) in [list, tuple]:
        if regex:
            keep_flags = [[len(re.findall(tar_i, val_i)) > 0 for val_i in value] for tar_i in target_value]
            keep_flag = np.array(keep_flags).all() if match_type == 'all' else np.array(keep_flags).any()
        else:
            if match_type == 'all':
                keep_flag = (len(set(value) & set(target_value)) == len(set(target_value)))
            else:
                keep_flag = len(set(value) & set(target_value)) > 0
    else:
        if regex:
            keep_flags = [len(re.findall(target_value_i, value)) > 0 for target_value_i in target_value]
            keep_flag = np.array(keep_flags).all() if match_type == 'all' else np.array(keep_flags).any()
        else:
            keep_flag = value in target_value
    # if keep_if_match==True : rowi is kept when "condition" in "condition ^ keep_if_match" is False
    return (not keep_flag) ^ keep_if_match


class CheckCode():
    def __init__(self):
        pass

    @staticmethod
    def check_code(width=120, height=30, char_length=5, font_file='tempt/aldhabi.ttf', font_size=28):
        code = []
        img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(img, mode='RGB')

        def rndChar():
            """
            生成随机字符（包括大小写字母和数字）
            :return:
            """
            ranNum = str(random.randint(0, 9))
            ranLower = chr(random.randint(65, 90))
            ranUpper = chr(random.randint(97, 120))
            return random.choice([ranNum, ranLower, ranUpper])

        def rndColor():
            """
            生成随机颜色
            :return:
            """
            return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

        # 写文字
        font = ImageFont.truetype(font_file, font_size)
        for i in range(char_length):
            char = rndChar()
            code.append(char)
            h = (height - font_size) / 2
            draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

        # 写干扰点
        for i in range(40):
            draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

        # 写干扰圆圈
        for i in range(40):
            draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

        # 画干扰线
        for i in range(5):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line((x1, y1, x2, y2), fill=rndColor())

        # 对图像加滤波 - 深度边缘增强滤波
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        return img, ''.join(code)

    def create(self, save_file='tempt/tempt.jpg'):

        # 写入内存
        # img, code = self.check_code()
        # from io import BytesIO  # 内存管理的模块
        # stream = BytesIO()  # stream是写入内存的文件句柄
        # img.save(stream, 'png')
        # data = stream.getvalue()
        # 写入文件
        img, code = self.check_code()
        with open(save_file, 'wb') as f:  # f是写入磁盘的文件句柄
            img.save(f, format='png')
        return code
