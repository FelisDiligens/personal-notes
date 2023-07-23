---
title: Windows Terminal
category: Windows
---

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

<details>
<summary>Panda</summary>

```json
{
	"name": "Panda",
	"background": "#1D1E20",
	"black": "#1F1F20",
	"blue": "#5C9FFF",
	"brightBlack": "#5C6370",
	"brightBlue": "#55ADFF",
	"brightCyan": "#26FFD4",
	"brightGreen": "#26FFD4",
	"brightPurple": "#FD95D0",
	"brightRed": "#FB055A",
	"brightWhite": "#F0F0F0",
	"brightYellow": "#FEBE7E",
	"cursorColor": "#FFFFFF",
	"cyan": "#26FFD4",
	"foreground": "#F0F0F0",
	"green": "#26FFD4",
	"purple": "#FC59A6",
	"red": "#FB055A",
	"selectionBackground": "#F0F0F0",
	"white": "#F0F0F0",
	"yellow": "#FDAA5A"
}
```

</details>

<details>
<summary>Lovelace</summary>

```json
{
  "name": "Lovelace",
  "black": "#282a36",
  "red": "#f37f97",
  "green": "#5adecd",
  "yellow": "#f2a272",
  "blue": "#8897f4",
  "purple": "#c574dd",
  "cyan": "#79e6f3",
  "white": "#fdfdfd",
  "brightBlack": "#414458",
  "brightRed": "#ff4971",
  "brightGreen": "#18e3c8",
  "brightYellow": "#ff8037",
  "brightBlue": "#556fff",
  "brightPurple": "#b043d1",
  "brightCyan": "#3fdcee",
  "brightWhite": "#bebec1",
  "background": "#1d1f28",
  "foreground": "#fdfdfd",
  "selectionBackground": "#c1deff",
  "cursorColor": "#c574dd"
}
```

</details>

<details>
<summary>Git Bash</summary>

```json
{
	"background": "#000000",
	"black": "#000000",
	"blue": "#0020C0",
	"brightBlack": "#606060",
	"brightBlue": "#7D97FF",
	"brightCyan": "#00F0F0",
	"brightGreen": "#00F200",
	"brightPurple": "#FF70FF",
	"brightRed": "#FF7676",
	"brightWhite": "#FFFFFF",
	"brightYellow": "#F2F200",
	"cursorColor": "#FFFFFF",
	"cyan": "#00A89A",
	"foreground": "#BFBFBF",
	"green": "#1CA800",
	"name": "Git-Bash-ColorScheme",
	"purple": "#863696",
	"red": "#A21E29",
	"selectionBackground": "#BFBFBF",
	"white": "#BFBFBF",
	"yellow": "#C0A000"
}
```

</details>

<details>
<summary>Ubuntu (Official)</summary>

```json
{
	"background": "#300A24",
	"black": "#171421",
	"blue": "#0037DA",
	"brightBlack": "#767676",
	"brightBlue": "#08458F",
	"brightCyan": "#2C9FB3",
	"brightGreen": "#26A269",
	"brightPurple": "#A347BA",
	"brightRed": "#C01C28",
	"brightWhite": "#F2F2F2",
	"brightYellow": "#A2734C",
	"cursorColor": "#FFFFFF",
	"cyan": "#3A96DD",
	"foreground": "#FFFFFF",
	"green": "#26A269",
	"name": "Ubuntu-ColorScheme",
	"purple": "#881798",
	"red": "#C21A23",
	"selectionBackground": "#FFFFFF",
	"white": "#CCCCCC",
	"yellow": "#A2734C"
}
```

</details>

## Shortcut to profile
`wt new-tab --profile "Spyder (Spy)"`