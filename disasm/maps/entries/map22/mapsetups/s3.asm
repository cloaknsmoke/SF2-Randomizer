
; SCRIPT SECTION maps\entries\map22\mapsetups\s3 :
; 
ms_map22_ZoneEvents:dc.b $FF
										dc.b $10
										dc.w sub_595E8-ms_map22_ZoneEvents
										dc.w $FD00
										dc.w nullsub_87-ms_map22_ZoneEvents

; =============== S U B R O U T I N E =======================================

nullsub_87:
										
										rts

	; End of function nullsub_87


; =============== S U B R O U T I N E =======================================

sub_595E8:
										
										trap    #CHECK_FLAG
										dc.w $309
										beq.s   return_59600
										trap    #CHECK_FLAG
										dc.w $20A
										bne.s   return_59600
										move.b  #$16,((EGRESS_MAP_INDEX-$1000000)).w
										lea     cs_5994E(pc), a0
										trap    #6
return_59600:
										
										rts

	; End of function sub_595E8

