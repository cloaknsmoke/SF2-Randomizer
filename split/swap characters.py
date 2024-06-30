from pathlib import Path
import random
import re

def swap_ALLY_r(p, a, b):
	for x in p.iterdir():
		if(x.is_dir()):
			swap_ALLY_r(x,a,b)
		elif(x.suffix == ".asm" and "sf2enums" not in x.name):
			try:
				f = open(x, 'r')
				file = f.read()
				f.close()
				if(a in file or b in file):
					file = file.replace(a, "{char1}").replace(b,"{char2}")
					file = file.replace("{char1}", b).replace("{char2}", a)
					f = open(x, 'w')
					f.write(file)
					f.close()
			except UnicodeDecodeError as e:
				continue

def replace_npc_rohde_sprite():
	f = open("..\\disasm\\sf2enums.asm", 'r')
	file1 = f.read()
	f.close()
	who_is_rohde = re.search("ALLY_[A-Z]*: equ 11", file1).group()[5:-8]
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm", 'r')
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
	new_sprite_index = file1[file1.find(mapsprite):file1.find("\n", file1.find(mapsprite))]
	new_sprite_index = new_sprite_index[new_sprite_index.find("equ")+5:new_sprite_index.find("equ")+7].strip()
	npc_rohde_index = file1.find("MAPSPRITE_NPC_ROHDE: equ $")+26
	file1 = file1[0:npc_rohde_index] + new_sprite_index + file1[file1.find("\n", npc_rohde_index):]
	f = open("..\\disasm\\sf2enums.asm", 'w')
	f.write(file1)
	f.close()

