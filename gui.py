from tkinter import *
from tkinter import ttk
from split.swap_characters import *
import subprocess
import os

disasm_prefix = r".\disasm"

def toggle_chars(a, b):
	for x in range(len(a)):
		if(a[x].get() == "???"):
			a[x].set(b[x])
		else:
			a[x].set("???")

def display_info(char, orig, frame, frame_vars, class_frames, notebook1, notebook2, char_index=None):
	if(char_index != None):
		char = char[char_index]
	if(0 in frame_vars):
		#why is this backwards!?
		frame.grid_slaves(0,2)[0].configure(text=frame.grid_slaves(0,0)[0]["text"])
		frame.grid_slaves(0,3)[0].configure(text=frame.grid_slaves(0,1)[0]["text"])
		frames2 = notebook2.tabs()
		for x in frames2:
			notebook2.hide(x)
		frames1 = notebook1.tabs()
		for x in range(len(frames1)):
			notebook2.add(frames2[x])
			notebook2.tab(frames2[x], text=notebook1.tab(frames1[x], option="text"))
			copy_frame = notebook2.nametowidget(frames2[x])
			for y in copy_frame.winfo_children():
				y.destroy()
			cur_frame = notebook1.nametowidget(frames1[x])
			for c in range(cur_frame.grid_size()[0]):
				for r in range(cur_frame.grid_size()[1]):
					slave = cur_frame.grid_slaves(r,c)
					if(len(slave) == 0):
						continue
					slave = slave[0].cget("text")
					ttk.Label(copy_frame, text=slave).grid(column=c, row=r, padx=5, sticky=W)
		notebook2.select(0)
	# set the class frames as invisible unless needed later
	for x in notebook1.tabs():
		notebook1.forget(x)
	# clear all of the text in every frame in case we need to use it later
	for k,v in frame_vars.items():
		for k2,v2 in v.items():
			for x in v2:
				v2[x].set("")
	# First index is the class, but 0 is special since it will just have the name
	# Second and third indicies are the col and row within the specified frame (class)
	if(0 not in frame_vars):
		frame_vars[0] = {}
		frame_vars[0][0] = {}
		frame_vars[0][0][0] = StringVar()
		ttk.Label(frame, textvariable=frame_vars[0][0][0]).grid(column=0, row=0, padx=5 ,sticky=W)
		ttk.Label(frame, text="").grid(column=2, row=0, padx=5 ,sticky=W)
		frame_vars[0][0][1] = StringVar()
		ttk.Label(frame, textvariable=frame_vars[0][0][1]).grid(column=1, row=0, padx=5 ,sticky=W)
		ttk.Label(frame, text="").grid(column=3, row=0, padx=5 ,sticky=W)
	frame_vars[0][0][0].set("Name")
	frame_vars[0][0][1].set(char)
	char = orig_values[char]
	char = "0" + str(char) if char < 10 else str(char)
	if(orig):
		f = open(disasm_prefix + r"\data\stats\allies\stats\orig_stats\allystats" + char + ".asm", 'r')
	else:
		f = open(disasm_prefix + r"\data\stats\allies\stats\allystats" + char + ".asm", 'r')
	file = f.read()
	f.close()
	classes = file.split("forClass")
	cur_row = 0
	cur_column = 0
	cur_class = 1
	for x in classes:
		if("AllyStats" in x or "projected" in x):
			continue
		if(len(class_frames) < cur_class):
			class_frames.append(ttk.Frame(notebook1, padding=10, relief=GROOVE, borderwidth=5))
			temp_frame = ttk.Frame(notebook2, padding=10, relief=GROOVE, borderwidth=5)
			notebook2.add(temp_frame)
		cur_frame = class_frames[cur_class-1]
		cur_frame.grid(column=cur_class+1, row=1 ,sticky=N)
		notebook1.add(cur_frame)
		if(cur_class not in frame_vars):
			frame_vars[cur_class] = {}
		vars_view = frame_vars[cur_class]
		cur_row = 0
		cur_column = 0
		if("spellList" in x):
			stats = x[0:x.find("spellList")].splitlines()
			for y in stats:
				if(y.strip() == ""):
					continue
				cur_column = 0
				if("Growth" in y):
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5, sticky=W)
					vars_view[cur_column][cur_row].set(y[y.find("Growth")-3:y.find("Growth")].strip().upper())
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Base")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Projected")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Average")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Type")
					
					cur_row += 1
					cur_column = 1
					base = y[y.find("Growth")+6:y.find(",")].strip()
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(base)
					cur_column += 1
					
					proj = y.find(",")+1
					proj = y[proj:y.find(",",proj)].strip()
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(proj)
					cur_column += 1
					
					base = int(base)
					proj = int(proj)
					avg = f"{(proj-base)/29.0:1.2}"
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(avg)
					cur_column += 1
					
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(y[y.rfind(",")+1:].strip())
					cur_row += 1
				else:
					cur_row = 1
					notebook1.tab(cur_frame, text=y.strip())
					cur_row += 1
			spells = x[x.find("spellList"):].split("&")
			cur_column = 0
			if(len(spells) == 1):
				cur_class += 1
				continue
			if(cur_column not in vars_view):
				vars_view[cur_column] = {}
			if(cur_row not in vars_view[cur_column]):
				vars_view[cur_column][cur_row] = StringVar()
				ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5, sticky=W)
			vars_view[cur_column][cur_row].set("Spell")
			cur_column += 1
			if(cur_row not in vars_view[cur_column]):
				vars_view[cur_column][cur_row] = StringVar()
				ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
			vars_view[cur_column][cur_row].set("Level")
			cur_column += 1
			if(cur_row not in vars_view[cur_column]):
				vars_view[cur_column][cur_row] = StringVar()
				ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
			vars_view[cur_column][cur_row].set("Learned")
			cur_row += 1
			for y in spells:
				if("," not in y):
					continue
				cur_column = 0
				index1 = y.find(",")
				index2 = y.find(",", index1+1)
				if(index2 == -1):
					index2 = len(y)
				if(cur_row not in vars_view[cur_column]):
					vars_view[cur_column][cur_row] = StringVar()
					ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5, sticky=W)
				vars_view[cur_column][cur_row].set(y[index1+1:index2].strip() if "LV" not in y else y[index1+1:y.find("|LV")].strip())
				cur_column += 1
				if(cur_row not in vars_view[cur_column]):
					vars_view[cur_column][cur_row] = StringVar()
					ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
				vars_view[cur_column][cur_row].set("1" if "LV" not in y else y[y.find("LV")+2:y.find("LV")+3])
				cur_column += 1
				if(cur_row not in vars_view[cur_column]):
					vars_view[cur_column][cur_row] = StringVar()
					ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
				vars_view[cur_column][cur_row].set(y[index1-2:index1].strip())
				cur_row += 1
		else:
			stats = x[0:x.find("useFirstSpellList")].splitlines()
			for y in stats:
				if(y.strip() == ""):
					continue
				cur_column = 0
				if("Growth" in y):
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5, sticky=W)
					vars_view[cur_column][cur_row].set(y[y.find("Growth")-3:y.find("Growth")].strip().upper())
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Base")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Projected")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Average")
					cur_column += 1
					
					if(cur_column not in vars_view):
						vars_view[cur_column] = {}
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set("Type")
					
					cur_row += 1
					cur_column = 1
					base = y[y.find("Growth")+6:y.find(",")].strip()
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(base)
					cur_column += 1
					
					proj = y.find(",")+1
					proj = y[proj:y.find(",",proj)].strip()
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(proj)
					cur_column += 1
					
					base = int(base)
					proj = int(proj)
					avg = f"{(proj-base)/29.0:1.2}"
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(avg)
					cur_column += 1
					
					if(cur_row not in vars_view[cur_column]):
						vars_view[cur_column][cur_row] = StringVar()
						ttk.Label(cur_frame, textvariable=vars_view[cur_column][cur_row]).grid(column=cur_column,row=cur_row, padx=5)
					vars_view[cur_column][cur_row].set(y[y.rfind(",")+1:].strip())
					cur_row += 1
				else:
					cur_row = 1
					notebook1.tab(cur_frame, text=y.strip())
					cur_row += 1
		cur_class += 1

