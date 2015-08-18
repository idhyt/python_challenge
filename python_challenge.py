#!/usr/bin/env python
# encoding: utf-8
"""
@author:     idhyt
@copyright:  2015 idhyt. All rights reserved.
@contact:
@date:       2015.08.08
@description:
"""
import requests
import re


# level 0
# 2的38次幂
def calc():
    return 2 ** 38


# level 1
# 右移两位 ocr
def map_():
    first_alpha = chr(ord("m") + 2)
    second_alpha = chr(ord("a") + 2)
    third_alpha = chr(ord("p") + 2)
    return "".join([first_alpha, second_alpha, third_alpha])


# level 2
# 查找出现次数最少的字符 equality
def ocr():
    stats = {}
    req = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
    page_source = req.text
    mess_pattern = re.compile(r"(%%[\s\S]+)-->", re.IGNORECASE)
    mess_content = mess_pattern.findall(page_source)[0]
    # print mess_content

    for character in mess_content:
        if character in stats:
            stats[character] += 1
        else:
            stats[character] = 1
    for key_, value_ in stats.items():
        print "%s -> %d" % (key_, value_)

    # a e i l q u t y
    return "".join(re.findall(r"[a-z]+", mess_content))


# level 3
# 小写字符两边有三个大写字母 linkedlist
def equality():
    req = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
    page_source = req.text
    mess_pattern = re.compile(r"kAewtloYgc[\s\S]+", re.IGNORECASE)
    mess_content = mess_pattern.findall(page_source)[0]
    return "".join(re.findall(r"[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}", mess_content))


# level 4
# 遍历页面
def linkedlist(times=1, param="12345"):
    try:
        url = "?nothing=".join(["http://www.pythonchallenge.com/pc/def/linkedlist.php", param])
        page_source = requests.get(url).text
        next_param = re.findall("and the next nothing is ([0-9]+)", page_source)[0]
        print "%d -> %s" % (times, next_param)
        times += 1
        linkedlist(times, next_param)
    # 匹配不到跳到异常
    except IndexError:
        print "the right url is : %s" % url
        return page_source


# level 5
# pickle模块的使用
def peak():
    import pickle
    page_source = requests.get("http://www.pythonchallenge.com/pc/def/peak.html").text
    banner_name = re.findall(r"<peakhell src=\"([\s\S]+?)\"/>", page_source)[0]
    banner_url = "".join(["http://www.pythonchallenge.com/pc/def/", banner_name])
    banner_content = requests.get(banner_url).text
    # print banner_content
    banner_obj = pickle.loads(banner_content)
    for list_ in banner_obj:
        print "".join([tuple_[0] * tuple_[1] for tuple_ in list_])


# level 6
def channel():
    import zipfile
    zf = zipfile.ZipFile("D:\\downloads\\channel.zip")
    result = []
    begin_file_name = "90052.txt"
    while True:
        z_info = zf.getinfo(begin_file_name)
        f = zf.open(z_info)
        f_content = f.read()
        next_file_name = re.findall(r"Next nothing is ([0-9]+)", f_content)
        f.close()
        result.append(z_info.comment)
        if next_file_name:
            begin_file_name = "%s.txt" % next_file_name[0]
        else:
            break

    print "".join(result)


# level 7
def oxygen():
    from PIL import Image
    img = Image.open("oxygen.png")
    # left,top,right,bottom
    box = (0, 43, 608, 52)
    belt = img.crop(box)
    # get a sequence object containing pixel values
    pixels = belt.getdata()
    print('mode: %s' % img.mode)
    print('amount of pixel: %d' % len(pixels))
    # print(pixels[0])

    # convert mode RGBA to mode L
    l_belt = belt.convert('L')
    # get a sequence object containing pixel values
    l_pixels = l_belt.getdata()

    result = []
    for i in range(0, 608, 7):
        result.append(chr(l_pixels[i]))

    print ''.join(result)


