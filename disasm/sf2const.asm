; SF2CONST.ASM INCLUDED AT START OF SF2.ASM

; START OF SEGMENT SRAM OFFSETS FROM SRAM:00200000 TO 0:00204000
byte_200000: equ $200000
SRAM_START: equ $200001
SAVED_ERRCODE_BYTE0: equ $200081
SAVED_ERRCODE_BYTE1: equ $200083
SAVED_ERRCODE_BYTE2: equ $200085
SAVED_ERRCODE_BYTE3: equ $200087
SAVED_ERRCODE_BYTE4: equ $200089
SAVED_ERRCODE_BYTE5: equ $20008B
SAVED_ERRCODE_BYTE6: equ $20008D
SAVED_ERRCODE_BYTE7: equ $20008F

saveSlotsStart = $2000B1

                rsset saveSlotsStart
SAVE1_DATA:     rs.b SAVE_SLOT_SIZE
SRAM_STRING:    rs.b SRAM_STRING_LENGTH
SAVE_FLAGS:     rs.b SAVE_FLAGS_SIZE
SAVE1_CHECKSUM: rs.b SAVE_CHECKSUM_SIZE
SAVE2_CHECKSUM: rs.b SAVE_CHECKSUM_SIZE
SAVE2_DATA:     rs.b SAVE_SLOT_SIZE

savedDataTotalSize = (__RS-saveSlotsStart)/2

SAVED_DATA_TOTAL_SIZE: equ savedDataTotalSize

    if (SAVED_DATA_TOTAL_SIZE>SRAM_SIZE)
        inform 3,"Fatal error: Excessive SRAM usage. Current=%d Max=%d",SAVED_DATA_TOTAL_SIZE,SRAM_SIZE
    endif

; END OF SEGMENT SRAM OFFSETS FROM SRAM:00200000 TO 0:00204000

; START OF SEGMENT Z80 OFFSETS FROM Z80:A00000 TO 0:00A0FFFF
Z80_Memory: equ $A00000

z80Channel1NotInUse = $A01383
    if (STANDARD_BUILD=1)
z80Channel1NotInUse = $A01813
    endif
Z80_CHANNEL_1_NOT_IN_USE: equ z80Channel1NotInUse

Z80_SoundDriverFadeInData: equ $A01FFC
Z80_SoundDriverMusicLevel: equ $A01FFD
Z80_SoundDriverCommand: equ $A01FFF
; END OF SEGMENT Z80 OFFSETS FROM Z80:A00000 TO 0:00A0FFFF

; START OF SEGMENT IO OFFSETS FROM IO:A10000 TO 0:00A10FFF
HW_Info: equ $A10001
DATA1: equ $A10003
DATA2: equ $A10005
DATA3: equ $A10007
CTRL1: equ $A10008
CTRL1_BIS: equ $A10009
CTRL2: equ $A1000B
CTRL3: equ $A1000C
CTRL3_BIS: equ $A1000D
TxDATA1: equ $A1000F
RxDATA1: equ $A10011
SCTRL1: equ $A10013
TxDATA2: equ $A10015
RxDATA2: equ $A10017
SCTRL2: equ $A10019
TxDATA3: equ $A1001B
RxDATA3: equ $A1001D
SCTRL3: equ $A1001F
; END OF SEGMENT IO OFFSETS FROM IO:A10000 TO 0:00A10FFF

; START OF SEGMENT Control OFFSETS FROM Control:A11000 TO 0:00A11FFF
MemMode: equ $A11000
Z80BusReq: equ $A11100
Z80BusReset: equ $A11200
; END OF SEGMENT Control OFFSETS FROM Control:A11000 TO 0:00A11FFF

; START OF SEGMENT VDP OFFSETS FROM VDP:00C00000 TO 0:00C00012
VDP_Data: equ $C00000
VDP_Control: equ $C00004
HV_Counter: equ $C00008
PSG: equ $C00011
; END OF SEGMENT VDP OFFSETS FROM VDP:00C00000 TO 0:00C00012

