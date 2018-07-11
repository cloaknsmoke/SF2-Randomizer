
; ASM FILE music03.asm :
; 0xA713..0xB0D0 : Music 03 and 04 combined for optimization
Music_3:        db 0
		db 0
		db 0
		db 0C9h
		dw Music_3_Channel_0
		dw Music_3_Channel_1
		dw Music_3_Channel_2
		dw Music_3_Channel_3
		dw Music_3_Channel_4
		dw Music_3_Channel_5
		dw Music_3_Channel_6
		dw Music_3_Channel_7
		dw Music_4_Channel_9
		dw Music_4_Channel_9
Music_4:        db 0
		db 0
		db 0
		db 0C9h
		dw Music_4_Channel_0
		dw Music_4_Channel_1
		dw Music_4_Channel_2
		dw Music_4_Channel_3
		dw Music_4_Channel_4
		dw Music_4_Channel_5
		dw Music_4_Channel_6
		dw Music_4_Channel_7
		dw Music_4_Channel_9
		dw Music_4_Channel_9
Music_3_Channel_0:
		ymStereo 0C0h
		ymInst 56
		release 01h
		vibrato 02Ch
		length 12
		ymVol 0Ch
		noteL 18,4
		length 8
		noteL 25,12
		length 6
		note 27
		noteL 15,36
		noteL 18,4
		length 8
		noteL 25,4
		length 8
		noteL 20,4
		length 8
		noteL 16,4
		length 8
		noteL 21,24
		noteL 26,4
		length 8
		noteL 17,12
		length 6
		note 17
		ymInst 12
		ymVol 0Ch
		noteL 21,120
		length 12
		ymSustain
		noteL 31,6
		release 01h
		note 32
		release 09h
		noteL 33,12
		note 27
		note 18
		note 20
		release 01h
		noteL 21,96
		length 12
		ymSustain
		noteL 30,6
		release 01h
		note 32
		release 09h
		noteL 33,12
		note 32
		note 30
		note 28
		note 27
		note 23
Music_4_Channel_0:
		ymStereo 0C0h
		vibrato 02Ch
		repeatStart
		length 24
		ymInst 12
		ymVol 0Ch
		release 01h
		note 25
		noteL 28,4
		length 14
		noteL 28,6
		release 09h
		noteL 21,12
		note 28
		note 33
		release 03h
		noteL 21,20
		length 4
		noteL 21,6
		note 21
		release 09h
		noteL 23,12
		note 30
		release 01h
		repeatSection1Start
		noteL 23,24
		repeatEnd
		repeatSection2Start
		noteL 23,36
		release 09h
		noteL 35,12
		note 33
		note 32
		ymSustain
		noteL 30,6
		release 01h
		note 32
		ymVol 0Bh
		mainLoopStart
		countedLoopStart 2
		release 03h
		noteL 33,6
		note 33
		noteL 33,24
		noteL 33,7
		length 17
		noteL 33,7
		length 17
		noteL 33,7
		length 5
		countedLoopEnd
		noteL 33,6
		note 33
		noteL 33,24
		noteL 33,7
		length 17
		noteL 33,7
		length 17
		noteL 32,7
		length 5
		noteL 30,6
		note 30
		noteL 30,24
		noteL 30,7
		length 17
		noteL 30,7
		length 17
		noteL 28,7
		length 5
		noteL 26,6
		note 26
		noteL 26,24
		noteL 26,7
		length 17
		noteL 26,7
		length 17
		noteL 25,7
		length 5
		noteL 23,6
		note 23
		noteL 23,24
		noteL 23,7
		length 17
		noteL 23,7
		length 17
		noteL 23,7
		length 5
		noteL 22,6
		note 22
		noteL 22,24
		noteL 22,7
		length 5
		noteL 34,6
		note 34
		noteL 34,24
		noteL 34,7
		length 5
		mainLoopEnd
