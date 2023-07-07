# Common paths and registry values

## Start menu

- Currently logged in user: `%APPDATA%\Microsoft\Windows\Start Menu\Programs`
- All users: `%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs`

## Icons

```txt
%SYSTEMROOT%\system32\imageres.dll
%SYSTEMROOT%\system32\shell32.dll
%SYSTEMROOT%\explorer.exe
%SYSTEMROOT%\system32\ddores.dll
```

- [NirSoft's IconsExtract](https://www.nirsoft.net/utils/iconsext.html)

## Environment variables

### User Variables

```
HKEY_CURRENT_USER\Environment
```

### System Variables

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
```

## "God mode" folder

Create a folder with the following name:  
`GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}`

The name before the dot actually doesn't matter. Just make sure the UUID is correct.

## Control Panel

| Target                                      | Input                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Control Panel                               | `control.exe`                                                                               |
| Sound                                       | `mmsys.cpl`                                                                                 |
| Environment Variables                       | `rundll32.exe sysdm.cpl,EditEnvironmentVariables`                                           |
| User accounts                               | `netplwiz`                                                                                  |
| Local Group Policy Editor                   | `gpedit.msc`                                                                                |
| Local Users and Groups (Local)              | `lusrmgr.msc`                                                                               |
| Devices and Printers                        | `Shell:::{A8A91A66-3A7D-4424-8D24-04E180695C7A}`                                            |
| Textdienste und Eingabesprachen (Alt+Shift) | `rundll32.exe Shell32.dll,Control_RunDLL input.dll,,{C07337D3-DB2C-4D0B-9A93-B722A6C106E2}` |

## Autostart folder

| Target                               | Input                  | Folder path                                                    |
| ------------------------------------ | ---------------------- | -------------------------------------------------------------- |
| Startup for currently logged in user | `shell:startup`        | `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`      |
| Startup for all users                | `shell:common startup` | `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` |

https://www.deskmodder.de/wiki/index.php/Autostart_Windows_10_Programme_deaktivieren_hinzuf%C3%BCgen_entfernen

## Looking for more folders to open?

| Target                | UUID                                             |
| --------------------- | ------------------------------------------------ |
| This PC / My Computer | `Shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}` |
| Recycle Bin           | `Shell:::{645FF040-5081-101B-9F08-00AA002F954E}` |
| Downloads             | `Shell:::{374DE290-123F-4565-9164-39C4925E467B}` |
| Documents             | `Shell:::{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}` |
| Pictures              | `Shell:::{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}` |
| Music                 | `Shell:::{1CF1260C-4DD0-4ebb-811F-33C572699FDE}` |