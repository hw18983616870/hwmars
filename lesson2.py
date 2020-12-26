"""
======================
@author:多测师-黄sir
@time:2020/12/23:9:18
@email:hw18983616870@163.com
======================
"""
'''
python中的数据驱动模块：ddt

'''
from ddt import ddt,data,unpack   #从ddt模块内导入ddt、data、unpack等函数
import unittest

# @ddt
# class Test_Ddt(unittest.TestCase):
#
#     @data(1,2)   #把一组数中的多个值进行拆分，依次进行传值
#     def test_01(self,value):
#         print('{} is a nunber'.format(value))
#
# if __name__ == '__main__':
#     unittest.main()

# 对元组进行拆分
# tuple1 = (1,2)    #全局变量
# @ddt
# class Test_Ddt(unittest.TestCase):
#     tuple1 = (1, 2)    #类变量
#     @data(*tuple1)   #把一组数中的多个值进行拆分，依次进行传值
#     def test_01(self,value):
#         print('{} is a nunber'.format(value))
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# 对字典进行拆分
# dic = ({'username':'xiaochen','age':'19'},{'username':'xiaozhao','age':'20'})
# @ddt
# class Test_Ddt(unittest.TestCase):
#     @data(*dic)
#     @unpack
#     def test_01(self,username,age):
#         print('姓名：{}   年龄：{}'.format(username,age))
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#对列表进行拆分

# list1 = [{'username':'xiaochen','age':'19'},{'username':'xiaozhao','age':'20'}]
# @ddt
# class Test_Ddt(unittest.TestCase):
#     @data(*list1)      # 对数组进行第一次拆分
#     @unpack            # 对数组进行第二次拆分
#     def test_01(self,username,age):
#         print('姓名：{}  年龄：{}'.format(username,age))
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# 练习：传入多组数据登录论坛
# from selenium import webdriver
# from time import sleep
# @ddt
# class Test_Bbs(unittest.TestCase):
#     list1=[{'username':'admin1','pwd':'a123456'},{'username':'admin2','pwd':'b123456'}]
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://discuz.e70w.com/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(20)
#     def tearDown(self) -> None:
#         self.driver.quit()
#
#     @data(*list1)
#     @unpack
#     def test_bbs(self,username,pwd):
#
#         self.driver.find_element_by_id('ls_username').send_keys(username)
#         sleep(2)
#         self.driver.find_element_by_id('ls_password').send_keys(pwd)
#         sleep(2)
#         self.driver.find_element_by_class_name('pn').click()
#         sleep(2)
# if __name__ == '__main__':
#     unittest.main()

# 用xlrd模块实现读取表格中的多行多列内容
# import xlrd
# path = r'D:\test.xlsx'
# book = xlrd.open_workbook(path)
# sheet = book.sheet_by_index(0)
#
# row_values = sheet.cell(0,0).value    #取表格中具体某一格的值
# col_num = sheet.ncols      #统计表格的列数
# row_num = sheet.nrows      #统计表格的行数
# print(row_values)
# print(col_num)
# print(row_num)
# l = []
# num = 1
# while 1:
#     dic = {}
#     for i in range(sheet.ncols):
#         # print(sheet.cell(num,i).value)
#         dic[sheet.cell(0,i).value] = sheet.cell(num,i).value
#     l.append(dic)
#     num = num + 1
#     if num>=sheet.nrows:
#         break
# print(l)


#练习：从excel表格中读取用户名和密码，实现论坛登录
import xlrd
from selenium import webdriver
from time import sleep
def read_exl():
    path = r'D:\test.xlsx'
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    l = []
    num = 1
    while 1:
        dic = {}
        for i in range(sheet.ncols):
            # print(sheet.cell(num,i).value)
            dic[sheet.cell(0,i).value] = sheet.cell(num,i).value
        l.append(dic)
        num = num + 1
        if num>=sheet.nrows:
            break
    return l

@ddt
class Test_Bbs(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://discuz.e70w.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*read_exl())
    @unpack
    def test_bbs(self,username,passwd):

        self.driver.find_element_by_id('ls_username').send_keys(username)
        sleep(2)
        self.driver.find_element_by_id('ls_password').send_keys(passwd)
        sleep(2)
        self.driver.find_element_by_class_name('pn').click()
        sleep(2)
if __name__ == '__main__':
    unittest.main(verbosity=2)













