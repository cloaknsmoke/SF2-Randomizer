
; ASM FILE data\stats\allies\allybattlesprites.asm :
; 0x1F806..0x1F914 : Ally battlesprites table
table_AllyBattlesprites:
                
; Syntax        allyBattleSprAndPlt [CLASS_]enum, [ALLYBATTLESPRITE_]enum, palette
;
; Notes: 3 entries per ally, 3 bytes per entry.
;        Palette range varies depending on the sprite.
;        Constant names ("enums"), shorthands (defined by macro), and numerical indexes are interchangeable.
                
; 0: BOWIE
                allyBattleSprAndPlt SDMN, SDMN, 0
                allyBattleSprAndPlt HERO, HERO, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 1: SARAH
                allyBattleSprAndPlt PRST, PRST, 0
                allyBattleSprAndPlt VICR, VICR, 1
                allyBattleSprAndPlt MMNK, MMNK, 1
                
; 2: CHESTER
                allyBattleSprAndPlt KNTE, KNTE, 0
                allyBattleSprAndPlt PLDN, PLDN, 0
                allyBattleSprAndPlt PGNT, PGNT, 0
                
; 3: JAHA
                allyBattleSprAndPlt WARR, WARR, 0
                allyBattleSprAndPlt GLDT, GLDT, 1
                allyBattleSprAndPlt BRN, BRN, 1
                
; 4: KAZIN
                allyBattleSprAndPlt MAGE_1, MAGE, 0
                allyBattleSprAndPlt WIZ, WIZ, 2
                allyBattleSprAndPlt SORC_1, SORC_MALE, 0
                
; 5: SLADE
                allyBattleSprAndPlt THIF, THIF, 0
                allyBattleSprAndPlt NINJ, NINJ, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 6: KIWI
                allyBattleSprAndPlt TORT, TORT, 0
                allyBattleSprAndPlt MNST, MNST, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 7: PETER
                allyBattleSprAndPlt PHNK, PHNK, 0
                allyBattleSprAndPlt PHNX, PHNX, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 8: MAY
                allyBattleSprAndPlt RNGR, RNGR, 0
                allyBattleSprAndPlt BWNT, BWNT, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 9: GERHALT
                allyBattleSprAndPlt WFMN, WFMN, 0
                allyBattleSprAndPlt WFBR, WFBR, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 10: LUKE
                allyBattleSprAndPlt BDMN, BDMN, 0
                allyBattleSprAndPlt BDBT, BDBT, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 11: ROHDE
                allyBattleSprAndPlt ACHR, ACHR, 2
                allyBattleSprAndPlt SNIP, SNIP, 2
                allyBattleSprAndPlt BRGN, BRGN, 1
                
; 12: RICK
                allyBattleSprAndPlt KNTE, KNTE, 1
                allyBattleSprAndPlt PLDN, PLDN, 1
                allyBattleSprAndPlt PGNT, PGNT, 1
                
; 13: ELRIC
                allyBattleSprAndPlt ACHR, ACHR, 1
                allyBattleSprAndPlt SNIP, SNIP, 0
                allyBattleSprAndPlt BRGN, BRGN, 0
                
; 14: ERIC
                allyBattleSprAndPlt KNTE, KNTE, 2
                allyBattleSprAndPlt PLDN, PLDN, 3
                allyBattleSprAndPlt PGNT, PGNT, 2
                
; 15: KARNA
                allyBattleSprAndPlt PRST, PRST, 1
                allyBattleSprAndPlt VICR, VICR, 2
                allyBattleSprAndPlt MMNK, MMNK, 2
                
; 16: RANDOLF
                allyBattleSprAndPlt WARR, WARR, 1
                allyBattleSprAndPlt GLDT, GLDT, 2
                allyBattleSprAndPlt BRN, BRN, 2
                
; 17: TYRIN
                allyBattleSprAndPlt MAGE_2, MAGE, 1
                allyBattleSprAndPlt WIZ, WIZ, 1
                allyBattleSprAndPlt SORC_2, SORC_MALE, 1
                
; 18: JANET
                allyBattleSprAndPlt ACHR, ACHR, 0
                allyBattleSprAndPlt SNIP, SNIP, 1
                allyBattleSprAndPlt BRGN, BRGN, 2
                
; 19: HIGINS
                allyBattleSprAndPlt KNTE, KNTE, 3
                allyBattleSprAndPlt PLDN, PLDN, 2
                allyBattleSprAndPlt PGNT, PGNT, 4
                
; 20: SKREECH
                allyBattleSprAndPlt BDMN, BDMN, 1
                allyBattleSprAndPlt BDBT, BDBT, 1
                allyBattleSprAndPlt NONE, NONE, 0
                
; 21: TAYA
                allyBattleSprAndPlt MAGE_3, MAGE, 2
                allyBattleSprAndPlt WIZ, WIZ, 3
                allyBattleSprAndPlt SORC_3, SORC_FEMALE, 0
                
; 22: FRAYJA
                allyBattleSprAndPlt PRST, PRST, 2
                allyBattleSprAndPlt VICR, VICR, 0
                allyBattleSprAndPlt MMNK, MMNK, 3
                
; 23: JARO
                allyBattleSprAndPlt KNTE, KNTE, 4
                allyBattleSprAndPlt PLDN, PLDN, 4
                allyBattleSprAndPlt PGNT, PGNT, 3
                
; 24: GYAN
                allyBattleSprAndPlt WARR, WARR, 2
                allyBattleSprAndPlt GLDT, GLDT, 0
                allyBattleSprAndPlt BRN, BRN, 3
                
; 25: SHEELA
                allyBattleSprAndPlt PRST, PRST, 3
                allyBattleSprAndPlt VICR, VICR, 3
                allyBattleSprAndPlt MMNK, MMNK, 0
                
; 26: ZYNK
                allyBattleSprAndPlt DRD, RBT, 1
                allyBattleSprAndPlt RBT, RBT, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 27: CHAZ
                allyBattleSprAndPlt MAGE_4, MAGE, 3
                allyBattleSprAndPlt WIZ, WIZ, 0
                allyBattleSprAndPlt SORC_4, SORC_MALE, 2
                
; 28: LEMON
                allyBattleSprAndPlt RWAR, SDMN, 1
                allyBattleSprAndPlt RDBN, BRN, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 29: CLAUDE
                allyBattleSprAndPlt CNST, GLM, 1
                allyBattleSprAndPlt GLM, GLM, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
                ; Additional entries to be defined with force members expansion patch
            if (STANDARD_BUILD&EXPANDED_FORCE_MEMBERS=1)
; 30: 
                allyBattleSprAndPlt RDBN, SDMN, 0
                allyBattleSprAndPlt NONE, NONE, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
; 31: 
                allyBattleSprAndPlt RDBN, SDMN, 0
                allyBattleSprAndPlt NONE, NONE, 0
                allyBattleSprAndPlt NONE, NONE, 0
                
            endif
