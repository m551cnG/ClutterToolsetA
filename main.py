import importlib

def main():
    # 在此处编写您的程序逻辑
    print("Hello, world!")
    playerImport()

def playerImport():
    while  True:
        print("请输入你想干什么(help查看帮助)：",end = "")
        command = input()
        if command == "help":
            try:
                with open('text/Help_Cn.txt', 'r', encoding='utf-8') as file:
                    # 一次性读取整个文件内容
                    content = file.read()
                    # 输出文件内容
                    print(content)
            except FileNotFoundError:
                print("Ok,帮助无啦！=)")
        else:
            print("?啥意思?")


# 跳转函数
def skip():
    module_name = input("Module name: ：")

if __name__ == '__main__':
    main()
