
; ASM FILE data\stats\allies\stats\allystats21.asm :
; 0x1EE6DA..0x1EE6FB : Ally stats 21
AllyStats21:    forClass  MAGE_3
                hpGrowth  9, 32, EARLY
                mpGrowth  6, 57, EARLY
                attGrowth 4, 19, LINEAR
                defGrowth 3, 24, LINEAR
                agiGrowth 7, 37, LINEAR
                spellList &
                    1, BLAZE, &
                    4, BLAZE|LV2, &
                    9, FREEZE, &
                    12, FREEZE|LV2, &
                    17, BOLT, &
                    22, BOLT|LV2, &
                    26, DESOUL, &
					27, DESOUL|LV2, &
                    30, BOLT|LV3, &
                    35, BOLT|LV4, &
                    39, FREEZE|LV3, &
                    43, FREEZE|LV4, &
                    48, BLAZE|LV3, &
                    52, BLAZE|LV4
                
                forClass  WIZ
                hpGrowth  24, 72, LINEAR
                mpGrowth  42, 78, LINEAR
                attGrowth 14, 26, LINEAR
                defGrowth 17, 50, LINEAR
                agiGrowth 26, 86, LINEAR
                useFirstSpellList
                
                forClass  SORC_3
                hpGrowth  24, 72, LINEAR
                mpGrowth  42, 85, LINEAR
                attGrowth 14, 26, LINEAR
                defGrowth 17, 53, LINEAR
                agiGrowth 26, 68, LINEAR
                spellList &
                    21, DAO, &
                    31, APOLLO, &
                    34, DAO|LV2, &
                    38, APOLLO|LV2, &
                    41, NEPTUN, &
                    44, ATLAS, &
                    47, NEPTUN|LV2, &
                    52, ATLAS|LV2
                
