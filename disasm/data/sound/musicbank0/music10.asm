
; ASM FILE music10.asm :
; 0x8325..0x87F5 : Music 10
Music_10:       db 0
		db 1
		db 0
		db 0C1h
		dw Music_10_Channel_0
		dw Music_10_Channel_1
		dw Music_10_Channel_2
		dw Music_10_Channel_3
		dw Music_10_Channel_4
		dw Music_10_Channel_5
		dw Music_10_Channel_6
		dw Music_10_Channel_7
		dw Music_10_Channel_9
		dw Music_10_Channel_9
Music_10_Channel_0:
		ymStereo 0C0h
		ymInst 4
		ymVol 0Ch
		release 01h
		vibrato 02Fh
		mainLoopStart
		countedLoopStart 1
		noteL 23,96
		noteL 35,24
		noteL 35,72
		countedLoopEnd
		noteL 22,96
		note 28
		note 22
		note 28
		note 20
		noteL 32,24
		noteL 32,48
		noteL 31,24
		noteL 29,96
		noteL 29,24
		noteL 29,48
		noteL 27,24
		noteL 26,96
		note 19
		note 20
		note 22
		mainLoopEnd
Music_10_Channel_1:
		ymStereo 0C0h
		release 01h
		vibrato 02Ch
		mainLoopStart
		ymInst 22
		ymVol 0Ch
		noteL 44,18
		noteL 43,16
		noteL 41,14
		noteL 40,72
		noteL 38,24
		note 40
		note 41
		noteL 43,18
		noteL 44,16
		noteL 52,14
		ymSustain
		noteL 49,96
		ymVol 0Eh
		release 01h
		noteL 47,48
		ymInst 16
		ymVol 0Bh
		noteL 60,0
		ymSlide 07h
		noteL 62,72
		ymStopSlide
		ymVol 08h
		noteL 62,6
		ymVol 0Bh
		note 62
		note 61
		note 60
		noteL 59,24
		noteL 58,48
		noteL 59,24
		noteL 60,18
		noteL 61,16
		noteL 64,14
		noteL 62,36
		noteL 60,6
		note 59
		noteL 58,12
		ymVol 08h
		noteL 58,6
		ymVol 06h
		note 58
		ymSlide 014h
		vibrato 070h
		ymVol 0Ah
		noteL 65,120
		ymStopSlide
		vibrato 02Ch
		ymInst 49
		ymVol 0Bh
		noteL 38,48
		ymSustain
		noteL 39,96
		ymVol 09h
		noteL 39,12
		ymVol 08h
		note 39
		ymVol 07h
		note 39
		ymVol 06h
		release 01h
		note 39
		ymVol 0Bh
		noteL 35,48
		note 36
		ymInst 40
		ymVol 0Ah
		noteL 38,24
		note 39
		note 41
		note 43
		note 44
		note 43
		note 41
		note 39
		noteL 38,48
		noteL 36,96
		noteL 37,72
		noteL 38,24
		mainLoopEnd
Music_10_Channel_2:
		ymStereo 0C0h
		release 01h
		vibrato 02Ch
		length 48
		mainLoopStart
		ymInst 49
		ymVol 0Bh
		noteL 31,48
		ymSustain
		noteL 32,96
		ymVol 09h
		noteL 32,12
		ymVol 08h
		note 32
		ymVol 07h
		note 32
		release 01h
		ymVol 06h
		note 32
		ymVol 0Bh
		noteL 31,48
		noteL 32,96
		ymInst 40
		ymVol 0Bh
		noteL 41,120
		noteL 40,24
		note 39
		note 40
		noteL 41,72
		noteL 40,24
		noteL 39,48
		note 38
		ymInst 9
		ymVol 0Bh
		noteL 46,0
		ymSlide 0Ah
		noteL 48,18
		ymStopSlide
		ymVol 0Ch
		noteL 46,16
		noteL 44,14
		noteL 43,72
		noteL 41,24
		note 43
		note 44
		ymSustain
		noteL 35,18
		ymSlide 08h
		release 01h
		noteL 36,16
		ymStopSlide
		noteL 43,14
		noteL 41,72
		ymInst 47
		ymVol 0Ch
		noteL 39,24
		note 41
		note 43
		note 44
		note 46
		note 48
		note 51
		note 50
		note 48
		note 47
		note 43
		ymSustain
		noteL 41,18
		noteL 39,16
		release 01h
		noteL 42,14
		ymSustain
		noteL 41,16
		release 01h
		note 39
		noteL 47,64
		ymSustain
		noteL 46,48
		ymVol 0Bh
		noteL 46,12
		ymVol 0Ah
		note 46
		ymVol 09h
		note 46
		ymVol 08h
		release 01h
		note 46
		mainLoopEnd
