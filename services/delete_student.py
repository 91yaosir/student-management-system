def delete_student(student_list, student_id):
    """
    根据学生ID删除学生信息
    :param student_list: 学生列表
    :param student_id: 要删除的学生ID
    :return: 删除成功返回True，失败返回False
    """
    # 判断列表是否为空
    if not student_list:
        print("当前没有任何学生信息，无法删除")
        return False

    # 遍历查找对应ID的学生
    for student in student_list:
        # 判断ID是否匹配
        if student.get("id") == student_id:
            student_list.remove(student)
            print(f"ID为 {student_id} 的学生已成功删除！")
            return True

    # 循环结束没找到，说明不存在
    print(f"未找到ID为 {student_id} 的学生，删除失败")
    return False


def delete_student_by_name(student_list, student_name):
    """
    根据姓名删除学生（支持同名）
    :param student_list: 学生列表
    :param student_name: 学生姓名
    :return: 删除数量
    """
    count = 0
    # 倒序遍历删除，避免漏删
    for i in range(len(student_list) - 1, -1, -1):
        if student_list[i].get("name") == student_name:
            del student_list[i]
            count += 1

    if count > 0:
        print(f"成功删除 {count} 个名为 {student_name} 的学生")
    else:
        print(f"未找到名为 {student_name} 的学生")
    return count


# 测试代码（可运行）
if __name__ == "__main__":
    # 模拟学生数据
    students = [
        {"id": 1, "name": "张三", "age": 18},
        {"id": 2, "name": "李四", "age": 19},
        {"id": 3, "name": "王五", "age": 20}
    ]

    print("删除前：", students)
    
    # 按ID删除
    delete_student(students, 2)
    
    # 按姓名删除
    delete_student_by_name(students, "张三")
    
    print("删除后：", students)