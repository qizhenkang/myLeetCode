@echo off


set /p number="please input the __number__ of new project:"
echo %number%


set /p name="please input the __name__ of new project:"

echo %name%

set "full_name=Solution_%number%_%name%.py"

echo "full_name -> %full_name%"

@REM 创建文件
cd .
cd . >.\code\%full_name%


exit