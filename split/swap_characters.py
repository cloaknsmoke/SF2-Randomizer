from pathlib import Path
import random
import re
import sys

loc = r".\disasm"

def swap_ALLY_r(p, a, b):
	if(len(a) != len(b)):
		raise Exception("Only swap lists of equal length.")
	for x in p.iterdir():
		if(x.is_dir()):
			swap_ALLY_r(x,a,b)
		elif(x.suffix == ".asm" and "sf2enums" not in x.name):
			try:
				f = open(x, 'r')
				file = f.read()
				f.close()
				for y in range(len(a)):
					if(a[y] in file):
						file = file.replace(a[y], "{char" + str(y) + "}")
				for y in range(len(b)):
					if(("{char" + str(y) + "}") in file):
						file = file.replace("{char" + str(y) + "}", b[y])
				f = open(x, 'w')
				f.write(file)
				f.close()
			except UnicodeDecodeError as e:
				continue

def replace_npc_rohde_sprite():
	f = open(loc + "\\sf2enums.asm", 'r')
	file1 = f.read()
	f.close()
	who_is_rohde = re.search("ALLY_[A-Z]*: equ 11", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm", 'r')
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_rohde, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	mapsprite = "MAPSPRITE_" + who_is_rohde + "_" + r_class_dict[new_class]
	new_sprite_index = file1[file1.find(mapsprite+": equ"):file1.find("\n", file1.find(mapsprite+": equ"))]
	new_sprite_index = new_sprite_index[new_sprite_index.find("equ")+4:]
	if(";" in new_sprite_index):
		new_sprite_index = new_sprite_index[0:new_sprite_index.find(";")]
	new_sprite_index = new_sprite_index.replace(" ", "").replace("\n", "")
	npc_rohde_index = file1.find("MAPSPRITE_NPC_ROHDE: equ ")+25 
	file1 = file1[0:npc_rohde_index] + new_sprite_index + file1[file1.find("\n", npc_rohde_index):]
	f = open(loc + "\\sf2enums.asm", 'w')
	f.write(file1)
	f.close()
	f = open(loc + r"\code\common\menus\caravan\caravanactions_1.asm", 'r')
	file = f.read()
	f.close()
	index1 = file.find("PORTRAIT_")
	index2 = file.find(",d0", index1)
	base = "_PROMO" if ("BOWIE" in who_is_rohde or "SLADE" in who_is_rohde or "KIWI" in who_is_rohde or "PETER" in who_is_rohde or "GERHALT" in who_is_rohde or "CLAUDE" in who_is_rohde) else ""
	file = file[0:index1] + "PORTRAIT_" + who_is_rohde + base + file[index2:]
	f = open(loc + r"\code\common\menus\caravan\caravanactions_1.asm", 'w')
	f.write(file)
	f.close()
	f = open(loc + r"\code\common\menus\caravan\displaycaravanmessagewithportrait.asm", 'r')
	file = f.read()
	f.close()
	index1 = file.find("PORTRAIT_")
	index2 = file.find(",d0", index1)
	base = "_PROMO" if ("BOWIE" in who_is_rohde or "SLADE" in who_is_rohde or "KIWI" in who_is_rohde or "PETER" in who_is_rohde or "GERHALT" in who_is_rohde or "CLAUDE" in who_is_rohde) else ""
	file = file[0:index1] + "PORTRAIT_" + who_is_rohde + base + file[index2:]
	f = open(loc + r"\code\common\menus\caravan\displaycaravanmessagewithportrait.asm", 'w')
	f.write(file)
	f.close()

def replace_spinning_elric():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_elric = re.search("ALLY_[A-Z]*: equ 13", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_elric, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	harpie_battle = file3[file3.find("HARPIES_POND"):file3.find("TERMINATOR_WORD",file3.find("HARPIES_POND"))]
	harpie_rep = harpie_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", harpie_battle).group(), "mapsprite " + who_is_elric + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(harpie_battle, harpie_rep)
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()

def replace_knocked_out_luke():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_luke = re.search("ALLY_[A-Z]*: equ 10", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_luke, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	polca_battle = file3[file3.find("POLCA_VILLAGE"):file3.find("TERMINATOR_WORD",file3.find("POLCA_VILLAGE"))]
	polca_rep = polca_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", polca_battle).group(), "mapsprite " + who_is_luke + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(polca_battle, polca_rep)
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()
	
def replace_knocked_out_higins():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_higins = re.search("ALLY_[A-Z]*: equ 19", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_higins, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	np_battle = file3[file3.find("OUTSIDE_KETTO"):file3.find("TERMINATOR_WORD",file3.find("OUTSIDE_KETTO"))]
	np_rep = np_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", np_battle).group(), "mapsprite " + who_is_higins + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(np_battle, np_rep)
	f = open(loc + "\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()

def replace_enemy_jaro():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_jaro = re.search("ALLY_[A-Z]*: equ 23", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_jaro, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\stats\\enemies\\enemymapsprites.asm", 'r')
	file3 = f.read()
	f.close()
	index1 = file3.find("mapsprite", file3.find("; 98: ZEON"))
	index2 = file3.find("; 99: JAR")
	file3 = file3[0:index1] + "mapsprite " + who_is_jaro + "_" + r_class_dict[new_class] + " " + file3[index2:]  
	f = open(loc + "\\data\\stats\\enemies\\enemymapsprites.asm", 'w')
	f.write(file3)
	f.close()
	f = open(loc + "\\data\\stats\\enemies\\enemynames-capitalized.asm", 'r')
	file3 = f.read()
	f.close()
	index1 = file3.find("enemyName", file3.find("\"Zeon\""))
	index2 = file3.find("\n", index1)
	file3 = file3[0:index1] + "enemyName \"" + who_is_jaro.capitalize() + "\"" + file3[index2:]
	f = open(loc + "\\data\\stats\\enemies\\enemynames-capitalized.asm", 'w')
	f.write(file3)
	f.close()

def replace_stone_taya():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_taya = re.search("ALLY_[A-Z]*: equ 21", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_taya, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + r"\data\maps\entries\map01\mapsetups\s6_initfunction.asm", 'r')
	file2 = f.read()
	f.close()
	index1 = file2.find(",", file2.find("setSprite", file2.find("; Taya joined")))+1
	index2 = file2.find("\n", index1)
	#special case if taya is still in her original spot since she has a unique sprite
	if(who_is_taya == "TAYA"):
		file2 = file2[0:index1] + "MAPSPRITE_OBJECT4" + file2[index2:]
	else:
		file2 = file2[0:index1] + "ALLY_" + who_is_taya + file2[index2:]
	f = open(loc + r"\data\maps\entries\map63\mapsetups\s6_initfunction.asm", 'w')
	f.write(file2)
	f.close()
	
def replace_frozen_claude():
	f = open(loc + "\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_claude = re.search("ALLY_[A-Z]*: equ 29", file1).group()[5:-8]
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file2 = f.read()
	f.close()
	new_class = re.search("startClass [A-Z]*_?\\d?         ; \\d*: " + who_is_claude, file2).group()
	new_class = new_class[11:new_class.find("         ")]
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + r"\data\maps\entries\map63\mapsetups\s6_initfunction.asm", 'r')
	file2 = f.read()
	f.close()
	index1 = file2.find(",", file2.find("setSprite", file2.find("; Claude joined")))+1
	index2 = file2.find("\n", index1)
	#special case if claude is still in his original spot since he has a unique sprite
	if(who_is_claude == "CLAUDE"):
		file2 = file2[0:index1] + "MAPSPRITE_POSE3" + file2[index2:]
	else:
		file2 = file2[0:index1] + "ALLY_" + who_is_claude + file2[index2:]
	f = open(loc + r"\data\maps\entries\map63\mapsetups\s6_initfunction.asm", 'w')
	f.write(file2)
	f.close()
	f = open(loc + r"\data\maps\entries\map63\mapsetups\scripts.asm", 'r')
	file2 = f.read()
	f.close()
	index1 = file2.find(",", file2.find("setSprite", file2.find("; Claude joined")))+1
	index2 = file2.find("\n", index1)
	#special case if claude is still in his original spot since he has a unique sprite
	if(who_is_claude == "CLAUDE"):
		file2 = file2[0:index1] + "MAPSPRITE_POSE3" + file2[index2:]
	else:
		file2 = file2[0:index1] + "ALLY_" + who_is_claude + file2[index2:]
	f = open(loc + r"\data\maps\entries\map63\mapsetups\scripts.asm", 'w')
	f.write(file2)
	f.close()


def remove_redundant_classes():
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm")
	file = f.read()
	f.close()
	splits = file.split("startClass")
	for x in range(2,32):
		cur_class = re.search(" [A-Z]*_?\\d? ", splits[x]).group()[1:-1]
		if(r_class_dict[cur_class] == "BASE"):
			continue
		num = int(re.search("; [0-9]*:", splits[x]).group()[2:-1])
		f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(num) if num > 9 else ("0" + str(num))) +".asm", 'r')
		file = f.read()
		f.close()
		splits2 = file.split("forClass")
		base_spells = ""
		class_data = ""
		for y in splits2:
			if("AllyStats" in y or "projected" in y):
				continue
			if("spellList" in y and base_spells == ""):
				base_spells = y[y.find("spellList"):].strip()
			if(cur_class in y):
				class_data = y
		if("useFirstSpellList" in class_data):
			class_data = class_data.replace("useFirstSpellList", base_spells)
		file = file[0:file.index("forClass")+9].replace("; Syntax", "        ") + class_data.strip()
		f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(num) if num > 9 else ("0" + str(num))) +".asm", 'w')
		f.write(file)
		f.close()
def adjust_promo_stats(ally_num, new_class, new_promo_level, growths):
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'r')
	file = f.read()
	f.close()
	splits = file.split("forClass")
	base_block = ""
	promo_block = ""
	for x in splits:
		if("AllyStats" in x or "projected" in x):
			continue
		if(new_class in x):
			promo_block = x
		for y in class_dict["BASE"]:
			if(y in x):
				base_block = x
	baseHP = float(base_block[base_block.find("hpGrowth")+9:base_block.find(",", (base_block.find("hpGrowth")))])
	baseHP_max = float(base_block[base_block.find(",", base_block.find("hpGrowth"))+2:base_block.rfind(",", 0, (base_block.find("mpGrowth")))])
	baseHP_growth = base_block[base_block.rfind(",", 0 ,base_block.find("\n", base_block.find("hpGrowth")))+2:base_block.find("\n", base_block.find("hpGrowth"))]
	baseMP = float(base_block[base_block.find("mpGrowth")+9:base_block.find(",", (base_block.find("mpGrowth")))])
	baseMP_max = float(base_block[base_block.find(",", base_block.find("mpGrowth"))+2:base_block.rfind(",", 0, (base_block.find("attGrowth")))])
	baseMP_growth = base_block[base_block.rfind(",", 0 ,base_block.find("\n", base_block.find("mpGrowth")))+2:base_block.find("\n", base_block.find("mpGrowth"))]
	baseATT = float(base_block[base_block.find("attGrowth")+10:base_block.find(",", (base_block.find("attGrowth")))])
	baseATT_max = float(base_block[base_block.find(",", base_block.find("attGrowth"))+2:base_block.rfind(",", 0, (base_block.find("defGrowth")))])
	baseATT_growth = base_block[base_block.rfind(",", 0 ,base_block.find("\n", base_block.find("attGrowth")))+2:base_block.find("\n", base_block.find("attGrowth"))]
	baseDEF = float(base_block[base_block.find("defGrowth")+10:base_block.find(",", (base_block.find("defGrowth")))])
	baseDEF_max = float(base_block[base_block.find(",", base_block.find("defGrowth"))+2:base_block.rfind(",", 0, (base_block.find("agiGrowth")))])
	baseDEF_growth = base_block[base_block.rfind(",", 0 ,base_block.find("\n", base_block.find("defGrowth")))+2:base_block.find("\n", base_block.find("defGrowth"))]
	baseAGI = float(base_block[base_block.find("agiGrowth")+10:base_block.find(",", (base_block.find("agiGrowth")))])
	baseAGI_max = float(base_block[base_block.find(",", base_block.find("agiGrowth"))+2:base_block.rfind(",", 0, (base_block.find("List")))])
	baseAGI_growth = base_block[base_block.rfind(",", 0 ,base_block.find("\n", base_block.find("agiGrowth")))+2:base_block.find("\n", base_block.find("agiGrowth"))]
	promoHP_base = float(promo_block[promo_block.find("hpGrowth")+9:promo_block.find(",", (promo_block.find("hpGrowth")))])
	promoHP_max = float(promo_block[promo_block.find(",", promo_block.find("hpGrowth"))+2:promo_block.rfind(",", 0, (promo_block.find("mpGrowth")))])
	promoMP_base = float(promo_block[promo_block.find("mpGrowth")+9:promo_block.find(",", (promo_block.find("mpGrowth")))])
	promoMP_max = float(promo_block[promo_block.find(",", promo_block.find("mpGrowth"))+2:promo_block.rfind(",", 0, (promo_block.find("attGrowth")))])
	promoATT_base = float(promo_block[promo_block.find("attGrowth")+10:promo_block.find(",", (promo_block.find("attGrowth")))])
	promoATT_max = float(promo_block[promo_block.find(",", promo_block.find("attGrowth"))+2:promo_block.rfind(",", 0, (promo_block.find("defGrowth")))])
	promoDEF_base = float(promo_block[promo_block.find("defGrowth")+10:promo_block.find(",", (promo_block.find("defGrowth")))])
	promoDEF_max = float(promo_block[promo_block.find(",", promo_block.find("defGrowth"))+2:promo_block.rfind(",", 0, (promo_block.find("agiGrowth")))])
	promoAGI_base = float(promo_block[promo_block.find("agiGrowth")+10:promo_block.find(",", (promo_block.find("agiGrowth")))])
	promoAGI_max = float(promo_block[promo_block.find(",", promo_block.find("agiGrowth"))+2:promo_block.rfind(",", 0, (promo_block.find("List")))])
	stat_list = [baseHP,baseMP,baseATT,baseDEF,baseAGI]
	cur_stat_list = [baseHP,baseMP,baseATT,baseDEF,baseAGI]
	stat_max_list = [baseHP_max,baseMP_max,baseATT_max,baseDEF_max,baseAGI_max]
	growth_list = [baseHP_growth,baseMP_growth,baseATT_growth,baseDEF_growth,baseAGI_growth]
	for x in range(0,int(new_promo_level-1)):
		for y in range(len(stat_list)):
			if(growth_list[y] == "NONE"):
				continue
			if(x < 29):
				expected_gain = int(float(growths[growth_list[y]][x][1])*(stat_max_list[y]-stat_list[y])/256.0 + random.random())
				expected_average = (stat_max_list[y]-stat_list[y])*(float(growths[growth_list[y]][x][0])/256.0)+stat_list[y]
				cur_stat_list[y] += expected_gain
				if(cur_stat_list[y] < expected_average):
					cur_stat_list[y] += 1
			else:
				expected_gain = int(1.5*(stat_max_list[y]-stat_list[y])/29 + random.random())
				expected_average = stat_max_list[y] + (stat_max_list[y]-stat_list[y])*1.5*(30-x)/29
				cur_stat_list[y] = cur_stat_list[y] + expected_gain
				if(cur_stat_list[y] < expected_average):
					cur_stat_list[y] += 1
	promo_new_max = [promoHP_max + (cur_stat_list[0] - promoHP_base),promoMP_max + (cur_stat_list[1] - promoMP_base),\
	promoATT_max + (cur_stat_list[2] - promoATT_base), promoDEF_max + (cur_stat_list[3] - promoDEF_base),\
	promoAGI_max + (cur_stat_list[4] - promoAGI_base)]
	splits = promo_block.split("\n")
	promo_block_rep = ""
	for x in splits:
		if("hpGrowth" in x):
			promo_block_rep += x[0:x.find("hpGrowth")] + "hpGrowth  " + str(int(cur_stat_list[0])) + ", " + str(int(promo_new_max[0])) + x[x.rfind(","):] + "\n"
		elif("mpGrowth" in x):
			promo_block_rep += x[0:x.find("mpGrowth")] + "mpGrowth  " + str(int(cur_stat_list[1])) + ", " + str(int(promo_new_max[1])) + x[x.rfind(","):] + "\n"
		elif("attGrowth" in x):
			promo_block_rep += x[0:x.find("attGrowth")] + "attGrowth " + str(int(cur_stat_list[2])) + ", " + str(int(promo_new_max[2])) + x[x.rfind(","):] + "\n"
		elif("defGrowth" in x):
			promo_block_rep += x[0:x.find("defGrowth")] + "defGrowth " + str(int(cur_stat_list[3])) + ", " + str(int(promo_new_max[3])) + x[x.rfind(","):] + "\n"
		elif("agiGrowth" in x):
			promo_block_rep += x[0:x.find("agiGrowth")] + "agiGrowth " + str(int(cur_stat_list[4])) + ", " + str(int(promo_new_max[4])) + x[x.rfind(","):] + "\n"
		else:
			promo_block_rep += x + "\n"
	promo_block_rep = promo_block_rep[0:-1]
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'w')
	f.write(file.replace(promo_block, promo_block_rep))
	f.close()