def randomize(	rand_depromo, rand_prepromo, rand_magic, chaos_magic, rand_promo_items, rand_stat_growths, rand_stats, \
				percent_change, adjust_level, promo_level, promo_elevel, orig_values, cur_values, cur_items, name_list):
	adjust_level = True if adjust_level.get() == 1 else False
	promo_level = promo_level.get()
	promo_elevel = promo_elevel.get()
	if(adjust_level):
		if(promo_level < promo_elevel):
			frm.bell()
			return
	rand_depromo = True if rand_depromo.get() == 1 else False
	rand_prepromo = True if rand_prepromo.get() == 1 else False
	orig_list, swap_dict = determine_swap_list(rand_depromo, rand_prepromo, promo_elevel, promo_level)
	r_swap_dict = {k : v for v, k in swap_dict.items()}
	temp = [x for x in range(30)]
	for x in temp:
		temp[x] = r_swap_dict[x]
	swap_characters(orig_list, temp, orig_values, rand_depromo, rand_prepromo)
	for x in range(30):
		f = open(disasm_prefix + "\\data\\stats\\allies\\stats\\orig_stats\\allystats" + ("0" if x < 10 else "") + str(x) + ".asm", 'r')
		g = open(disasm_prefix + "\\data\\stats\\allies\\stats\\allystats" + ("0" if x < 10 else "") + str(x) + ".asm", 'w')
		g.write(f.read())
		f.close()
		g.close()
	replace_npc_rohde_sprite()
	replace_spinning_elric()
	replace_knocked_out_luke()
	replace_knocked_out_higins()
	replace_enemy_jaro()
	replace_stone_taya()
	replace_frozen_claude()
	rand_promo_items = True if rand_promo_items.get() == 1 else False
	randomize_promo_items(r_swap_dict, cur_items)
	rand_stat_growths = True if rand_stat_growths.get() == 1 else False
	if(rand_stat_growths):
		for x in range(30):
			randomize_growths(x)
	rand_stats = True if rand_stats.get() == 1 else False
	pos_change = int(percent_change[0].get())
	neg_change = int(percent_change[1].get())
	if(rand_stats):
		for x in range(30):
			randomize_stats(x, pos_change, neg_change)
	rand_magic = True if rand_magic.get() == 1 else False
	chaos_magic = True if chaos_magic.get() == 1 else False
	if(rand_magic):
		spells_1 = ["EGRESS", "DISPEL", "SLEEP", "ATTACK", "DISPEL"]
		spells_2 = ["BOLT", "HEAL", "DETOX", "BLAST", "SLOW", "BLAZE", "MUDDLE", "DESOUL", "DAO", "APOLLO", "NEPTUN", "ATLAS",\
		"KATON", "RAIJIN", "HEAL", "BLAST", "BOOST", "AURA", "BLAZE", "FREEZE", "BOLT", "DAO", "APOLLO", "NEPTUN", "ATLAS",\
		"BLAZE", "FREEZE", "BOLT", "DESOUL", "DAO", "APOLLO", "NEPTUN", "ATLAS", "HEAL", "DETOX", "AURA", "HEAL", "BLAST", "MUDDLE", "BOOST",\
		"BLAZE", "FREEZE", "BOLT", "DAO", "APOLLO", "NEPTUN", "ATLAS"]
		levels = {"EGRESS" : 1, "BOLT" : 4, "HEAL" : 4, "DETOX" : 4, "BLAST" : 4, "SLOW" : 2, "BLAZE" : 4, "FREEZE" : 4, "MUDDLE" : 2, "DISPEL" : 1,\
		"DESOUL" : 2, "DAO" : 2, "APOLLO" : 2, "NEPTUN" : 2, "ATLAS" : 2, "KATON" : 3, "RAIJIN" : 3, "BOOST" : 2, "AURA" : 4, "SLEEP" : 1, "ATTACK" : 1}
		starter_spells = ["BLAZE", "FREEZE", "HEAL", "BLAST"]
		if(chaos_magic):
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
		randomize_spells(temp, spells_1, spells_2, levels, starter_spells, bowie_spells,sarah_spells,kazin_spells,sorc_spells,slade_spells,karna_spells,tyrin_spells,taya_spells,frayja_spells,sheela_spells,chaz_spells)
	
	if(adjust_level):
		adjust_levels(promo_elevel, promo_level, orig_values)
	remove_redundant_classes()
	for x in r_swap_dict:
		cur_values[x] = r_swap_dict[x]
	toggle_chars(name_list, cur_values)
	toggle_chars(name_list, cur_values)
	
