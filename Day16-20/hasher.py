#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StreamHasher():
    """哈希摘要生成"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()


def main():
    """主函数"""
    hasher1 = StreamHasher()
    with open(r'D:\python\file\learn\test\1513344441-0.jpg', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open(r'D:\python\file\learn\test\1513344441-0.jpg', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()