Music_3_Channel_1:
		ymStereo 0C0h
		ymInst 13
		ymVol 0Ch
		release 01h
		vibrato 02Ch
		noteL 41,24
		note 43
		ymVol 09h
		noteL 43,12
		ymVol 0Ch
		noteL 45,24
		noteL 46,6
		ymVol 09h
		note 46
		ymInst 20
		ymVol 0Ch
		note 53
		ymVol 09h
		note 53
		ymVol 0Ch
		note 54
		ymVol 09h
		note 54
		ymVol 0Ch
		note 51
		ymVol 09h
		note 51
		ymVol 0Ch
		noteL 56,24
		noteL 54,6
		ymVol 09h
		note 54
		ymVol 0Ch
		noteL 52,9
		ymVol 09h
		noteL 52,6
		ymVol 07h
		noteL 52,3
		ymVol 0Ch
		noteL 57,6
		ymVol 0Bh
		note 54
		ymVol 08h
		note 54
		ymInst 27
		ymVol 0Bh
		noteL 28,12
		noteL 30,6
		silence
		note 39
		silence
		noteL 37,36
		noteL 30,6
		silence
		noteL 32,9
		silence
		noteL 44,6
		noteL 42,72
		length 12
		ymInst 27
		ymVol 0Bh
		note 28
		noteL 30,6
		silence
		note 39
		silence
		note 37
		silence
		noteL 33,12
		noteL 35,9
		silence
		noteL 44,6
		noteL 47,72
		noteL 45,24
Music_4_Channel_1:
		ymStereo 0C0h
		vibrato 02Ch
		release 01h
		repeatStart
		ymInst 13
		ymVol 0Ch
		noteL 44,30
		ymVol 09h
		noteL 44,6
		ymVol 0Ch
		note 44
		note 44
		noteL 47,9
		ymVol 09h
		noteL 47,6
		ymVol 07h
		noteL 47,3
		ymVol 0Ch
		noteL 49,6
		repeatSection1Start
		noteL 44,54
		ymVol 09h
		noteL 44,6
		ymVol 0Ch
		note 44
		note 44
		note 42
		ymVol 09h
		note 42
		ymVol 0Ch
		note 40
		ymVol 09h
		note 40
		ymVol 0Ch
		noteL 42,24
		repeatEnd
		repeatSection2Start
		noteL 52,54
		ymVol 09h
		noteL 52,6
		ymVol 0Ch
		note 52
		note 52
		note 51
		ymVol 09h
		note 51
		ymVol 0Ch
		note 49
		ymVol 09h
		note 49
		ymVol 0Ch
		noteL 51,30
		ymVol 09h
		noteL 51,6
		ymVol 0Ch
		note 56
		note 56
		note 54
		ymVol 09h
		note 54
		ymVol 0Ch
		note 52
		ymVol 09h
		note 52
		ymVol 0Ch
		note 54
		ymVol 09h
		note 54
		mainLoopStart
		ymInst 7
		ymVol 0Ch
		noteL 49,48
		note 52
		noteL 51,6
		note 52
		noteL 54,60
		noteL 52,12
		note 51
		noteL 52,36
		noteL 49,6
		ymVol 0Ah
		note 49
		ymVol 0Ch
		noteL 49,36
		noteL 52,6
		ymVol 0Ah
		note 52
		ymVol 0Ch
		noteL 51,96
		noteL 52,48
		note 56
		noteL 54,6
		note 56
		noteL 57,60
		noteL 56,12
		note 54
		countedLoopStart 1
		noteL 56,36
		noteL 49,6
		ymVol 0Ah
		note 49
		ymVol 0Ch
		noteL 49,36
		noteL 56,6
		ymVol 0Ah
		note 56
		ymVol 0Ch
		countedLoopEnd
		mainLoopEnd
