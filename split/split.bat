echo off
cls
echo Start of split operation for file split/sf2.bin
echo Executing tools/splitrom.exe ...
cd ../disasm/
@"../tools/splitrom" ../rom/sf2.bin ../split/sf2splits.txt
echo End of split operation. Data extracted in disasm/ folder.
cd ../split
@call ./patch_battlesprites.bat
echo Patched battlesprites
@python ./expand_mapsprites.py
echo Expanded mapsprites
@call ./patch_mapsprites.bat
echo Patched mapsprites
@python "./swap characters.py"
echo Randomized various things
@call ../build/buildstandard.bat