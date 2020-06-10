import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='text',
    charset='utf8'
)
cur = conn.cursor()
print("学生管理系统")
print("输入你要选择的对象")
print("1添加数据，2删除数据,3更改数据，4查看数据")
a = int(input("输入你的选择："))
if a == 1:
    sql = input("输入sql语句添加数据信息：")
    try:
        cur.execute(sql)
        conn.commit()
        print("添加成功！")
    except Exception as e:
        conn.rollback()
        print("添加失败！{}\n".format())
    cur.close()
if a == 2:
    sql = input("输入sql语句删除数据信息：")
    try:
        cur.execute(sql)
        conn.commit()
        print("删除成功！")
    except Exception as e:
        conn.rollback()
        print("删除失败！{}\n".format())
    cur.close()
if a == 3:
    sql = input("输入sql语句更改数据信息：")
    try:
        cur.execute(sql)
        conn.commit()
        print("更改成功！")
    except Exception as e:
        conn.rollback()
        print("更改失败！{}\n".format())
    cur.close()
if a == 4:
    sql = input("输入sql语句查看数据：")
    try:
        cur.execute(sql)
        data = cur.fetchall()
        for i in data[:]:
            print(i)
        conn.commit()
        print("查看成功！")
    except Exception as e:
        conn.rollback()
        print("查看失败！{}\n".format())
    cur.close()
