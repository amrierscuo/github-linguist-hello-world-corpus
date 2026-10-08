[Setup]
AppName=Hello World
AppVersion=1.0
DefaultDirName={autopf}\CorpusHelloWorld
CreateAppDir=no
Uninstallable=no
OutputBaseFilename=hello-world-setup

[Code]
procedure InitializeWizard();
begin
  MsgBox('Hello, World!', mbInformation, MB_OK);
end;