Music_3_Channel_2:
		ymStereo 0C0h
		ymInst 13
		ymVol 0Ch
		release 01h
		vibrato 02Ch
		noteL 39,24
		note 41
		ymVol 09h
		noteL 41,12
		ymVol 0Ch
		noteL 43,24
		noteL 44,6
		ymVol 09h
		note 44
		ymInst 20
		ymVol 0Bh
		note 51
		ymVol 08h
		note 51
		ymVol 0Bh
		note 47
		ymVol 08h
		note 47
		ymVol 0Bh
		note 47
		ymVol 08h
		note 47
		ymVol 0Bh
		noteL 52,24
		noteL 50,6
		ymVol 08h
		note 50
		ymVol 0Bh
		noteL 48,9
		ymVol 08h
		noteL 48,6
		ymVol 06h
		noteL 48,3
		ymVol 0Bh
		noteL 52,6
		ymVol 0Ch
		note 59
		ymVol 09h
		note 59
		ymVol 07h
		note 59
		ymVol 05h
		note 59
		length 156
		ymInst 20
		ymVol 0Ch
		noteL 54,6
		note 54
		note 54
		ymVol 09h
		note 54
		ymVol 07h
		note 54
		ymVol 05h
		note 54
		length 108
		ymVol 0Ch
		noteL 54,6
		note 54
		note 54
		ymVol 09h
		note 54
		ymVol 0Ch
		note 54
		ymVol 09h
		note 54
		ymVol 0Ch
		noteL 54,12
		ymVol 09h
		noteL 54,6
		ymVol 07h
		note 54
Music_4_Channel_2:
		ymStereo 0C0h
		vibrato 02Ch
		release 01h
		ymInst 13
		repeatStart
		ymVol 0Ch
		noteL 41,30
		ymVol 09h
		noteL 41,6
		ymVol 0Ch
		note 41
		note 41
		noteL 44,9
		ymVol 09h
		noteL 44,6
		ymVol 07h
		noteL 44,3
		ymVol 0Ch
		noteL 47,6
		repeatSection1Start
		noteL 40,54
		ymVol 09h
		noteL 40,6
		ymVol 0Ch
		note 40
		note 40
		note 37
		ymVol 09h
		note 37
		ymVol 0Ch
		note 37
		ymVol 09h
		note 37
		ymVol 0Ch
		noteL 37,24
		repeatEnd
		repeatSection2Start
		noteL 47,54
		ymVol 09h
		noteL 47,6
		ymVol 0Ch
		note 47
		note 47
		note 47
		ymVol 09h
		note 47
		ymVol 0Ch
		note 47
		ymVol 09h
		note 47
		ymVol 0Ch
		noteL 47,30
		ymVol 09h
		noteL 47,6
		ymVol 0Ch
		note 51
		note 51
		countedLoopStart 1
		ymVol 0Ch
		noteL 49,6
		ymVol 09h
		note 49
		countedLoopEnd
		ymVol 0Ch
		noteL 51,6
		ymVol 09h
		note 51
		mainLoopStart
		countedLoopStart 1
		ymVol 0Bh
		noteL 45,6
		note 45
		noteL 45,18
		ymVol 08h
		noteL 45,6
		ymVol 0Bh
		note 45
		ymVol 08h
		note 45
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 37,6
		length 18
		noteL 37,6
		silence
		ymInst 13
		ymVol 0Bh
		note 47
		note 47
		noteL 47,18
		ymVol 08h
		noteL 47,6
		ymVol 0Bh
		note 47
		ymVol 08h
		note 47
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 39,6
		length 18
		noteL 39,6
		silence
		ymInst 13
		countedLoopEnd
		ymVol 0Bh
		noteL 45,6
		note 45
		noteL 45,18
		ymVol 08h
		noteL 45,6
		ymVol 0Bh
		note 45
		ymVol 08h
		note 45
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 40,6
		length 18
		noteL 40,6
		silence
		countedLoopStart 1
		ymInst 13
		ymVol 0Bh
		noteL 45,6
		note 45
		noteL 45,18
		ymVol 08h
		noteL 45,6
		ymVol 0Bh
		note 45
		ymVol 08h
		note 45
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 42,6
		length 18
		noteL 42,6
		silence
		countedLoopEnd
		ymInst 13
		ymVol 0Bh
		noteL 41,6
		note 41
		noteL 41,18
		ymVol 08h
		noteL 41,6
		ymVol 0Bh
		note 41
		ymVol 08h
		note 41
		ymVol 0Bh
		note 44
		note 44
		noteL 44,18
		ymVol 08h
		noteL 44,6
		ymVol 0Bh
		note 44
		ymVol 08h
		note 44
		mainLoopEnd
