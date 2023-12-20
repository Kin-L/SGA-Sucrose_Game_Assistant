@echo Rem µçÄÔË¯Ãß
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
TIMEOUT /T 2
powercfg -h off
rundll32.exe powrprof.dll,SetSuspendState 0,1,0
EXIT
echo