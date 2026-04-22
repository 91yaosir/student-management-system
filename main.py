#学生信息管理系统 -主程序
#作者：姚贺竞

def display_menu():
    """ 显示主菜单"""
    print("\n" + "="*50)
    print("       学生信息管理系统 v1.0")
    print("="*50)
    print("1. [+] 添加学生信息")
    print("2. [-] 删除学生信息")
    print("3. [*] 修改学生信息")
    print("4. [?] 查询学生信息")
    print("5. [#] 显示所有学生")
    print("6. [x] 退出系统")
    print("="*50)

    while True:
        choice = input("请输入您的选择 (1-6): ").strip()
        
        if choice == '1':
            print("\n[添加学生功能 - 由组员王浩炫开发]")
            # from services.add_student import add_student
            # add_student()
        elif choice == '2':
            print("\n[删除学生功能 - 由组员卢铖闻开发]")
        elif choice == '3':
            print("\n[修改学生功能 - 由组员雷景超开发]")
        elif choice == '4':
            print("\n[查询学生功能 - 由组长负责]")
        elif choice == '5':
            print("\n[显示所有学生]")
        elif choice == '6':
            print("感谢使用，再见！")
            break
        else:
            print("[x] 输入无效，请重新输入1-6之间的数字")

if __name__ == "__main__":
    display_menu()