# level 8
def integrity():
    import bz2
    # page_source = requests.get("http://www.pythonchallenge.com/pc/def/integrity.html").text
    # result = re.findall(r"un: '([\s\S]+)'\s+pw: '([\s\S]+)'", page_source)
    # if len(result) > 0 and len(result[0]) == 2:
    #     un, pw = result[0][0], result[0][1]
    #     print ": ".join(["username", bz2.decompress(un)])
    #     print ": ".join(["password", bz2.decompress(pw)])
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print ": ".join(["username", bz2.decompress(un)])
    print ": ".join(["password", bz2.decompress(pw)])


# level 9
def good():
    from PIL import Image, ImageDraw
    im = Image.new('RGB', (500, 500))
    draw = ImageDraw.Draw(im)

    headers = {
        "Authorization": "Basic aHVnZTpmaWxl"
    }
    page_source = requests.get("http://www.pythonchallenge.com/pc/return/good.html", headers=headers).text
    result = re.findall(r"first:\s([\s\S]+)second:\s([\s\S]+)-->", page_source)
    if len(result) > 0 and len(result[0]) == 2:
        first, second = result[0][0], result[0][1]
        first_points = list(eval(first.replace("\n", "")))
        second_points = list(eval(second.replace("\n", "")))
        for i in range(0, len(first_points), 2):
            draw.line(first_points[i:i + 4], fill='white')
        for i in range(0, len(second_points), 2):
            draw.line(second_points[i:i + 4], fill='white')
        im.save('img/09.jpg')


# level 10
def bull():

    def get_next_item(str_item=""):
        item = []
        if len(str_item) == 0:
            item.append("1")
        elif len(str_item) > 0:
            cur_list = list(str_item)
            same_count = 1
            if len(cur_list) == 1:
                item.append("".join([str(same_count), cur_list[0]]))
            elif len(cur_list) > 1:
                for i in range(len(cur_list)):
                    if i + 1 >= len(cur_list):
                        item.append("".join([str(same_count), cur_list[i]]))
                    elif i + 1 < len(cur_list):
                        if cur_list[i] == cur_list[i+1]:
                            same_count += 1
                        else:
                            item.append("".join([str(same_count), cur_list[i]]))
                            same_count = 1
        return "".join(item)

    index = 0
    cur_item = ""
    while index < 31:
        cur_item = get_next_item(cur_item)
        index += 1
    print "len(a[%d]) = %d" % (index-1, len(cur_item))


def bull_ex():
    from itertools import groupby
    a = '1'
    for i in range(30):
        a = ''.join(str(len(list(v))) + k for k, v in groupby(a))
    print len(a)


# level 11
def odd_even():
    from PIL import Image
    im = Image.open("img/python-challenge-11.jpg")
    w, h = im.size

    imgs = [Image.new(im.mode, (w / 2, h / 2)) for i in xrange(2)]
    imgs_load = [img.load() for img in imgs]
    org = im.load()

    for i in xrange(w):
        for j in xrange(h):
            if (i + j) % 2 == 0:
                org_pos = (i, j)
                new_pos = (i / 2, j / 2)
                imgs_load[i % 2][new_pos] = org[org_pos]

    [imgs[i].save('img/python-challenge-11-%d.jpg' % i) for i in xrange(2)]


# level 12
def evil():
    f = open('files/evil2.gfx', 'rb+')
    content = f.read()
    f.close()

    for i in xrange(5):
        f = open('files/evil2-%d.jpg' % i, 'wb+')
        f.write(content[i::5])
        f.close()


# level 13
def disproportional():
    import xmlrpclib
    xml_rpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print xml_rpc.system.listMethods()
    print xml_rpc.system.methodHelp('phone')
    print xml_rpc.phone('Bert')


# level 14
def italy_error():
    from PIL import Image
    org_img = Image.open('img/wire.png')
    org_data = list(org_img.getdata())
    res_img = Image.new(org_img.mode, (100, 100))
    res_data = res_img.load()
    org_index = 0
    for i in xrange(100):
        for j in xrange(100):
            res_data[j, i] = org_data[org_index]
            org_index += 1
    res_img.save("img/wire-0.png")