def display_patches():
	f = open(disasm_prefix + r"\sf2patches.asm", 'r')
	file = f.read()
	f.close()
	index1 = file.find("; Quality of life features")
	index2 = file.find("\n\n", index1)
	qol = {}
	temp = file[index1:index2].splitlines()
	for x in temp:
		if("equ" in x):
			temp1 = x.split("equ", 1)
			key = temp1[0].strip()[0:-1]
			if(";" in temp1[1]):
				index = temp1[1].find(";")
				val = temp1[1][1:index].strip()
				desc = temp1[1][index+2:]
			else:
				val = temp1[1][1:].strip()
				desc = ""
			if(key in "NO_AI_JARONO_AI_PETER"):	
				desc = "They will immediately join instead."
			if(key in "NO_RANDOM_BATTLES"):	
				desc = ""
			qol[key] = [val,desc]
	
	index1 = file.find("; Misc. features")
	index2 = file.find("\n\n", index1)
	misc = {}
	temp = file[index1:index2].splitlines()
	for x in temp:
		if("equ" in x):
			temp1 = x.split("equ", 1)
			key = temp1[0].strip()[0:-1]
			if(";" in temp1[1]):
				index = temp1[1].find(";")
				val = temp1[1][1:index].strip()
				desc = temp1[1][index+2:]
			else:
				val = temp1[1][1:].strip()
				desc = ""
			if(key in "DIFFICULTY_FACTORS"):	
				desc = "Hard = 1.25x enemy ATT, Super = 1.56x enemy ATT, Ouch = 1.56x enemy ATT and 1.5x enemy AGI"
			misc[key] = [val,desc]
				
	index1 = file.find("; AI enhancements")
	index2 = file.find("\n\n", index1)
	ai = {}
	temp = file[index1:index2].splitlines()
	for x in temp:
		if("equ" in x):
			temp1 = x.split("equ", 1)
			key = temp1[0].strip()[0:-1]
			if(";" in temp1[1]):
				index = temp1[1].find(";")
				val = temp1[1][1:index].strip()
				desc = temp1[1][index+2:]
			else:
				val = temp1[1][1:].strip()
				desc = ""
			ai[key] = [val,desc]
	
	index1 = file.find("; Menu enhancements")
	index2 = file.find("\n\n", index1)
	menu = {}
	temp = file[index1:index2].splitlines()
	for x in temp:
		if("equ" in x):
			temp1 = x.split("equ", 1)
			key = temp1[0].strip()[0:-1]
			if(";" in temp1[1]):
				index = temp1[1].find(";")
				val = temp1[1][1:index].strip()
				desc = temp1[1][index+2:]
			else:
				val = temp1[1][1:].strip()
				desc = ""
			if(key in "SHOW_ENEMY_LEVEL"):	
				desc = "Enemies will grant full exp up to their level plus 4. At level plus 7, only 1 exp will be granted."
			menu[key] = [val,desc]
	
	root = Tk()
	root.title("Patches")
	frm = ttk.Frame(root)
	frm.bind("<Destroy>", func=lambda a, b=[qol, misc, ai, menu]: write_patches(b))
	cur_row = 0
	special_cases = "MUSCLE_MAGICMUSCLE_MAGIC_STATPERCENT_POISON_DAMAGEALTERNATE_JEWEL_ICONS_DISPLAYORIGINAL_TAROS_INVULNERABILITY"
	ttk.Label(root, text="Quality of Life").grid(column=0, row=cur_row)
	cur_row += 1
	for k, v in qol.items():
		ttk.Label(root, text=k).grid(column=0, row=cur_row, sticky=W, padx=5)
		ttk.Label(root, text=":").grid(column=1, row=cur_row, padx=5)
		if(k not in special_cases):
			var = IntVar(root)
			ttk.Checkbutton(root, variable=var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		else:
			var = StringVar(root)
			ttk.Entry(root, textvariable = var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		ttk.Label(root, text=v[1]).grid(column=3, row=cur_row, sticky=W, padx=5)
		cur_row += 1
	ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=cur_row, columnspan=4, sticky=E+W)
	ttk.Label(root, text="Miscellaneous").grid(column=0, row=cur_row+1)
	cur_row += 2
	for k, v in misc.items():
		ttk.Label(root, text=k).grid(column=0, row=cur_row, sticky=W, padx=5)
		ttk.Label(root, text=":").grid(column=1, row=cur_row, padx=5)
		if(k not in special_cases):
			var = IntVar(root)
			ttk.Checkbutton(root, variable=var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		else:
			var = StringVar(root)
			ttk.Entry(root, textvariable = var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		ttk.Label(root, text=v[1]).grid(column=3, row=cur_row, sticky=W, padx=5)
		cur_row += 1
	ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=cur_row, columnspan=4, sticky=E+W)
	ttk.Label(root, text="AI Related").grid(column=0, row=cur_row+1)
	cur_row += 2
	for k, v in ai.items():
		ttk.Label(root, text=k).grid(column=0, row=cur_row, sticky=W, padx=5)
		ttk.Label(root, text=":").grid(column=1, row=cur_row, padx=5)
		if(k not in special_cases):
			var = IntVar(root)
			ttk.Checkbutton(root, variable=var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		else:
			var = StringVar(root)
			ttk.Entry(root, textvariable = var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		ttk.Label(root, text=v[1]).grid(column=3, row=cur_row, sticky=W, padx=5)
		cur_row += 1
	ttk.Separator(root, orient=HORIZONTAL).grid(column=0, row=cur_row, columnspan=4, sticky=E+W)
	ttk.Label(root, text="Menu Related").grid(column=0, row=cur_row+1)
	cur_row += 2
	for k, v in menu.items():
		ttk.Label(root, text=k).grid(column=0, row=cur_row, sticky=W, padx=5)
		ttk.Label(root, text=":").grid(column=1, row=cur_row, padx=5)
		if(k not in special_cases):
			var = IntVar(root)
			ttk.Checkbutton(root, variable=var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		else:
			var = StringVar(root)
			ttk.Entry(root, textvariable = var).grid(column=2, row=cur_row, sticky=W)
			var.set(v[0])
			v[0] = var
		ttk.Label(root, text=v[1]).grid(column=3, row=cur_row, sticky=W, padx=5)
		cur_row += 1
	
def write_patches(patches):
	f = open(disasm_prefix + "/sf2patches.asm", 'r')
	file = f.read()
	f.close()
	for x in patches:
		for k,v in x.items():
			rep_num = len(str(v[0].get()))
			index1 = file.find(k)
			index1 = file.find("equ", index1+len(k))+4
			if(";" in file[index1:file.find("\n", index1)]):
				index2 = file.find(" ", index1)
			else:
				index2 = file.find("\n", index1)
			val = str(v[0].get())
			if(len(val) < index2-index1):
				for y in range(index2-index1 - len(val)):
					val += " "
			if(len(val) > index2-index1):
				index2 += len(val)-(index2-index1)
			file = file[0:index1] + val + file[index2:]
	f = open(disasm_prefix + "/sf2patches.asm", 'w')
	f.write(file)
	f.close()

def write_config(args):
	f = open("config.txt", 'w')
	for x in iter(args):
		if(type(args[x]) is not str):
			args[x] = args[x].get()
	f.write(repr(args))
	f.close()

def build():
	os.chdir("build")
	subprocess.run(["buildstandard.bat"])
	os.chdir("..")
	Path(r".\build\standardbuild-last.bin").replace(Path(r".\sf2.bin"))

orig_values = {\
"BOWIE" : 0,"SARAH" : 1,"CHESTER" : 2,"JAHA" : 3,"KAZIN" : 4,"SLADE" : 5,"KIWI" : 6,"PETER" : 7,"MAY" : 8,"GERHALT" : 9,"LUKE" : 10,\
"ROHDE" : 11,"RICK" : 12,"ELRIC" : 13,"ERIC" : 14,"KARNA" : 15,"RANDOLF" : 16,"TYRIN" : 17,"JANET" : 18,"HIGINS" : 19,"SKREECH" : 20,\
"TAYA" : 21,"FRAYJA" : 22,"JARO" : 23,"GYAN" : 24,"SHEELA" : 25,"ZYNK" : 26,"CHAZ" : 27,"LEMON" : 28, "CLAUDE" : 29}
cur_values = {}
f = open(disasm_prefix + r"\sf2enums.asm", 'r')
file = f.read()
f.close()
index1 = file.find("; enum Allies")
index1 = file.find("\n", index1)+1
index2 = file.find("; ---------------------------------------------------------------------------", index1)
splits = file[index1:index2].splitlines()
for x in splits:
	if("equ" not in x):
		continue
	ally = x.split(": equ ")[0][5:]
	num = int(x.split(": equ ")[1])
	cur_values[num] = ally
try:
	f = open("config.txt", 'r')
	config = eval(f.read())
	f.close()
except Exception:
	print("Either no config or it was corrupted.")
	config = {}
root = Tk()
root.title("Shining Force 2 Randomizer")
frm = ttk.Frame(root, padding=10)
frm.grid()
frm.bind("<Destroy>", func=lambda a, b=config: write_config(b))
char_frm = ttk.Frame(frm, padding=10)
char_frm.grid(column=0, row=0, padx=5)
name_list = [x for x in range(30)]
for k,v in orig_values.items():
	name_list[v] = k
offset = 1
max_char_length = 0
for x in orig_values:
	if(len(x) > max_char_length):
		max_char_length = len(x)
max_char_length = int(max_char_length*1.5)
info_frm = ttk.Frame(frm, padding=10)
info_frm.grid(column=0, row = 2, columnspan=32 ,sticky=W+N)
info_note1 = ttk.Notebook(info_frm, padding=10)
info_note1.grid(column=0, row = 1, columnspan=2)
info_note2 = ttk.Notebook(info_frm, padding=10)
info_note2.grid(column=2, row = 1, columnspan=2, sticky=W+N)
c_frms = []
frame_vars = {}
cur_row_offset = 0
char_row_offset = 6
char_mod = 12
for x in range(len(name_list)):
	cur_row_offset_t = int(x/12)*5
	if(cur_row_offset_t > cur_row_offset):
		offset =1
		char_row_offset += 6
	cur_row_offset = cur_row_offset_t
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+0,sticky=E+W)
	ttk.Button(char_frm, text=name_list[x], width = max_char_length, command=lambda a=name_list[x], b=info_frm, c=frame_vars, d=c_frms, e=info_note1, f=info_note2 : display_info(a, True, b, c, d, e, f)).grid(column=x%char_mod+1+offset, row=cur_row_offset+1, padx=5)
	name_list[x] = StringVar()
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+2,sticky=E+W)
	ttk.Button(char_frm, textvariable=name_list[x], width = max_char_length, command=lambda a=cur_values, b=info_frm, c=frame_vars, d=c_frms, e=info_note1, f=info_note2, g=x : display_info(a, False, b, c, d, e, f, g)).grid(column=x%char_mod+1+offset, row=cur_row_offset+3, padx=5)
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+4,sticky=E+W)
	name_list[x].set("???")
	offset += 1
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+0,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+1,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+2,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+3,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x%char_mod+1+offset, row=cur_row_offset+4,sticky=N+S)
for x in range(char_row_offset+4):
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=1, row=x,sticky=N+S)
show_chars_con = IntVar()
ttk.Checkbutton(char_frm, variable = show_chars_con, text="Show Characters", command=lambda a=name_list, b=cur_values : toggle_chars(a, b)).grid(column=0,row=cur_row_offset+3, padx=5, sticky=W)
show_chars_con.set(0)
rand_frm = ttk.Frame(frm, padding=10)
rand_frm.grid(column=0, row=1, columnspan=40, sticky=W)
rand_depromo = IntVar()
if("rand_depromo" in  config):
	rand_depromo.set(config["rand_depromo"])