Music_3_Channel_3:
		ymStereo 0C0h
		ymInst 13
		ymVol 0Ch
		release 01h
		vibrato 02Ch
		noteL 34,24
		note 36
		ymVol 09h
		noteL 36,12
		ymVol 0Ch
		noteL 38,24
		noteL 39,6
		ymVol 09h
		note 39
		ymInst 20
		ymVol 0Bh
		note 44
		ymVol 08h
		note 44
		ymVol 0Bh
		note 44
		ymVol 08h
		note 44
		ymVol 0Bh
		note 44
		ymVol 08h
		note 44
		ymVol 0Bh
		noteL 49,24
		noteL 45,6
		ymVol 08h
		note 45
		ymVol 0Bh
		noteL 45,9
		ymVol 08h
		noteL 45,6
		ymVol 06h
		noteL 45,3
		ymVol 0Bh
		noteL 48,6
		note 51
		ymVol 08h
		note 51
		ymVol 06h
		note 51
		ymVol 04h
		note 51
		length 156
		ymInst 20
		ymVol 0Bh
		noteL 51,6
		note 51
		note 51
		ymVol 08h
		note 51
		ymVol 06h
		note 51
		ymVol 04h
		note 51
		length 108
		ymVol 0Bh
		noteL 51,6
		note 51
		note 51
		ymVol 08h
		note 51
		ymVol 0Bh
		note 51
		ymVol 08h
		note 51
		ymVol 0Bh
		noteL 51,12
		ymVol 08h
		noteL 51,6
		ymVol 06h
		note 51
Music_4_Channel_3:
		ymStereo 0C0h
		vibrato 02Ch
		release 01h
		ymInst 13
		repeatStart
		ymVol 0Ch
		noteL 37,30
		ymVol 09h
		noteL 37,6
		ymVol 0Ch
		note 37
		note 37
		note 40
		ymVol 09h
		note 40
		ymVol 07h
		note 40
		ymVol 0Ch
		note 42
		repeatSection1Start
		noteL 35,54
		ymVol 09h
		noteL 35,6
		ymVol 0Ch
		note 35
		note 35
		note 35
		ymVol 09h
		note 35
		ymVol 0Ch
		note 35
		ymVol 09h
		note 35
		ymVol 0Ch
		noteL 35,24
		repeatEnd
		repeatSection2Start
		noteL 44,54
		ymVol 09h
		noteL 44,6
		ymVol 0Ch
		note 44
		note 44
		note 42
		ymVol 09h
		note 42
		ymVol 0Ch
		note 40
		ymVol 09h
		note 40
		ymVol 0Ch
		noteL 42,30
		ymVol 09h
		noteL 42,6
		ymVol 0Ch
		note 47
		note 47
		countedLoopStart 2
		ymVol 0Ch
		noteL 47,6
		ymVol 09h
		note 47
		countedLoopEnd
		mainLoopStart
		countedLoopStart 1
		ymVol 0Bh
		noteL 37,6
		note 37
		noteL 37,18
		ymVol 08h
		noteL 37,6
		ymVol 0Bh
		note 37
		ymVol 08h
		note 37
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 33,6
		length 18
		noteL 33,6
		silence
		ymInst 13
		ymVol 0Bh
		note 39
		note 39
		noteL 39,18
		ymVol 08h
		noteL 39,6
		ymVol 0Bh
		note 39
		ymVol 08h
		note 39
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 35,6
		length 18
		noteL 35,6
		silence
		ymInst 13
		countedLoopEnd
		ymVol 0Bh
		noteL 37,6
		note 37
		noteL 37,18
		ymVol 08h
		noteL 37,6
		ymVol 0Bh
		note 37
		ymVol 08h
		note 37
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 33,6
		length 18
		noteL 33,6
		silence
		ymInst 13
		ymVol 0Bh
		note 42
		note 42
		noteL 42,18
		ymVol 08h
		noteL 42,6
		ymVol 0Bh
		note 42
		ymVol 08h
		note 42
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 38,6
		length 18
		noteL 38,6
		silence
		ymInst 13
		ymVol 0Bh
		note 38
		note 38
		noteL 38,18
		ymVol 08h
		noteL 38,6
		ymVol 0Bh
		note 38
		ymVol 08h
		note 38
		length 12
		ymInst 56
		ymVol 0Bh
		noteL 38,6
		length 18
		noteL 38,6
		silence
		countedLoopStart 1
		ymInst 13
		ymVol 0Bh
		noteL 38,6
		note 38
		noteL 38,18
		ymVol 08h
		noteL 38,6
		ymVol 0Bh
		note 38
		ymVol 08h
		note 38
		countedLoopEnd
		mainLoopEnd
