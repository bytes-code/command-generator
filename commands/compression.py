from .command_template import CommandTemplate

class GzipCommand(CommandTemplate):
    def get_parameters(self):
        return [
            {"name": "input_file", "label": "要压缩的文件", "default": ""},
            {"name": "keep_original", "label": "保留原文件", "type": "bool", "default": True}
        ]
    
    def generate_command(self, params):
        keep_flag = "-k" if params['keep_original'] else ""
        return f"gzip {keep_flag} {params['input_file']}".strip()
    