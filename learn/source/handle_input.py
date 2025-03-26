import tkinter as tk
import time
import threading

# 这个函数模拟后台任务并输出日志到控制台
def background_task(root):
    for i in range(100):
        time.sleep(2)
        print(f"Log Entry {i+1}: Task is running...")
    print("Task completed!")
    root.quit()


# 创建主窗口
def create_ui():
    # 创建窗口
    root = tk.Tk()
    root.title("test orchestrator")

    # 输入框
    input_label = tk.Label(root, text="请输入你的命令:")
    input_label.pack(pady=(5, 0))
    input_entry = tk.Entry(root, width=40)
    input_entry.pack(pady=5)

    # 处理按钮点击事件
    def on_button_click():
        user_input = input_entry.get()  # 获取输入框内容
        print(f"用户输入: {user_input}")
        # 触发后台任务（模拟执行任务）
        if user_input.lower() == "stop":
            print("用户输入: stop，程序退出")
            root.quit()  # 退出GUI
        if user_input == 'sleep':
            time.sleep(20)

    # 按钮，触发处理
    process_button = tk.Button(root, text="处理输入", command=on_button_click)
    process_button.pack(pady=10)
    threading.Thread(target=background_task, daemon=True, args=(root,)).start()

    # 启动GUI主循环
    root.mainloop()


if __name__ == "__main__":

    create_ui()
