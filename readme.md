# 生成exe
pyinstaller -F -w --clean --distpath release --workpath temp_build --specpath temp_build --name=CommandGenerator main.py; Remove-Item -Recurse -Force temp_build 