config["rand_depromo"] = rand_depromo
ttk.Checkbutton(rand_frm, variable = rand_depromo, text="Allow Depromotion").grid(column=1,row=0, padx=5, sticky=W)
rand_prepromo = IntVar()
if("rand_prepromo" in  config):
	rand_prepromo.set(config["rand_prepromo"])
config["rand_prepromo"] = rand_prepromo
ttk.Checkbutton(rand_frm, variable = rand_prepromo, text="Allow Random Promotion Path").grid(column=2,row=0, padx=5, sticky=W)
chaos_magic = IntVar()
if("chaos_magic" in  config):
	chaos_magic.set(config["chaos_magic"])
config["chaos_magic"] = chaos_magic
chaos_magic_button = ttk.Checkbutton(rand_frm, variable = chaos_magic, text="Randomize Spell Learn Levels")
chaos_magic_button.grid(column=4, row=0, padx=5, sticky=W)
chaos_magic_button.state(["disabled"])
rand_magic = IntVar()
if("rand_magic" in  config):
	rand_magic.set(config["rand_magic"])
config["rand_magic"] = rand_magic
if(rand_magic.get() == 1):
	chaos_magic_button.state(["!disabled"])
def toggle_state(button, button_var, state, off_state):
	for x in range(len(button)):
		if(state.get() == 0):
			button_var[x].set(off_state)
			button[x].state(["disabled"])
		else:
			button[x].state(["!disabled"])
