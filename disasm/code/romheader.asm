
; ASM FILE code\romheader.asm :
; 0x0..0x200 : ROM Header
InitStack:      ; File Name   : D:\SEGADEV\IDB\SF2\sf2.bin
                dc.l InitStack          ; Initial Stack
p_Start:        dc.l Start              ; Start Address
                dc.l Int_OtherError     ; Bus Error
                dc.l Int_AdressError    ; Address Error
off_10:         dc.l Int_IllegalInstruction; Illegal instruction
                dc.l Int_ZeroDivide     ; Zero Divide
                dc.l Int_OtherError     ; CHK instruction
off_1C:         dc.l Int_OtherError     ; TRAPV instruction
                dc.l Int_OtherError     ; Privilege Violation
                dc.l Int_OtherError     ; Trace
                dc.l Int_OtherError     ; Line 1010 Emulator
                dc.l Int_OtherError     ; Line 1111 Emulator
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Unitialized Interrrupt
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Spurious Interrupt
                dc.l Int_ExternalInterrupt; Level 1 interrupt
                dc.l Int_ExternalInterrupt; Level 2/External  interrupt
                dc.l Int_ExternalInterrupt; Level 3 interrupt
                dc.l HInt               ; Level 4/Horizontal interrupt
                dc.l Int_ExternalInterrupt; Level 5 interrupt
                dc.l VInt               ; Level 6/Vertical interrupt
                dc.l IntLvl7            ; Level 7 interrupt
                dc.l Trap0_SoundCommand 
                dc.l Trap1_CheckFlag
                dc.l Trap2_SetFlag
                dc.l Trap3_ClearFlag
                dc.l Trap4_CheckFlag
                dc.l Trap5_TextBox
                dc.l Trap6_TriggerAndExecuteMapScript
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Trap9_ManageContextualFunctions; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_ExternalInterrupt; Trap
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
                dc.l Int_OtherError     ; Reserved
aSegaGenesis:   dc.b 'SEGA GENESIS    '
aCSega1994_jul: dc.b '(C)SEGA 1994.JUL'
aShiningForce2: dc.b 'SHINING FORCE 2 '
                dc.b '                '
                dc.b '                '
aShiningForce_0:dc.b 'SHINING FORCE 2 '
                dc.b '                '
                dc.b '                '
aGmMk13150:     dc.b 'GM MK-1315 -0'    ; Serial Number
                dc.b $30
                dc.w $8921              ; checksum
aJ:             dc.b 'J               '
                dc.l 0                  ; Rom Start Adress
RomEndAddress:  declareRomEnd           ; Rom End Adress
                dc.l $FF0000            ; Ram Start Adress
                dc.l $FFFFFF            ; Ram End Adress
                dc.l $5241F820          ; SRam data
                dc.l $200001            ; Sram Start Address
                dc.l $203FFF            ; Sram End Address
                dc.b '            '     ; Modem data
                dc.b '                    '; Memo
                dc.b '                    '
aU:             headerRegion            ; Countries codes
