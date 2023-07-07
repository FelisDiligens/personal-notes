<img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Windows_Terminal_logo.svg" width="96">

# Windows Terminal

## settings.json

The path for your Windows Terminal settings.json file may be found in one of the following directories:
- Terminal (stable / general release): `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`
- Terminal (preview release): `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json`
- Terminal (unpackaged: Scoop, Chocolately, etc): `%LOCALAPPDATA%\Microsoft\Windows Terminal\settings.json`

But you can simply open it from the settings.

### Defaults

```json
"defaults": 
{
	"antialiasingMode": "cleartype",
	"closeOnExit": "always",
	"cursorShape": "filledBox",
	"colorScheme": "Catppuccin Mocha",
	"snapOnInput": true,
	"font": 
	{
		"face": "FiraCode NF"
	}
},
```

### Font

```json
{
    "profiles": {
        "defaults": {
            "font": {
                "face": "FiraCode NF"
            }
        },
    }
}
```

- Windows: `FiraCode NF`
- Linux: `FiraCode Nerd Font`


### PowerShell profile

Add `-nologo` to the `commandLine` option, like so:

```json
{
    "commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -nologo",
}
```

### Git Bash profile

```json
{
	"guid": "{9183170b-949e-4f19-9616-9969814918ab}",
	"commandline": "C:\\Program Files\\Git\\bin\\bash.exe -i -l",
	"icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
	"name": "Git Bash",
	"startingDirectory": "~",
	"hidden": false
},
```

### Cygwin profile

```json
{
    "guid": "{56f5c0d8-8dfa-48ae-a9a3-5287ab830a1a}",
    "commandline": "C:\\cygwin64\\bin\\bash.exe /bin/xhere /bin/bash",
    "icon": "C:\\cygwin64\\Bash.ico",
    "name": "Cygwin Bash",
    "startingDirectory": "C:\\cygwin64\\home\\username",
    "hidden": false
},
```

## Color Schemes
1. Find any color scheme here: https://windowsterminalthemes.dev/
2. Click "Get theme" to copy it to your clipboard
3. Open `settings.json` and paste it into `"schemes": [ ... ]`

- More themes: https://iterm2colorschemes.com/
- Docs: https://learn.microsoft.com/de-de/windows/terminal/customize-settings/color-schemes
- ColorTool (`scoop install colortool`): https://github.com/microsoft/terminal/tree/main/src/tools/ColorTool
- Catppuccin: https://github.com/catppuccin/windows-terminal

## Shortcut to profile
`wt new-tab --profile "Spyder (Spy)"`