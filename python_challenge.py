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


# 2的38次幂
def calc():
    return 2 ** 38


# 右移两位 ocr
def map_():
    first_alpha = chr(ord("m") + 2)
    second_alpha = chr(ord("a") + 2)
    third_alpha = chr(ord("p") + 2)
    return "".join([first_alpha, second_alpha, third_alpha])


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


# 小写字符两边有三个大写字母 linkedlist
def equality():
    req = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
    page_source = req.text
    mess_pattern = re.compile(r"kAewtloYgc[\s\S]+", re.IGNORECASE)
    mess_content = mess_pattern.findall(page_source)[0]
    return "".join(re.findall(r"[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}", mess_content))


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


def evil():
    f = open('files/evil2.gfx', 'rb+')
    content = f.read()
    f.close()

    for i in xrange(5):
        f = open('files/evil2-%d.jpg' % i, 'wb+')
        f.write(content[i::5])
        f.close()


def disproportional():
    import xmlrpclib
    xml_rpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print xml_rpc.system.listMethods()
    print xml_rpc.system.methodHelp('phone')
    print xml_rpc.phone('Bert')


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
    romance()
    pass

if __name__ == "__main__":
    challenge()
