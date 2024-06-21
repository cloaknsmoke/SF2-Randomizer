
; ASM FILE data\stats\allies\allymapsprites-standard.asm :
;
; Works in tandem with class types table located in data\stats\allies\classes\classtypes.asm

table_AllyMapsprites:

; 3 bytes per ally, one for each class type (base, promo, special)
;
; Syntax        mapsprite [MAPSPRITE_]enum (or index)
                
; 0: Bowie
                mapsprite BOWIE_BASE
                mapsprite BOWIE_PROMO
                mapsprite DEFAULT
                
; 1: Sarah
                mapsprite SARAH_BASE
                mapsprite SARAH_PROMO
                mapsprite SARAH_SPECIAL
                
; 2: Chester
                mapsprite CHESTER_BASE
                mapsprite CHESTER_PROMO
                mapsprite CHESTER_SPECIAL
                
; 3: Jaha
                mapsprite JAHA_BASE
                mapsprite JAHA_PROMO
                mapsprite JAHA_SPECIAL
                
; 4: Kazin
                mapsprite KAZIN_BASE
                mapsprite KAZIN_PROMO
                mapsprite KAZIN_SPECIAL
                
; 5: Slade
                mapsprite SLADE_BASE
                mapsprite SLADE_PROMO
                mapsprite DEFAULT
                
; 6: Kiwi
                mapsprite KIWI_BASE
                mapsprite KIWI_PROMO
                mapsprite DEFAULT
                
; 7: Peter
                mapsprite PETER_BASE
                mapsprite PETER_PROMO
                mapsprite DEFAULT
                
; 8: May
                mapsprite MAY_BASE
                mapsprite MAY_PROMO
                mapsprite DEFAULT
                
; 9: Gerhalt
                mapsprite GERHALT_BASE
                mapsprite GERHALT_PROMO
                mapsprite DEFAULT
                
; 10: Luke
                mapsprite LUKE_BASE
                mapsprite LUKE_PROMO
                mapsprite DEFAULT
                
; 11: Rohde
                mapsprite ROHDE_BASE
                mapsprite ROHDE_PROMO
                mapsprite ROHDE_SPECIAL
                
; 12: Rick
                mapsprite RICK_BASE
                mapsprite RICK_PROMO
                mapsprite RICK_SPECIAL
                
; 13: Elric
                mapsprite ELRIC_BASE
                mapsprite ELRIC_PROMO
                mapsprite ELRIC_SPECIAL
                
; 14: Eric
                mapsprite ERIC_BASE
                mapsprite ERIC_PROMO
                mapsprite ERIC_SPECIAL
                
; 15: Karna
                mapsprite KARNA_BASE
                mapsprite KARNA_PROMO
                mapsprite KARNA_SPECIAL
                
; 16: Randolf
                mapsprite RANDOLF_BASE
                mapsprite RANDOLF_PROMO
                mapsprite RANDOLF_SPECIAL
                
; 17: Tyrin
                mapsprite TYRIN_BASE
                mapsprite TYRIN_PROMO
                mapsprite TYRIN_SPECIAL
                
; 18: Janet
                mapsprite JANET_BASE
                mapsprite JANET_PROMO
                mapsprite JANET_SPECIAL
                
; 19: Higins
                mapsprite HIGINS_BASE
                mapsprite HIGINS_PROMO
                mapsprite HIGINS_SPECIAL
                
; 20: Skreech
                mapsprite SKREECH_BASE
                mapsprite SKREECH_PROMO
                mapsprite DEFAULT
                
; 21: Taya
                mapsprite TAYA_BASE
                mapsprite TAYA_PROMO
                mapsprite TAYA_SPECIAL
                
; 22: Frayja
                mapsprite FRAYJA_BASE
                mapsprite FRAYJA_PROMO
                mapsprite FRAYJA_SPECIAL
                
; 23: Jaro
                mapsprite JARO_BASE
                mapsprite JARO_PROMO
                mapsprite JARO_SPECIAL
                
; 24: Gyan
                mapsprite GYAN_BASE
                mapsprite GYAN_PROMO
                mapsprite GYAN_SPECIAL
                
; 25: Sheela
                mapsprite SHEELA_BASE
                mapsprite SHEELA_PROMO
                mapsprite SHEELA_SPECIAL
                
; 26: Zynk
                mapsprite ZYNK_BASE
                mapsprite ZYNK_PROMO
                mapsprite DEFAULT
                
; 27: Chaz
                mapsprite CHAZ_BASE
                mapsprite CHAZ_PROMO
                mapsprite CHAZ_SPECIAL
                
; 28: Lemon
                mapsprite LEMON_BASE
                mapsprite DEFAULT
                mapsprite LEMON_SPECIAL
                
; 29: Claude
                mapsprite CLAUDE_BASE
                mapsprite CLAUDE_PROMO
                mapsprite DEFAULT
                
            if (EXPANDED_FORCE_MEMBERS=1)
; 30: 
                mapsprite DEFAULT
                mapsprite DEFAULT
                mapsprite DEFAULT
                
; 31: 
                mapsprite DEFAULT
                mapsprite DEFAULT
                mapsprite DEFAULT
                
            endif


; Allies who use a different mapsprite before joining the Force.
table_AllyMapspritesIfNotJoined:
                
            if (EXPANDED_MAPSPRITES=1)
                dc.w ALLY_ROHDE, MAPSPRITE_NPC_ROHDE
                
                tableEnd
            else
                dc.b ALLY_ROHDE, MAPSPRITE_NPC_ROHDE
                
                tableEnd.b
            endif
