@echo off
CHCP 65001
mkdir "..\disasm\data\graphics\icons\output"
.\xdelta3_x86_64_win.exe -f -v -d -s "..\disasm\data\graphics\icons\icon061.bin" ".\vcdiff\icon061.bin.vcdiff" "..\disasm\data\graphics\icons\output\icon061.bin"
move "..\disasm\data\graphics\icons\output\icon061.bin" "..\disasm\data\graphics\icons\icon061.bin"
echo Completed!