def determine_new_class(name, class_old, with_class, promo_dict, r_promo_dict, wiz_flag, depromote, rand_promo):
	orig_promos = orig_values = {"ROHDE" : "BRGN", "HIGINS" : "PLDN", "SKREECH" : "BDBT", "TAYA" : "SORC_3", "FRAYJA" : "VICR",\
	"JARO" : "PGNT", "GYAN" : "GLDT", "SHEELA" : "MMNK", "ZYNK" : "RBT", "CHAZ" : "WIZ", "LEMON" : "RDBN", "CLAUDE" : "GLM"}
	is_old_promo = False if class_old in promo_dict else True
	is_new_promo = False if with_class in promo_dict else True
	if(class_old == "WIZ"):
		match wiz_flag:
			case 1:
				r_promo_dict[class_old] = "MAGE_1"
			case 2:
				r_promo_dict[class_old] = "MAGE_2"
			case 3:
				r_promo_dict[class_old] = "MAGE_3"
			case 4:
				r_promo_dict[class_old] = "MAGE_4"
	if(is_old_promo):
		if(is_new_promo):
			class_options = promo_dict[r_promo_dict[class_old]] if rand_promo else class_old
			if(type(class_options) is tuple):
				return random.choice(class_options)
			else:
				return class_options
		else:
			return r_promo_dict[class_old] if depromote else class_old
	else:
		if(is_new_promo):
			if(rand_promo):
				class_options = promo_dict[class_old]
			elif(name in orig_promos):
				class_options = orig_promos[name]
			else:
				class_options = class_old
			if(type(class_options) is tuple):
				return random.choice(class_options)
			else:
				return class_options
		else:
			return class_old

