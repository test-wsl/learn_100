#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Persion(object):
    __slots__ = ('_name', '_age', '_gender')  # 限制绑定属性

    def __init__(self, name, age):
        """
        初始化方法
        :param name:
        :param age:
        """
        self._name = name
        self._age = age

    # 访问器 -getter方法
    @property
    def name(self):
        return self._name

    # 修改器 -setter方法
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("{}正在玩飞行棋".format(self._name))
        else:
            print("{}玩斗地主".format(self._name))


def main():
    person1 = Persion('王大锤', 12)
    person1.play()
    person1.age = 22
    person1.play()
    person1._gender = '男'
    print(person1._gender)
    person1._is_gay = True


if __name__ == '__main__':
    main()