Music_3_Channel_4:
		shifting 020h
		length 6
		ymStereo 040h
		ymInst 13
		ymVol 0Bh
		release 01h
		vibrato 02Ch
		noteL 41,24
		note 43
		ymVol 08h
		noteL 43,12
		ymVol 0Bh
		noteL 45,24
		noteL 46,6
		ymVol 08h
		note 46
		ymInst 20
		ymStereo 080h
		ymVol 0Bh
		note 53
		ymVol 08h
		note 53
		ymVol 0Bh
		note 54
		ymVol 08h
		note 54
		ymVol 0Bh
		note 51
		ymVol 08h
		note 51
		ymVol 0Bh
		noteL 56,24
		noteL 54,6
		ymVol 08h
		note 54
		ymVol 0Bh
		noteL 52,9
		ymVol 08h
		noteL 52,6
		ymVol 06h
		noteL 52,3
		ymVol 0Bh
		noteL 57,6
		note 59
		ymVol 08h
		note 59
		ymStereo 040h
		ymInst 27
		ymVol 0Ah
		noteL 28,12
		noteL 30,6
		silence
		note 39
		silence
		noteL 37,36
		noteL 30,6
		silence
		noteL 32,9
		silence
		noteL 44,6
		noteL 42,60
		ymStereo 080h
		ymInst 20
		ymVol 0Bh
		noteL 54,6
		note 54
		note 54
		ymVol 08h
		note 54
		ymStereo 040h
		ymInst 27
		ymVol 0Ah
		noteL 28,12
		noteL 30,6
		silence
		note 39
		silence
		note 37
		silence
		noteL 33,12
		noteL 35,9
		silence
		noteL 44,6
		noteL 47,36
		ymStereo 080h
		ymInst 20
		ymVol 0Bh
		noteL 54,6
		note 54
		note 54
		ymVol 08h
		note 54
		ymVol 0Bh
		note 54
		ymVol 08h
		note 54
		ymVol 0Bh
		noteL 54,12
		ymVol 08h
		noteL 54,6
Music_4_Channel_4:
		shifting 020h
		ymStereo 040h
		length 6
		ymInst 13
		release 01h
		vibrato 02Ch
		repeatStart
		ymVol 0Bh
		noteL 44,30
		ymVol 08h
		noteL 44,6
		ymVol 0Bh
		note 44
		note 44
		noteL 47,9
		ymVol 08h
		noteL 47,6
		ymVol 06h
		noteL 47,3
		ymVol 0Bh
		noteL 49,6
		repeatSection1Start
		noteL 44,54
		ymVol 08h
		noteL 44,6
		ymVol 0Bh
		note 44
		note 44
		note 42
		ymVol 08h
		note 42
		ymVol 0Bh
		note 40
		ymVol 08h
		note 40
		ymVol 0Bh
		noteL 42,24
		repeatEnd
		repeatSection2Start
		noteL 52,54
		ymVol 08h
		noteL 52,6
		ymVol 0Bh
		note 52
		note 52
		note 51
		ymVol 08h
		note 51
		ymVol 0Bh
		note 49
		ymVol 08h
		note 49
		ymVol 0Bh
		noteL 51,30
		ymVol 08h
		noteL 51,6
		ymVol 0Bh
		note 56
		note 56
		note 54
		ymVol 08h
		note 54
		ymVol 0Bh
		note 52
		ymVol 08h
		note 52
		ymVol 0Bh
		note 54
		ymVol 08h
		note 54
		ymStereo 040h
		mainLoopStart
		ymInst 7
		ymVol 0Bh
		noteL 49,48
		note 52
		noteL 51,6
		note 52
		noteL 54,60
		noteL 52,12
		note 51
		noteL 52,36
		noteL 49,6
		ymVol 09h
		note 49
		ymVol 0Bh
		noteL 49,36
		noteL 52,6
		ymVol 09h
		note 52
		ymVol 0Bh
		noteL 51,96
		noteL 52,48
		note 56
		noteL 54,6
		note 56
		noteL 57,60
		noteL 56,12
		note 54
		countedLoopStart 1
		noteL 56,36
		noteL 49,6
		ymVol 09h
		note 49
		ymVol 0Bh
		noteL 49,36
		noteL 56,6
		ymVol 09h
		note 56
		ymVol 0Bh
		countedLoopEnd
		mainLoopEnd
