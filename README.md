# noscription
noscription 铭文自动化脚本

# 安装三方库
```
pip install selenium
pip install webdriver_manager
```

# 运行
```
python miner.py
```

# 打包成EXE文件 (前提是安装了第三方组件pyinstaller)
```
pyinstaller -F -i okx.ico .\mint.py
```
okx.ico是图标文件，我随便找的
