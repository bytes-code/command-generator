from abc import ABC, abstractmethod

class CommandTemplate(ABC):
    @abstractmethod
    def get_parameters(self):
        """返回命令所需的参数列表"""
        pass
    
    @abstractmethod
    def generate_command(self, params):
        """根据参数生成具体命令"""
        pass 