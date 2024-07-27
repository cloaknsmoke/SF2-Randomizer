# SF2DISASM

A disassembly of the game "Shining Force II" for documentation and fan-project purposes, which can be assembled back into a bit-perfect replica of the original rom file.

This project is based on the dissasembly of Shining Force II. The original can be found [here](https://github.com/ShiningForceCentral/SF2DISASM)


# Randomizer

The purpose of this project is to allow certain aspects of the game to be randomized in order to provide a new experience to veteran players. I tried to keep the rest of the
experience as vanilla as possible except for a few select changes.

## New additions:
- Claude, Zynk, and Lemon have new base classes in the event that they start in your party before promotion. They will only promote to their original class. 
- New sprites for Rohde, Higins, Skreech, Taya, Frayja, Jaro, Gyan, Sheela, Zynk, Chaz, Lemon, and Claude were added for their base classes
- New sprites for Rohde, Higins, Taya, Frayja, Jaro, Gyan, Sheela, and Chaz were added for their alternate promotion path.
- A new portrait was added for Claude's base class.
- New spell tables have been added for Chaz as a Sorcerer and Taya as a Mage/Wizard. They are roughly in line with the other similar characters.
- I changed Hell Blast to Wind Blast because I think it makes more sense.
- The second Vigor Ball has been swapped with one of the mithrils earlier in the game so that it's actually relevant. The pegasus wing is still in Pacalon though.
- Lemon starts with a weapon that is not cursed in addition the the Dark Sword.
- Kiwi, Zynk, and Claude have resistances to magic that actually make sense instead of ones that do almost nothing.
- All characters that can cast magic by default will now gain experience from healing and healing items. 
- The Achilles Sword is now a ring that can be equipped by any class. It has no stats associated with it. All it does is allow you to attack Taros if you equip it and let you get Rohde.
- The Levanter is now exclusively equippable by BDBTs. It always bugged me that only Bowie could use it even though he gets an amazing weapon 2 battles after the blacksmith.
- Spell learn levels have been scaled down to be between 1 and 52 (32 promoted). Some characters had to get to level 40 promoted to learn some spells. No enemy outside of bosses can give you experience beyond level 31 promoted. I personally consider this a design flaw.

The gui will automatically extract the rom and well as make certain changes when opened for the first time. It won't work properly if sf2.bin is not already in the rom folder.

## Aspects that can be randomized:

The point in the game that each character joins. It will be based on the location a character joins in the original game. No new characters are introduced, so each character will still only join at a predefined point in the story.
The randomized characters have several options:
- Allow depromotion - Characters that normally cannot join as an unpromoted class will have new class definitions added to allow them to start in a base class appropriate for their original promoted class
- Allow random promotion path - Characters that join promoted will be given a random promotion from among their promotion branches. For instance, even if Frayja joins at a point where he would already be promoted, he might join as a Master Monk instead of Vicar with this option enabled. This obviously does not affect classes that only have 1 promotion.
- Randomize learned spells - The spells all character will learn get shuffled. No new spells are added except for the two special exceptions stated above. If a character joins in a "magic exclusive" class that is expected to gain exp from magic and not weapon combat, they will get a starter spell from among [Heal, Blaze, Freeze, Blast] as their level 1 spell so long as they join at or before Ribble (May). The level spells are learned are based on when the character originally learned spells. Any spells that has at least 2 levels can be replaced by any other spell with at least 2 levels. Each will be assigned randomly to the set of levels the original could be learned at. This has necessitated adding some slots for characters with level 2 or 3 spells. They aren't used unless you randomize the spells. Also, due to a game engine limitation, no character can learn 16 spells. At least one spell must be a level 2 or 3 spell for this reason.
- Randomize learned spell levels - Must randomize spells also. For all classes except Ninja and Sorcerer, all spells can be learned randomly at any point between 1 and 52. Starter spell rules still apply here. Ninja learns between 22 and 52. Sorcerer learns between 21 and 52. I can see this potentially causing issues if you adjust the effective promo level above 20, but sorcs will still learn their base spell and then get the lower levels if they learn a higher level spell where they don't know the lower level I think.
- Promotion Items - I highly recommend using this option since it will take into account who joins unpromoted. It basically makes a list of every character that could potentially use a promotion item based on who joins unpromoted then randomly selects 6. While it's possible you could get 5 pegasus wings if every centaur joins unpromoted, the alternative is worse. You could get no centaurs and then the pegasus wing would have no use if you don't let the randomizer replace it.
- Stat growth type - Every stat will now get a random growth type. No logic is applied here, so your Bowie replacement could get all late growths making the early game very hard. That is statistically unlikely though.
- Stats - There is a positive and negative change field. Every character's base and max stats will be between neg/100 * x and (100+pos)/100 * x. There is a minimum of 1 in every stat that starts above 0. If the max stat is now lower than the base, they will just be made equal and will never grow. Well, unless they are promoted and their stat is lower than the minimum. In that case they will get the pity growth point until they get to the base/max. There's a max of 100 in each field. High values for the positive adjustment can easily lead to some characters hitting the stat cap of 200.
- Level adjustment - Ever had a game where the promoted characters were just disappointing compared to the ones you trained in the early game? Well, this is because the base stats are defined based on an expected promotion level of 20. If you don't promote your characters until level 30 or 40, then there's no way they can compete. This fixes that problem. The first field will essentially level the character to that level through their unpromoted class then adjust the stats of their promoted class so they will have effectively leveled before promoting. Characters should remain competitive for the entire game. The minimum value for this is 24 because I didn't feel like lowering the cap on charactrers that join over 20. The second option changes the level you can promote at as well as what level the game will add when determining spells learning and exp gain. Changing this can make things either extremely easy or much harder.

The game only has growth tables for up to level 30. Every level beyond this gets effectively 1.5 times the average growth between levels 1 and 30. So be careful when you adjust levels since early 
promotion below 20 can really break any game balance in the late game. 

I did not test this with every combination of options. I personally like turning everything on, setting stat random to +-50, and adjusting the promotion effective level to 30. +=50 stats can be
very extreme and make the early game very challenging if you are playing on modified Ouch difficulty. For new players of the disasm, Ouch difficulty now has 1.56x enemy att and 1.5x enemy agi.
Super in the base game has 1.25x enemy att.

## Patches

The disasm includes a number of patches that can be applied to change some game features. I have included a window to allow you to change them without having to open a text editor and change them in
sf2patches.asm. It saves automatically when the window is closed. All fixes included with the disasm are applied automatically. 

## Stat viewer

Due to the nature of randomization, it's possible you might want to review how good or bad characters are after randomization or maybe just the order you recruit. By default, who joins and where is 
not shown in case you want to keep the mystery. There is a checkbox to reveal the randomized characters. They replace the character above them. 

Clicking on a character button will open a viewer of their stats and spells as well as their promotions' stats and spells. This will still work even if you don't have them revealed. Obviously, their 
name will be shown in the stats screen. Clicking a new character moves the previous one to the second area so you can compare them. 

## Build

Once you are happy with the randomization, the build button will perform a standard build of the game then put the resulting file in sf2.bin in the root directory. 