def italy():
    from PIL import Image
    # 100*100 ＝ （100 + 99 + 99 + 98)+(...
    items = [[i, i-1, i-1, i-2] for i in xrange(100, 1, -2)]

    org_img = Image.open('img/wire.png')
    org_data = list(org_img.getdata())
    new_img = Image.new(org_img.mode, (100, 100))
    new_data = new_img.load()

    index = 0
    x = y = 0
    for item in items:
        for j in xrange(item[0]):
            new_data[x, y] = org_data[index]
            x += 1
            index += 1
        x -= 1
        for j in xrange(item[1]):
            new_data[x, y] = org_data[index]
            y += 1
            index += 1
        y -= 1
        for j in xrange(item[2]):
            new_data[x, y] = org_data[index]
            x -= 1
            index += 1
        x += 1
        for j in xrange(item[3]):
            new_data[x, y] = org_data[index]
            y -= 1
            index += 1
        y += 1

    new_img.save('img/wire-cat.png')


# level 15
# run in python 3.0+
def uzi():
    from datetime import datetime

    def get_week_day(year_, mouth_, day_):
        return datetime(year_, mouth_, day_).strftime("%w")

    leap_years = [i for i in range(1006, 1997, 10) if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0]
    print (leap_years)
    match_year = [y for y in leap_years if get_week_day(y, 2, 29) == "0"]
    print (match_year)
    print ("%d-01-17" % match_year[-2])


# level 16
def mozart():
    from PIL import Image
    org_img = Image.open('img/mozart.gif')
    org_size = org_img.size
    org_data = list(org_img.getdata())

    # new_img = Image.new(org_img.mode, org_size)
    new_img = org_img.copy()
    new_data = new_img.load()

    for y in range(org_size[1]):
        line_pixels = org_data[org_size[0] * y: org_size[0] * (y + 1)]
        pink_index = line_pixels.index(195)
        for x, pixel in enumerate(line_pixels[pink_index:] + line_pixels[:pink_index]):
            new_data[x, y] = pixel

    new_img.save("img/romance.gif")


# level 17
def romance():
    import urllib2
    import cookielib
    import urllib

    cj = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(handler)

    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    param = "12345"
    times = 1
    info = []

    while True:
        try:
            url = "?busynothing=".join([base_url, param])
            page_source = opener.open(url).read()
            param = re.findall("and the next busynothing is ([0-9]+)", page_source)[0]
            ck = cj._cookies.values()[0]['/']['info'].value
            info.append(ck)
            print "%d -> %s -> %s" % (times, param, ck)
            times += 1
        # 匹配不到跳到异常
        except IndexError:
            print "the end is : %d" % times
            break

    message = "".join(info)
    print message
    # 转义
    message = urllib.unquote_plus(message)
    result = message.decode("bz2")
    print result

    # ---level 13 code ---#

    # url = "?busynothing=".join([base_url, param])
    # page_source = opener.open(url).read()
    cj._cookies.values()[0]['/']['info'].value = 'the+flowers+are+on+their+way'
    violin_source = opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()
    print violin_source


# level 18
def balloons():
    import difflib
    f_delta = open('files/delta.txt', 'r+')
    deltas = f_delta.read().split('\n')
    f_delta.close()

    left_data = []
    right_data = []

    for line in deltas:
        left_data.append(line[:53]+'\n')
        right_data.append(line[56:]+'\n')

    diff = difflib.Differ()
    cmp_result = list(diff.compare(left_data, right_data))

    left_pic = open('img/18-left-diff.png', 'wb')
    right_pic = open('img/18-right-diff.png', 'wb')
    common_pic = open('img/18-common.png', 'wb')

    for line in cmp_result:
        bytes = [(chr(int(h, 16))) for h in line[2:].split()]
        if line.startswith('-'):
            map(left_pic.write, bytes)
        elif line.startswith('+'):
            map(right_pic.write, bytes)
        elif line.startswith(' '):
            map(common_pic.write, bytes)

    right_pic.close()
    left_pic.close()
    common_pic.close()


