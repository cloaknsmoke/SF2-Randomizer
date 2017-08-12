
; ASM FILE data\battles\entries\battle29\cs_beforebattle.asm :
; 0x4C3DC..0x4C5E6 : Cutscene before battle 29
bbcs_29:        textCursor $A9E         ; Initial text line $A9E : "You can't enter Mitula{N}Shrine now.{W1}"
		loadMapFadeIn $0,$A,$1C
		loadMapEntities ce_4C5AE; Entity data to figure out and format
		setActscript $0,$FF,eas_Init
		setActscript $7,$FF,eas_Init
		entityPosDir $7,$10,$22,$1
		setActscript $1F,$FF,eas_Init
		entityPosDir $1F,$E,$22,$1
		playSound MUSIC_MITULA_SHRINE
		fadeInB
		csc45 $30               ; (null)
		moveEntity $0,$0,$1,$1
		endMove $8080
		moveEntity $7,$0,$1,$1
		endMove $8080
		moveEntity $1F,$FF,$1,$1
		endMove $8080
		nextSingleText $0,$80   ; "You can't enter Mitula{N}Shrine now.{W1}"
		setEntityDir $7,$2
		nextSingleText $0,$7    ; "Sir Astral, what do we do{N}now?{W1}"
		nextSingleText $0,$1F   ; "Hmmm....{W1}"
		moveEntity $1F,$FF,$1,$1
		endMove $8080
		setEntityDir $1F,$0
		nextSingleText $0,$1F   ; "{LEADER}, what do you{N}think?{W1}"
		setEntityDir $0,$2
		nextSingleText $0,$0    ; "I'm not sure.{W1}"
		moveEntity $7,$FF,$1,$1
		endMove $8080
		setEntityDir $7,$2
		nextSingleText $0,$7    ; "{LEADER}, it's obvious!{W1}"
		setEntityDir $0,$0
		entityNod $1F
		nextText $0,$1F         ; "I agree.  We have to see the{N}storytellers and listen to{N}the legends.{W2}"
		nextSingleText $0,$1F   ; "Make a break for it!{W1}"
		setCamDest $A,$1A
		customActscript $0,$FF
		dc.w $10                ;   0010 SET SPEED X=$30 Y=$30
		dc.b $30
		dc.b $30
		dc.w $34                ;   0034 JUMP TO ABSOLUTE ADDR. 0x451FC
		dc.l eas_Idle           
		dc.w $8080              ; 0014 END OF CUSTOM ACTSCRIPT
		customActscript $1F,$FF
		dc.w $10                ;   0010 SET SPEED X=$30 Y=$30
		dc.b $30
		dc.b $30
		dc.w $34                ;   0034 JUMP TO ABSOLUTE ADDR. 0x451FC
		dc.l eas_Idle           
		dc.w $8080              ; 0014 END OF CUSTOM ACTSCRIPT
		customActscript $7,$FF
		dc.w $10                ;   0010 SET SPEED X=$30 Y=$30
		dc.b $30
		dc.b $30
		dc.w $34                ;   0034 JUMP TO ABSOLUTE ADDR. 0x451FC
		dc.l eas_Idle           
		dc.w $8080              ; 0014 END OF CUSTOM ACTSCRIPT
		moveEntity $1F,$0,$1,$3
		endMove $8080
		moveEntity $0,$0,$2,$1
		moreMove $1,$2
		endMove $8080
		moveEntity $7,$0,$2,$2
		moreMove $1,$1
		endMove $8080
		csWait $A
		customActscript $80,$FF
		dc.w $10                ;   0010 SET SPEED X=$40 Y=$40
		dc.b $40
		dc.b $40
		dc.w $34                ;   0034 JUMP TO ABSOLUTE ADDR. 0x451FC
		dc.l eas_Idle           
		dc.w $8080              ; 0014 END OF CUSTOM ACTSCRIPT
		moveEntity $80,$0,$1,$2
		moreMove $2,$1
		endMove $8080
		waitIdle $80
		setEntityDir $80,$3
		waitIdle $7
		nextText $0,$80         ; "Wait, wait.  You must not{N}enter the holy shrine.{W2}"
		nextSingleText $0,$80   ; "So be it!  Let the truth be{N}known!{W1}"
		playSound $FD
		animEntityFadeInOut $80,$6
		setCamDest $C,$13
		entityPosDir $80,$10,$17,$3
		animEntityFadeInOut $80,$7
		csWait $28
		animEntityFadeInOut $80,$6
		setCamDest $8,$F
		entityPosDir $80,$C,$12,$3
		animEntityFadeInOut $80,$7
		csWait $28
		animEntityFadeInOut $80,$6
		setCamDest $9,$9
		entityPosDir $80,$E,$D,$3
		animEntityFadeInOut $80,$7
		csWait $28
		entityFlashWhite $80,$1E
		playSound MUSIC_BATTLE_THEME_1
		stopEntity $80
		entitySprite $80,$AF
		setEntityDir $80,$1
		csWait $8
		setEntityDir $80,$2
		csWait $8
		setEntityDir $80,$3
		csWait $8
		entitySprite $80,$55
		startEntity $80
		entityPosDir $81,$E,$C,$3
		csWait $1E
		entityPosDir $82,$F,$D,$3
		csWait $1E
		entityPosDir $83,$F,$E,$3
		csWait $1E
		entityPosDir $84,$B,$E,$3
		csWait $1E
		nextSingleText $0,$80   ; "Go away!  The devils already{N}occupy this shrine!{W1}"
		nextText $0,$1F         ; "Devils again!{W2}"
		nextSingleText $0,$1F   ; "{LEADER}, attack!{W1}"
		csc_end                 ; END OF CUTSCENE SCRIPT
ce_4C5AE:       dc.b   0
		dc.b  $F
		dc.w $21
		dc.w 1
		dc.b $10
		dc.b $22
		dc.b 1
		dc.b 7
		dc.l eas_Init           
		dc.b $F
		dc.b $1E
		dc.b 3
		dc.b $C0
		dc.l eas_Init           
		dc.b $3F
		dc.b $3F
		dc.b 3
		dc.b $8D
		dc.l eas_Init           
		dc.b $3F
		dc.b $3F
		dc.b 3
		dc.b $56
		dc.l eas_Init           
		dc.b $3F
		dc.b $3F
		dc.b 3
		dc.b $88
		dc.l eas_Init           
		dc.b $3F
		dc.b $3F
		dc.b 3
		dc.b $54
		dc.l eas_Init           
		dc.w $FFFF