ttk.Checkbutton(rand_frm, variable = rand_magic, text="Randomize Learned Spells", command= lambda a=rand_magic, b=chaos_magic_button, c=chaos_magic : toggle_state([b], c, a, 0)).grid(column=3,row=0, padx=5, sticky=W)
rand_promo_items = IntVar()
if("rand_promo_items" in  config):
	rand_promo_items.set(config["rand_promo_items"])
config["rand_promo_items"] = rand_promo_items
ttk.Checkbutton(rand_frm, variable = rand_promo_items, text="Randomize Promotion Items").grid(column=0,row=1, padx=5, sticky=W)
rand_stat_growths = IntVar()
if("rand_stat_growths" in  config):
	rand_stat_growths.set(config["rand_stat_growths"])
config["rand_stat_growths"] = rand_stat_growths
ttk.Checkbutton(rand_frm, variable = rand_stat_growths, text="Randomize Stat Growth Rates").grid(column=1,row=1, padx=5, sticky=W)

percent_change_pos = StringVar()
pos = ttk.Entry(rand_frm, width=30, textvariable = percent_change_pos, invalidcommand = lambda a=percent_change_pos : a.set("Integer between 0 and 100 only"),\
validate="focusout", validatecommand=lambda a = percent_change_pos: (a.get().isdecimal() and int(a.get()) >= 0 and int(a.get()) <= 100))
pos.grid(column=2,row=2, padx=5, sticky=W)
ttk.Label(rand_frm, text="Positive Change %").grid(column=1,row=2, padx=5, sticky=W)
if("percent_change_pos" in  config):
	percent_change_pos.set(config["percent_change_pos"])