# level 19
def hex_bin():
    import base64
    import wave
    headers = {
        "Authorization": "Basic YnV0dGVyOmZseQ=="
    }
    page_source = requests.get("http://www.pythonchallenge.com/pc/hex/bin.html", headers=headers).text
    wav_data = re.findall(r"base64([\s\S]+?)--", page_source)[0].strip("\n")
    indian = open("files/indian.wav", "wb")
    indian.write(base64.b64decode(wav_data))
    indian.close()

    indian = wave.open("files/indian.wav", "rb")
    reverse = wave.open("files/indian-reverse.wav", "wb")
    reverse.setnchannels(1)
    reverse.setframerate(indian.getframerate())
    reverse.setsampwidth(indian.getsampwidth())
    for i in range(indian.getnframes()):
        reverse.writeframes(indian.readframes(1)[::-1])
    indian.close()
    reverse.close()


# level 20
def idiot2():
    pic_url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
    next_range = 30203
    end_range = 2123456789
    while next_range <= end_range:
        headers = {
            "Authorization": "Basic YnV0dGVyOmZseQ==",
            "Range": "bytes=%d-" % next_range
        }
        img = requests.get(pic_url, headers=headers)
        if img.status_code == 206:
            print "range : %d -> %s" % (next_range, img.text)
            content_range = img.headers.get("Content-Range")
            next_range = re.findall(r"bytes.+-(\d+)/", content_range)[0]
            next_range = int(next_range) + 1
        else:
            break

    # reverse
    cur_range = 2123456789
    end_range = 2123456789
    is_download = False
    while cur_range <= end_range:
        headers = {
            "Authorization": "Basic YnV0dGVyOmZseQ==",
            "Range": "bytes=%d-" % cur_range
        }
        img = requests.get(pic_url, headers=headers)
        if img.status_code == 206:
            if is_download is True:
                open("files/invader.zip", "wb").write(img.content)
                break

            print "range : %d -> %s" % (cur_range, img.text)
            content_range = img.headers.get("Content-Range")
            cur_range = re.findall(r"bytes (\d+)-", content_range)[0]
            cur_range = int(cur_range) - 1

            img_text = img.text
            result = [text_[::-1] for text_ in img_text.split()[::-1]]
            print " ".join(result)
        elif img.status_code == 416:
            cur_range = img_text.split()[-1].strip(".")
            cur_range = int(cur_range)
            is_download = True


# level 21
def package():
    import bz2
    import zlib

    data = open("files/invader/package.pack", "rb+").read()
    result = []
    while True:
        if data.startswith("x\x9c"):
            data = zlib.decompress(data)
            result.append(" ")
        elif data.startswith("BZ"):
            data = bz2.decompress(data)
            result.append("#")
        elif data.endswith("\x9cx"):
            data = data[::-1]
            result.append("\n")
        elif data.endswith("ZB"):
            data = data[::-1]
            result.append("*")
        else:
            break

    print "".join(result)


# level 22
def copper():
    from PIL import Image, ImageDraw, ImageSequence
    org_img = Image.open("img/white.gif")
    new_img = Image.new('RGB', org_img.size, "black")
    new_img_draw = ImageDraw.Draw(new_img)
    x = 0
    y = 0
    for s in ImageSequence.Iterator(org_img):
        left, upper, right, lower = org_img.getbbox()
        dx = left-100
        dy = upper-100
        x += dx
        y += dy
        if dx == dy == 0:
            x += 20
            y += 30
        new_img_draw.point((x, y))

    new_img.save("img/copper.png")


