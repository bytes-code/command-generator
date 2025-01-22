from .command_template import CommandTemplate

class DockerSaveCommand(CommandTemplate):
    def get_parameters(self):
        return [
            {"name": "output_file", "label": "输出文件名 (.tar)", "default": ""},
            {"name": "image_name", "label": "镜像名称", "default": ""},
            {"name": "image_tag", "label": "镜像标签", "default": ""}
        ]
    
    def generate_command(self, params):
        output_file = params["output_file"]
        if not output_file.endswith('.tar'):
            output_file += '.tar'
        return f"docker save -o {output_file} {params['image_name']}:{params['image_tag']}" 