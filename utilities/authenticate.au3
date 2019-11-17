ConsoleWrite( "Started running AutoIt script to fill in credentials" & @CRLF)

Local $browserNames = ["Firefox", "Internet Explorer", "Chrome"]
Local $titles[3] = ["Authentication Required", "Windows Security", "https://qa-task.backbasecloud.com - Google Chrome"]

$iMax = UBound($titles)
For $i = 0 to $iMax - 1
   $hWnd = 0
   If Not WinExists($titles[$i]) Then
	  $hWnd = WinWait($titles[$i], "", 1)
   Else
	  ConsoleWrite( "Give focus to browser = " & $browserNames[$i] & @CRLF)
	  $hWnd = WinActivate($titles[$i])

	  ConsoleWrite( "Fill in credentials" & @CRLF)
	  Send("candidatex")
	  Send("{TAB}")
	  Send("qa-is-cool")
	  Send("{ENTER}")
	  Sleep(500)
   EndIf
Next
ConsoleWrite( "Finished running AutoIt script !" & @CRLF)