# level 23
def bonus():
    def shift(str_value, shift_num):
        ret_list = []
        alphas = list(str_value)
        for alpha in alphas:
            temp_ord = ord(alpha) + shift_num
            if 97 <= temp_ord <= 122:
                ret_list.append(chr(temp_ord))
            elif temp_ord > 122:
                ret_list.append(chr(temp_ord - 122 + 96))
            else:
                ret_list.append(" ")
        return "".join(ret_list)

    org_str = "va gur snpr bs jung"
    for i in range(1, 26):
        print ">>%d -> %s" % (i, shift(org_str, i))


# level 24
def ambiguity():
    import Image
    org_img = Image.open("img/maze.png").getdata()
    org_img_size = org_img.size
    new_img = Image.new("RGBA", org_img_size, "black")
    start_pos, end_pos = None, None
    start_pos_count, end_pos_count = 0, 0
    for x in range(org_img_size[0]):
        if org_img.getpixel((x, 0))[0] == 0:
            start_pos = (x, 0)
            start_pos_count += 1
        if org_img.getpixel((x, org_img_size[1]-1))[0] == 0:
            end_pos = (x, org_img_size[1]-1)
            end_pos_count += 1

    if start_pos is None or end_pos is None or start_pos_count != 1 or end_pos_count != 1:
        print "[error] : get start pos or end pos error!"
        return False
    print "[*] start_pos: %s and end_pos: %s" % (start_pos, end_pos)

    path = []
    whole_path = []

    # 右 下 左 上
    dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    wall = (255,)*4

    while start_pos != end_pos:
        org_img.putpixel(start_pos, wall)
        flag = 0
        new_pos = start_pos
        for offset in dire:
            try:
                pp = (start_pos[0]+offset[0], start_pos[1]+offset[1])
                if org_img.getpixel(pp) != wall:
                    flag += 1
                    new_pos = pp
            except Exception, e:
                print str(e)
                pass
        # 未找到下个出口
        if flag == 0:
            if not path:
                path = whole_path.pop()
                continue
            start_pos = path[0]
            path = []
        # 分岔口,找到多个像素点,备份之前的坐标队列,以此分岔口作为新的入口点
        elif flag > 1:
            whole_path.append(path)
            path = [start_pos]
            start_pos = new_pos
        # 找到唯一出口,flag = 1
        else:
            path.append(start_pos)
            start_pos = new_pos

    path.append(start_pos)
    whole_path.append(path)

    org_img = Image.open("img/maze.png").getdata()
    data = []
    for path in whole_path:
        for k in path:
            new_img.putpixel(k, wall)
            data.append(org_img.getpixel(k)[0])

    out = open("files/out24.zip", "wb")
    for i in data[1::2]:
        out.write(chr(i))
    out.close()
    new_img.save("img/out24.png")


# level 25
def lake():
    from PIL import Image
    import requests
    import base64
    import StringIO
    import wave

    headers = {
            "Authorization": "Basic %s" % base64.encodestring("butter:fly").replace("\n", "")
            }
    wave_url = 'http://www.pythonchallenge.com/pc/hex/lake%i.wav'
    new_img = Image.new('RGB', (300, 300))
    for i in range(25):
        print "%i/%i" % (i + 1, 25)
        wave_content = requests.get(wave_url % (i + 1), headers=headers).content
        data = wave.open(StringIO.StringIO(wave_content))
        patch = Image.fromstring('RGB', (60, 60), data.readframes(data.getnframes()))
        pos = (60 * (i % 5), 60 * (i / 5))
        new_img.paste(patch, pos)

    new_img.save("img/out25.jpg")


def challenge():
    # print calc()
    # print map_()
    # print ocr()
    # print equality()
    # print linkedlist()
    # peak()
    # channel()
    # oxygen()
    # integrity()
    # good()
    # bull()
    # bull_ex()
    # odd_even()
    # evil()
    # disproportional()
    # italy()
    # uzi()
    # mozart()
    # romance()
    # balloons()
    # hex_bin()
    # hex_bin()
    # idiot2()
    # package()
    # copper()
    # bonus()
    # ambiguity()
    lake()
    pass

if __name__ == "__main__":
    challenge()
