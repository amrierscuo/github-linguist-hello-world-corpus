# Microsoft Developer Studio Project File - Name="Hello" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# TARGTYPE "Win32 (x86) Console Application" 0x0103
CFG=Hello - Win32 Debug
# Begin Project
# PROP AllowPerConfigDependencies 0
CPP=cl.exe
!IF  "$(CFG)" == "Hello - Win32 Debug"
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "Debug"
# PROP Intermediate_Dir "Debug"
# ADD CPP /nologo /MDd /W3 /Od /D "WIN32" /D "_DEBUG" /D "_CONSOLE" /c
LINK32=link.exe
# ADD LINK32 kernel32.lib /nologo /subsystem:console /debug /machine:I386
!ENDIF
# Begin Target
# Name "Hello - Win32 Debug"
# Begin Group "Source Files"
# PROP Default_Filter "c;cpp;cxx"
# Begin Source File
SOURCE=.\hello.c
# End Source File
# End Group
# End Target
# End Project
