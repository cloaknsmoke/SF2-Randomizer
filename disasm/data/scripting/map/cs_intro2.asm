
; ASM FILE data\scripting\map\cs_intro2.asm :
; 0x48380..0x48540 : Intro cutscene 2
IntroCutscene2: textCursor $106A        ; Initial text line $106A : "Quite a storm.{D2}"
		mapLoad $41,$7,$2
		loadMapEntities ce_48510; Entity data to figure out and format
		setActscript $0,$FF,eas_Init
		cloneEntity $84,$83
		csc36                   ; 0036 UNKNOWN, RELATED TO LOADING A MAP
		fadeInB
		csc46 $7,$2             ; 0046 UNKNOWN
		nextSingleText $80,$80  ; "Quite a storm.{D2}"
		loadMapFadeIn $41,$7,$2
		fadeInB
		csWait $28
		playSound SFX_DEMON_BREATH
		executeSubroutine ApplyStormEffect
		executeSubroutine ApplyStormEffect
		csWait $3C
		setEntityDir $81,$0
		nextSingleText $0,$81   ; "Excuse me?{D2}"
		nextSingleText $80,$80  ; "It's a stormy night.{D2}"
		setEntityDir $81,$1
		csWait $1E
		playSound SFX_DEMON_BREATH
		executeSubroutine ApplyStormEffect
		executeSubroutine ApplyStormEffect
		csWait $28
		setEntityDir $81,$0
		entityNod $81
		csWait $14
		nextSingleText $0,$81   ; "It's unusual for this time{N}of year.{D2}"
		csWait $1E
		nextSingleText $0,$82   ; "Excuse me, your majesty.{D2}"
		setEntityDir $81,$3
		moveEntity $82,$FF,$1,$3
		endMove $8080
		setCamDest $7,$4
		nextSingleText $0,$81   ; "Is it time to go to the{N}Ancient Tower?{D2}"
		entityNod $82
		nextSingleText $0,$82   ; "Yes, sire.{D2}"
		moveEntity $81,$FF,$3,$1
		moreMove $0,$2
		moreMove $B,$A
		endMove $8080
		nextSingleText $0,$81   ; "It's stormy outside.{N}Be careful.{D2}"
		entityNod $82
		csWait $1E
		setCameraEntity $82
		moveEntity $82,$FF,$3,$3
		moreMove $2,$5
		moreMove $5,$3
		moreMove $2,$1
		moreMove $1,$1
		endMove $8080
		hideEntity $82
		setCameraEntity $FFFF
		csWait $1E
		setCamDest $7,$2
		csWait $28
		entityShiver $80
		nextSingleText $80,$80  ; "Hmmm....{D2}"
		setEntityDir $81,$1
		nextSingleText $0,$81   ; "Excuse me, sire?{D2}"
		nextSingleText $80,$80  ; "I have a bad feeling...{N}Oh, well.{D2}"
		csWait $28
		setEntityDir $81,$2
		csWait $28
		customActscript $81,$FF
		dc.w $10                ;   0010 SET SPEED X=$A Y=$A
		dc.b $A
		dc.b $A
		dc.w $34                ;   0034 JUMP TO ABSOLUTE ADDR. 0x451FC
		dc.l eas_Idle           
		dc.b $80                ; 0014 END OF CUSTOM ACTSCRIPT
		dc.b $80
		moveEntity $81,$FF,$2,$2
		moreMove $B,$1
		endMove $8080
		playSound SFX_SPELL_CAST
		nextSingleText $0,$81   ; "Oh, a gust of wind!{D2}"
		csWait $14
		entityShiver $80
		setEntityDir $80,$3
		nextSingleText $80,$80  ; "Make sure all the doors and{N}windows are shut!{D2}"
		playSound SFX_SPELL_CAST
		csWait $1E
		animEntityFadeInOut $83,$6
		tintMap
		csWait $5
		setActscript $81,$0,eas_461B6
		csWait $1E
		csWait $5
		setActscript $80,$0,eas_461B6
		playSound SFX_DEMON_BREATH
		csWait $1E
		executeSubroutine ApplyStormEffect
		executeSubroutine ApplyStormEffect
		csWait $28
		playSound SFX_DEMON_BREATH
		executeSubroutine ApplyStormEffect
		executeSubroutine ApplyStormEffect
		csWait $5
		setActscript $81,$0,eas_461B6
		csWait $1E
		csWait $5
		setActscript $80,$0,eas_461B6
		csWait $46
		fadeOutToBlackHalf
		csWait $1E
		csc_end                 ; END OF CUTSCENE SCRIPT
ce_48510:       dc.w $3F
		dc.w $3F
		dc.w 1
		dc.b $C
		dc.b 6
		dc.b 3
		dc.b $CB
		dc.l eas_Init           
		dc.b $A
		dc.b 7
		dc.b 3
		dc.b $CD
		dc.l eas_Init           
		dc.b $C
		dc.b $D
		dc.b 1
		dc.b $CE
		dc.l eas_Init           
		dc.b 9
		dc.b 6
		dc.b 2
		dc.b $BB
		dc.l eas_Init           
		dc.b $F
		dc.b 6
		dc.b 2
		dc.b $BB
		dc.l eas_Init           
		dc.w $FFFF