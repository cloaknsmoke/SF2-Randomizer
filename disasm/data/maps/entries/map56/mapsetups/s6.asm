
; ASM FILE data\maps\entries\map56\mapsetups\s6.asm :
; 0x61508..0x6153E : 

; =============== S U B R O U T I N E =======================================

ms_map56_InitFunction:
		
		rts

	; End of function ms_map56_InitFunction

cs_6150A:       textCursor $E14         ; Initial text line $E14 : "Unbelievable!  You've{N}finally arrived.{W1}"
		csc52 $80,$0            ; 0052 UNKNOWN, RELATED TO TWO ENTITIES
		nextSingleText $0,$80   ; "Unbelievable!  You've{N}finally arrived.{W1}"
		csc52 $0,$80            ; 0052 UNKNOWN, RELATED TO TWO ENTITIES
		csc52 $7,$80            ; 0052 UNKNOWN, RELATED TO TWO ENTITIES
		nextSingleText $0,$7    ; "Creed...I mean, Mr...{W1}"
		nextText $0,$80         ; "That's OK, {NAME;7}.{N}I doubted you'd ever make{N}it here.{W2}"
		nextSingleText $0,$80   ; "The enemies you've faced so{N}far were strong.{W1}"
		nextSingleText $0,$0    ; "Yes, they were.{W1}"
		nextText $0,$80         ; "Why am I here?  Is that your{N}question, {LEADER}?{W2}"
		nextText $0,$80         ; "I wanted to help you.{W2}"
		csc_end                 ; END OF CUTSCENE SCRIPT