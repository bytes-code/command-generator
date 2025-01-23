# 生成exe(移除temp_build)
pyinstaller -F -w --clean --distpath release --workpath temp_build --specpath temp_build --name=CommandGenerator main.py; Copy-Item "release\CommandGenerator.exe" "$env:USERPROFILE\Desktop\"; Remove-Item -Recurse -Force temp_build 

# 生成exe(不移除temp_build)
pyinstaller -F -w --clean --distpath release --workpath temp_build --specpath temp_build --name=CommandGenerator main.py; Copy-Item "release\CommandGenerator.exe" "$env:USERPROFILE\Desktop\"
