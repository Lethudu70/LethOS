
; Script Inno Setup pour LethOS File Explorer
[Setup]
AppName=LethOS File Explorer
AppVersion=1.0
DefaultDirName={pf}\LethOS Explorer
DefaultGroupName=LethOS
OutputDir=dist
OutputBaseFilename=LethOS_Explorer_Setup
SetupIconFile=LethOS_FileExplorer_Icon.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\Leth_Exploro.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\LethOS File Explorer"; Filename: "{app}\Leth_Exploro.exe"
Name: "{commondesktop}\LethOS File Explorer"; Filename: "{app}\Leth_Exploro.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Créer une icône sur le bureau"; GroupDescription: "Icônes supplémentaires:"
