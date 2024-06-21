
; ASM FILE data\stats\allies\classes\promotions-standard.asm :
; Promotions
table_Promotions: 
; Syntax        promotionSection [CLASS_]enum,..[CLASS_]enum
                
                promotionSection &      ; 00: Regular base classes
                    SDMN, KNTE, WARR, MAGE_1,  MAGE_2, MAGE_3, MAGE_4, PRST, ACHR, BDMN, WFMN, RNGR, PHNK, THIF, TORT, RWAR, DRD, CNST
                
                promotionSection &      ; 01: Regular promoted classes
                    HERO, PLDN, GLDT, WIZ, WIZ, WIZ, WIZ, VICR, SNIP, BDBT, WFBR, BWNT, PHNX, NINJ, MNST, RDBN, RBT, GLM
                
                promotionSection &      ; 02: Pegasus Wing base classes
                    KNTE
                
                promotionSection &      ; 03: Pegasus Wing promoted classes
                    PGNT
                
                promotionSection &      ; 04: Warrior Pride base classes
                    WARR
                
                promotionSection &      ; 05: Warrior Pride promoted classes
                    BRN
                
                promotionSection &      ; 06: Secret Book base classes
                    MAGE_1, MAGE_2, MAGE_3, MAGE_4
                
                promotionSection &      ; 07: Secret Book promoted classes
                    SORC_1, SORC_2, SORC_3, SORC_4
                
                promotionSection &      ; 08: Vigor Ball base classes
                    PRST
                
                promotionSection &      ; 09: Vigor Ball promoted classes
                    MMNK
                
                promotionSection &      ; 10: Silver Tank base classes
                    ACHR
                
                promotionSection &      ; 11: Silver Tank promoted classes
                    BRGN
                
                
table_PromotionItems:
                ; Item, base classes section, promoted classes section
                dc.b ITEM_PEGASUS_WING, 2, 3
                dc.b ITEM_WARRIORS_PRIDE, 4, 5
                dc.b ITEM_SECRET_BOOK, 6, 7
                dc.b ITEM_VIGOR_BALL, 8, 9
                dc.b ITEM_SILVER_TANK, 10, 11
                
                tableEnd.b
                
                
table_LoseAllSpellsClasses:
                ; Class, replacement spell
                dc.b CLASS_SORC_1, SPELL_DAO
				dc.b CLASS_SORC_2, SPELL_DAO
				dc.b CLASS_SORC_3, SPELL_DAO
				dc.b CLASS_SORC_4, SPELL_DAO
                
                tableEnd.b
                
                
table_DifferentWeaponTypeClasses:
                ; Classes that have their weapon unequipped when promoting
                dc.b CLASS_MMNK
                dc.b CLASS_NINJ
                
                tableEnd.b
