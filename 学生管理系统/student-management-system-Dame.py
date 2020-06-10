# 定义一个函数，显示可以使用的功能列表给用户
def showInof():
    '''
    显示可以使用的功能列表给用户
    :return:
    '''
    print("-"*30)
    print("      学生管理系统      ")
    print(" 1.添加学生的信息")
    print(" 2.删除学生的信息")
    print(" 3.修改学生的信息")
    print(" 4.查询学生的信息")
    print(" 5.遍历所有学生的信息")
    print(" 0.退出系统")
    print('-' * 30)

# 定义一个列表，用来存储多个学生的信息
students = []


# 添加学生函数
def addStudent():
    '''
        添加一个学生，需要传入姓名、年龄、学号
    '''
    # 输入学员姓名、年龄、学号
    stuName = input("请输入学生姓名：")
    stuId = input("请输入学生学号(学号不可重复)：")
    stuAge = input("请输入学生年龄:")
    # 验证学号是否唯一 #i记录要删除的下标，leap为标志位，如果找到leap=1，否则为0
    i = 0
    leap = 0
    # 循环判断
    for stu in students:
        if stu['stuId'] == stuId:
            leap = 1
            break
        else:
            i = i + 1
    # leap == 1代表学生学号
    if leap == 1:
        print("输入学生学号重复，添加失败！")
    else:
        # 定义一个字典，存放单个学生信息
        stuInfo = {}
        stuInfo['stuName'] = stuName
        stuInfo['stuId'] = stuId
        stuInfo['stuAge'] = stuAge

        # 单个学生信息放入列表
        students.append(stuInfo)
        print("添加成功！")

#删除学生函数
def deleteStudent():
    '''
        根据学号删除学生，学号
    '''
    print("您选择了删除学生功能")
    delId=input("请输入要删除的学生学号:")
    #i记录要删除的下标，leap为标志位，如果找到leap=1，否则为0
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == delId:
            leap = 1
            break
        else:
            i=i+1
    if leap == 0:
        print("没有此学生学号，删除失败！")
    else:
        del students[i]
        print("删除成功！")

#修改学生函数
def updateStudent():
    '''
        根据学号修改学生信息，学号
    '''
    print("您选择了修改学生信息功能")
    alterId=input("请输入你要修改学生的学号:")
    #检测是否有此学号，然后进行修改信息
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == alterId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 1:
        updateOperate()
    else:
        print("没有此学号，修改失败！")

def updateOperate():
    '''
        根据用户选择不同的操作来修改学生的信息
    '''
    while True:
        alterNum=int(input(" 1.修改学号\n 2.修改姓名 \n 3.修改年龄 \n 4.退出修改\n"))
        if alterNum == 1:
            newId=input("输入更改后的学号:")
            #修改后的学号要验证是否唯一
            i = 0
            leap1 = 0
            for stu1 in students:
                if stu1['stuId'] == newId:
                    leap1 = 1
                    break
                else:
                    i = i + 1
            if leap1 == 1:
                print("输入学号不可重复，修改失败！")
            else:
                stu1['stuId']=newId
                print("学号修改成功")
        elif alterNum == 2:
            #修改姓名操作
            newName=input("输入更改后的姓名:")
            stu1['stuName'] = newName
            print("姓名修改成功")
        elif alterNum == 3:
            #修改年龄操作
            newAge=input("输入更改后的年龄:")
            stu1['stuAge'] = newAge
            print("年龄修改成功")
        elif alterNum == 4:
            break
        else:
            print("输入错误请重新输入")


# 查询单个学生信息函数
def getStudentById():
    '''
        根据学号查询学生信息,需要传入学号
    '''
    print("您选择了查询学生信息功能")
    searchID = input("请输入你要查询学生的学号:")
    # 验证是否有此学号
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == searchID:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 0:
        print("没有此学生学号，查询失败！")
    else:
        print("找到此学生，信息如下：")
        print("学号：%s\n姓名：%s\n年龄：%s\n" % (stu['stuId'], stu['stuName'], stu['stuAge']))


# 查询所有学生信息函数
def getAllStudent():
    '''
        查询所有学生信息
    '''
    # 遍历并输出所有学生的信息
    print('*' * 20)
    print("接下来进行遍历所有的学生信息...")
    print("stuId      姓名         年龄")
    for stu in students:
        print("%s     %s     %s" % (stu['stuId'], stu['stuName'], stu['stuAge']))
    print("*" * 20)


# 主函数
def main():
    '''
        主函数：程序的入口
    '''
    while True:
        # 把功能列表进行显示给用户
        showInof()
        # 提示用户选择功能
        # 获取用户选择的功能
        key = int(input("请选择功能（序号）："))

        # 根据用户选择，完成相应功能
        if key == 1:
            addStudent()
        elif key == 2:
            deleteStudent()
        elif key == 3:
            updateStudent()
        elif key == 4:
            getStudentById()
        elif key == 5:
            getAllStudent()
        elif key == 0:
            # 退出功能，尽量往不退出的方向引
            quitconfirm = input("亲，真的要退出么 （yes或者no）")
            if quitconfirm == 'yes':
                print("欢迎使用本系统，谢谢")
                break;
        else:
            print("您输入有误，请重新输入")


main()