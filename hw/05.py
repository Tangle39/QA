#接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
while True:
    try:
        print(int(input(),16))
    except:
        break

# 转10进制，使用int()
#16 -> hex   8-> oct 2-> bin
