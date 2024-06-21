
; ASM FILE data\stats\allies\classes\blacksmitheligibleclasses.asm :
; 0x21EB6..0x21ED6 : Blacksmith eligible classes list
list_BlacksmithEligibleClasses:
                
; List of word-sized class indexes, prefixed with length.
;
; Syntax        classes [CLASS_]enum,..[CLASS_]enum
                
                classes HERO, PLDN, PGNT, GLDT, BRN, WIZ, SORC_1, VICR, MMNK, SNIP, BRGN, BDBT, BWNT, NINJ, RDBN, SORC_2, SORC_3, SORC_4
