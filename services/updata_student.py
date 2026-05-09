#修改学生信息模块
#作者：雷景超
def update_student():
    """
    修改学生信息的功能模块
    核心功能：
    1. 搜索并定位目标学生
    2. 显示当前信息供查看
    3. 选择性更新指定字段
    4. 记录修改历史和时间戳
    """
    print("\n--- 修改学生功能 ---")
    print("此模块由组员C负责开发")
    print("核心代码要求：不少于15行")
    print("建议实现：字段选择、数据校验、修改日志等功能")
    
    # TODO: 雷景超在这里写代码...
    students = [{"id": "001", "name": "张三", "age": 18, "class": "高一 1 班"},{"id": "002", "name": "李四", "age": 17, "class": "高一 2 班"},{"id": "003", "name": "王五", "age": 19, "class": "高一 3 班"}]
1. 输入要修改的学生 ID
stu_id = input ("请输入要修改的学生 ID：")
2. 查找目标学生
target = Nonefor stu in students:if stu["id"] == stu_id:target = stubreak
if not target:print ("未找到该学生！")return
3. 显示当前信息
print ("\n 找到学生信息：")print (f"ID：{target ['id']}")print (f"姓名：{target ['name']}")print (f"年龄：{target ['age']}")print (f"班级：{target ['class']}")
4. 选择要修改的字段
print ("\n 请选择要修改的内容：")print ("1. 修改姓名")print ("2. 修改年龄")print ("3. 修改班级")choice = input ("请输入选项（1-3）：")
5. 根据选择执行修改
if choice == "1":new_name = input ("请输入新姓名：")if new_name.strip () != "":target ["name"] = new_nameprint ("姓名修改成功！")elif choice == "2":new_age = input ("请输入新年龄：")if new_age.isdigit () and 15 <= int (new_age) <= 25:target ["age"] = new_ageprint ("年龄修改成功！")else:print ("输入年龄不合法，修改失败！")elif choice == "3":new_class = input ("请输入新班级：")if new_class.strip () != "":target ["class"] = new_classprint ("班级修改成功！")else:print ("输入选项无效！")return
6. 记录修改日志
print (f"\n【修改日志】学生 {stu_id} 信息已更新")print ("修改完成，返回主菜单...")
if name == "main":update_student()
    

if __name__ == "__main__":
    update_student()