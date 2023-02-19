:: 依据路径安装APP
@echo off
set lujing=
if "%lujing%"=="" (
	set /p lujing=Please Input lujing: 
::set /p a=promptstring
::先显示promptstring，再接受用户输入的内容,以回车表示结束，赋值给变量a
)
adb install -r %lujing%
:: %%:变量引用
:: -r可以覆盖安装
pause