def new_items(items, with_class, is_promo, level, weapon_ranges, equips):
	if(is_promo):
		level = level + 20
	for x in range(len(items)):
		if(items[x] in weapon_ranges):
			for y in equips[with_class]:
				if(level >= weapon_ranges[y][1]):
					items[x] = y

'''
char_a_list : The original characters to be replaced
char_b_list : The characters to be put in
'''
def swap_characters(char_a_list, char_b_list, orig_nums, depromote, rand_promo):
	if(len(char_a_list) != len(char_b_list)):
		raise Exception("Only swap character lists of equal length")
	if(len(char_a_list) != len(set(char_a_list))):
		raise Exception("Only unique characters in each list")
	if(len(char_b_list) != len(set(char_b_list))):
		raise Exception("Only unique characters in each list")
	for x in char_a_list:
		if(x not in char_b_list):
			raise Exception("All characters must be matched to somewherre in the opposite list.")
	char_a_name_list = [x.capitalize() for x in char_a_list]
	char_b_name_list = [x.capitalize() for x in char_b_list]
	p = Path(loc + "")
	f = open(loc + "\\sf2enums.asm", 'r')
	file = f.read()
	f.close()
	char_a_value = [file.find("ALLY_"+x) for x in char_a_list]
	char_a_value = [file[char_a_value[x]+len(char_a_list[x])+11:file.find("\n", char_a_value[x])] for x in range(len(char_a_value))]
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		base = "_BASE" if ("BOWIE" in cur_char or "SLADE" in cur_char or "KIWI" in cur_char or "PETER" in cur_char or "GERHALT" in cur_char or "CLAUDE" in cur_char) else ""
		file = file.replace("ALLY_"+cur_char + ": equ " + char_a_value[x], "{ally" + str(x) + "}")
		file = file.replace("PORTRAIT_" + cur_char + base + ": equ " + char_a_value[x], "{portrait" + str(x) + "}")
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		base = "_BASE" if ("BOWIE" in cur_char or "SLADE" in cur_char or "KIWI" in cur_char or "PETER" in cur_char or "GERHALT" in cur_char or "CLAUDE" in cur_char) else ""
		file = file.replace("{ally" + str(x) + "}", "ALLY_"+cur_char + ": equ " + char_a_value[x])
		file = file.replace("{portrait" + str(x) + "}", "PORTRAIT_" + cur_char + base + ": equ " + char_a_value[x])
	f = open(loc + "\\sf2enums.asm", 'w')
	f.write(file)
	f.close()

	swap_ALLY_r(Path(loc + ""), ["ALLY_"+x for x in char_a_list],["ALLY_"+x for x in char_b_list])
	
	f = open(loc + "\\data\\stats\\allies\\allydialogproperties-standard.asm", 'r')
	file = f.read()
	f.close()
	temp = {}
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		loc_a = file.find("; " + str(orig_nums[cur_char]) + ": ")
		line_e = file.find("\n", loc_a)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		text = file[loc_a:line_e]
		file = file.replace(text, "{char" + str(x) + "}")
		temp[cur_char] = text
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		text = temp[cur_char]
		file = file.replace("{char" + str(x) + "}", text)
	f = open(loc + "\\data\\stats\\allies\\allydialogproperties-standard.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\stats\\allies\\stats\\entries.asm", 'r')
	file = f.read()
	f.close()
	temp = {}
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		loc_a = file.find("AllyStats" + (str(orig_nums[cur_char]) if orig_nums[cur_char] > 9 else ("0" + str(orig_nums[cur_char]))))
		line_e = file.find("\n", loc_a)
		text = file[loc_a:line_e]
		file = file.replace(text, "{char" + str(x) + "}")
		temp[cur_char] = text
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		text = temp[cur_char]
		file = file.replace("{char" + str(x) + "}", text)
	f = open(loc + "\\data\\stats\\allies\\stats\\entries.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\stats\\allies\\allybattlesprites.asm", 'r')
	file = f.read()
	f.close()
	temp = {}
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		loc_a = file.find("; " + str(orig_nums[cur_char]) + ": ")
		line_e = file.find("\n", loc_a)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		text = file[loc_a:line_e]
		file = file.replace(text, "{char" + str(x) + "}")
		temp[cur_char] = text
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		text = temp[cur_char]
		file = file.replace("{char" + str(x) + "}", text)
	f = open(loc + "\\data\\stats\\allies\\allybattlesprites.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\stats\\allies\\allymapsprites-standard.asm", 'r')
	file = f.read()
	f.close()
	temp = {}
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		loc_a = file.find("; " + str(orig_nums[cur_char]) + ": ")
		line_e = file.find("\n", loc_a)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		line_e = file.find("\n", line_e+1)
		text = file[loc_a:line_e]
		file = file.replace(text, "{char" + str(x) + "}")
		temp[cur_char] = text
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		text = temp[cur_char]
		file = file.replace("{char" + str(x) + "}", text)
	f = open(loc + "\\data\\stats\\allies\\allymapsprites-standard.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\stats\\allies\\allynames-capitalized.asm", 'r')
	file = f.read()
	f.close()
	for x in range(len(char_a_name_list)):
		cur_char = char_a_name_list[x]
		file = file.replace(cur_char, "{char" + str(x) + "}")
	for x in range(len(char_b_name_list)):
		cur_char = char_b_name_list[x]
		file = file.replace("{char" + str(x) + "}", cur_char)
	f = open(loc + "\\data\\stats\\allies\\allynames-capitalized.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm", 'r')
	file = f.read()
	f.close()
	valid_promos = {"SDMN" : ("HERO"), "KNTE" : ("PLDN", "PGNT"), "PRST" : ("VICR", "MMNK"), "WARR" : ("GLDT", "BRN"), "MAGE_1" : ("WIZ", "SORC_1"), \
	"MAGE_2" : ("WIZ", "SORC_2"), "MAGE_3" : ("WIZ", "SORC_3"), "MAGE_4" : ("WIZ", "SORC_4"), "ACHR" : ("SNIP", "BRGN"), "BDMN" : ("BDBT"), \
	"WFMN" : ("WFBR"), "RNGR" : ("BWNT"), "PHNK" : ("PHNX"), "THIF" : ("NINJ"), "TORT" : ("MNST"), "DRD" : ("RBT"), "CNST":("GLM"), "RWAR":("RDBN")}
	valid_classes = []
	reverse_valid_promos = {}
	for (k,v) in valid_promos.items():
		valid_classes.append(k)
		
		if(type(v) is tuple):
			valid_classes.extend(v)
			for x in v:
				reverse_valid_promos[x] = k
		else:
			valid_classes.append(v)
			reverse_valid_promos[v] = k
	valid_equips = {
	"SDMN" : ["WOODEN_SWORD","SHORT_SWORD","MIDDLE_SWORD","LONG_SWORD","STEEL_SWORD"],
	"HERO" : ["BROAD_SWORD", "BUSTER_SWORD", "GREAT_SWORD"],
	"KNTE" : ["WOODEN_STICK","SHORT_SPEAR","BRONZE_LANCE","SPEAR","STEEL_LANCE","POWER_SPEAR"],
	"PLDN" : ["HEAVY_LANCE","JAVELIN","CHROME_LANCE"],
	"PGNT" : ["HEAVY_LANCE","JAVELIN","CHROME_LANCE"],
	"PRST" : ["WOODEN_ROD","SHORT_ROD","BRONZE_ROD","IRON_ROD","POWER_STICK"],
	"VICR" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"MMNK" : ["LEATHER_GLOVE","POWER_GLOVE","BRASS_KNUCKLES","IRON_KNUCKLES"],
	"WARR" : ["SHORT_AXE","HAND_AXE","MIDDLE_AXE","POWER_AXE","BATTLE_AXE"],
	"GLDT" : ["LARGE_AXE","GREAT_AXE"],
	"BRN" : ["BROAD_SWORD", "BUSTER_SWORD", "GREAT_SWORD"],
	"MAGE_1" : ["WOODEN_ROD","SHORT_ROD","BRONZE_ROD","IRON_ROD","POWER_STICK"],
	"MAGE_2" : ["WOODEN_ROD","SHORT_ROD","BRONZE_ROD","IRON_ROD","POWER_STICK"],
	"MAGE_3" : ["WOODEN_ROD","SHORT_ROD","BRONZE_ROD","IRON_ROD","POWER_STICK"],
	"MAGE_4" : ["WOODEN_ROD","SHORT_ROD","BRONZE_ROD","IRON_ROD","POWER_STICK"],
	"WIZ" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"SORC_1" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"SORC_2" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"SORC_3" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"SORC_4" : ["FLAIL","GUARDIAN_STAFF","INDRA_STAFF"],
	"ACHR" : ["WOODEN_ARROW","IRON_ARROW","STEEL_ARROW"],
	"SNIP" : ["ROBIN_ARROW","ASSAULT_SHELL","GREAT_SHOT"],
	"BRGN" : ["ROBIN_ARROW","ASSAULT_SHELL","GREAT_SHOT"],
	"BDMN" : ["WOODEN_SWORD","SHORT_SWORD","MIDDLE_SWORD","LONG_SWORD","STEEL_SWORD"],
	"BDBT" : ["BROAD_SWORD", "BUSTER_SWORD", "GREAT_SWORD"],
	"RNGR" : ["WOODEN_ARROW","IRON_ARROW","STEEL_ARROW"],
	"BWNT" : ["ROBIN_ARROW","ASSAULT_SHELL","GREAT_SHOT"],
	"THIF" : ["SHORT_KNIFE","DAGGER","KNIFE","THIEVES_DAGGER"],
	"NINJ" : ["BROAD_SWORD", "BUSTER_SWORD", "GREAT_SWORD"],
	"RWAR" : ["SHORT_AXE","HAND_AXE","MIDDLE_AXE","POWER_AXE","BATTLE_AXE"],
	"RDBN" : ["LARGE_AXE","GREAT_AXE"]
	}
	valid_weapon_level_ranges = {
	"WOODEN_SWORD":(False, 1,3),
	"SHORT_SWORD":(False, 4,7),
	"MIDDLE_SWORD":(False, 8,9),
	"LONG_SWORD":(False, 10,18),
	"STEEL_SWORD":(False, 19,99),
	"BROAD_SWORD":(True, 21,23),
	"BUSTER_SWORD":(True, 24,26),
	"GREAT_SWORD":(True, 27,99),
	"WOODEN_ROD":(False, 1,4),
	"SHORT_ROD":(False, 5,10),
	"BRONZE_ROD":(False, 11,18),
	"IRON_ROD":(False, 99,99),
	"POWER_STICK":(False, 19,99),
	"FLAIL":(True, 21,23),
	"GUARDIAN_STAFF":(True, 24,26),
	"INDRA_STAFF":(True, 27,99),
	"WOODEN_STICK":(False, 1,3),
	"SHORT_SPEAR":(False, 4,4),
	"BRONZE_LANCE":(False, 5,8),
	"SPEAR":(False, 9,12),
	"STEEL_LANCE":(False, 13,18),
	"POWER_SPEAR":(False, 19,99),
	"HEAVY_LANCE":(True, 24,26),
	"JAVELIN":(True, 27,30),
	"CHROME_LANCE":(True, 31,99),
	"SHORT_AXE":(False, 1,4),
	"HAND_AXE":(False, 6,12),
	"MIDDLE_AXE":(False, 13,18),
	"POWER_AXE":(False, 99,99),
	"BATTLE_AXE":(False, 19,99),
	"LARGE_AXE":(True, 24,30),
	"GREAT_AXE":(True, 31,99),
	"SHORT_KNIFE":(False, 1,9),
	"DAGGER":(False, 10,12),
	"KNIFE":(False, 13,18),
	"THIEVES_DAGGER":(False, 19,99),
	"LEATHER_GLOVE":(True, 21,23),
	"POWER_GLOVE":(True, 24,30),
	"BRASS_KNUCKLES":(True, 31,33),
	"IRON_KNUCKLES":(True, 34,99),
	"WOODEN_ARROW":(False, 1,12),
	"IRON_ARROW":(False, 13,18),
	"STEEL_ARROW":(False, 19,99),
	"ROBIN_ARROW":(True, 21,23),
	"ASSAULT_SHELL":(True, 24,26),
	"GREAT_SHOT":(True, 27,99)}
	temp = {}
	temp_rep = {}
	for x in range(len(char_a_list)):
		cur_char_a = char_a_list[x]
		if(cur_char_a not in temp):
			loc_a = file.find("; " + str(orig_nums[cur_char_a]) + ": ")
			loc_a = file.rfind("\n", 0,loc_a)+1
			line_e = file.find("\n", loc_a)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			text = file[loc_a:line_e]
			temp[cur_char_a] = text
		else:
			text = temp[cur_char_a]
		class_a = text[text.find("startClass")+11:text.find("startClass")+15]
		if(class_a not in valid_classes):
			if("MAGE" in class_a or "SORC" in class_a):
				class_a = text[text.find("startClass")+11:text.find("startClass")+17]
			else:
				class_a = text[text.find("startClass")+11:text.find("startClass")+14]
		level_a = text[text.find("startLevel")+11:text.find("startLevel")+13]
		if(not level_a.isdecimal()):
			level_a = text[text.find("startLevel")+11:text.find("startLevel")+12]
		item_1a_in = text.find("&")+1
		item_1a = text[item_1a_in:text.find("&", item_1a_in)].strip()
		item_1a = item_1a.replace("|EQUIPPED","").replace(",", "")
		item_2a_in = text.find("&", item_1a_in)+1
		item_2a = text[item_2a_in:text.find("&", item_2a_in)].strip()
		item_2a = item_2a.replace("|EQUIPPED","").replace(",", "")
		item_3a_in = text.find("&", item_2a_in)+1
		item_3a = text[item_3a_in:text.find("&", item_3a_in)].strip()
		item_3a = item_3a.replace("|EQUIPPED","").replace(",", "")
		item_4a_in = text.find("&", item_3a_in)+1
		item_4a = text[item_4a_in:].strip()
		item_4a = item_4a.replace("|EQUIPPED","").replace(",", "")
		file = file.replace(text, "{char" + str(x) + "}")

		cur_char_b = char_b_list[x]
		if(cur_char_b not in temp):
			loc_b = file.find("; " + str(orig_nums[cur_char_b]) + ": ")
			loc_b = file.rfind("\n", 0,loc_b)+1
			line_e = file.find("\n", loc_b)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			line_e = file.find("\n", line_e+1)
			text = file[loc_b:line_e]
			temp[cur_char_b] = text
		else:
			text = temp[cur_char_b]
		class_b = text[text.find("startClass")+11:text.find("startClass")+15]
		if(class_b not in valid_classes):
			if("MAGE" in class_b or "SORC" in class_b):
				class_b = text[text.find("startClass")+11:text.find("startClass")+17]
			else:
				class_b = text[text.find("startClass")+11:text.find("startClass")+14]
		level_b = text[text.find("startLevel")+11:text.find("startLevel")+13]
		if(not level_b.isdecimal()):
			level_b = text[text.find("startLevel")+11:text.find("startLevel")+12]
		item_1b_in = text.find("&")+1
		item_1b = text[item_1b_in:text.find("&", item_1b_in)].strip()
		item_1b = item_1b.replace("|EQUIPPED","").replace(",", "")
		item_2b_in = text.find("&", item_1b_in)+1
		item_2b = text[item_2b_in:text.find("&", item_2b_in)].strip()
		item_2b = item_2b.replace("|EQUIPPED","").replace(",", "")
		item_3b_in = text.find("&", item_2b_in)+1
		item_3b = text[item_3b_in:text.find("&", item_3b_in)].strip()
		item_3b = item_3b.replace("|EQUIPPED","").replace(",", "")
		item_4b_in = text.find("&", item_3b_in)+1
		item_4b = text[item_4b_in:].strip()
		item_4b = item_4b.replace("|EQUIPPED","").replace(",", "")
		
		match char_b_name_list[x]:
			case "Kazin":
				wiz_flag = 1
			case "Tyrin":
				wiz_flag = 2
			case "Taya":
				wiz_flag = 3
			case "Chaz":
				wiz_flag = 4
			case _:
				wiz_flag = 0
		new_class_b = determine_new_class(cur_char_b, class_b, class_a, valid_promos, reverse_valid_promos, wiz_flag, depromote, rand_promo)
		if(new_class_b in valid_promos and class_a in reverse_valid_promos):
			level_a = str(int(level_a) + 20)
		if(new_class_b in reverse_valid_promos and class_a in valid_promos):
			level_a = str(int(level_b) - 20)
		
		items_a = [item_1a, item_2a, item_3a, item_4a]
		items_b = [item_1b, item_2b, item_3b, item_4b]
		for y in range(3, -1, -1):
			if(items_a[y] == "NOTHING"):
				items_a.pop(y)
			if(items_b[y] == "NOTHING"):
				items_b.pop(y)
		new_items(items_b, new_class_b, new_class_b in reverse_valid_promos, int(level_a), valid_weapon_level_ranges, valid_equips)
		for y in range(len(items_a)-1, -1, -1):
			if(items_a[y] in valid_weapon_level_ranges):
				items_a.pop(y)
		for y in range(len(items_b)-1, -1, -1):
			if(items_b[y] not in valid_weapon_level_ranges):
				items_b.pop(y)
		items_b.extend(items_a)
		while(len(items_b) < 4):
			items_b.append("NOTHING")
		
		text_b = "                startClass "+ new_class_b + "         ; "+str(orig_values[cur_char_b])+": "+cur_char_b + "\n"+\
		"                startLevel "+level_a+"\n"+\
		"                startItems &\n"+\
		"                    "+items_b[0]+("|EQUIPPED" if items_b[0] in valid_weapon_level_ranges else "")+", &\n"+\
		"                    "+items_b[1]+("|EQUIPPED" if items_b[1] in valid_weapon_level_ranges else "")+", &\n"+\
		"                    "+items_b[2]+("|EQUIPPED" if items_b[2] in valid_weapon_level_ranges else "")+", &\n"+\
		"                    "+items_b[3]+("|EQUIPPED" if items_b[3] in valid_weapon_level_ranges else "")
		temp_rep[cur_char_b] = text_b
	for x in range(len(char_b_list)):
		file = file.replace("{char" + str(x) + "}", temp_rep[char_b_list[x]])
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm", 'w')
	f.write(file)
	f.close()
	
	f = open(loc + "\\data\\graphics\\portraits\\entries.asm", 'r')
	file = f.read()
	f.close()
	temp = {}
	for x in range(len(char_a_list)):
		cur_char = char_a_list[x]
		file = file.replace("dc.l Portrait" + ("0" if orig_values[cur_char] < 10 else "") + str(orig_values[cur_char]), "{char" + str(x) + "}")
	for x in range(len(char_b_list)):
		cur_char = char_b_list[x]
		file = file.replace("{char" + str(x) + "}", "dc.l Portrait" + ("0" if orig_values[cur_char] < 10 else "") + str(orig_values[cur_char]))
	f = open(loc + "\\data\\graphics\\portraits\\entries.asm", 'w')
	f.write(file)
	f.close()
	
