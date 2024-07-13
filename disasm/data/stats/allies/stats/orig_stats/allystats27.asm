
; ASM FILE data\stats\allies\stats\allystats27.asm :
; 0x1EE782..0x1EE7AD : Ally stats 27
AllyStats27:    forClass  MAGE_4
                hpGrowth  11, 36, MIDDLE
                mpGrowth  7, 56, EARLY
                attGrowth 4, 20, LINEAR
                defGrowth 3, 23, MIDDLE
                agiGrowth 7, 37, LINEAR
                spellList &
				    1, BLAZE, &
                    5, FREEZE, &
                    10, BLAZE|LV2, &
                    15, FREEZE|LV2, &
                    22, FREEZE|LV3, &
                    35, BOLT, &
                    36, DISPEL, &
                    38, BOLT|LV2, &
                    40, FREEZE|LV4, &
                    42, BOLT|LV3, &
                    46, BOLT|LV4, &
                    49, BLAZE|LV3, &
                    52, BLAZE|LV4
                
                forClass  WIZ
                hpGrowth  28, 83, LINEAR
                mpGrowth  42, 88, LINEAR
                attGrowth 15, 29, LINEAR
                defGrowth 17, 61, MIDDLE
                agiGrowth 27, 58, LINEAR
                useFirstSpellList
                
                forClass  SORC_4
                hpGrowth  28, 83, LINEAR
                mpGrowth  42, 96, LINEAR
                attGrowth 15, 29, LINEAR
                defGrowth 17, 64, MIDDLE
                agiGrowth 27, 46, LINEAR
                spellList &
                    21, DAO, &
                    25, ATLAS, &
                    29, NEPTUN, &
                    34, APOLLO, &
                    38, ATLAS|LV2, &
                    43, DAO|LV2, &
                    47, APOLLO|LV2, &
                    52, NEPTUN|LV2
                
