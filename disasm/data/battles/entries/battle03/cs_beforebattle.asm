
; ASM FILE data\battles\entries\battle03\cs_beforebattle.asm :
; 0x4980E..0x4981E : Cutscene before battle 3
bbcs_03:        executeSubroutine csub_49816
		csc_end                 ; END OF CUTSCENE SCRIPT

; =============== S U B R O U T I N E =======================================

csub_49816:
		move.b  #5,($FFFFF719).w
		rts

	; End of function csub_49816