Music_10_Channel_3:
		ymStereo 0C0h
		release 01h
		vibrato 02Ch
		length 48
		mainLoopStart
		ymInst 49
		ymVol 0Bh
		noteL 25,48
		ymSustain
		noteL 26,96
		ymVol 09h
		noteL 26,12
		ymVol 08h
		note 26
		ymVol 07h
		note 26
		release 01h
		ymVol 06h
		note 26
		ymVol 0Bh
		noteL 28,48
		noteL 29,96
		ymInst 40
		ymVol 0Ah
		note 32
		note 32
		note 32
		ymSustain
		note 32
		ymVol 08h
		noteL 32,12
		ymVol 07h
		note 32
		ymVol 06h
		note 32
		ymVol 05h
		release 01h
		note 32
		ymInst 49
		ymVol 0Bh
		noteL 35,48
		ymSustain
		noteL 36,96
		ymVol 09h
		noteL 36,12
		ymVol 08h
		note 36
		ymVol 07h
		note 36
		ymVol 06h
		release 01h
		note 36
		ymVol 0Bh
		noteL 31,48
		noteL 32,96
		ymInst 40
		ymVol 0Ah
		noteL 38,48
		note 36
		note 35
		noteL 31,96
		noteL 30,48
		note 28
		ymSustain
		note 29
		ymVol 0Ah
		noteL 29,12
		ymVol 09h
		note 29
		ymVol 08h
		note 29
		ymVol 07h
		release 01h
		note 29
		mainLoopEnd
Music_10_Channel_4:
		shifting 020h
		length 12
		ymStereo 080h
		release 01h
		vibrato 02Ch
		mainLoopStart
		ymInst 22
		ymVol 0Ah
		noteL 44,18
		note 43
		ymVol 0Ch
		note 44
		noteL 43,16
		noteL 41,14
		ymVol 0Ah
		noteL 40,36
		noteL 38,24
		note 40
		note 41
		noteL 43,18
		note 44
		ymVol 0Ch
		note 43
		noteL 44,16
		noteL 52,14
		ymSustain
		ymVol 0Ah
		noteL 49,60
		ymVol 0Ch
		release 01h
		noteL 47,42
		ymInst 16
		ymVol 0Ah
		noteL 60,0
		ymSlide 07h
		noteL 62,42
		ymVol 0Bh
		ymStopSlide
		noteL 60,0
		ymSlide 07h
		noteL 62,30
		ymStopSlide
		ymVol 07h
		noteL 62,6
		ymVol 0Ah
		note 62
		note 61
		note 60
		noteL 59,24
		noteL 58,48
		noteL 59,24
		noteL 60,18
		noteL 61,16
		noteL 64,14
		noteL 62,36
		noteL 60,6
		note 59
		noteL 58,12
		ymVol 07h
		noteL 58,6
		ymVol 05h
		noteL 58,12
		ymSlide 014h
		vibrato 075h
		ymVol 09h
		noteL 65,102
		ymStopSlide
		vibrato 02Ch
		length 6
		ymInst 9
		ymVol 09h
		noteL 46,0
		ymSlide 0Ah
		noteL 48,18
		ymStopSlide
		ymVol 0Ah
		noteL 46,16
		noteL 44,14
		noteL 43,36
		noteL 41,24
		note 43
		note 44
		ymSustain
		noteL 35,18
		release 01h
		ymSlide 08h
		note 36
		ymStopSlide
		ymSustain
		ymVol 0Bh
		note 35
		ymSlide 08h
		release 01h
		noteL 36,16
		ymStopSlide
		noteL 43,14
		ymVol 0Ah
		noteL 41,36
		ymInst 47
		ymVol 0Ah
		noteL 39,24
		note 41
		note 43
		ymInst 40
		ymVol 09h
		noteL 38,48
		note 36
		note 35
		noteL 31,96
		noteL 30,48
		note 28
		note 29
		mainLoopEnd
Music_10_Channel_5:
		shifting 010h
		length 6
		ymStereo 040h
		release 01h
		vibrato 02Ch
		mainLoopStart
		ymInst 22
		ymVol 0Bh
		noteL 44,18
		noteL 43,16
		noteL 41,14
		noteL 40,72
		noteL 38,24
		note 40
		note 41
		noteL 43,18
		noteL 44,16
		noteL 52,14
		ymSustain
		noteL 49,96
		ymVol 0Dh
		release 01h
		noteL 47,48
		ymInst 40
		ymVol 0Ah
		noteL 41,120
		noteL 40,24
		note 39
		note 40
		noteL 41,72
		noteL 40,24
		noteL 39,48
		note 38
		ymInst 9
		ymVol 0Ah
		noteL 46,0
		ymSlide 0Ah
		noteL 48,18
		ymStopSlide
		ymVol 0Bh
		noteL 46,16
		noteL 44,14
		noteL 43,72
		noteL 41,24
		note 43
		note 44
		ymSustain
		noteL 35,18
		release 01h
		ymSlide 08h
		noteL 36,16
		ymStopSlide
		noteL 43,14
		noteL 41,72
		ymInst 47
		ymVol 0Bh
		noteL 39,24
		note 41
		note 43
		note 44
		note 46
		note 48
		note 51
		note 50
		note 48
		note 47
		note 43
		ymSustain
		noteL 41,18
		noteL 39,16
		release 01h
		noteL 42,14
		ymSustain
		noteL 41,16
		release 01h
		note 39
		noteL 47,64
		noteL 46,48
		mainLoopEnd