else:
	percent_change_pos.set("0")
config["percent_change_pos"] = percent_change_pos
pos.state(["disabled"])
percent_change_neg = StringVar()
neg = ttk.Entry(rand_frm, width=30, textvariable = percent_change_neg, invalidcommand = lambda a=percent_change_neg : a.set("Integer between 0 and 100 only"),\
validate="focusout", validatecommand=lambda a = percent_change_neg: (a.get().isdecimal() and int(a.get()) >= 0 and int(a.get()) <= 100))
neg.grid(column=4,row=2, padx=5, sticky=W)
ttk.Label(rand_frm, text="Negative Change %").grid(column=3,row=2, padx=5, sticky=W)
if("percent_change_neg" in  config):
	percent_change_neg.set(config["percent_change_neg"])
else:
	percent_change_neg.set("0")
config["percent_change_neg"] = percent_change_neg
neg.state(["disabled"])
rand_stats = IntVar()
if("rand_stats" in  config):
	rand_stats.set(config["rand_stats"])
config["rand_stats"] = rand_stats
if(rand_stats.get() == 1):
	pos.state(["!disabled"])
	neg.state(["!disabled"])
ttk.Checkbutton(rand_frm, variable = rand_stats, text="Randomize Stats", command=\
lambda a=rand_stats, b=[pos, neg], c=[percent_change_pos, percent_change_neg] : toggle_state(b, c, a, 0)).grid(column=0,row=2, padx=5, sticky=W)

