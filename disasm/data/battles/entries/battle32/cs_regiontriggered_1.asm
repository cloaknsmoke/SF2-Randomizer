
; ASM FILE data\battles\entries\battle32\cs_regiontriggered_1.asm :
; 0x4CD10..0x4CDB4 : Region-activated cutscene for battle 32
rbcs_battle32:  textCursor $B21         ; Initial text line $B21 : "I'm tired of this.  I can no{N}longer fight for devils.{W1}"
		executeSubroutine csub_4CD56
		csc45 $38               ; (null)
		setCameraEntity $17
		csWait $3C
		nextSingleText $0,$17   ; "I'm tired of this.  I can no{N}longer fight for devils.{W1}"
		setCameraEntity $80
		csWait $3C
		nextSingleText $0,$80   ; "{NAME;23}, what?{W1}"
		setCameraEntity $17
		csWait $3C
		setEntityDir $17,$1
		nextSingleText $0,$17   ; "Didn't you hear me?{W1}"
		setEntityDir $17,$3
		nextSingleText $0,$17   ; "Hey, Granseal guys!{N}I'm on your side from now{N}on! OK?{W1}"
		csc54 $17,$FFFF         ; 0054 UNKNOWN
		setF $182               ; set during battle 32, after Jaro switches sides
		csc_end                 ; END OF CUTSCENE SCRIPT

; =============== S U B R O U T I N E =======================================

; Jaro joins the Force

csub_4CD56:
		move.w  #$8F,d0 
		jsr     j_GetXPos
		move.w  d1,d7
		jsr     j_GetYPos
		move.w  d1,d6
		clr.w   d1
		jsr     j_SetCurrentHP
		move.w  #$FFFF,d1
		jsr     j_SetXPos
		move.w  #$FFFF,d1
		jsr     j_SetYPos
		moveq   #$17,d0
		move.w  d7,d1
		jsr     j_SetXPos
		move.w  d6,d1
		jsr     j_SetYPos
		moveq   #$17,d0
		jsr     j_JoinForce
		moveq   #$17,d0
		jsr     j_JoinBattleParty
		move.b  ((byte_FFB160+$F)).l,(ENTITY_EVENT_IDX_LIST+$17).l
		rts

	; End of function csub_4CD56