'''
Generate the text for the relevant allyStatsXX.asm file.
join_num       : Which position the character joins. This is relevant for determining if someone needs a starter spell for leveling purposes.
starter_spells : Spells which can be used at level 1 to get xp. Low mp usage basically
char_spells    : List with the levels a character can learn spells
levels         : The levels each spell has
spells_1       : All available spells that have only 1 level. I didn't increase the slots for those slots. Use spells will be removed from the list in place.
spells_2       : All available spells that have 2 or more levels. Used spells will be removed from the list in place.
level1_spells  : How many single level spells this character needs spots for.
level2_spells  : How many multi-level spells this character needs spots for.
mage           : Only mage type characters need a starter spell.
'''
def generate_text(join_num, starter_spells, char_spells, levels, spells_1, spells_2, level1_spells, level2_spells, mage):
	#guarantee a starter spell if you join in Ribble or earlier as a mage
	if(join_num < 9 and mage):
		temp_spell = random.choice(starter_spells)
		#keep rerolling our choice until we get a spell that is still available
		#fairly unlikely, but it can happen
		while(temp_spell not in spells_2):
			temp_spell = random.choice(starter_spells)
		cur_spells = [temp_spell]
		spells_2.remove(temp_spell)
		level2_spells = level2_spells - 1
	else:
		temp_spell = random.choice(spells_2)
		cur_spells = [temp_spell]
		spells_2.remove(temp_spell)
		level2_spells = level2_spells - 1
	for x in range(level1_spells):
		temp_spell = random.choice(spells_1)
		while(temp_spell in cur_spells):
			temp_spell = random.choice(spells_1)
		cur_spells.append(temp_spell)
		spells_1.remove(temp_spell)
	for x in range(level2_spells):
		temp_spell = random.choice(spells_2)
		while(temp_spell in cur_spells):
			if(set(cur_spells) >= set(spells_2)):
				raise Exception(f"Welp, all of the remaining spell options are already in {cur_spells}. Possible picks include {spells_2}.")
			temp_spell = random.choice(spells_2)
		cur_spells.append(temp_spell)
		spells_2.remove(temp_spell)
	
	#as it turns out, you can't have 4 level 4 spells, so we have to start over if we get that
	level4_spells = 0
	for x in cur_spells:
		if(levels[x] == 4):
			level4_spells = level4_spells+1
	if(level4_spells == 4):
		raise Exception(f"We generated a character with 4 slots of level 4 spells which is a no-no in the game engine for some reason.")
	
	spell_dict = {}
	#we need to make sure we start with the starter spell in the first slot
	if(join_num < 9 and mage):
		spell_dict[1] = cur_spells[0]
		char_spells.remove(1)
		#all starter spells are 4 level spells and we already assigned level 1
		for y in range(3):
			index = random.choice(char_spells)
			spell_dict[index] =  cur_spells[0]
			char_spells.remove(index)
		for z in range(3):
			#start on spell 2
			z = z+1
			for y in range(levels[cur_spells[z]]):
				index = random.choice(char_spells)
				spell_dict[index] =  cur_spells[z]
				char_spells.remove(index)
	else:
		for z in range(len(cur_spells)):
			for y in range(levels[cur_spells[z]]):
				index = random.choice(char_spells)
				spell_dict[index] =  cur_spells[z]
				char_spells.remove(index)
	
	#need to make sure the levels are learned in the right order
	for z in range(len(cur_spells)):
		cur_level = 1
		for y in sorted(spell_dict.keys()):
			if(spell_dict[y] == cur_spells[z]):
				spell_dict[y] = cur_spells[z] + ("|LV" + str(cur_level) if cur_level > 1 else "")
				cur_level = cur_level + 1
	text = "spellList &\n"
	for y in sorted(spell_dict.keys()):
		text = text + "                    " + str(y) + ", " + spell_dict[y] + ", &\n"
	text = text[0:-4]
	return cur_spells, text
	