promo_level = StringVar()
lvl1 = ttk.Entry(rand_frm, width=30, textvariable = promo_level, invalidcommand = lambda a=promo_level : a.set("Integer between 1 and 40 only"),\
validate="focusout", validatecommand=lambda a = promo_level: (a.get().isdecimal() and int(a.get()) > 0 and int(a.get()) <= 40))
lvl1.grid(column=2,row=3, padx=5, sticky=W)
ttk.Label(rand_frm, text="Pre-promoted effective level also level cap").grid(column=1,row=3, padx=5, sticky=W)
if("promo_level" in  config):
	promo_level.set(config["promo_level"])
else:
	promo_level.set("20")
config["promo_level"] = promo_level
lvl1.state(["disabled"])
promo_elevel = StringVar()
lvl2 = ttk.Entry(rand_frm, width=30, textvariable = promo_elevel, invalidcommand = lambda a=promo_elevel : a.set("Integer between 1 and 40 only"),\
validate="focusout", validatecommand=lambda a = promo_elevel: (a.get().isdecimal() and int(a.get()) > 0 and int(a.get()) <= 40))
lvl2.grid(column=4,row=3, padx=5, sticky=W)
ttk.Label(rand_frm, text="Game Treats Promoted Characters as This Plus 1").grid(column=3,row=3, padx=5, sticky=W)
if("promo_elevel" in  config):
	promo_elevel.set(config["promo_elevel"])
