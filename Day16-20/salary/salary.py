#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
月薪结算
部门经理 15000 ， 程序员每小时200， 销售员 1800 + 5%的提成
"""
import abc
from abc import ABCMeta


class Employee(metaclass=ABCMeta):
    """ 员工（抽象类） """

    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super(Programmer, self).__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        super(Salesman, self).__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """工厂类"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp


def main():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000)
    ]
    for emp in emps:
        print('{}:{}元'.format(emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
