[Setup]
AppName=Reproductor
AppVersion=1.0
DefaultDirName={pf}\Reproductor
DefaultGroupName=Reproductor
OutputDir=.\Output
OutputBaseFilename=Reproductor
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\Reproductor.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Reproductor"; Filename: "{app}\Reproductor.exe"

[Run]
Filename: "{app}\Reproductor.exe"; Description: "Ejecutar Mi Reproductor de Audio"; Flags: nowait postinstall skipifsilent
