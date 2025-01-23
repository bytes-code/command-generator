import tkinter as tk
from tkinter import ttk
from commands.docker_save import DockerSaveCommand
from commands.file_transfer import ScpCommand
from commands.compression import GzipCommand
from commands.ZkLogParse import ZkLogParseCommand

class CommandGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("命令生成器")
        
        # 设置窗口最小尺寸
        self.root.minsize(600, 400)
        
        # 创建主框架并设置padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 命令类型字典
        self.commands = {
            "Docker Save": DockerSaveCommand(),
            "SCP": ScpCommand(),
            "Gzip": GzipCommand(),
            "ZkLogParse": ZkLogParseCommand()
        }
        
        # 创建命令选择下拉框
        ttk.Label(main_frame, text="选择命令类型:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.command_type = ttk.Combobox(main_frame, values=list(self.commands.keys()), width=50)
        self.command_type.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.command_type.bind('<<ComboboxSelected>>', self.update_parameters)
        
        # 参数框架
        self.param_frame = ttk.Frame(main_frame)
        self.param_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # 生成按钮
        self.generate_btn = ttk.Button(main_frame, text="生成命令", command=self.generate_command)
        self.generate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # 结果显示区域
        self.result = tk.Text(main_frame, height=5, width=60)
        self.result.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # 配置列权重以实现自适应布局
        main_frame.columnconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
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
                if param.get("type") == "text":
                    # 创建可选择的只读文本框
                    text = tk.Text(self.param_frame, wrap=tk.WORD, height=2,
                                 borderwidth=1, highlightthickness=0)
                    text.insert("1.0", param["content"])
                    text.configure(state="disabled", fg="black")
                    text.grid(row=i, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=2)
                else:
                    # 创建参数标签和输入框
                    ttk.Label(self.param_frame, text=param["label"]).grid(row=i, column=0, padx=5, pady=2, sticky=tk.E)
                    entry = ttk.Entry(self.param_frame, width=50)
                    entry.insert(0, param.get("default", ""))
                    entry.grid(row=i, column=1, padx=5, pady=2, sticky=(tk.W, tk.E))
                    self.param_entries[param["name"]] = entry
            
            # 配置列权重
            self.param_frame.columnconfigure(1, weight=1)

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

    def create_parameter_inputs(self, command):
        # 清除现有的输入框
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        
        parameters = command.get_parameters()
        self.param_entries = {}
        
        for i, param in enumerate(parameters):
            if param.get("type") == "text":
                # 文本类型，创建Label
                label = ttk.Label(self.param_frame, text=param["content"], wraplength=500)
                label.grid(row=i, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=2)
            else:
                # 创建参数标签
                label = ttk.Label(self.param_frame, text=param["label"])
                label.grid(row=i, column=0, sticky=tk.E, padx=5, pady=2)
                
                # 创建输入框
                entry = ttk.Entry(self.param_frame, width=50)
                entry.insert(0, param.get("default", ""))
                entry.grid(row=i, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)
                
                self.param_entries[param["name"]] = entry
        
        # 配置列权重
        self.param_frame.columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CommandGenerator(root)
    root.mainloop()
