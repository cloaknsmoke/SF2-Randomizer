
; ASM FILE data\maps\entries\map01\mapsetups\s6_initfunction.asm :
; 0x5E760..0x5E772 : 

; =============== S U B R O U T I N E =======================================


ms_map1_InitFunction:
                
                 
                chkFlg  21              ; Taya joined
                bne.s   return_5E770
                script  cs_new01
return_5E770:
                
                rts

    ; End of function ms_map1_InitFunction

cs_new01:       setSprite ALLY_TAYA,MAPSPRITE_OBJECT4
                setFacing ALLY_TAYA,DOWN
                stopEntity ALLY_TAYA
				csc_end