Music_10_Channel_6:
		release 00h
		vibrato 04Ch
		mainLoopStart
		countedLoopStart 1
		psgInst 118
		noteL 58,4
		note 59
		note 58
		psgInst 119
		note 59
		note 58
		note 59
		psgInst 120
		note 58
		note 59
		note 58
		psgInst 121
		note 59
		note 58
		note 59
		psgInst 122
		note 58
		note 59
		note 58
		psgInst 123
		note 59
		note 58
		note 59
		psgInst 124
		note 58
		note 59
		note 58
		psgInst 125
		note 59
		note 58
		note 59
		note 58
		note 59
		note 58
		psgInst 124
		note 59
		note 58
		note 59
		psgInst 123
		note 58
		note 59
		note 58
		psgInst 122
		note 59
		note 58
		note 59
		psgInst 121
		note 58
		note 59
		note 58
		psgInst 120
		note 59
		note 58
		note 59
		psgInst 119
		note 58
		note 59
		note 58
		psgInst 118
		note 59
		note 58
		note 59
		countedLoopEnd
		psgInst 0
		length 192
		silence
		countedLoopStart 1
		psgInst 118
		noteL 55,4
		note 56
		note 55
		psgInst 119
		note 56
		note 55
		note 56
		psgInst 120
		note 55
		note 56
		note 55
		psgInst 121
		note 56
		note 55
		note 56
		psgInst 122
		note 55
		note 56
		note 55
		psgInst 123
		note 56
		note 55
		note 56
		psgInst 124
		note 55
		note 56
		note 55
		psgInst 125
		note 56
		note 55
		note 56
		note 55
		note 56
		note 55
		psgInst 124
		note 56
		note 55
		note 56
		psgInst 123
		note 55
		note 56
		note 55
		psgInst 122
		note 56
		note 55
		note 56
		psgInst 121
		note 55
		note 56
		note 55
		psgInst 120
		note 56
		note 55
		note 56
		psgInst 119
		note 55
		note 56
		note 55
		psgInst 118
		note 56
		note 55
		note 56
		countedLoopEnd
		psgInst 0
		length 192
		silence
		mainLoopEnd
Music_10_Channel_7:
		psgInst 0
		length 6
		shifting 010h
		release 00h
		vibrato 04Ch
		mainLoopStart
		countedLoopStart 1
		psgInst 116
		noteL 58,4
		note 59
		note 58
		psgInst 117
		note 59
		note 58
		note 59
		psgInst 118
		note 58
		note 59
		note 58
		psgInst 119
		note 59
		note 58
		note 59
		psgInst 120
		note 58
		note 59
		note 58
		psgInst 121
		note 59
		note 58
		note 59
		psgInst 122
		note 58
		note 59
		note 58
		psgInst 123
		note 59
		note 58
		note 59
		note 58
		note 59
		note 58
		psgInst 122
		note 59
		note 58
		note 59
		psgInst 121
		note 58
		note 59
		note 58
		psgInst 120
		note 59
		note 58
		note 59
		psgInst 119
		note 58
		note 59
		note 58
		psgInst 118
		note 59
		note 58
		note 59
		psgInst 117
		note 58
		note 59
		note 58
		psgInst 116
		note 59
		note 58
		note 59
		countedLoopEnd
		psgInst 0
		length 192
		silence
		countedLoopStart 1
		psgInst 116
		noteL 55,4
		note 56
		note 55
		psgInst 117
		note 56
		note 55
		note 56
		psgInst 118
		note 55
		note 56
		note 55
		psgInst 119
		note 56
		note 55
		note 56
		psgInst 120
		note 55
		note 56
		note 55
		psgInst 121
		note 56
		note 55
		note 56
		psgInst 122
		note 55
		note 56
		note 55
		psgInst 123
		note 56
		note 55
		note 56
		note 55
		note 56
		note 55
		psgInst 122
		note 56
		note 55
		note 56
		psgInst 121
		note 55
		note 56
		note 55
		psgInst 120
		note 56
		note 55
		note 56
		psgInst 119
		note 55
		note 56
		note 55
		psgInst 118
		note 56
		note 55
		note 56
		psgInst 117
		note 55
		note 56
		note 55
		psgInst 116
		note 56
		note 55
		note 56
		countedLoopEnd
		psgInst 0
		length 192
		silence
		mainLoopEnd
Music_10_Channel_9:
		channel_end