import os
from pathlib import Path

adds = [26,27,50,52,53,55,56,58,60,61,62,64,66,67,68,70,72,74,75,77]
entries = {}
entries2 = []
change = 0

for x in adds:
	padded = "mapsprite" + (("0" + ( "0"+str(x) if x < 10 else str(x))) if x < 100 else str(x)) + "-0"
	entries2.append(padded)
	padded = "mapsprite" + (("0" + ( "0"+str(x) if x < 10 else str(x))) if x < 100 else str(x)) + "-1"
	entries2.append(padded)
	padded = "mapsprite" + (("0" + ( "0"+str(x) if x < 10 else str(x))) if x < 100 else str(x)) + "-2"
	entries2.append(padded)
	

for x in Path("..\\disasm\\data\\graphics\\mapsprites").iterdir():
	if(not x.name.endswith("bin")):
		continue
	name = x.stem
	index = int(name[9:-2])+change
	while(index in adds):
		change = change+1
		adds.remove(index)
		index = index+1
	index = index - change
	padded = "mapsprite" + (("0" + ( "0"+str(index) if index < 10 else str(index))) if index < 100 else str(index)) + name[-2:]
	index = index + change
	padded_c = "mapsprite" + (("0" + ( "0"+str(index) if index < 10 else str(index))) if index < 100 else str(index)) + name[-2:]
		
	entries[padded] = padded_c
	
for x in sorted(list(entries), reverse=True):
	p = Path(f"..\\disasm\\data\\graphics\\mapsprites\\{x}.bin")
	p.rename(p.with_name(f"{entries[x]}.bin"))
	
for x in entries2:
	p = Path(f"..\\disasm\\data\\graphics\\mapsprites\\{x}.bin")
	p.touch()