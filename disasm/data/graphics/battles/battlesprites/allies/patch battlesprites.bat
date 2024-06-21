@echo off
CHCP 65001
mkdir output
echo Place the files to be patched in this directory with the following names:
echo --------------------
echo allybattlesprite01.bin
echo allybattlesprite02.bin
echo allybattlesprite03.bin
echo allybattlesprite04.bin
echo allybattlesprite10.bin
echo allybattlesprite12.bin
echo allybattlesprite13.bin
echo allybattlesprite15.bin
echo allybattlesprite17.bin
echo allybattlesprite19.bin
echo allybattlesprite20.bin
echo allybattlesprite21.bin
echo allybattlesprite22.bin
echo allybattlesprite23.bin
echo allybattlesprite25.bin
echo allybattlesprite31.bin
echo allybattlesprite00.bin
echo --------------------
echo Patched files will be in the "output" directory
pause
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite01.bin" ".\vcdiff\allybattlesprite01.bin.vcdiff" ".\output\allybattlesprite00.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite02.bin" ".\vcdiff\allybattlesprite02.bin.vcdiff" ".\output\allybattlesprite01.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite03.bin" ".\vcdiff\allybattlesprite03.bin.vcdiff" ".\output\allybattlesprite02.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite04.bin" ".\vcdiff\allybattlesprite04.bin.vcdiff" ".\output\allybattlesprite03.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite10.bin" ".\vcdiff\allybattlesprite10.bin.vcdiff" ".\output\allybattlesprite04.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite12.bin" ".\vcdiff\allybattlesprite12.bin.vcdiff" ".\output\allybattlesprite10.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite13.bin" ".\vcdiff\allybattlesprite13.bin.vcdiff" ".\output\allybattlesprite12.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite15.bin" ".\vcdiff\allybattlesprite15.bin.vcdiff" ".\output\allybattlesprite13.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite17.bin" ".\vcdiff\allybattlesprite17.bin.vcdiff" ".\output\allybattlesprite15.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite19.bin" ".\vcdiff\allybattlesprite19.bin.vcdiff" ".\output\allybattlesprite17.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite20.bin" ".\vcdiff\allybattlesprite20.bin.vcdiff" ".\output\allybattlesprite19.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite21.bin" ".\vcdiff\allybattlesprite21.bin.vcdiff" ".\output\allybattlesprite20.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite22.bin" ".\vcdiff\allybattlesprite22.bin.vcdiff" ".\output\allybattlesprite21.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite23.bin" ".\vcdiff\allybattlesprite23.bin.vcdiff" ".\output\allybattlesprite22.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite25.bin" ".\vcdiff\allybattlesprite25.bin.vcdiff" ".\output\allybattlesprite23.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite31.bin" ".\vcdiff\allybattlesprite31.bin.vcdiff" ".\output\allybattlesprite25.bin"
.\xdelta3_x86_64_win.exe -v -d -s ".\allybattlesprite00.bin" ".\vcdiff\allybattlesprite00.bin.vcdiff" ".\output\allybattlesprite31.bin"
echo Completed!
@pause