Music_3_Channel_5:
		ymStereo 0C0h
		length 60
		sampleL 1,24
		sampleL 1,12
		sample 0
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,6
		sample 3
		sampleL 5,24
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,6
		sample 4
		sample 3
		sample 3
		sampleL 5,132
		countedLoopStart 1
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,12
		countedLoopEnd
		sampleL 2,6
		sample 2
		sampleL 5,108
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		countedLoopStart 1
		sampleL 2,6
		sample 3
		sample 3
		sample 3
		countedLoopEnd
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,12
Music_4_Channel_5:
		ymStereo 0C0h
		repeatStart
		length 24
		sampleL 0,12
		sampleL 2,6
		sample 3
		sampleL 2,18
		sampleL 3,6
		sample 2
		sample 3
		sample 3
		sample 3
		sampleL 2,12
		sampleL 0,24
		sampleL 2,6
		sample 3
		sampleL 2,12
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		repeatSection1Start
		sampleL 2,24
		repeatEnd
		repeatSection2Start
		sampleL 2,12
		sampleL 0,24
		sampleL 2,6
		sample 3
		sample 2
		sample 2
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,12
		mainLoopStart
		countedLoopStart 2
		sampleL 2,6
		sample 3
		sampleL 2,12
		sample 0
		sampleL 2,24
		sampleL 2,4
		sample 3
		sample 3
		sampleL 2,6
		sample 3
		sampleL 2,12
		countedLoopEnd
		sampleL 2,6
		sample 3
		sampleL 2,12
		sample 0
		sampleL 2,18
		sampleL 2,6
		sample 2
		sample 2
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 2,6
		sample 2
		countedLoopStart 2
		sampleL 2,6
		sample 3
		sampleL 2,12
		sample 0
		sampleL 2,24
		sampleL 2,4
		sample 3
		sample 3
		sampleL 2,6
		sample 3
		sampleL 2,12
		countedLoopEnd
		countedLoopStart 1
		sampleL 2,6
		sample 3
		sampleL 2,3
		sample 3
		sample 3
		sample 4
		sampleL 0,12
		sample 2
		countedLoopEnd
		mainLoopEnd
Music_3_Channel_6:
		psgInst 124
		release 01h
		vibrato 04Ch
		noteL 46,6
		note 41
		note 39
		note 41
		note 48
		note 43
		note 41
		note 43
		note 41
		note 43
		note 50
		note 45
		note 43
		note 45
		note 51
		note 46
		note 53
		note 49
		note 54
		note 51
		note 47
		note 44
		note 56
		note 52
		note 49
		note 45
		note 54
		note 50
		note 48
		note 52
		note 57
		note 60
		note 63
		psgInst 123
		length 18
		repeatStart
		countedLoopStart 14
		noteL 40,4
		note 42
		countedLoopEnd
		psgInst 125
		noteL 45,6
		note 46
		note 47
		note 48
		note 49
		note 50
		note 51
		note 52
		repeatSection1Start
		noteL 54,6
		psgInst 123
		length 18
		repeatEnd
		repeatSection2Start
