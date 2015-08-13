#!/usr/bin/env python
# encoding: utf-8
"""
@author:     idhyt
@copyright:  2015 idhyt. All rights reserved.
@contact:
@date:       2015.08.08
@description:   modify by http://blog.csdn.net/yangalbert/article/details/7603338
"""
import os
import string

from PIL import Image
from PIL.GifImagePlugin import getheader, getdata


# 将gif图像每一帧拆成独立的位图
def gif_to_images(file_name, save_dir=".", save_type="bmp"):
    files = []
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    print "spliting %s" % file_name

    im = Image.open(file_name)
    # skip to the second frame
    im.seek(0)
    cnt = 0
    save_type = string.lower(save_type)

    mode = im.mode
    save_name = "".join([save_dir, "/", str(cnt), ".", save_type])
    im.convert(mode).save(save_name)
    files.append(save_name)
    
    cnt += 1
    try:
        while True:
            save_name = "".join([save_dir, "/", str(cnt), ".", save_type])
            im.seek(im.tell()+1)
            im.convert(mode).save(save_name)
            files.append(save_name)
            cnt += 1
    except EOFError:
        # end of sequence
        pass

    print "%s has been splited %d pic to directory: [%s] " % (file_name, cnt, save_dir)
    return files


def modify_pixel(pic_list, tag_rgb, modify_color):
    for pic in pic_list:
        im = Image.open(pic).convert("RGB")
        size = im.size
        pixels = im.load()
        for i in range(size[0]):
            for j in range(size[1]):
                if pixels[i, j] == tag_rgb:
                    print i, j, pixels[i, j]
                    pixels[i, j] = modify_color
        im.convert("RGB").save(pic)
    return True


def int_to_bin(i):
    """ 把整型数转换为双字节 """
    # 先分成两部分,高8位和低8位
    i1 = i % 256
    i2 = int(i/256)
    # 合成小端对齐的字符串
    return chr(i1) + chr(i2)


def get_header_animat(im):
    """ 生成动画文件头 """
    bb = "GIF89a"
    bb += int_to_bin(im.size[0])
    bb += int_to_bin(im.size[1])
    bb += "\x87\x00\x00"  # 使用全局颜色表
    return bb


def get_app_ext(loops=0):
    """ 应用扩展,默认为0,为0是表示动画是永不停止
    """
    bb = "\x21\xFF\x0B"  # application extension
    bb += "NETSCAPE2.0"
    bb += "\x03\x01"
    if loops == 0:
        loops = 2**16-1
    bb += int_to_bin(loops)
    bb += '\x00'  # end
    return bb


def get_graphics_control_ext(duration=0.1):
    """ 设置动画时间间隔 """
    bb = '\x21\xF9\x04'
    bb += '\x08'  # no transparancy
    bb += int_to_bin(int(duration*100))   # in 100th of seconds
    bb += '\x00'  # no transparant color
    bb += '\x00'  # end
    return bb


def write_gif_to_file(fp, images, durations, loops):
    """ 把一系列图像转换为字节并存入文件流中
    """
    # 初始化
    frames = 0
    previous = None
    for im in images:
        if not previous:
            # 第一个图像
            # 获取相关数据
            palette = getheader(im)[1]  # 取第一个图像的调色板
            data = getdata(im)
            im_des, data = data[0], data[1:]
            header = get_header_animat(im)
            app_ext = get_app_ext(loops)
            graph_ext = get_graphics_control_ext(durations[0])

            # 写入全局头
            fp.write(header)
            fp.write(palette)
            fp.write(app_ext)

            # 写入图像
            fp.write(graph_ext)
            fp.write(im_des)
            for d in data:
                fp.write(d)

        else:
            # 获取相关数据
            data = getdata(im)
            im_des, data = data[0], data[1:]
            graph_ext = get_graphics_control_ext(durations[frames])

            # 写入图像
            fp.write(graph_ext)
            fp.write(im_des)
            for d in data:
                fp.write(d)
        # 准备下一个回合
        previous = im.copy()
        frames += 1
    # 写入完成
    fp.write(";")
    return frames


# 将多帧位图合成为一幅gif图像
def images_to_gif(images, gif_file, durations=0.05, loops=1):
    seq = []
    for image in images:
        im = Image.open(image)
        background = Image.new('RGB', im.size, (255, 255, 255))
        background.paste(im, (0, 0))
        seq.append(background)

    images2 = []
    for im in seq:
        # 如果是PIL Image
        if isinstance(im, Image.Image):
            images2.append(im.convert('P', dither=loops))

    # 检查动画播放时间
    durations = [durations] * len(images2)
    # 打开文件
    fp = open(gif_file, 'wb')
    # 写入GIF
    try:
        frames = write_gif_to_file(fp, images2, durations, loops)
    finally:
        fp.close()
    print frames, 'images has been merged to', gif_file


def modify_gif_pixel(org_gif, save_dir, save_type, new_gif):
    modify_color = (255, 255, 255)
    tag_rgb = (8, 8, 8)

    pic_list = gif_to_images(org_gif, save_dir, save_type)
    modify_pixel(pic_list, tag_rgb, modify_color)
    images_to_gif(pic_list, new_gif)


if __name__ == "__main__":
    modify_gif_pixel("img/white.gif", "img/white", "png", "img/white_new.gif")
    pass