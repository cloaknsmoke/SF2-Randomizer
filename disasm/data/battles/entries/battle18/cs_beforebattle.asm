
; ASM FILE data\battles\entries\battle18\cs_beforebattle.asm :
; 0x4B1D8..0x4B2F2 : Cutscene before battle 18
bbcs_18:        textCursor $9D8         ; Initial text line $9D8 : "Stop!{W1}"
		loadMapFadeIn $C,$7,$16
		loadMapEntities ce_4B2DA; Entity data to figure out and format
		setActscript $0,$FF,eas_Init
		setActscript $7,$FF,eas_Init
		setActscript $1F,$FF,eas_Init
		setActscript $B,$FF,eas_Init
		entityPosDir $7,$D,$21,$1
		entityPosDir $1F,$C,$21,$1
		entityPosDir $B,$B,$21,$1
		stopEntity $81
		playSound MUSIC_SHRINE
		fadeInB
		csc45 $40               ; (null)
		moveEntity $0,$0,$1,$6
		endMove $8080
		moveEntity $7,$0,$1,$6
		endMove $8080
		moveEntity $B,$0,$1,$6
		endMove $8080
		moveEntity $1F,$FF,$1,$6
		endMove $8080
		nextSingleText $0,$80   ; "Stop!{W1}"
		csWait $5
		setActscript $0,$0,eas_461B6
		csWait $5
		setActscript $7,$0,eas_461B6
		csWait $5
		setActscript $B,$0,eas_461E4
		csWait $5
		setActscript $1F,$0,eas_461B6
		csWait $1E
		moveEntity $7,$FF,$1,$1
		endMove $8080
		nextSingleText $C0,$7   ; "Who IS that big guy?{W1}"
		moveEntity $B,$FF,$1,$1
		endMove $8080
		nextSingleText $0,$B    ; "Don't you know?{W1}"
		setEntityDir $0,$1
		setEntityDir $7,$1
		setEntityDir $1F,$1
		csWait $1E
		setCameraEntity $80
		nextSingleText $0,$B    ; "That's Taros.  The guardian of{N}this ancient shrine.{W1}"
		nextSingleText $0,$80   ; "Again, stop right there, or{N}I'll attack you.{W1}"
		setCamDest $7,$16
		setEntityDir $0,$0
		setEntityDir $7,$2
		setEntityDir $B,$0
		nextSingleText $C0,$7   ; "What should we do?{W1}"
		setEntityDir $0,$2
		nextSingleText $0,$B    ; "The Caravan is there, behind{N}him.  We must have it!{W1}"
		setEntityDir $0,$1
		setEntityDir $7,$1
		setEntityDir $B,$1
		nextSingleText $0,$80   ; "Time's up!  Now we battle.{W1}"
		csc_end                 ; END OF CUTSCENE SCRIPT
ce_4B2DA:       dc.b   0
		dc.b  $C
		dc.w $20
		dc.w 1
		dc.b $C
		dc.b 8
		dc.b 3
		dc.b $FF
		dc.l eas_Init           
		dc.b $C
		dc.b 5
		dc.b 3
		dc.b $3E
		dc.l eas_Init           
		dc.w $FFFF