Music_4_Channel_6:
		vibrato 04Ch
		release 01h
		psgInst 125
		noteL 53,6
		silence
		repeatStart
		noteL 56,4
		note 58
		note 60
		noteL 61,6
		silence
		psgInst 0
		length 36
		psgInst 125
		noteL 35,6
		note 40
		note 44
		note 47
		note 52
		silence
		noteL 52,4
		note 54
		note 55
		noteL 56,6
		psgInst 123
		length 18
		psgInst 125
		noteL 54,6
		note 59
		note 54
		note 52
		repeatSection1Start
		noteL 51,6
		note 49
		note 47
		note 42
		length 12
		repeatEnd
		repeatSection2Start
		noteL 54,6
		silence
		noteL 54,4
		note 56
		note 57
		note 59
		length 20
		noteL 47,6
		note 45
		note 42
		note 44
		note 45
		note 47
		mainLoopStart
		psgInst 0
		length 96
		silence
		silence
		length 12
		psgInst 13
		noteL 54,6
		note 56
		note 57
		note 59
		note 57
		note 56
		note 54
		note 52
		note 49
		note 51
		note 59
		note 57
		note 53
		note 54
		silence
		psgInst 0
		length 96
		silence
		psgInst 13
		noteL 47,6
		note 49
		note 50
		note 52
		note 54
		note 57
		note 56
		note 54
		note 52
		note 49
		note 50
		note 52
		note 50
		note 52
		note 54
		note 56
		note 55
		note 53
		note 61
		note 59
		note 56
		note 55
		note 53
		note 52
		note 50
		note 49
		note 61
		note 59
		note 56
		note 52
		note 53
		mainLoopEnd
Music_3_Channel_7:
		psgInst 124
		release 01h
		vibrato 04Ch
		noteL 30,6
		note 34
		note 37
		note 34
		note 32
		note 36
		note 39
		note 36
		note 39
		note 36
		note 34
		note 38
		note 41
		note 38
		note 42
		note 39
		note 37
		note 41
		note 32
		note 35
		note 39
		note 35
		note 33
		note 37
		note 40
		note 37
		note 38
		note 42
		note 45
		note 40
		note 36
		note 45
		note 42
		psgInst 123
		length 18
		repeatStart
		countedLoopStart 14
		noteL 37,4
		note 39
		countedLoopEnd
		psgInst 125
		noteL 37,6
		note 38
		note 39
		note 40
		note 41
		note 42
		note 43
		note 44
		repeatSection1Start
		noteL 45,6
		psgInst 123
		length 18
		repeatEnd
		repeatSection2Start
Music_4_Channel_7:
		vibrato 04Ch
		release 01h
		psgInst 125
		noteL 44,6
		length 18
		repeatStart
		shifting 010h
		psgInst 123
		noteL 56,4
		note 58
		note 60
		noteL 61,6
		silence
		psgInst 0
		length 36
		psgInst 123
		noteL 35,6
		note 40
		note 44
		note 47
		note 52
		silence
		noteL 52,4
		note 54
		note 55
		noteL 56,6
		psgInst 121
		length 18
		psgInst 123
		noteL 54,6
		note 59
		note 54
		note 52
		repeatSection1Start
		noteL 51,6
		note 49
		note 47
		note 42
		length 12
		repeatEnd
		repeatSection2Start
		noteL 54,6
		silence
		noteL 54,4
		note 56
		note 57
		note 59
		length 20
		noteL 47,6
		note 45
		note 42
		note 44
		note 45
		note 47
		mainLoopStart
		psgInst 0
		length 96
		silence
		silence
		length 12
		psgInst 11
		noteL 54,6
		note 56
		note 57
		note 59
		note 57
		note 56
		note 54
		note 52
		note 49
		note 51
		note 59
		note 57
		note 53
		note 54
		silence
		psgInst 0
		length 96
		silence
		psgInst 11
		noteL 47,6
		note 49
		note 50
		note 52
		note 54
		note 57
		note 56
		note 54
		note 52
		note 49
		note 50
		note 52
		note 50
		note 52
		note 54
		note 56
		note 55
		note 53
		note 61
		note 59
		note 56
		note 55
		note 53
		note 52
		note 50
		note 49
		note 61
		note 59
		note 56
		note 52
		note 53
		mainLoopEnd
Music_4_Channel_9:
		channel_end