#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'


def generate_thumbnails(infile, size, format='PNG'):
    """生成缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('*.png'):
        for size in (32, 64, 128):
            # 创建启动线程
            threading.Thread(
                target=generate_thumbnails,
                args=(infile, (size, size))
            ).start()


if __name__ == '__main__':
    main()