; START OF SEGMENT RAM OFFSETS FROM RAM:FF0000 TO 0:01000000
FF0000_RAM_START: equ $FF0000
byte_FF0C00: equ $FF0C00
FF1000_MAP_TILESET_4: equ $FF1000
FF2000_LOADING_SPACE: equ $FF2000
FF3000_MAP_TILESET_1: equ $FF3000
FF3800_LOADING_SPACE: equ $FF3800
byte_FF4000: equ $FF4000
FF4400_LOADING_SPACE: equ $FF4400
byte_FF4A00: equ $FF4A00
FF4D00_LOADING_SPACE: equ $FF4D00
FF5000_LOADING_SPACE: equ $FF5000
FF5600_LOADING_SPACE: equ $FF5600
word_FF5C00: equ $FF5C00
word_FF5C02: equ $FF5C02
word_FF5C04: equ $FF5C04
word_FF5C06: equ $FF5C06
byte_FF5C08: equ $FF5C08
BATTLE_TERRAIN_ARRAY: equ $FF5F00
MAP_LAYOUT_HISTORY_MAP_SIZES: equ $FF6000
FF6800_MAP_LOADING_LEFT_HISTORY_MAP: equ $FF6800
FF6802_LOADING_SPACE: equ $FF6802
byte_FF6942: equ $FF6942
byte_FF6C02: equ $FF6C02
byte_FF7002: equ $FF7002
byte_FF7402: equ $FF7402
byte_FF7802: equ $FF7802
FF7A02_LOADING_SPACE: equ $FF7A02
byte_FF7C02: equ $FF7C02
FF8002_LOADING_SPACE: equ $FF8002
FF8800_MAP_LOADING_UPPER_HISTORY_MAP: equ $FF8800
FF8804_LOADING_SPACE: equ $FF8804
TEMP_NAME_ENTRY_SPACE: equ $FF8805
TARGETS_REACHABLE_BY_SPELL_NUMBER: equ $FF8806
TARGETS_REACHABLE_BY_ITEM_NUMBER: equ $FF8808
byte_FF8809: equ $FF8809
ATTACK_COMMAND_ITEM_SLOT: equ $FF880A
ATTACK_COMMAND_SPELL: equ $FF880C
TARGETS_REACHABLE_BY_ATTACK_LIST: equ $FF880E
TARGETS_REACHABLE_BY_SPELL_LIST: equ $FF883E
TARGETS_REACHABLE_BY_ITEM_LIST: equ $FF886E
ATTACK_MOVEMENT_TO_REACHABLE_TARGETS: equ $FF889E
SPELL_MOVEMENT_TO_REACHABLE_TARGETS: equ $FF88CE
ITEM_MOVEMENT_TO_REACHABLE_TARGETS: equ $FF88FE
byte_FF8904: equ $FF8904
ATTACK_TARGET_PRIORITIES_LIST: equ $FF892E
SPELL_TARGET_PRIORITIES_LIST: equ $FF895E
byte_FF8984: equ $FF8984
ITEM_TARGET_PRIORITIES_LIST: equ $FF898E
FF8A04_LOADING_SPACE: equ $FF8A04
byte_FF8A44: equ $FF8A44
byte_FF8B04: equ $FF8B04
FF8C02_LOADING_SPACE: equ $FF8C02
byte_FF8C84: equ $FF8C84
byte_FF8D04: equ $FF8D04
byte_FF8E04: equ $FF8E04
byte_FF8EC4: equ $FF8EC4
byte_FF8F04: equ $FF8F04
ENEMY_BATTLESPRITE_UNCOMP_SPACE: equ $FF9002
FF9004_LOADING_SPACE: equ $FF9004
byte_FF9104: equ $FF9104
byte_FF9202: equ $FF9202
byte_FF9284: equ $FF9284
word_FF9802: equ $FF9802
BATTLE_ENTITY_MOVE_STRING: equ $FF9804
byte_FF9904: equ $FF9904
byte_FF9984: equ $FF9984
byte_FF9A04: equ $FF9A04
byte_FF9A84: equ $FF9A84
CURRENT_MAP_TILESET_2_COPY: equ $FF9B04
FF9C02_LOADING_SPACE: equ $FF9C02
FFA202_LOADING_SPACE: equ $FFA202
VIEW_PLANE_A_X_COUNTER: equ $FFA804
VIEW_PLANE_B_X_COUNTER: equ $FFA806
VIEW_PLANE_A_Y_COUNTER: equ $FFA808
VIEW_PLANE_B_Y_COUNTER: equ $FFA80A
QUAKE_AMPLITUDE: equ $FFA80C
TILE_PALETTE_MASK: equ $FFA80E
VIEW_PLANE_A_PIXEL_X: equ $FFA810
VIEW_PLANE_A_PIXEL_Y: equ $FFA812
VIEW_PLANE_B_PIXEL_X: equ $FFA814
VIEW_PLANE_B_PIXEL_Y: equ $FFA816
word_FFA818: equ $FFA818
word_FFA81A: equ $FFA81A
word_FFA81C: equ $FFA81C
word_FFA81E: equ $FFA81E
word_FFA820: equ $FFA820
word_FFA822: equ $FFA822
word_FFA824: equ $FFA824
word_FFA826: equ $FFA826
word_FFA828: equ $FFA828
VIEW_SCROLLING_PLANES_BITFIELD: equ $FFA82A
VIEW_TARGET_ENTITY: equ $FFA82C
VIEW_PLANE_UPDATE_TRIGGERS: equ $FFA82D
MAP_AREA_LAYER1_STARTX: equ $FFA82E
MAP_AREA_LAYER1_STARTY: equ $FFA830
MAP_AREA_LAYER1_ENDX: equ $FFA832
MAP_AREA_LAYER1_ENDY: equ $FFA834
MAP_AREA_LAYER2_STARTX: equ $FFA836
MAP_AREA_LAYER2_STARTY: equ $FFA838
MAP_AREA_BACKGROUND_STARTX: equ $FFA83A
MAP_AREA_BACKGROUND_STARTY: equ $FFA83C
MAP_AREA_LAYER1_PARALLAX_X: equ $FFA83E
MAP_AREA_LAYER1_PARALLAX_Y: equ $FFA840
MAP_AREA_LAYER2_PARALLAX_X: equ $FFA842
MAP_AREA_LAYER2_PARALLAX_Y: equ $FFA844
MAP_AREA_LAYER1_AUTOSCROLL_X: equ $FFA846
MAP_AREA_LAYER1_AUTOSCROLL_Y: equ $FFA847
MAP_AREA_LAYER2_AUTOSCROLL_X: equ $FFA848
MAP_AREA_LAYER2_AUTOSCROLL_Y: equ $FFA849
MAP_EVENT_TYPE: equ $FFA84A
MAP_EVENT_PARAM_1: equ $FFA84C
MAP_EVENT_PARAM_2: equ $FFA84D
MAP_EVENT_PARAM_3: equ $FFA84E
MAP_EVENT_PARAM_4: equ $FFA84F
MAP_EVENT_PARAM_5: equ $FFA850
TILE_ANIMATION_DATA_ADDRESS: equ $FFA86A
TILE_ANIMATION_COUNTER: equ $FFA86E
TILE_ANIMATION_MAP_INDEX: equ $FFA870
WINDOW_LAYOUTS_END: equ $FFA87A
WINDOW_ENTRIES: equ $FFA87E
byte_FFA8FE: equ $FFA8FE
byte_FFA8FF: equ $FFA8FF
MOVING_WINDOWS_BITFIELD: equ $FFA900
ENTITY_DATA: equ $FFA902
ENTITY_Y: equ $FFA904
ENTITY_X_DEST: equ $FFA90E
ENTITY_Y_DEST: equ $FFA910
ENTITY_FACING: equ $FFA912
ENTITY_MAPSPRITE: equ $FFA915
ENTITY_ANIMATION_COUNTER: equ $FFA920
OTHER_ENTITIES_DATA: equ $FFA922
ENTITY_RAFT_DATA: equ $FFACE2
ENTITY_SPECIAL_SPRITE_DATA: equ $FFAEE2
ENTITY_SPECIAL_SPRITE_DESTINATION: equ $FFAEEE
ENTITY_SPECIAL_SPRITE_LAYER: equ $FFAEF3
ENTITY_UNIT_CURSOR_DATA: equ $FFAF02
FOLLOWERS_LIST: equ $FFAF22
byte_FFAF23: equ $FFAF23
byte_FFAF26: equ $FFAF26
word_FFAF42: equ $FFAF42
SPRITE_SIZE: equ $FFAF44
MAP_AREA_LAYER_TYPE: equ $FFAF46
byte_FFAF47: equ $FFAF47
SPRITES_TO_LOAD_NUMBER: equ $FFAF67
byte_FFAF69: equ $FFAF69
byte_FFAF6A: equ $FFAF6A
byte_FFAF6B: equ $FFAF6B
TEXT_WINDOW_INDEX: equ $FFAF6C
DIALOGUE_VDPTILE_ROW_SCROLLING_OFFSET: equ $FFAF6E
STRING_BYTE: equ $FFAF70
STRING_BIT_COUNTER: equ $FFAF72
DECODED_TEXT_SYMBOL: equ $FFAF74
MINISTATUS_WINDOW_INDEX: equ $FFAF76
DISPLAYED_ICON_1: equ $FFAF7A
DISPLAYED_ICON_2: equ $FFAF7C
DISPLAYED_ICON_3: equ $FFAF7E
DISPLAYED_ICON_4: equ $FFAF80
LEVELUP_ARGUMENTS: equ $FFAF82
CURRENT_MEMBERSUMMARY_PAGE: equ $FFAF8C
UNIT_CURSOR_RADIUS: equ $FFAF8E
BATTLE_ENTITY_CHOSEN_X: equ $FFAF90
BATTLE_ENTITY_CHOSEN_Y: equ $FFAF91
IS_TARGETING: equ $FFAF93
word_FFAF9E: equ $FFAF9E
byte_FFAFA0: equ $FFAFA0
byte_FFAFA1: equ $FFAFA1
dword_FFAFAA: equ $FFAFAA
word_FFAFAE: equ $FFAFAE
byte_FFAFB0: equ $FFAFB0
byte_FFAFB1: equ $FFAFB1
word_FFAFB2: equ $FFAFB2
byte_FFAFB4: equ $FFAFB4
byte_FFAFC6: equ $FFAFC6
byte_FFAFCE: equ $FFAFCE
CURRENT_DIAMENU_CHOICE: equ $FFAFE7
SPEECH_SOUND_TOGGLE: equ $FFAFFB
BLINK_TILE_NUMBER: equ $FFAFFE
BLINK_DATA: equ $FFB000
BLINK_COUNTER: equ $FFB03C
MOUTH_TILE_NUMBER: equ $FFB03E
MOUTH_DATA: equ $FFB040
word_FFB07C: equ $FFB07C
word_FFB07E: equ $FFB07E
PORTRAIT_WINDOW_INDEX: equ $FFB080
BLINK_CONTROL_TOGGLE: equ $FFB082
CURRENTLY_TYPEWRITING: equ $FFB083
PORTRAIT_IS_FLIPPED: equ $FFB084
PORTRAIT_IS_ON_RIGHT: equ $FFB085
word_FFB086: equ $FFB086
LAND_EFFECT_WINDOW_INDEX: equ $FFB088
TIMER_WINDOW_INDEX: equ $FFB08A
ALLY_NAME_WINDOW_INDEX: equ $FFB08C
word_FFB08E: equ $FFB08E
word_FFB090: equ $FFB090
word_FFB092: equ $FFB092
word_FFB094: equ $FFB094
MINISTATUS_WINDOW_WIDTH: equ $FFB096
MOVE_SFX: equ $FFB098
CURRENT_SAVE_SLOT: equ $FFB09A
SPEECH_SFX: equ $FFB09C
SPEECH_SFX_BACKUP: equ $FFB09E
CURRENT_PORTRAIT: equ $FFB0A0
SOUND_COMMANDS_DEACTIVATED: equ $FFB0A3
ROM_CHECKSUM: equ $FFB0A4
SPECIAL_TURBO_TOGGLE: equ $FFB0A8
DEBUG_MODE_TOGGLE: equ $FFB0A9
CONTROL_OPPONENT_CHEAT: equ $FFB0AA
AUTO_BATTLE_CHEAT: equ $FFB0AB
CONFIGURATION_MODE_ACTIVATED: equ $FFB0AC
MAP_AREA_MUSIC_INDEX: equ $FFB0AD
GENERIC_LIST: equ $FFB0AE
GENERIC_LIST_LENGTH: equ $FFB12E
CURRENT_ITEMLIST_PAGE: equ $FFB130
CURRENT_ITEMLIST_SELECTION: equ $FFB132
word_FFB134: equ $FFB134
DISPLAYED_MEMBERLIST_FIRST_ENTRY: equ $FFB136
DISPLAYED_MEMBERLIST_SELECTED_ENTRY: equ $FFB138
SELECTED_ITEM_INDEX: equ $FFB13A
byte_FFB13C: equ $FFB13C
CURRENT_MEMBERLIST_PAGE: equ $FFB13D
WINDOW_IS_PRESENT: equ $FFB13F
ENTITY_EVENT_INDEX_LIST: equ $FFB140
byte_FFB160: equ $FFB160
byte_FFB16F: equ $FFB16F
CHEST_CONTENTS: equ $FFB180
BATTLESCENE_MUSIC_INDEX: equ $FFB188
MOVING_BATTLE_ENTITY_INDEX: equ $FFB18A
word_FFB18C: equ $FFB18C
BATTLE_EQUIP_WINDOW_SLOT: equ $FFB18E
VIEW_SCROLLING_SPEED: equ $FFB194
word_FFB196: equ $FFB196
byte_FFB198: equ $FFB198
DEACTIVATE_WINDOW_HIDING: equ $FFB199
HIDE_WINDOWS: equ $FFB19A
AFTER_INTRO_JUMP_OFFSET: equ $FFB19C
ENTITY_WALKING_PARAMS: equ $FFB1A0
dword_FFB1A4: equ $FFB1A4
WARP_SFX: equ $FFB1A8
CONFMODE_AND_CREDITS_SEQUENCE_POINTER: equ $FFB1AA
AI_LAST_TARGET_TABLE: equ $FFB1AC
byte_FFB1DC: equ $FFB1DC
BATTLE_REGION_FLAGS_TO_BE_TRIGGERED: equ $FFB20C
dword_FFB3C0: equ $FFB3C0
word_FFB3C4: equ $FFB3C4
dword_FFB3C6: equ $FFB3C6
word_FFB3CA: equ $FFB3CA
BATTLESCENE_FRAME_COUNTER: equ $FFB3CC
byte_FFB3CD: equ $FFB3CD
BATTLESCENE_ENEMY: equ $FFB3CE
BATTLESCENE_ENEMYBATTLESPRITE: equ $FFB3D0
BATTLESCENE_ENEMYBATTLEPALETTE: equ $FFB3D2
BATTLESCENE_ALLY: equ $FFB3D4
BATTLESCENE_ALLYBATTLESPRITE: equ $FFB3D6
BATTLESCENE_ALLYBATTLEPALETTE: equ $FFB3D8
BATTLESCENE_WEAPONSPRITE: equ $FFB3DA
BATTLESCENE_WEAPONPALETTE: equ $FFB3DC
BATTLESCENE_ENEMYBATTLESPRITE_ANIMATION_SPEED: equ $FFB3DE
BATTLESCENE_ENEMYBATTLESPRITE_ANIMATION_COUNTER: equ $FFB3E0
BATTLESCENE_ALLYBATTLESPRITE_ANIMATION_SPEED: equ $FFB3E2
BATTLESCENE_ALLYBATTLESPRITE_ANIMATION_COUNTER: equ $FFB3E4
BATTLESCENE_ENEMYBATTLEANIMATION: equ $FFB3E6
BATTLESCENE_ALLYBATTLEANIMATION: equ $FFB3E8
word_FFB3EA: equ $FFB3EA
word_FFB3EC: equ $FFB3EC
word_FFB3EE: equ $FFB3EE
word_FFB3F0: equ $FFB3F0
word_FFB3F2: equ $FFB3F2
word_FFB3F4: equ $FFB3F4
word_FFB3F6: equ $FFB3F6
word_FFB3F8: equ $FFB3F8
word_FFB3FA: equ $FFB3FA
word_FFB3FC: equ $FFB3FC
word_FFB3FE: equ $FFB3FE
BATTLESCENE_ALLY_COPY: equ $FFB400
DEAD_COMBATANTS_LIST_LENGTH: equ $FFB402
byte_FFB404: equ $FFB404
byte_FFB406: equ $FFB406
byte_FFB41E: equ $FFB41E
byte_FFB496: equ $FFB496
byte_FFB532: equ $FFB532
dword_FFB536: equ $FFB536
byte_FFB53A: equ $FFB53A
BATTLESCENE_BACKGROUND_PALETTE: equ $FFB542
word_FFB562: equ $FFB562
byte_FFB568: equ $FFB568
byte_FFB569: equ $FFB569
byte_FFB56A: equ $FFB56A
byte_FFB56B: equ $FFB56B
ACTOR_TO_MAKE_IDLE: equ $FFB56C
byte_FFB56D: equ $FFB56D
byte_FFB56E: equ $FFB56E
byte_FFB56F: equ $FFB56F
WEAPON_FRAME_INDEX: equ $FFB570
WEAPON_FRAME_LAYER: equ $FFB571
WEAPON_FRAME_X: equ $FFB572
WEAPON_FRAME_Y: equ $FFB573
WEAPON_IDLE_FRAME1_INDEX: equ $FFB574
WEAPON_IDLE_FRAME1_X: equ $FFB576
WEAPON_IDLE_FRAME1_Y: equ $FFB577
WEAPON_IDLE_FRAME2_X: equ $FFB578
WEAPON_IDLE_FRAME2_Y: equ $FFB579
ALLY_BATTLESPRITE_PROP1: equ $FFB57A
ALLY_BATTLESPRITE_PROP2: equ $FFB57B
ENEMY_BATTLESPRITE_PROP1: equ $FFB57C
ENEMY_BATTLESPRITE_PROP2: equ $FFB57D
BATTLESCENE_ALLY_STATUS_ANIMATION: equ $FFB57E
BATTLESCENE_ENEMY_STATUS_ANIMATION: equ $FFB57F
byte_FFB580: equ $FFB580
byte_FFB581: equ $FFB581
BATTLESCENE_BACKGROUND: equ $FFB582
byte_FFB583: equ $FFB583
byte_FFB584: equ $FFB584
byte_FFB585: equ $FFB585
SPELLANIMATION_VARIATION_AND_MIRRORED_BIT: equ $FFB586
CURRENT_SPELLANIMATION: equ $FFB587
byte_FFB588: equ $FFB588
byte_FFB589: equ $FFB589
DEAD_COMBATANTS_LIST: equ $FFB58A
byte_FFB59A: equ $FFB59A
BATTLESCENE_GOLD: equ $FFB62A
BATTLESCENE_EXP: equ $FFB62C
CURRENT_BATTLEACTION: equ $FFB62E
BATTLEACTION_ITEM_OR_SPELL: equ $FFB630
BATTLEACTION_ITEM_OR_SPELL_COPY: equ $FFB632
BATTLEACTION_ITEM_SLOT: equ $FFB634
BATTLESCENE_ATTACK_TYPE: equ $FFB636
BATTLESCENE_SPELL_INDEX: equ $FFB638
BATTLESCENE_SPELL_LEVEL: equ $FFB63A
BATTLESCENE_ITEM: equ $FFB63C
TARGETS_LIST_LENGTH: equ $FFB63E
BATTLE_PARTY_MEMBERS_NUMBER: equ $FFB640
OTHER_PARTY_MEMBERS_NUMBER: equ $FFB642
CUTSCENE_DIALOG_INDEX: equ $FFB646
SKIP_CUTSCENE_TEXT: equ $FFB648
BATTLESCENE_FIRST_ALLY: equ $FFB64A
BATTLESCENE_LAST_ALLY: equ $FFB64B
BATTLESCENE_FIRST_ENEMY: equ $FFB64C
BATTLESCENE_LAST_ENEMY: equ $FFB64D
BATTLESCENE_ATTACKER: equ $FFB64E
BATTLESCENE_ATTACKER_COPY: equ $FFB64F
byte_FFB651: equ $FFB651
TARGETS_LIST: equ $FFB652
byte_FFB653: equ $FFB653
BATTLE_PARTY_MEMBERS: equ $FFB682
RESERVE_MEMBERS: equ $FFB68E
ENEMY_LIST: equ $FFB6A2
MOVE_COSTS_TABLE: equ $FFB6C2
CURRENT_SHOP_INDEX: equ $FFB6D2
DIALOGUE_TYPEWRITING_CURRENT_X: equ $FFB6D4
DIALOGUE_TYPEWRITING_CURRENT_Y: equ $FFB6D5
USE_REGULAR_DIALOGUE_FONT: equ $FFB6D6
COMPRESSED_STRING_LENGTH: equ $FFB6D7
byte_FFB6D8: equ $FFB6D8
TEXT_NAME_INDEX_1: equ $FFB6E8
TEXT_NAME_INDEX_2: equ $FFB6EA
TEXT_NAME_INDEX_3: equ $FFB6EC
DIALOGUE_STRING_TO_PRINT: equ $FFB6F0
TEXT_NUMBER: equ $FFB776
CURRENT_ITEM_PRICE: equ $FFB778
CURRENT_DIALOGUE_ASCII_BYTE_ADDRESS: equ $FFB77A
COMPRESSED_STRING_POINTER: equ $FFB77E
CURRENT_DIALOGUE_NAME_INDEX_ADDRESS: equ $FFB782
EQUIPPABLE_ITEMS: equ $FFB786
WINDOW_TILE_LAYOUTS: equ $FFB800
byte_FFB812: equ $FFB812
byte_FFB852: equ $FFB852
PLANE_A_MAP_LAYOUT: equ $FFC000
byte_FFC180: equ $FFC180
byte_FFC1B8: equ $FFC1B8
byte_FFC286: equ $FFC286
byte_FFC350: equ $FFC350
byte_FFC358: equ $FFC358
byte_FFC398: equ $FFC398
byte_FFC41A: equ $FFC41A
byte_FFC480: equ $FFC480
PLANE_A_MAP_AND_WINDOWS_LAYOUT: equ $FFC800
byte_FFCC86: equ $FFCC86
PALETTE_1_CURRENT: equ $FFD000
PALETTE_1_CURRENT_01: equ $FFD002
PALETTE_1_CURRENT_02: equ $FFD004
PALETTE_2_CURRENT: equ $FFD020
PALETTE_3_CURRENT: equ $FFD040
PALETTE_3_CURRENT_02: equ $FFD044
PALETTE_4_CURRENT: equ $FFD060
PALETTE_1_BASE: equ $FFD080
PALETTE_1_BASE_01: equ $FFD082
PALETTE_1_BASE_02: equ $FFD084
PALETTE_1_BASE_0E: equ $FFD09C
PALLETE_2_BASE: equ $FFD0A0
PALETTE_3_BASE: equ $FFD0C0
PALETTE_4_BASE: equ $FFD0E0
HORIZONTAL_SCROLL_DATA: equ $FFD100
byte_FFD1C0: equ $FFD1C0
VERTICAL_SCROLL_DATA: equ $FFD500
DMA_QUEUE: equ $FFD550
VDP_COMMAND_QUEUE: equ $FFD780
byte_FFDB80: equ $FFDB80
SPRITE_TABLE: equ $FFDC80
SPRITE_00_LINK: equ $FFDC83
SPRITE_00_TILE_FLAGS: equ $FFDC84
SPRITE_01: equ $FFDC88
SPRITE_01_TILE_FLAGS: equ $FFDC8C
SPRITE_03: equ $FFDC98
SPRITE_04: equ $FFDCA0
SPRITE_04_TILE_FLAGS: equ $FFDCA4
SPRITE_05: equ $FFDCA8
SPRITE_07: equ $FFDCB8
SPRITE_07_LINK: equ $FFDCBB
SPRITE_08: equ $FFDCC0
SPRITE_09_LINK: equ $FFDCCB
SPRITE_10: equ $FFDCD0
SPRITE_14: equ $FFDCF0
SPRITE_14_TILE_FLAGS: equ $FFDCF4
SPRITE_14_Y: equ $FFDCF6
SPRITE_16: equ $FFDD00
SPRITE_17: equ $FFDD08
SPRITE_18: equ $FFDD10
SPRITE_19: equ $FFDD18
SPRITE_20: equ $FFDD20
SPRITE_20_TILE_FLAGS: equ $FFDD24
SPRITE_38: equ $FFDDB0
SPRITE_40: equ $FFDDC0
SPRITE_46: equ $FFDDF0
SPRITE_60: equ $FFDE60
SPRITE_63_LINK: equ $FFDE7B
LOADED_NUMBER: equ $FFDE80
byte_FFDE85: equ $FFDE85
VINT_PARAMS: equ $FFDE94
VDP_COMMAND_COUNTER: equ $FFDE95
DMA_QUEUE_SIZE: equ $FFDE96
P1_INPUT: equ $FFDE97
P2_INPUT: equ $FFDE99
CURRENT_PLAYER_INPUT: equ $FFDE9B
PRIMARY_WALKING_DIRECTION: equ $FFDE9C
CONTROLLING_UNIT_CURSOR: equ $FFDE9D
byte_FFDE9E: equ $FFDE9E
byte_FFDE9F: equ $FFDE9F
FRAME_COUNTER: equ $FFDEA0
byte_FFDEA1: equ $FFDEA1
DMA_ADDR_MSBYTE: equ $FFDEA2
RANDOM_SEED: equ $FFDEA4
word_FFDEA6: equ $FFDEA6
word_FFDEA8: equ $FFDEA8
VDP_REG00_STATUS: equ $FFDEAA
VDP_REG01_STATUS: equ $FFDEAC
VDP_REG01_VALUE: equ $FFDEAD
VDP_REG0B_VALUE: equ $FFDEC1
VDP_COMMAND_QUEUE_POINTER: equ $FFDED0
DMA_QUEUE_POINTER: equ $FFDED4
SOUND_COMMAND_QUEUE: equ $FFDED8
MUSIC_STACK_LENGTH: equ $FFDEE0
MUSIC_STACK: equ $FFDEE1
WAIT_FOR_MUSIC_END: equ $FFDEEB
LAST_PLAYER_INPUT: equ $FFDEEC
INPUT_REPEAT_DELAYER: equ $FFDEED
FADING_SETTING: equ $FFDEF0
FADING_COUNTER_MAX: equ $FFDEF2
FADING_POINTER: equ $FFDEF3
FADING_COUNTER: equ $FFDEF4
FADING_PALETTE_BITFIELD: equ $FFDEF5
VINT_ENABLED: equ $FFDEF6
WAITING_NEXT_VINT: equ $FFDEF7
VINT_FUNCS_ENABLED_BITFIELD: equ $FFDEF8
SECONDS_COUNTER_FRAMES: equ $FFDEF9
VINT_FUNC_ADDRS: equ $FFDEFA
SECONDS_COUNTER: equ $FFDF1E
SPECIAL_BATTLE_TIME: equ $FFDF22
GAME_INTRO_SP_OFFSET: equ $FFDF26
PALETTE_1_BACKUP: equ $FFDF2A
PALETTE_2_BACKUP: equ $FFDF4A
FADING_TIMER_WORD: equ $FFDFAA
FADING_TIMER_BYTE: equ $FFDFAB
RANDOM_WAITING_FOR_INPUT: equ $FFDFB0
PLANE_B_LAYOUT: equ $FFE000
byte_FFE0DC: equ $FFE0DC
PLANE_B_WITCH_HEAD: equ $FFE15C
byte_FFE184: equ $FFE184
byte_FFE19C: equ $FFE19C
byte_FFE21E: equ $FFE21E
byte_FFE29E: equ $FFE29E
byte_FFE31C: equ $FFE31C