else:
	promo_elevel.set("20")
config["promo_elevel"] = promo_elevel
lvl2.state(["disabled"])
adjust_level = IntVar()
if("adjust_level" in  config):
	adjust_level.set(config["adjust_level"])
config["adjust_level"] = adjust_level
if(adjust_level.get() == 1):
	lvl1.state(["!disabled"])
	lvl2.state(["!disabled"])
ttk.Checkbutton(rand_frm, variable = adjust_level, text="Adjust Levels", command=\
lambda a=adjust_level, b=[lvl2, lvl1], c=[promo_elevel, promo_level] : toggle_state(b, c, a, 20)).grid(column=0,row=3, padx=5, sticky=W)
cur_items = []
ttk.Button(rand_frm, text="Randomize", command=\
lambda a=rand_depromo, b=rand_prepromo, c=rand_magic, d=chaos_magic, e=rand_promo_items, f=rand_stat_growths, g=rand_stats,\
h=[percent_change_pos, percent_change_neg], i=adjust_level, j=promo_level, k=promo_elevel, l=cur_values, m=cur_items, o=name_list : randomize(a,b,c,d,e,f,g,h,i,j,k, orig_values,l,m, o)).grid(column=0, row=0, sticky=W)

orig_items = ["WARRIOR_PRIDE", "SILVER_TANK", "SECRET_BOOK", "VIGOR_BALL", "VIGOR_BALL", "PEGASUS_WING"]
f = open(disasm_prefix + "\\data\\maps\\entries\\map07\\8-other-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("143")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
f = open(disasm_prefix + "\\data\\maps\\entries\\map48\\7-chest-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("146")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
f = open(disasm_prefix + "\\data\\maps\\entries\\map23\\8-other-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("158")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
f = open(disasm_prefix + "\\data\\maps\\entries\\map23\\7-chest-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("221")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
f = open(disasm_prefix + "\\data\\maps\\entries\\map67\\8-other-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("214")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
f = open(disasm_prefix + "\\data\\maps\\entries\\map36\\8-other-items.asm", 'r')
file = f.read()
f.close()
index1 = file.find("175")+5
index2 = file.find("\n", index1)
temp = file[index1:index2]
if(";" in temp):
	temp = temp[0:temp.find(";")-1]
cur_items.append(temp)
offset = 2
show_items_con = IntVar()

ttk.Checkbutton(char_frm, variable = show_items_con, text="Show Promo Items", command=lambda a=orig_items, b=cur_items : toggle_chars(a, b)).grid(column=0,row=char_row_offset+3, padx=5, sticky=W)
show_items_con.set(0)
for x in range(len(orig_items)):
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x+offset, row=char_row_offset+0,sticky=E+W, columnspan=4)
	ttk.Label(char_frm, text=orig_items[x]).grid(column=x+offset, row=char_row_offset+1, padx=5, columnspan=4)
	orig_items[x] = StringVar()
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x+offset, row=char_row_offset+2,sticky=E+W, columnspan=4)
	ttk.Label(char_frm, textvariable=orig_items[x]).grid(column=x+offset, row=char_row_offset+3, padx=5, columnspan=4)
	ttk.Separator(char_frm, orient=HORIZONTAL).grid(column=x+offset, row=char_row_offset+4,sticky=E+W, columnspan=4)
	orig_items[x].set("???")
	offset += 3
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x+offset, row=char_row_offset+0,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x+offset, row=char_row_offset+1,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x+offset, row=char_row_offset+2,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x+offset, row=char_row_offset+3,sticky=N+S)
	ttk.Separator(char_frm, orient=VERTICAL).grid(column=x+offset, row=char_row_offset+4,sticky=N+S)
if("split" not in config):
	os.chdir("split")
	subprocess.run([r"split.bat"])
	os.chdir("..")
	config["split"] = "done"
ttk.Button(char_frm, text = "Patches", command=display_patches).grid(column=0, row=1,sticky=W)
ttk.Button(char_frm, text = "Build", command=build).grid(column=0, row=3,sticky=W)
root.mainloop()
