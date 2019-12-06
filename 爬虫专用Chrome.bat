@echo **********************************************************************************************
@echo *****尝试删除缓存 C:\selenium  多开应用会导致占用  拒绝被删除文件
@echo *****找到chrome.exe打开，找不到可改地址
@echo *****Chrome默认地址为C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
@echo *****端口9222
@echo **********************************************************************************************

rd /s /q  C:\selenium
cd C:\Program Files (x86)\Google\Chrome\Application\
start "" "chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium" 

@echo **********************************************************************************************
@echo *****30秒后批处理界面自动关闭，不影响操作
@echo **********************************************************************************************

TIMEOUT /T 30 /NOBREAK
exit