def replace_spinning_elric():
	f = open("..\\disasm\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_elric = re.search("ALLY_[A-Z]*: equ 13", file1).group()[5:-8]
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm")
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
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	harpie_battle = file3[file3.find("HARPIES_POND"):file3.find("TERMINATOR_WORD",file3.find("HARPIES_POND"))]
	harpie_rep = harpie_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", harpie_battle).group(), "mapsprite " + who_is_elric + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(harpie_battle, harpie_rep)
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()

def replace_knocked_out_luke():
	f = open("..\\disasm\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_luke = re.search("ALLY_[A-Z]*: equ 10", file1).group()[5:-8]
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm")
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
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	polca_battle = file3[file3.find("POLCA_VILLAGE"):file3.find("TERMINATOR_WORD",file3.find("POLCA_VILLAGE"))]
	polca_rep = polca_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", polca_battle).group(), "mapsprite " + who_is_luke + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(polca_battle, polca_rep)
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()
	
def replace_knocked_out_higins():
	f = open("..\\disasm\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_higins = re.search("ALLY_[A-Z]*: equ 19", file1).group()[5:-8]
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm")
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
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'r')
	file3 = f.read()
	f.close()
	np_battle = file3[file3.find("OUTSIDE_KETTO"):file3.find("TERMINATOR_WORD",file3.find("OUTSIDE_KETTO"))]
	np_rep = np_battle.replace(re.search("mapsprite [A-Z]*_[A-Z]*\n", np_battle).group(), "mapsprite " + who_is_higins + "_" + r_class_dict[new_class] + "\n")
	file3 = file3.replace(np_battle, np_rep)
	f = open("..\\disasm\\data\\battles\\global\\battleneutralentities.asm", 'w')
	f.write(file3)
	f.close()

def replace_enemy_jaro():
	f = open("..\\disasm\\sf2enums.asm")
	file1 = f.read()
	f.close()
	who_is_jaro = re.search("ALLY_[A-Z]*: equ 23", file1).group()[5:-8]
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm")
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
	f = open("..\\disasm\\data\\stats\\enemies\\enemymapsprites.asm", 'r')
	file3 = f.read()
	f.close()
	file3 = file3.replace("JARO_SPECIAL", who_is_jaro + r_class_dict[new_class])
	f = open("..\\disasm\\data\\stats\\enemies\\enemymapsprites.asm", 'w')
	f.write(file3)
	f.close()
	f = open("..\\disasm\\data\\stats\\enemies\\enemynames-capitalized.asm", 'r')
	file3 = f.read()
	f.close()
	f = open("..\\disasm\\data\\stats\\enemies\\enemynames-capitalized.asm", 'w')
	f.write(file3.replace("Jaro", who_is_jaro.capitalize()))
	f.close()

def remove_redundant_classes():
	class_dict = {"BASE" : ("SDMN", "KNTE", "WARR", "MAGE_1", "MAGE_2", "MAGE_3", "MAGE_4", "PRST", "ACHR", "BDMN", "WFMN", "RNGR", "PHNK", "THIF", "TORT", "RWAR", "DRD", "CNST")}
	class_dict["PROMO"] = ("HERO", "PLDN", "GLDT", "WIZ", "WIZ", "WIZ", "WIZ", "VICR", "SNIP", "BDBT", "WFBR", "BWNT", "PHNX", "NINJ", "MNST", "RBT", "GLM")
	class_dict["SPECIAL"] = ("PGNT", "BRN", "SORC_1", "SORC_2", "SORC_3", "SORC_4", "MMNK", "BRGN", "RDBN")
	r_class_dict = {}
	for v,k in class_dict.items():
		for x in k:
			r_class_dict[x] = v
	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm")
	file = f.read()
	f.close()
	splits = file.split("startClass")
	for x in range(2,32):
		cur_class = re.search(" [A-Z]*_?\\d? ", splits[x]).group()[1:-1]
		if(r_class_dict[cur_class] == "BASE"):
			continue
		num = int(re.search("; [0-9]*:", splits[x]).group()[2:-1])
		f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats" + (str(num) if num > 9 else ("0" + str(num))) +".asm", 'r')
		file = f.read()
		f.close()
		splits2 = file.split("forClass")
		base_spells = ""
		class_data = ""
		for y in splits2:
			if("AllyStats" in y):
				continue
			if("spellList" in y and base_spells == ""):
				base_spells = y[y.find("spellList"):].strip()
			if(cur_class in y):
				class_data = y
		if("useFirstSpellList" in class_data):
			class_data = class_data.replace("useFirstSpellList", base_spells)
		file = file[0:file.index("forClass")+9] + class_data.strip()
		f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats" + (str(num) if num > 9 else ("0" + str(num))) +".asm", 'w')
		f.write(file)
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

def swap_characters(char_a, char_b, char_a_name, char_b_name, orig_a_num, orig_b_num, depromote, rand_promo):
	p = Path("..\\disasm")
	f = open("..\\disasm\\sf2enums.asm", 'r')
	file = f.read()
	f.close()
	char_a_value = file.find("ALLY_"+char_a)
	char_b_value = file.find("ALLY_"+char_b)
	char_a_value = file[char_a_value+len(char_a)+11:file.find("\n", char_a_value)]
	char_b_value = file[char_b_value+len(char_b)+11:file.find("\n", char_b_value)]
	base_a = "_BASE" if ("BOWIE" in char_a or "SLADE" in char_a or "KIWI" in char_a or "PETER" in char_a or "GERHALT" in char_a or "CLAUDE" in char_a) else ""
	base_b = "_BASE" if ("BOWIE" in char_b or "SLADE" in char_b or "KIWI" in char_b or "PETER" in char_b or "GERHALT" in char_b or "CLAUDE" in char_b) else ""
	file = file.replace("ALLY_"+char_a + ": equ " + char_a_value, "{char1a}")
	file = file.replace("ALLY_"+char_b + ": equ " + char_b_value, "{char2a}")
	file = file.replace("PORTRAIT_" + char_a + base_a + ": equ " + char_a_value, "{char1b}")
	file = file.replace("PORTRAIT_" + char_b + base_b + ": equ " + char_b_value, "{char2b}")
	file = file.replace("{char1a}", "ALLY_"+char_b + ": equ " + char_a_value)
	file = file.replace("{char2a}", "ALLY_"+char_a + ": equ " + char_b_value)
	file = file.replace("{char1b}", "PORTRAIT_" + char_b + base_b + ": equ " + char_a_value)
	file = file.replace("{char2b}", "PORTRAIT_" + char_a + base_a + ": equ " + char_b_value)
	f = open("..\\disasm\\sf2enums.asm", 'w')
	f.write(file)
	f.close()



	swap_ALLY_r(Path("..\\disasm"), "ALLY_"+char_a,"ALLY_"+char_b)
			
	f = open("..\\disasm\\data\\stats\\allies\\allydialogproperties-standard.asm", 'r')
	file = f.read()
	f.close()
	loc_a = file.find("; " + str(orig_a_num) + ": ")
	line_e = file.find("\n", loc_a)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_a = file[loc_a:line_e]
	file = file.replace(text_a, "{char1}")
	loc_b = file.find("; " + str(orig_b_num) + ": ")
	line_e = file.find("\n", loc_b)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_b = file[loc_b:line_e]
	file = file.replace(text_b, "{char2}")
	file = file.replace("{char1}", text_b).replace("{char2}", text_a)
	f = open("..\\disasm\\data\\stats\\allies\\allydialogproperties-standard.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\stats\\allies\\stats\\entries.asm", 'r')
	file = f.read()
	f.close()
	loc_a = file.find("AllyStats" + (str(orig_a_num) if orig_a_num > 9 else ("0" + str(orig_a_num))))
	line_e = file.find("\n", loc_a)
	text_a = file[loc_a:line_e]
	file = file.replace(text_a, "{char1}")
	loc_b = file.find("AllyStats" + (str(orig_b_num) if orig_b_num > 9 else ("0" + str(orig_b_num))))
	line_e = file.find("\n", loc_b)
	text_b = file[loc_b:line_e]
	file = file.replace(text_b, "{char2}")
	file = file.replace("{char1}", text_b).replace("{char2}", text_a)
	f = open("..\\disasm\\data\\stats\\allies\\stats\\entries.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\stats\\allies\\allybattlesprites.asm", 'r')
	file = f.read()
	f.close()
	loc_a = file.find("; " + str(orig_a_num) + ": ")
	line_e = file.find("\n", loc_a)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_a = file[loc_a:line_e]
	file = file.replace(text_a, "{char1}")
	loc_b = file.find("; " + str(orig_b_num) + ": ")
	line_e = file.find("\n", loc_b)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_b = file[loc_b:line_e]
	file = file.replace(text_b, "{char2}")
	file = file.replace("{char1}", text_b).replace("{char2}", text_a)
	f = open("..\\disasm\\data\\stats\\allies\\allybattlesprites.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\stats\\allies\\allymapsprites-standard.asm", 'r')
	file = f.read()
	f.close()
	loc_a = file.find("; " + str(orig_a_num) + ": ")
	line_e = file.find("\n", loc_a)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_a = file[loc_a:line_e]
	file = file.replace(text_a, "{char1}")
	loc_b = file.find("; " + str(orig_b_num) + ": ")
	line_e = file.find("\n", loc_b)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_b = file[loc_b:line_e]
	file = file.replace(text_b, "{char2}")
	file = file.replace("{char1}", text_b).replace("{char2}", text_a)
	f = open("..\\disasm\\data\\stats\\allies\\allymapsprites-standard.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\stats\\allies\\allynames-capitalized.asm", 'r')
	file = f.read()
	f.close()
	file = file.replace(char_a_name, "{char1}").replace(char_b_name, "{char2}")
	file = file.replace("{char1}", char_b_name).replace("{char2}", char_a_name)
	f = open("..\\disasm\\data\\stats\\allies\\allynames-capitalized.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm", 'r')
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
	loc_a = file.find("; " + str(orig_a_num) + ": ")
	loc_a = file.rfind("\n", 0,loc_a)+1
	line_e = file.find("\n", loc_a)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_a = file[loc_a:line_e]
	class_a = text_a[text_a.find("startClass")+11:text_a.find("startClass")+15]
	if(class_a not in valid_classes):
		if("MAGE" in class_a or "SORC" in class_a):
			class_a = text_a[text_a.find("startClass")+11:text_a.find("startClass")+17]
		else:
			class_a = text_a[text_a.find("startClass")+11:text_a.find("startClass")+14]
	level_a = text_a[text_a.find("startLevel")+11:text_a.find("startLevel")+13]
	if(not level_a.isdecimal()):
		level_a = text_a[text_a.find("startLevel")+11:text_a.find("startLevel")+12]
	item_1a_in = text_a.find("&")+1
	item_1a = text_a[item_1a_in:text_a.find("&", item_1a_in)].strip()
	item_1a = item_1a.replace("|EQUIPPED","").replace(",", "")
	item_2a_in = text_a.find("&", item_1a_in)+1
	item_2a = text_a[item_2a_in:text_a.find("&", item_2a_in)].strip()
	item_2a = item_2a.replace("|EQUIPPED","").replace(",", "")
	item_3a_in = text_a.find("&", item_2a_in)+1
	item_3a = text_a[item_3a_in:text_a.find("&", item_3a_in)].strip()
	item_3a = item_3a.replace("|EQUIPPED","").replace(",", "")
	item_4a_in = text_a.find("&", item_3a_in)+1
	item_4a = text_a[item_4a_in:].strip()
	item_4a = item_4a.replace("|EQUIPPED","").replace(",", "")
	file = file.replace(text_a, "{char1}")

	loc_b = file.find("; " + str(orig_b_num) + ": ")
	loc_b = file.rfind("\n", 0,loc_b)+1
	line_e = file.find("\n", loc_b)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	line_e = file.find("\n", line_e+1)
	text_b = file[loc_b:line_e]
	class_b = text_b[text_b.find("startClass")+11:text_b.find("startClass")+15]
	if(class_b not in valid_classes):
		if("MAGE" in class_b or "SORC" in class_b):
			class_b = text_b[text_b.find("startClass")+11:text_b.find("startClass")+17]
		else:
			class_b = text_b[text_b.find("startClass")+11:text_b.find("startClass")+14]
	level_b = text_b[text_b.find("startLevel")+11:text_b.find("startLevel")+13]
	if(not level_b.isdecimal()):
		level_b = text_b[text_b.find("startLevel")+11:text_b.find("startLevel")+12]
	item_1b_in = text_b.find("&")+1
	item_1b = text_b[item_1b_in:text_b.find("&", item_1b_in)].strip()
	item_1b = item_1b.replace("|EQUIPPED","").replace(",", "")
	item_2b_in = text_b.find("&", item_1b_in)+1
	item_2b = text_b[item_2b_in:text_b.find("&", item_2b_in)].strip()
	item_2b = item_2b.replace("|EQUIPPED","").replace(",", "")
	item_3b_in = text_b.find("&", item_2b_in)+1
	item_3b = text_b[item_3b_in:text_b.find("&", item_3b_in)].strip()
	item_3b = item_3b.replace("|EQUIPPED","").replace(",", "")
	item_4b_in = text_b.find("&", item_3b_in)+1
	item_4b = text_b[item_4b_in:].strip()
	item_4b = item_4b.replace("|EQUIPPED","").replace(",", "")
	file = file.replace(text_b, "{char2}")
	match char_a_name:
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
	new_class_a = determine_new_class(char_a, class_a, class_b, valid_promos, reverse_valid_promos, wiz_flag, depromote, rand_promo)
	match char_b_name:
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
	new_class_b = determine_new_class(char_b, class_b, class_a, valid_promos, reverse_valid_promos, wiz_flag, depromote, rand_promo)
	if(new_class_a in valid_promos and class_b in reverse_valid_promos):
		level_b = str(int(level_b) + 20)
	if(new_class_a in reverse_valid_promos and class_b in valid_promos):
		level_b = str(int(level_b) - 20)
	if(new_class_b in valid_promos and class_a in reverse_valid_promos):
		level_a = str(int(level_a) + 20)
	if(new_class_b in reverse_valid_promos and class_a in valid_promos):
		level_a = str(int(level_b) - 20)
	items_a = [item_1a, item_2a, item_3a, item_4a]
	new_items(items_a, new_class_a, new_class_a in reverse_valid_promos, int(level_b), valid_weapon_level_ranges, valid_equips)
	items_b = [item_1b, item_2b, item_3b, item_4b]
	new_items(items_b, new_class_b, new_class_b in reverse_valid_promos, int(level_a), valid_weapon_level_ranges, valid_equips)
	swap_to_b = []
	for x in items_a:
		if(x not in valid_weapon_level_ranges):
			swap_to_b.append(x)
			items_a.remove(x)
			items_a.append("NOTHING")
	swap_to_a = []
	for x in items_b:
		if(x not in valid_weapon_level_ranges):
			swap_to_a.append(x)
			items_b.remove(x)
			items_b.append("NOTHING")
			
	for x in swap_to_a:
		items_a.remove("NOTHING")
		items_a.append(x)
	for x in swap_to_b:
		items_b.remove("NOTHING")
		items_b.append(x)
	text_a = "                startClass "+ new_class_a + "         ; "+str(orig_a_num)+": "+char_a + "\n"+\
	"                startLevel "+level_b+"\n"+\
	"                startItems &\n"+\
	"                    "+items_a[0]+("|EQUIPPED" if items_a[0] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_a[1]+("|EQUIPPED" if items_a[1] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_a[2]+("|EQUIPPED" if items_a[2] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_a[3]+("|EQUIPPED" if items_a[3] in valid_weapon_level_ranges else "")+"\n"
	text_b = "                startClass "+ new_class_b + "         ; "+str(orig_b_num)+": "+char_b + "\n"+\
	"                startLevel "+level_a+"\n"+\
	"                startItems &\n"+\
	"                    "+items_b[0]+("|EQUIPPED" if items_b[0] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_b[1]+("|EQUIPPED" if items_b[1] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_b[2]+("|EQUIPPED" if items_b[2] in valid_weapon_level_ranges else "")+", &\n"+\
	"                    "+items_b[3]+("|EQUIPPED" if items_b[3] in valid_weapon_level_ranges else "")+"\n"
	file = file.replace("{char1}", text_b).replace("{char2}", text_a)

	f = open("..\\disasm\\data\\stats\\allies\\allystartdefs.asm", 'w')
	f.write(file)
	f.close()

	f = open("..\\disasm\\data\\graphics\\portraits\\entries.asm", 'r')
	file = f.read()
	f.close()
	file = file.replace("dc.l Portrait" + ("0" if orig_a_num < 10 else "") + str(orig_a_num), "{char1}")
	file = file.replace("dc.l Portrait" + ("0" if orig_b_num < 10 else "")+str(orig_b_num), "{char2}")
	file = file.replace("{char1}", "dc.l Portrait" + ("0" if orig_b_num < 10 else "")+str(orig_b_num))
	file = file.replace("{char2}", "dc.l Portrait" + ("0" if orig_a_num < 10 else "")+str(orig_a_num))
	f = open("..\\disasm\\data\\graphics\\portraits\\entries.asm", 'w')
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
	
def randomize_spells(silent_output, chars, spells_1, spells_2, levels, starter_spells, bowie_spells,sarah_spells,kazin_spells,sorc_spells,slade_spells,karna_spells,tyrin_spells,taya_spells,frayja_spells,sheela_spells,chaz_spells):
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
	args = [silent_output, chars, spells_1c, spells_2c, levels, starter_spells, bowie_spellsc,sarah_spellsc,kazin_spellsc,sorc_spells,slade_spellsc,karna_spellsc,tyrin_spellsc,taya_spellsc,frayja_spellsc,sheela_spellsc,chaz_spellsc]
	try:
		output = ""
		for x in range(len(chars)):
			cur_char = chars[x]
			match cur_char:
				case "BOWIE":
					spells,text = generate_text(x, starter_spells, bowie_spells, levels, spells_1, spells_2, 1, 1, False)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats00.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats00.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Bowie now learns {text}\n"
				case "SARAH":
					spells,text = generate_text(x, starter_spells, sarah_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats01.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats01.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Sarah now learns {text}\n"
				case "KAZIN":
					spells1,text_1 = generate_text(x, starter_spells, kazin_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats04.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats04.asm", 'w')
					f.write(file)
					f.close()
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					# print(text_2)
					file = file.replace("dc.b CLASS_SORC_1, SPELL_DAO", "dc.b CLASS_SORC_1, SPELL_" + base_spell)
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Kazin now learns {text_1}\n"
					output = output + f"Sorc Kazin now learns {text_2}\n"
				case "SLADE":
					spells,text = generate_text(x, starter_spells, slade_spells, levels, spells_1, spells_2, 0, 2, False)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats05.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats05.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Slade now learns {text}\n"
				case "KARNA":
					spells,text = generate_text(x, starter_spells, karna_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats15.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats15.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Karna now learns {text}\n"
				case "TYRIN":
					spells1,text_1 = generate_text(x, starter_spells, tyrin_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats17.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats17.asm", 'w')
					f.write(file)
					f.close()
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					# print(text_2)
					file = file.replace("dc.b CLASS_SORC_2, SPELL_DAO", "dc.b CLASS_SORC_2, SPELL_" + base_spell)
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Tyrin now learns {text_1}\n"
					output = output + f"Sorc Tyrin now learns {text_2}\n"
				case "TAYA":
					spells1,text_1 = generate_text(x, starter_spells, taya_spells, levels, spells_1, spells_2, 0, 4, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats21.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats21.asm", 'w')
					f.write(file)
					f.close()
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					# print(text_2)
					file = file.replace("dc.b CLASS_SORC_3, SPELL_DAO", "dc.b CLASS_SORC_3, SPELL_" + base_spell)
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Taya now learns {text_1}\n"
					output = output + f"Sorc Taya now learns {text_2}\n"
				case "FRAYJA":
					spells,text = generate_text(x, starter_spells, frayja_spells, levels, spells_1, spells_2, 1, 3, True)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats22.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats22.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Frayja now learns {text}\n"
				case "SHEELA":
					spells,text = generate_text(x, starter_spells, sheela_spells, levels, spells_1, spells_2, 0, 4, True)
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats25.asm", 'r')
					file = f.read()
					f.close()
					spell_start = file.find("spellList &")
					spell_end = file.rfind("&")
					spell_end = file.find("\n", spell_end+2)
					file = file[0:spell_start] + text + file[spell_end:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats25.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Sheela now learns {text}\n"
				case "CHAZ":
					spells1,text_1 = generate_text(x, starter_spells, chaz_spells, levels, spells_1, spells_2, 1, 3, True)
					spells2,text_2 = generate_text(x, starter_spells, sorc_spells[:], levels, spells_1, spells_2, 0, 4, False)
					text_2 = "spellList &\n                    21" + text_2[34:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats27.asm", 'r')
					file = f.read()
					f.close()
					spell_start1 = file.find("spellList &")
					spell_end2 = file.rfind("&")
					spell_end2 = file.find("\n", spell_end2+2)
					spell_start2 = file.rfind("spellList &")
					spell_end1 = file.rfind("&",0, spell_start2)
					spell_end1 = file.find("\n", spell_end1+2)
					file = file[0:spell_start1] + text_1 + file[spell_end1:spell_start2] + text_2 + file[spell_end2:]
					f = open("..\\disasm\\data\\stats\\allies\\stats\\allystats27.asm", 'w')
					f.write(file)
					f.close()
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'r')
					file = f.read()
					f.close()
					base_spell = text_2[36:text_2.find(',', 36)]
					# print(text_2)
					file = file.replace("dc.b CLASS_SORC_4, SPELL_DAO", "dc.b CLASS_SORC_4, SPELL_" + base_spell)
					f = open("..\\disasm\\data\\stats\\allies\\classes\\promotions-standard.asm", 'w')
					f.write(file)
					f.close()
					output = output + f"Chaz now learns {text_1}\n"
					output = output + f"Sorc Chaz now learns {text_2}\n"
		if(not silent_output):
			print(output)
	except Exception as e:
		if(not silent_output):
			print(str(e) +  " Trying again.")
		randomize_spells(*args)

def take_inputs():
	rand_chars = input("Randomize characters? ")
	while(rand_chars != "y" and rand_chars != "Y" and rand_chars != "n" and rand_chars != "N"):
		if(rand_chars == "help"):
			rand_chars = input("This will change where each character in the game is recruited. Their weapon and level will be on par with what the original character recruited in that position would have gotten. ")
		else:
			rand_chars = input("Invalid response. ")
	rand_chars = True if rand_chars == "y" or rand_chars == "Y" else False
	rand_depromo = input("Allow characters to depromote while randomizing? ")
	while(rand_depromo != "y" and rand_depromo != "Y" and rand_depromo != "n" and rand_depromo != "N"):
		if(rand_depromo == "help"):
			rand_depromo = input("Yes will allow characters to depromote into an approprate class that they did not have access to in the original game. Otherwise, promoted characters cannot random with anyone under level 21 in their original recruitment spot. ")
		else:
			rand_depromo = input("Invalid response. ")
	rand_depromo = True if rand_depromo == "y" or rand_depromo == "Y" else False
	rand_prepromo = input("Randomize promotion path for pre-promoted characters? ")
	while(rand_prepromo != "y" and rand_prepromo != "Y" and rand_prepromo != "n" and rand_prepromo != "N"):
		if(rand_prepromo == "help"):
			rand_prepromo = input("Yes will take any character whose final recruitment would result in them being promoted to randomly select between their two promotion options assuming they had two options. ")
		else:
			rand_prepromo = input("Invalid response. ")
	rand_prepromo = True if rand_prepromo == "y" or rand_prepromo == "Y" else False
	rand_magic = input("Randomize magic learned? ")
	while(rand_magic != "y" and rand_magic != "Y" and rand_magic != "n" and rand_magic != "N"):
		if(rand_magic == "help"):
			rand_magic = input("Any spell in the original that had at least 2 levels can become any 2-4 level spell. The whole spell-pool remains the same though, so no having 2 people learn Raijin for instance. 1 level spells are randomized amongst themselves. Yes this includes sorcerers. ")
		else:
			rand_magic = input("Invalid response. ")
	rand_magic = True if rand_magic == "y" or rand_magic == "Y" else False
	chaos_magic = input("Fully randomize learned levels? ")
	while(chaos_magic != "y" and chaos_magic != "Y" and chaos_magic != "n" and chaos_magic != "N"):
		if(chaos_magic == "help"):
			chaos_magic = input("Normally, characters will still only learn spells when they would otherwise in the base game, but this options just picks completely random levels between 1 and 52. ")
		else:
			chaos_magic = input("Invalid response. ")
	chaos_magic = True if chaos_magic == "y" or chaos_magic == "Y" else False
	rand_promo_items = input("Randomize which promo items you get? ")
	while(rand_promo_items != "y" and rand_promo_items != "Y" and rand_promo_items != "n" and rand_promo_items != "N"):
		if(rand_promo_items == "help"):
			rand_promo_items = input("Picks random promotion items to replace the existing ones. They have the same locations (except the second Vigor Ball which I moved). All items will be usable. If you random all centaurs promoted, then you won't get any Pegasus Wings. You will never get more of an item than potential characters that can use it either. ")
		else:
			rand_promo_items = input("Invalid response. ")
	rand_promo_items = True if rand_promo_items == "y" or rand_promo_items == "Y" else False
	rand_stat_growths = input("Randomize stat progression? ")
	while(rand_stat_growths != "y" and rand_stat_growths != "Y" and rand_stat_growths != "n" and rand_stat_growths != "N"):
		if(rand_stat_growths == "help"):
			rand_stat_growths = input("Randomzies the growth rate of each character between the existing growth rates of early, middle, late, early + late, and linear. The max/base stats are not affected. ")
		else:
			rand_stat_growths = input("Invalid response. ")
	rand_stat_growths = True if rand_stat_growths == "y" or rand_stat_growths == "Y" else False
	rand_stats = input("Randomize stats by up to 10% in either direction? ")
	while(rand_stats != "y" and rand_stats != "Y" and rand_stats != "n" and rand_stats != "N"):
		if(rand_stats == "help"):
			rand_stats = input("Randomizes base and max stats of each character by up to 10% in either direction. ")
		else:
			rand_stats = input("Invalid response. ")
	rand_stats = True if rand_stats == "y" or rand_stats == "Y" else False
	silent_output = input("Print the outcome to the command line? ")
	while(silent_output != "y" and silent_output != "Y" and silent_output != "n" and silent_output != "N"):
		if(silent_output == "help"):
			silent_output = input("Yes if you want to know what is getting changed to what. Otherwise, the output will be nothing to keep it a mystery. ")
		else:
			silent_output = input("Invalid response. ")
	silent_output = False if silent_output == "y" or silent_output == "Y" else True
	return {"Characters" : rand_chars, "Depromos" : rand_depromo, "Promo" : rand_prepromo, "Magic" : rand_magic, "Magic levels" : chaos_magic, "Items" : rand_promo_items, "Growths" : rand_stat_growths, "Stats" : rand_stats, "Silent" : silent_output}


config = {}
print("Answer questions with y, Y, n, N, or help.")
if(Path("config.txt").exists()):
	f = open("config.txt", 'r')
	config = eval(f.read())
	f.close()
	if("No Prompt" not in config):
		resp = input("Use saved settings? ")
		while(resp != "y" and resp != "Y" and resp != "n" and resp != "N"):
			if(resp == "help"):
				resp = input("Previous responses will be saved in config.txt. ")
			else:
				resp = input("Invalid response. ")
		if(resp == "n" or resp == "N"):
			config = take_inputs()
else:
	config = take_inputs()
f = open("config.txt", 'w')
f.write(repr(config))
f.close()

chars_m = ["BOWIE","SARAH","CHESTER","JAHA","KAZIN","SLADE","KIWI","PETER","MAY","GERHALT","LUKE","ROHDE","RICK","ELRIC","ERIC","KARNA","RANDOLF","TYRIN","JANET","HIGINS","SKREECH","TAYA","FRAYJA","JARO","GYAN","SHEELA","ZYNK","CHAZ","LEMON", "CLAUDE"]
chars_b = ["BOWIE","SARAH","CHESTER","JAHA","KAZIN","SLADE","KIWI","PETER","MAY","GERHALT","LUKE","RICK"]
chars_b20 = ["ELRIC","ERIC","KARNA","RANDOLF","TYRIN","JANET"]
chars_p = ["ROHDE","HIGINS","SKREECH","TAYA","FRAYJA","JARO","GYAN","SHEELA","ZYNK","CHAZ","LEMON", "CLAUDE"]
chars_b2 = chars_b.copy()
chars_b202 = chars_b20.copy()
chars_p2 = chars_p.copy()
chars = chars_b+chars_b20+chars_p

orig_values = {\
"BOWIE" : 0,"SARAH" : 1,"CHESTER" : 2,"JAHA" : 3,"KAZIN" : 4,"SLADE" : 5,"KIWI" : 6,"PETER" : 7,"MAY" : 8,"GERHALT" : 9,"LUKE" : 10,\
"ROHDE" : 11,"RICK" : 12,"ELRIC" : 13,"ERIC" : 14,"KARNA" : 15,"RANDOLF" : 16,"TYRIN" : 17,"JANET" : 18,"HIGINS" : 19,"SKREECH" : 20,\
"TAYA" : 21,"FRAYJA" : 22,"JARO" : 23,"GYAN" : 24,"SHEELA" : 25,"ZYNK" : 26,"CHAZ" : 27,"LEMON" : 28, "CLAUDE" : 29}
if(config["Characters"]):
	while(len(chars) > 1):
		swap_char_a = random.choice(chars)
		swap_set = []
		if(swap_char_a in chars_b):
			swap_set = chars_b + chars_b20
			if(config["Depromos"]):
				swap_set += chars_p
		elif(swap_char_a in chars_b20):
			swap_set = chars_b + chars_b20 + chars_p
		else:
			swap_set = chars_p + chars_b20
			if(config["Depromos"]):
				swap_set += chars_b
		swap_set.remove(swap_char_a)
		chars.remove(swap_char_a)
		if(swap_char_a in chars_b):
			chars_b.remove(swap_char_a)
		if(swap_char_a in chars_b20):
			chars_b20.remove(swap_char_a)
		if(swap_char_a in chars_p):
			chars_p.remove(swap_char_a)
		#this character has no prospective swaps due to the depromo rule, but there might be others that work. Remove it from the pool
		if(len(swap_set) == 0):
			print(f"Noone to swap {swap_char_a} with")
			continue
		swap_char_b = random.choice(swap_set)
		chars.remove(swap_char_b)
		if(swap_char_b in chars_b):
			chars_b.remove(swap_char_b)
		if(swap_char_b in chars_b20):
			chars_b20.remove(swap_char_b)
		if(swap_char_b in chars_p):
			chars_p.remove(swap_char_b)
		name_a = swap_char_a.capitalize()
		name_b = swap_char_b.capitalize()
		#first char is below level 20 and not promoted
		if(swap_char_a in chars_b2):
			#second char is over level 20 but not promoted
			if(swap_char_b in chars_b202):
				chars_b2.remove(swap_char_a)
				chars_b202.append(swap_char_a)
				chars_b202.remove(swap_char_b)
				chars_b2.append(swap_char_b)
			#second char is promoted
			elif(swap_char_b in chars_p2):
				#Depromos must be true for this condition to be true to begin with
				#If we are allowing random promotions, the character will be in the promo set
				if(config["Promo"]):
					chars_b2.remove(swap_char_a)
					chars_p2.append(swap_char_a)
				#otherwise, they are in the non-promoted but over 20 set
				else:
					chars_b2.remove(swap_char_a)
					chars_b202.append(swap_char_a)
				#Depromos has to be true to get to this point so we don't need to check
				chars_p2.remove(swap_char_b)
				chars_b2.append(swap_char_b)
		#first char is above 20 but not promoted
		elif(swap_char_a in chars_b202):
			#second char is below 20 and not promoted
			if(swap_char_b in chars_b2):
				chars_b202.remove(swap_char_a)
				chars_b2.append(swap_char_a)
				chars_b2.remove(swap_char_b)
				chars_b202.append(swap_char_b)
			#second char is promoted
			elif(swap_char_b in chars_p2):
				#Depromos is not guaranteed to be true in this case
				#If we are allowing random promotions, the character will be in the promo set
				if(config["Promo"]):
					chars_b202.remove(swap_char_a)
					chars_p2.append(swap_char_a)
				#otherwise, they don't move
				#only change the second char if allowing depromos
				if(config["Depromos"]):
					chars_p2.remove(swap_char_b)
					chars_b202.append(swap_char_b)
		#first character is promoted
		else:
			#second char is below 20 and not promoted
			#this implies depromos are allowed
			if(swap_char_b in chars_b2):
				chars_p2.remove(swap_char_a)
				chars_b2.append(swap_char_a)
				chars_b2.remove(swap_char_b)
				chars_p2.append(swap_char_b)
			#second char is over 20 and not promoted
			elif(swap_char_b in chars_b202):
				#only move if allowing depromos
				if(config["Depromos"]):
					chars_p2.remove(swap_char_a)
					chars_b202.append(swap_char_a)
				#only move if allowing random promos
				if(config["Promo"]):
					chars_b202.remove(swap_char_b)
					chars_p2.append(swap_char_b)
		index_a = chars_m.index(swap_char_a)
		index_b = chars_m.index(swap_char_b)
		chars_m[index_a] = swap_char_b
		chars_m[index_b] = swap_char_a
		swap_characters(swap_char_a, swap_char_b, name_a, name_b, orig_values[swap_char_a], orig_values[swap_char_b], config["Depromos"], config["Promo"])

	chars = chars_b2+chars_b202+chars_p2
	#There is an edge case that doesn't work if you have depromo turned on, but random promos turned off. Depromoted characters will not be 
	#allowed to repromote in step 2 in that case. I did write the protection for this case into the new class function, but I don't feel like
	#separating them off in the logic of this part.
	while(len(chars) > 1):
		swap_char_a = random.choice(chars)
		swap_set = []
		if(swap_char_a in chars_b2):
			swap_set = chars_b2 + chars_b202
			if(config["Depromos"]):
				swap_set += chars_p2
		elif(swap_char_a in chars_b202):
			swap_set = chars_b2 + chars_b202 + chars_p2
		else:
			swap_set = chars_p2 + chars_b202
			if(config["Depromos"]):
				swap_set += chars_b2
		swap_set.remove(swap_char_a)
		chars.remove(swap_char_a)
		if(swap_char_a in chars_b2):
			chars_b2.remove(swap_char_a)
		if(swap_char_a in chars_b202):
			chars_b202.remove(swap_char_a)
		if(swap_char_a in chars_p2):
			chars_p2.remove(swap_char_a)
		#this character has no prospective swaps due to the depromo rule, but there might be others that work. Remove it from the pool
		if(len(swap_set) == 0):
			print(f"Noone to swap {swap_char_a} with")
			continue
		swap_char_b = random.choice(swap_set)
		chars.remove(swap_char_b)
		if(swap_char_b in chars_b2):
			chars_b2.remove(swap_char_b)
		if(swap_char_b in chars_b202):
			chars_b202.remove(swap_char_b)
		if(swap_char_b in chars_p2):
			chars_p2.remove(swap_char_b)
		name_a = swap_char_a.capitalize()
		name_b = swap_char_b.capitalize()
		index_a = chars_m.index(swap_char_a)
		index_b = chars_m.index(swap_char_b)
		chars_m[index_a] = swap_char_b
		chars_m[index_b] = swap_char_a
		swap_characters(swap_char_a, swap_char_b, name_a, name_b, orig_values[swap_char_a], orig_values[swap_char_b], config["Depromos"], config["Promo"])
	if(not config["Silent"]):
		print(f"New character order\n{chars_m}")
	replace_npc_rohde_sprite()
	replace_spinning_elric()
	replace_knocked_out_luke()
	replace_knocked_out_higins()
if(config["Magic"]):
	spells_1 = ["EGRESS", "DISPEL", "SLEEP", "ATTACK", "DISPEL"]
	spells_2 = ["BOLT", "HEAL", "DETOX", "BLAST", "SLOW", "BLAZE", "MUDDLE", "DESOUL", "DAO", "APOLLO", "NEPTUN", "ATLAS",\
	"KATON", "RAIJIN", "HEAL", "BLAST", "BOOST", "AURA", "BLAZE", "FREEZE", "BOLT", "DAO", "APOLLO", "NEPTUN", "ATLAS",\
	"BLAZE", "FREEZE", "BOLT", "DESOUL", "DAO", "APOLLO", "NEPTUN", "ATLAS", "HEAL", "DETOX", "AURA", "HEAL", "BLAST", "MUDDLE", "BOOST",\
	"BLAZE", "FREEZE", "BOLT", "DAO", "APOLLO", "NEPTUN", "ATLAS"]
	levels = {"EGRESS" : 1, "BOLT" : 4, "HEAL" : 4, "DETOX" : 4, "BLAST" : 4, "SLOW" : 2, "BLAZE" : 4, "FREEZE" : 4, "MUDDLE" : 2, "DISPEL" : 1,\
	"DESOUL" : 2, "DAO" : 2, "APOLLO" : 2, "NEPTUN" : 2, "ATLAS" : 2, "KATON" : 3, "RAIJIN" : 3, "BOOST" : 2, "AURA" : 4, "SLEEP" : 1, "ATTACK" : 1}
	starter_spells = ["BLAZE", "FREEZE", "HEAL", "BLAST"]
	if(config["Magic levels"]):
		chaos = [x for x in range(1,53)]
		bowie_spells = chaos.copy()
		sarah_spells = chaos.copy()
		kazin_spells = chaos.copy()
		sorc_spells = [x for x in range(21,53)]
		slade_spells = [x for x in range(22,53)]
		karna_spells = chaos.copy()
		tyrin_spells = chaos.copy()
		taya_spells = chaos.copy()
		frayja_spells = chaos.copy()
		sheela_spells = chaos.copy()
		chaz_spells = chaos.copy()
	else:
		bowie_spells = [1,22,31,42,51]
		sarah_spells = [1,7,22,40,4,13,33,44,10,16,25,36,19,29,48,52]
		kazin_spells = [1,5,21,32,9,24,37,47,13,17,28,42,52]
		sorc_spells = [21,32,34,50,23,30,36,38,26,40,42,46,28,44,48,52]
		slade_spells = [24,29,35,45,34,39,43,52]
		karna_spells = [1,4,19,40,7,14,23,32,10,17,26,44,29,36,48,52]
		tyrin_spells = [1,10,44,49,4,19,27,33,22,24,30,47,52]
		taya_spells = [1,4,48,52,9,12,39,43,17,22,30,35,14,26,27,45]
		frayja_spells = [1,11,49,52,4,15,32,37,29,36,40,45,42]
		sheela_spells = [1,5,36,51,7,18,38,47,11,24,32,41,13,20,28,44]
		chaz_spells = [1,10,49,52,5,15,22,40,35,38,42,46,36]

	randomize_spells(config["Silent"],chars_m, spells_1, spells_2, levels, starter_spells, bowie_spells,sarah_spells,kazin_spells,sorc_spells,slade_spells,karna_spells,tyrin_spells,taya_spells,frayja_spells,sheela_spells,chaz_spells)
remove_redundant_classes()
if(config["Items"]):
	promo_item_dict = {"VIGOR_BALL" : ["SARAH", "Karna", "FRAYJA", "SHEELA"], "WARRIORS_PRIDE" : ["JAHA", "RANDOLF", "GYAN"], \
	"SECRET_BOOK" : ["KAZIN", "TYRIN", "TAYA", "CHAZ"], "PEGASUS_WING" : ["CHESTER", "RICK", "ERIC", "HIGINS", "JARO"], \
	"SILVER_TANK" : ["ROHDE", "ELRIC", "JANET"]}
	promo_item_dict_r = {}
	for x in promo_item_dict.keys():
		for y in promo_item_dict[x]:
			promo_item_dict_r[y] = x
	item_nums = [0,0,0,0,0]
	for x in [y for y in range(0, 11)]+[y for y in range(12,19)]:
		char = chars_m[x]
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
	f = open("..\\disasm\\data\\maps\\entries\\map07\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map07\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Warrior's Pride with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("WARRIORS_PRIDE", temp_item))
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map46\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map46\\8-other-items.asm", 'w')
	f.write(file.replace("WARRIORS_PRIDE", temp_item))
	f.close()
	
	f = open("..\\disasm\\data\\maps\\entries\\map23\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map23\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Secret Book with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("SECRET_BOOK", temp_item))
	f.close()
	
	f = open("..\\disasm\\data\\maps\\entries\\map23\\7-chest-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map23\\7-chest-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Vigor Ball 1 with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("VIGOR_BALL", temp_item))
	f.close()
	
	f = open("..\\disasm\\data\\maps\\entries\\map36\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map36\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Pegasus Wing with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("PEGASUS_WING", temp_item))
	f.close()
	
	f = open("..\\disasm\\data\\maps\\entries\\map67\\8-other-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map67\\8-other-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Vigor Ball 2 with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("VIGOR_BALL", temp_item))
	f.close()
	
	f = open("..\\disasm\\data\\maps\\entries\\map48\\7-chest-items.asm", 'r')
	file = f.read()
	f.close()
	f = open("..\\disasm\\data\\maps\\entries\\map48\\7-chest-items.asm", 'w')
	temp_item = random.choice(rep_list)
	if(not config["Silent"]):
		print("Swapped Silver Tank with", temp_item)
	rep_list.remove(temp_item)
	f.write(file.replace("SILVER_TANK", temp_item))
	f.close()