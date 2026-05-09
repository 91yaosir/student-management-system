#添加学生信息模块
#作者：王浩炫

def add_student():
    """
    添加新学生信息的功能模块
    核心功能：
    1. 收集学生基本信息（学号、姓名、年龄等）
    2. 数据验证（确保学号唯一、年龄合法）
    3. 保存到数据存储（文件或数据库）
    """
    print("\n--- 添加学生功能 ---")
    print("此模块由组员A负责开发")
    print("核心代码要求：不少于15行")
    print("建议实现：输入验证、数据保存、错误处理等功能")
    
    # TODO: 王浩炫在这里写代码...
    # services/add_student.py
# 添加学生功能模块

import json
import os
from datetime import datetime

# 学生数据文件路径（假设项目根目录下有个 data 文件夹）
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.json')

def load_students():
    """加载现有学生数据，若文件不存在则返回空列表"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_students(students):
    """保存学生数据到文件"""
    # 确保 data 目录存在
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def add_student(student_id, name, age, grade):
    """
    添加新学生
    :param student_id: 学号（字符串）
    :param name: 姓名（字符串）
    :param age: 年龄（整数）
    :param grade: 班级（字符串，如 "计算机1班"）
    :return: (是否成功, 消息)
    """
    # 输入验证
    if not student_id or not name:
        return False, "学号和姓名不能为空"
    if not isinstance(age, int) or age < 0 or age > 120:
        return False, "年龄必须是 0~120 之间的整数"
    if not grade:
        return False, "班级不能为空"

    # 加载现有数据
    students = load_students()

    # 检查学号是否已存在
    for s in students:
        if s['student_id'] == student_id:
            return False, f"学号 {student_id} 已存在，请勿重复添加"

    # 创建新学生记录
    new_student = {
        'student_id': student_id,
        'name': name,
        'age': age,
        'grade': grade,
        'created_at': datetime.now().isoformat()
    }

    # 添加并保存
    students.append(new_student)
    save_students(students)
    return True, f"学生 {name}({student_id}) 添加成功"

# 如果直接运行此脚本，可以演示添加功能
if __name__ == '__main__':
    # 示例：添加一个学生
    success, msg = add_student("2024001", "张三", 20, "软件工程1班")
    print(msg)
    
    
    if __name__ == "__main__":
        add_student()