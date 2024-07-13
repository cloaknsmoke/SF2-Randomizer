
; ASM FILE data\stats\allies\stats\allystats25.asm :
; 0x1EE748..0x1EE771 : Ally stats 25
AllyStats25:    forClass  PRST
                hpGrowth  8, 40, LINEAR
                mpGrowth  7, 45, EARLYANDLATE
                attGrowth 6, 25, LINEAR
                defGrowth 5, 26, LINEAR
                agiGrowth 5, 29, LINEAR
                spellList &
                    1, HEAL, &
                    5, HEAL|LV2, &
                    7, BLAST, &
                    11, MUDDLE, &
                    18, BLAST|LV2, &
                    20, BOOST, &
                    36, HEAL|LV3, &
                    38, BLAST|LV3, &
                    41, MUDDLE|LV2, &
                    44, BOOST|LV2, &
                    47, BLAST|LV4, &
                    51, HEAL|LV4
                
                forClass  VICR
                hpGrowth  29, 79, LINEAR
                mpGrowth  31, 79, LINEAR
                attGrowth 19, 21, LINEAR
                defGrowth 19, 51, EARLY
                agiGrowth 21, 61, LINEAR
                useFirstSpellList
				
				forClass  MMNK
                hpGrowth  29, 79, LINEAR
                mpGrowth  31, 65, LINEAR
                attGrowth 19, 36, LINEAR
                defGrowth 19, 61, EARLYANDLATE
                agiGrowth 21, 62, LINEAR
                useFirstSpellList
                
