from .command_template import CommandTemplate

class ScpCommand(CommandTemplate):
    def get_parameters(self):
        return [
            {"name": "source", "label": "源文件路径", "default": ""},
            {"name": "user", "label": "目标用户名", "default": ""},
            {"name": "host", "label": "目标主机", "default": ""},
            {"name": "destination", "label": "目标路径", "default": ""}
        ]
    
    def generate_command(self, params):
        return f"scp {params['source']} {params['user']}@{params['host']}:{params['destination']}" 
