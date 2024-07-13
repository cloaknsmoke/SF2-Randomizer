
; ASM FILE data\stats\allies\stats\allystats17.asm :
; 0x1EE628..0x1EE685 : Ally stats 17
AllyStats17:    forClass  MAGE_2
                hpGrowth  8, 28, LINEAR
                mpGrowth  6, 54, EARLY
                attGrowth 4, 22, LINEAR
                defGrowth 3, 27, LINEAR
                agiGrowth 7, 33, LINEAR
                spellList &
                    1, BLAZE, &
                    4, FREEZE, &
                    10, BLAZE|LV2, &
                    19, FREEZE|LV2, &
                    22, SLEEP, &
                    24, BOLT, &
                    27, FREEZE|LV3, &
                    30, BOLT|LV2, &
                    33, FREEZE|LV4, &
                    44, BLAZE|LV3, &
                    47, BOLT|LV3, &
                    49, BLAZE|LV4, &
                    52, BOLT|LV4
                
                forClass  WIZ
                hpGrowth  21, 69, LINEAR
                mpGrowth  40, 80, LINEAR
                attGrowth 16, 30, EARLYANDLATE
                defGrowth 19, 57, EARLY
                agiGrowth 24, 66, LINEAR
                useFirstSpellList
                
                forClass  SORC_2
                hpGrowth  21, 69, LINEAR
                mpGrowth  40, 87, LINEAR
                attGrowth 16, 30, EARLYANDLATE
                defGrowth 19, 60, EARLY
                agiGrowth 24, 58, LINEAR
                spellList &
                    21, DAO, &
                    23, APOLLO, &
                    28, NEPTUN, &
                    32, DAO|LV2, &
                    36, APOLLO|LV2, &
                    40, ATLAS, &
                    45, NEPTUN|LV2, &
                    49, ATLAS|LV2
                
