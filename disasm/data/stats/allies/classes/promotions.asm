
; ASM FILE data\stats\allies\classes\promotions.asm :
; 0x21046..0x21072 : Promotions
table_Promotions:
                
; Syntax        promotionSection [CLASS_]enum,..[CLASS_]enum
;               promotionItems   [ITEM_]enum,..[ITEM_]enum
;
; Notes: 4 promotion sections and 1 promotion items list are required.
;        Constant names ("enums"), shorthands (defined by macro), and numerical indexes are interchangeable.
                
                promotionSection &      ; Regular base classes
                    SDMN, KNTE, WARR, MAGE_1,  MAGE_2, MAGE_3, MAGE_4, PRST, ACHR, BDMN, WFMN, RNGR, PHNK, THIF, TORT, RWAR, DRD, CNST
                
                promotionSection &      ; Regular promoted classes
                    HERO, PLDN, GLDT, WIZ, WIZ, WIZ, WIZ, VICR, SNIP, BDBT, WFBR, BWNT, PHNX, NINJ, MNST, RDBN, RBT, GLM
                
                promotionSection &      ; Special base classes
                    KNTE, WARR, MAGE_1, MAGE_2, MAGE_3, MAGE_4, PRST, ACHR
                
                promotionSection &      ; Special promoted classes
                    PGNT, BRN, SORC_1, SORC_2, SORC_3, SORC_4, MMNK, BRGN
                
                promotionItems &        ; Special promotion items
                    PEGASUS_WING, WARRIORS_PRIDE, SECRET_BOOK, VIGOR_BALL, SILVER_TANK
