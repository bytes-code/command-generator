import tkinter as tk
from tkinter import ttk

from commands.docker_save import DockerSaveCommand
from commands.file_transfer_commands import ScpCommand
from commands.compression_commands import GzipCommand

class CommandGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("命令生成器")
        
        # 命令类型字典
        self.commands = {
            "Docker Save": DockerSaveCommand(),
            "SCP": ScpCommand(),
            "Gzip": GzipCommand()
        }
        
        # 创建命令选择下拉框
        ttk.Label(root, text="选择命令类型:").grid(row=0, column=0, padx=5, pady=5)
        self.command_type = ttk.Combobox(root, values=list(self.commands.keys()))
        self.command_type.grid(row=0, column=1, padx=5, pady=5)
        self.command_type.bind('<<ComboboxSelected>>', self.update_parameters)
        
        # 参数框架
        self.param_frame = ttk.Frame(root)
        self.param_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # 生成按钮
        self.generate_btn = ttk.Button(root, text="生成命令", command=self.generate_command)
        self.generate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # 结果显示区域
        self.result = tk.Text(root, height=3, width=50)
        self.result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.param_entries = {}
        
    def update_parameters(self, event=None):
        # 清除现有参数输入框
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        
        self.param_entries.clear()
        
        # 获取选中的命令类型
        command_type = self.command_type.get()
        if command_type in self.commands:
            # 创建新的参数输入框
            for i, param in enumerate(self.commands[command_type].get_parameters()):
                ttk.Label(self.param_frame, text=param["label"]).grid(row=i, column=0, padx=5, pady=2)
                entry = ttk.Entry(self.param_frame)
                entry.insert(0, param["default"])
                entry.grid(row=i, column=1, padx=5, pady=2)
                self.param_entries[param["name"]] = entry
    
    def generate_command(self):
        command_type = self.command_type.get()
        if command_type in self.commands:
            # 收集参数值
            params = {name: entry.get() for name, entry in self.param_entries.items()}
            
            # 生成命令
            command = self.commands[command_type].generate_command(params)
            
            # 显示结果
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, command)

if __name__ == "__main__":
    root = tk.Tk()
    app = CommandGenerator(root)
    root.mainloop()
