
; ASM FILE data\battles\entries\battle16\cs_afterbattle.asm :
; 0x4B1BC..0x4B1D8 : Cutscene after battle 16
abcs_battle16:  executeSubroutine csub_4B1D0
		mapSysEvent $451D3302
		csc_end                 ; END OF CUTSCENE SCRIPT

; =============== S U B R O U T I N E =======================================

csub_4B1CA:
		clr.b   ($FFFFF710).w   
		rts

	; End of function csub_4B1CA


; =============== S U B R O U T I N E =======================================

csub_4B1D0:
		move.b  #2,((PLAYER_TYPE-$1000000)).w
		rts

	; End of function csub_4B1D0