; Saved Data

savedDataStart = $FFE800

COMBATANT_ENTRIES:          equ savedDataStart+SAVED_DATA_OFFSET_COMBATANT_ENTRIES
CURRENT_GOLD:               equ savedDataStart+SAVED_DATA_OFFSET_CURRENT_GOLD
DEALS_ITEMS:                equ savedDataStart+SAVED_DATA_OFFSET_DEALS_ITEMS
CARAVAN_ITEMS_NUMBER:       equ savedDataStart+SAVED_DATA_OFFSET_CARAVAN_ITEMS_NUMBER
CARAVAN_ITEMS:              equ savedDataStart+SAVED_DATA_OFFSET_CARAVAN_ITEMS
GAME_FLAGS:                 equ savedDataStart+SAVED_DATA_OFFSET_GAME_FLAGS
BATTLE_AREA_X:              equ savedDataStart+SAVED_DATA_OFFSET_BATTLE_AREA_X
BATTLE_AREA_Y:              equ savedDataStart+SAVED_DATA_OFFSET_BATTLE_AREA_Y
BATTLE_AREA_WIDTH:          equ savedDataStart+SAVED_DATA_OFFSET_BATTLE_AREA_WIDTH
BATTLE_AREA_HEIGHT:         equ savedDataStart+SAVED_DATA_OFFSET_BATTLE_AREA_HEIGHT
PLAYER_TYPE:                equ savedDataStart+SAVED_DATA_OFFSET_PLAYER_TYPE
CURRENT_MAP:                equ savedDataStart+SAVED_DATA_OFFSET_CURRENT_MAP
CURRENT_BATTLE:             equ savedDataStart+SAVED_DATA_OFFSET_CURRENT_BATTLE
RAFT_MAP:                   equ savedDataStart+SAVED_DATA_OFFSET_RAFT_MAP
RAFT_X:                     equ savedDataStart+SAVED_DATA_OFFSET_RAFT_X
RAFT_Y:                     equ savedDataStart+SAVED_DATA_OFFSET_RAFT_Y
MESSAGE_SPEED:              equ savedDataStart+SAVED_DATA_OFFSET_MESSAGE_SPEED
DISPLAY_BATTLE_MESSAGES:    equ savedDataStart+SAVED_DATA_OFFSET_DISPLAY_BATTLE_MESSAGES
EGRESS_MAP:                 equ savedDataStart+SAVED_DATA_OFFSET_EGRESS_MAP
BATTLE_TURN_ORDER:          equ savedDataStart+SAVED_DATA_OFFSET_BATTLE_TURN_ORDER
CURRENT_BATTLE_TURN:        equ savedDataStart+SAVED_DATA_OFFSET_CURRENT_BATTLE_TURN
SAVED_SECONDS_COUNTER:      equ savedDataStart+SAVED_DATA_OFFSET_SAVED_SECONDS_COUNTER
SPECIAL_BATTLE_RECORD:      equ savedDataStart+SAVED_DATA_OFFSET_SPECIAL_BATTLE_RECORD
ENEMY_ITEM_DROPPED_FLAGS:   equ savedDataStart+SAVED_DATA_OFFSET_ENEMY_ITEM_DROPPED_FLAGS
MITHRIL_WEAPONS_ON_ORDER:   equ savedDataStart+SAVED_DATA_OFFSET_MITHRIL_WEAPONS_ON_ORDER

ERRCODE_BYTE0: equ $FFFFF8
ERRCODE_BYTE1: equ $FFFFF9
ERRCODE_BYTE2: equ $FFFFFA
ERRCODE_BYTE3: equ $FFFFFB
ERRCODE_BYTE4: equ $FFFFFC
ERRCODE_BYTE5: equ $FFFFFD
ERRCODE_BYTE6: equ $FFFFFE
ERRCODE_BYTE7: equ $FFFFFF
; END OF SEGMENT RAM OFFSETS FROM RAM:FF0000 TO 0:01000000

