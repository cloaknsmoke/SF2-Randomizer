
; ASM FILE data\stats\allies\stats\allystats22.asm :
; 0x1EE6FB..0x1EE726 : Ally stats 22
AllyStats22:    forClass  PRST
                hpGrowth  8, 41, LINEAR
                mpGrowth  7, 43, MIDDLE
                attGrowth 5, 24, LINEAR
                defGrowth 5, 24, LINEAR
                agiGrowth 6, 30, LINEAR
                spellList &
                    1, HEAL, &
                    4, DETOX, &
                    11, HEAL|LV2, &
                    15, DETOX|LV2, &
                    29, AURA, &
                    32, DETOX|LV3, &
                    35, AURA|LV2, &
                    37, DETOX|LV4, &
                    40, AURA|LV3, &
                    42, ATTACK, &
                    45, AURA|LV4, &
                    49, HEAL|LV3, &
                    52, HEAL|LV4
                
                forClass  VICR
                hpGrowth  30, 81, LINEAR
                mpGrowth  32, 74, LINEAR
                attGrowth 18, 42, LINEAR
                defGrowth 18, 59, LATE
                agiGrowth 22, 58, LINEAR
                useFirstSpellList
				
				forClass  MMNK
                hpGrowth  30, 81, LINEAR
                mpGrowth  32, 61, LINEAR
                attGrowth 18, 73, LINEAR
                defGrowth 18, 71, MIDDLE
                agiGrowth 22, 58, LINEAR
                useFirstSpellList
                
