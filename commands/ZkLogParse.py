from .command_template import CommandTemplate

class ZkLogParseCommand(CommandTemplate):
    def get_parameters(self):
        return [
            {"name": "logfile", "label": "日志文件路径", "default": ""},
            {"name": "output", "label": "输出文件路径", "default": ""},
            {"name": "zk_path", "label": "ZooKeeper安装路径", "default": "/usr/share/zookeeper"},
            {"type": "text", "content": "如果未安装ZooKeeper，请从 http://archive.apache.org/dist/zookeeper/ 下载"}
        ]
    
    def generate_command(self, params):
        return f"java -cp {params['zk_path']}/lib/*:{params['zk_path']}/zookeeper.jar org.apache.zookeeper.server.LogFormatter {params['logfile']} > {params['output']}"