def randomize_spells(chars, spells_1, spells_2, levels, starter_spells, bowie_spells,sarah_spells,kazin_spells,sorc_spells,slade_spells,karna_spells,tyrin_spells,taya_spells,frayja_spells,sheela_spells,chaz_spells):
	#make shallow copies of the lists in case we have to start over
	spells_1c = spells_1[:]
	spells_2c = spells_2[:]
	bowie_spellsc = bowie_spells[:]
	sarah_spellsc = sarah_spells[:]
	kazin_spellsc = kazin_spells[:]
	slade_spellsc = slade_spells[:]
	karna_spellsc = karna_spells[:]
	tyrin_spellsc = tyrin_spells[:]
	taya_spellsc = taya_spells[:]
	frayja_spellsc = frayja_spells[:]
	sheela_spellsc = sheela_spells[:]
	chaz_spellsc = chaz_spells[:]
	args = [chars, spells_1c, spells_2c, levels, starter_spells, bowie_spellsc,sarah_spellsc,kazin_spellsc,sorc_spells,slade_spellsc,karna_spellsc,tyrin_spellsc,taya_spellsc,frayja_spellsc,sheela_spellsc,chaz_spellsc]
	try:
		# output = ""
		for x in range(len(chars)):
			cur_char = chars[x]
			match cur_char:
				case "BOWIE":
					spells,text = generate_text(x, starter_spells, bowie_spells, levels, spells_1, spells_2, 1, 1, False)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats00.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats00.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Bowie now learns {text}\n"
				case "SARAH":
					spells,text = generate_text(x, starter_spells, sarah_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats01.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats01.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Sarah now learns {text}\n"
				case "KAZIN":
					spells1,text_1 = generate_text(x, starter_spells, kazin_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats04.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats04.asm", 'w')
					f.write(file)
					f.close()
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					index1 = file.find("dc.b CLASS_SORC_1,")
					index2 = file.find("\n", index1)
					file = file[0:index1] + "dc.b CLASS_SORC_1, SPELL_" + base_spell + file[index2:]
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Kazin now learns {text_1}\n"
					# output = output + f"Sorc Kazin now learns {text_2}\n"
				case "SLADE":
					spells,text = generate_text(x, starter_spells, slade_spells, levels, spells_1, spells_2, 0, 2, False)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats05.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats05.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Slade now learns {text}\n"
				case "KARNA":
					spells,text = generate_text(x, starter_spells, karna_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats15.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats15.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Karna now learns {text}\n"
				case "TYRIN":
					spells1,text_1 = generate_text(x, starter_spells, tyrin_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats17.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats17.asm", 'w')
					f.write(file)
					f.close()
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					index1 = file.find("dc.b CLASS_SORC_2,")
					index2 = file.find("\n", index1)
					file = file[0:index1] + "dc.b CLASS_SORC_2, SPELL_" + base_spell + file[index2:]
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Tyrin now learns {text_1}\n"
					# output = output + f"Sorc Tyrin now learns {text_2}\n"
				case "TAYA":
					spells1,text_1 = generate_text(x, starter_spells, taya_spells, levels, spells_1, spells_2, 0, 4, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats21.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats21.asm", 'w')
					f.write(file)
					f.close()
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					index1 = file.find("dc.b CLASS_SORC_3,")
					index2 = file.find("\n", index1)
					file = file[0:index1] + "dc.b CLASS_SORC_3, SPELL_" + base_spell + file[index2:]
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Taya now learns {text_1}\n"
					# output = output + f"Sorc Taya now learns {text_2}\n"
				case "FRAYJA":
					spells,text = generate_text(x, starter_spells, frayja_spells, levels, spells_1, spells_2, 1, 3, True)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats22.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats22.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Frayja now learns {text}\n"
				case "SHEELA":
					spells,text = generate_text(x, starter_spells, sheela_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats25.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats25.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Sheela now learns {text}\n"
				case "CHAZ":
					spells1,text_1 = generate_text(x, starter_spells, chaz_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats27.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open(loc + "\\data\\stats\\allies\\stats\\allystats27.asm", 'w')
					f.write(file)
					f.close()
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					index1 = file.find("dc.b CLASS_SORC_4,")
					index2 = file.find("\n", index1)
					file = file[0:index1] + "dc.b CLASS_SORC_4, SPELL_" + base_spell + file[index2:]
					f = open(loc + "\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					# output = output + f"Chaz now learns {text_1}\n"
					# output = output + f"Sorc Chaz now learns {text_2}\n"
		# print(output)
	except Exception as e:
		print(str(e) +  " Trying again.")
		randomize_spells(*args)
		
def randomize_growths(ally_num):
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'r')
	file = f.read()
	f.close()
	splits = file.splitlines(True)
	file = ""
	growths = ["LINEAR", "EARLY", "MIDDLE", "LATE", "EARLYANDLATE"]
	for x in splits:
		if("LINEAR" in x or "EARLY" in x or "MIDDLE" in x or "LATE" in x or "EARLYANDLATE" in x):
			cur_growth = random.choice(growths)
			x = x[0:x.rfind(",")+2] + cur_growth + "\n"
		file += x
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'w')
	f.write(file)
	f.close()
	
def randomize_stats(ally_num, pos_change, neg_change):
	pos_change = (pos_change+100)/100.0
	neg_change = (100-neg_change)/100.0
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'r')
	file = f.read()
	f.close()
	splits = file.splitlines(True)
	file = ""
	growths = ["LINEAR", "EARLY", "MIDDLE", "LATE", "EARLYANDLATE"]
	for x in splits:
		if("LINEAR" in x or "EARLY" in x or "MIDDLE" in x or "LATE" in x or "EARLYANDLATE" in x):
			cur_growth_base = random.uniform(neg_change, pos_change)
			cur_growth_max = random.uniform(neg_change, pos_change)
			index1 = x.find(",")
			index2 = x.rfind(",")
			base = int(int(x[index1-2:index1].lstrip().strip())*cur_growth_base+0.5)
			max = int(int(x[index1+1:index2].lstrip().strip())*cur_growth_max+0.5)
			if(base > max):
				max = base
			if(base < 1):
				base = 1
			new = x[0:index1-2]
			if(x[index1-2] == " "):
				new += " "
			new += str(base) + ", " + str(max) + x[index2:]
			x = new
		file += x
	f = open(loc + "\\data\\stats\\allies\\stats\\allystats" + (str(ally_num) if ally_num > 9 else ("0" + str(ally_num))) +".asm", 'w')
	f.write(file)
	f.close()

orig_values = {\
"BOWIE" : 0,"SARAH" : 1,"CHESTER" : 2,"JAHA" : 3,"KAZIN" : 4,"SLADE" : 5,"KIWI" : 6,"PETER" : 7,"MAY" : 8,"GERHALT" : 9,"LUKE" : 10,\
"ROHDE" : 11,"RICK" : 12,"ELRIC" : 13,"ERIC" : 14,"KARNA" : 15,"RANDOLF" : 16,"TYRIN" : 17,"JANET" : 18,"HIGINS" : 19,"SKREECH" : 20,\
"TAYA" : 21,"FRAYJA" : 22,"JARO" : 23,"GYAN" : 24,"SHEELA" : 25,"ZYNK" : 26,"CHAZ" : 27,"LEMON" : 28, "CLAUDE" : 29}
r_orig_values = {v:k for k,v in orig_values.items()}

def determine_swap_list(allow_depromo, allow_rand_promo, promo_level, max_level):
	promo_level = int(promo_level)
	max_level = int(max_level)
	f = open(loc + "\\sf2enums.asm", 'r')
	file1 = f.read()
	f.close()
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm", 'r')
	file2 = f.read()
	f.close()
	valid_promos = {"SDMN" : ("HERO"), "KNTE" : ("PLDN", "PGNT"), "PRST" : ("VICR", "MMNK"), "WARR" : ("GLDT", "BRN"), "MAGE_1" : ("WIZ", "SORC_1"), \
	"MAGE_2" : ("WIZ", "SORC_2"), "MAGE_3" : ("WIZ", "SORC_3"), "MAGE_4" : ("WIZ", "SORC_4"), "ACHR" : ("SNIP", "BRGN"), "BDMN" : ("BDBT"), \
	"WFMN" : ("WFBR"), "RNGR" : ("BWNT"), "PHNK" : ("PHNX"), "THIF" : ("NINJ"), "TORT" : ("MNST"), "DRD" : ("RBT"), "CNST":("GLM"), "RWAR":("RDBN")}
	valid_classes = []
	reverse_valid_promos = {}
	for (k,v) in valid_promos.items():
		valid_classes.append(k)
		
		if(type(v) is tuple):
			valid_classes.extend(v)
			for x in v:
				reverse_valid_promos[x] = k
		else:
			valid_classes.append(v)
			reverse_valid_promos[v] = k
	chars_m = []
	chars_b = {}
	chars_bp = {}
	chars_pb = {}
	chars_p = {}
	for x in range(30):
		cur_char = re.search("ALLY_[A-Z]*: equ " + str(x), file1).group()[5:-1*(6+len(str(x)))]
		chars_m.append(cur_char)
		new_class = re.search("startClass [A-Z]*_?\\d?\\s*; \\d*: " + cur_char, file2).group()
		new_class = new_class[11:new_class.find("         ")]
		new_level = re.search(cur_char + "\n                startLevel \\d*", file2).group()
		new_level = int(new_level[new_level.find("startLevel")+11:])
		if(new_class in reverse_valid_promos):
			if(new_level+promo_level <= max_level):
				chars_pb[cur_char] = x
			else:
				chars_p[cur_char] = x
		elif(new_level >= promo_level):
			chars_bp[cur_char] = x
		else:
			chars_b[cur_char] = x
	#shuffle within guaranteed swap classes
	tempa = list(chars_b.values())
	random.shuffle(tempa)
	tempb = list(chars_b.keys())
	for x in range(len(tempb)):
		chars_b[tempb[x]] = tempa[x]
		
	tempa = list(chars_bp.values())
	random.shuffle(tempa)
	tempb = list(chars_bp.keys())
	for x in range(len(tempb)):
		chars_bp[tempb[x]] = tempa[x]
		
	tempa = list(chars_pb.values())
	random.shuffle(tempa)
	tempb = list(chars_pb.keys())
	for x in range(len(tempb)):
		chars_pb[tempb[x]] = tempa[x]
		
	tempa = list(chars_p.values())
	random.shuffle(tempa)
	tempb = list(chars_p.keys())
	for x in range(len(tempb)):
		chars_p[tempb[x]] = tempa[x]
	
	chars_swap = {}
	chars_sel = list(chars_m)
	while(len(chars_sel) > 0):
		cur_char = random.choice(chars_sel)
		chars_sel.remove(cur_char)
		swaps = []
		#below promo threshold
		if(cur_char in chars_b):
			orig_index = chars_b.pop(cur_char)
			orig_list = chars_b
			#these chars already start unpromoted, so they are automatically ok regardless of preferences
			swaps += list(chars_b) + list(chars_bp)
			#the promo sets are only ok if the promo char can depromote and we are allowing promotions
			if(allow_depromo and allow_rand_promo):
				swaps += list(chars_pb) + list(chars_p)
		#unpromoted but above promo threshold
		elif(cur_char in chars_bp):
			orig_index = chars_bp.pop(cur_char)
			orig_list = chars_bp
			#anyone who isn't promoted or under the max level cap is in by default
			swaps += list(chars_b) + list(chars_bp) + list(chars_pb)
			#these chars are over the max level threshold, so we have to allow this char to be promoted
			if(allow_rand_promo):
				swaps += list(chars_p)
		#promoted but under level cap
		elif(cur_char in chars_pb):
			orig_index = chars_pb.pop(cur_char)
			orig_list = chars_pb
			#anyone who is promoted or over promo threshold is in by default
			swaps +=  list(chars_bp) + list(chars_pb) + list(chars_p)
			#swapping with these chars necessitates depromotion, but the reverse is not true
			if(allow_depromo):
				swaps += list(chars_b)
		#promoted and over the level cap
		else:
			orig_index = chars_p.pop(cur_char)
			orig_list = chars_p
			#anyone who is promoted is in by default
			swaps +=  list(chars_pb) + list(chars_p)
			#swapping with these chars necessitates depromotion and mandatory promotion
			if(allow_depromo and allow_depromo):
				swaps += list(chars_b) + list(chars_bp)
		#no one elligible to swap with
		if(len(swaps) == 0):
			chars_swap[cur_char] = orig_index
		else:
			#pick a random choice from elligible candidates
			swap_char = random.choice(swaps)
			#determine which promo class the new char is in and remove it while saving the index
			if(swap_char in chars_b):
				new_index = chars_b.pop(swap_char)
			elif(swap_char in chars_bp):
				new_index = chars_bp.pop(swap_char)
			elif(swap_char in chars_pb):
				new_index = chars_pb.pop(swap_char)
			else:
				new_index = chars_p.pop(swap_char)
			chars_swap[cur_char] = new_index
			orig_list[swap_char] = orig_index
	return chars_m, chars_swap

def adjust_levels(treat_promo_as, new_promo_level, orig_values):
	f = open(loc + "\\data\\stats\\allies\\allystartdefs.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\stats\\allies\\growthcurves.asm", 'r')
	file2 = f.read()
	f.close()
	split = file2.split("dc.w")
	growth_dict = {}
	cur_growth = ""
	for x in split:
		if("Linear" in x):
			cur_growth = "LINEAR"
			growth_dict[cur_growth] = []
			continue
		growth_dict[cur_growth].append((x[1:x.find(",")], x[x.find(",")+2 : x.find(";")].strip()))
		if("Early and late" in x):
			cur_growth = "EARLYANDLATE"
			growth_dict[cur_growth] = []
		elif("Early" in x):
			cur_growth = "EARLY"
			growth_dict[cur_growth] = []
		elif("Middle" in x):
			cur_growth = "MIDDLE"
			growth_dict[cur_growth] = []
		elif("Late" in x):
			cur_growth = "LATE"
			growth_dict[cur_growth] = []
	for x in iter(orig_values):
		new_class = re.search("startClass [A-Z]*_?\\d?\\s*; \\d*: " + x, file).group()
		new_class = new_class[11:new_class.find("         ")]
		class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
		class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
		class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
		r_class_dict = {}
		for k, v in class_dict.items():
			for y in v:
				r_class_dict[y] = k
		if(new_class in class_dict["BASE"]):
			continue
		adjust_promo_stats(orig_values[x], new_class, int(new_promo_level),growth_dict)
	f = open(loc + "\\sf2enums.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\sf2enums.asm", 'w')
	file = file[0:file.find("CHAR_CLASS_EXTRALEVEL")] + "CHAR_CLASS_EXTRALEVEL: equ " + str(treat_promo_as) + file[file.find("\n", file.find("CHAR_CLASS_EXTRALEVEL")):]
	file = file[0:file.find("CHAR_LEVELCAP_BASE")] + "CHAR_LEVELCAP_BASE: equ " + str(new_promo_level) + file[file.find("\n", file.find("CHAR_LEVELCAP_BASE")):]
	f.write(file)
	f.close()

def randomize_promo_items(char_list, cur_items):
	promo_item_dict = {"VIGOR_BALL" : ["SARAH", "Karna", "FRAYJA", "SHEELA"], "WARRIORS_PRIDE" : ["JAHA", "RANDOLF", "GYAN"], \
	"SECRET_BOOK" : ["KAZIN", "TYRIN", "TAYA", "CHAZ"], "PEGASUS_WING" : ["CHESTER", "RICK", "ERIC", "HIGINS", "JARO"], \
	"SILVER_TANK" : ["ROHDE", "ELRIC", "JANET"]}
	promo_item_dict_r = {}
	for x in promo_item_dict.keys():
		for y in promo_item_dict[x]:
			promo_item_dict_r[y] = x
	item_nums = [0,0,0,0,0]
	for x in [y for y in range(0, 11)]+[y for y in range(12,19)]:
		char = char_list[x]
		if(char in promo_item_dict_r):
			match promo_item_dict_r[char]:
				case "VIGOR_BALL":
					item_nums[0] = item_nums[0]+1
				case "WARRIORS_PRIDE":
					item_nums[1] = item_nums[1]+1
				case "SECRET_BOOK":
					item_nums[2] = item_nums[2]+1
				case "PEGASUS_WING":
					item_nums[3] = item_nums[3]+1
				case "SILVER_TANK":
					item_nums[4] = item_nums[4]+1
	rep_list = ["VIGOR_BALL" for x in range(item_nums[0])]
	rep_list = rep_list + ["WARRIORS_PRIDE" for x in range(item_nums[1])]
	rep_list = rep_list + ["SECRET_BOOK" for x in range(item_nums[2])]
	rep_list = rep_list + ["PEGASUS_WING" for x in range(item_nums[3])]
	rep_list = rep_list + ["SILVER_TANK" for x in range(item_nums[4])]

	f = open(loc + "\\data\\maps\\entries\\map07\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map07\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Warrior's Pride with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[0], temp_item))
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map46\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map46\\8-other-items.asm", 'w')
	f.write(file.replace(cur_items[0], temp_item))
	cur_items[0] = temp_item
	f.close()
	
	f = open(loc + "\\data\\maps\\entries\\map23\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map23\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Secret Book with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[2], temp_item))
	cur_items[2] = temp_item
	f.close()
	
	f = open(loc + "\\data\\maps\\entries\\map23\\7-chest-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map23\\7-chest-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Vigor Ball 1 with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[3], temp_item))
	cur_items[3] = temp_item
	f.close()
	
	f = open(loc + "\\data\\maps\\entries\\map36\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map36\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Pegasus Wing with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[5], temp_item))
	cur_items[5] = temp_item
	f.close()
	
	f = open(loc + "\\data\\maps\\entries\\map67\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map67\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Vigor Ball 2 with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[4], temp_item))
	cur_items[4] = temp_item
	f.close()
	
	f = open(loc + "\\data\\maps\\entries\\map48\\7-chest-items.asm", 'r')
	file = f.read()
	f.close()
	f = open(loc + "\\data\\maps\\entries\\map48\\7-chest-items.asm", 'w')
	temp_item = random.choice(rep_list)
	# print("Swapped Silver Tank with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace(cur_items[1], temp_item))
	cur_items[1] = temp_item
	f.close()