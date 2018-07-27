#!/bin/bash/python
#coding=utf-8

# 用来保存学生的所有信息
student_infos = []

# 打印功能提示
def print_menu():
    print("="*30)
    print("学生管理系统v1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示学生信息")
    print("0.退出系统")
    print("="*30)

# 添加一个学生信息
def add_info():
    # 提示并获取学生的姓名
    new_name = input("请输入新学生的姓名:")
    # 提示并获取学生的性别
    new_sex = input("请输入新学生的性别(男或女):")
    # 提示并获取学生的手机号码
    new_phone = input("请输入新学生的手机号码:")
    new_infos = {}
    new_infos['name'] = new_name
    new_infos['sex'] = new_sex
    new_infos['phone'] = new_phone
    student_infos.append(new_infos)

# 删除一个学生信息
def del_info(student):
    del_number = int(input ("请输入要删除的序号:")) - 1
    del_student[del_number]

# 修改一个学生信息
def modify_info():
    student_id = int(input("请输入要修改的学生的序号:"))
    new_name = input("请输入新学生的姓名:")
    new_sex = input("请输入新学生的性别(男或女):")
    new_phone = input("请输入新学生的手机号码:")
    student_infos[student_id-1]['name'] = new_name
    student_infos[student_id-1]['sex'] = new_sex
    student_infos[student_id-1]['phone'] = new_phone

# 显示所有学生信息
def show_infos():
    print("="*30)
    print("学生的信息如下：")
    print("="*30)
    print("序号  姓名  性别  手机号码")
    i = 1
    for temp in student_infos:
        print("%d %s  %s  %s" %(i,temp["name"],temp["sex"],temp["phone"]))
        i += 1

# 定义一个主函数
def main():
    while True:
        print_menu()
        key = int(input("请输入功能对应的数字:"))
        if key == 1:
            add_info()
        elif key == 2:
            del_info(student_infos)
        elif key == 3:
            modify_info()
        elif key == 4:
            show_infos()
        elif key == 0:
            quit_confirm = input("是否真的退出系统?(Yes or No):")
            if quit_confirm == "Yes":
                break
            elif quit_confirm == "yes":
                break
            else:
                print("输入有误，请重新输入")
# 调用主函数
main()
