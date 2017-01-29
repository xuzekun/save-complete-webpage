ControlFocus("另存为", "","Edit1");ControlFocus("title","text",controlID) Edit1=Edit instance 1
; Wait 10 seconds for the Upload window to appear

  WinWait("[CLASS:#32770]","",10)

; Set input focus to the edit control of Upload window using the handle returned by WinWait

  ControlFocus("另存为","","Edit1")

  Sleep(500)

; Set the File name text on the Edit field

  ControlSetText("另存为", "", "Edit1", $CmdLine[1])

  Sleep(500)


; Click on the Open button

  ControlClick("另存为", "","Button2");


ControlFocus("确认另存为", "","Button1");
   WinWait("[CLASS:#32770]","",10)
   Sleep(500)

   ControlClick("确认另存为", "","Button1");
   Sleep(500)