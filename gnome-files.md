---
title: GNOME Files (Nautilus)
category: Linux
---

<img src="assets/files-adwaita.svg" width="96px">

## GNOME Files (Nautilus)

### Extensions
- [Open any terminal](https://github.com/Stunkymonkey/nautilus-open-any-terminal)

### Scripts

You can create scripts that can be run when through the context menu in Nautilus:

- Create a file, e.g. `Terminal`, under `$HOME/.local/share/nautilus/scripts`
	```bash
	#!/bin/bash
	gnome-terminal
	```
	(You can also have spaces in the file name)
- Make it executable, e.g. `chmod +x Terminal`
- Edit the file `.config/nautilus/scripts-accels` and add a shortcut to it (optional, if you want a shortcut):
    ```
	F4 Terminal
	; Commented lines must have a space after the semicolon
	; Examples of other key combinations:
	; <Control>F12 Terminal
	; <Alt>F12 Terminal
	; <Shift>F12 Terminal
	```
- Enter `nautilus -q` or logout/login for changes to take effect.
- (Bug workaround) You may need to run the script by right-clicking and selecting Scripts → \<your script\> first. Then the shortcut should work.


#### Available parameters passed to the script

When Nautilus calls a script, it passes some important information to the script as environment variables.

| Advanced Parameters (Environment Variables)                                                              ||
|-----------------------------------------|-----------------------------------------------------------------|
| NAUTILUS\_SCRIPT\_SELECTED\_FILE\_PATHS | Paths of the selected files, separated by a new line (if local) |
| NAUTILUS\_SCRIPT\_SELECTED\_URIS        | URIs of the selected files, also separated by a new line        |
| NAUTILUS\_SCRIPT\_CURRENT\_URI          | URI of the current location                                     |
| NAUTILUS\_SCRIPT\_WINDOW\_GEOMETRY      | Position and size of the current window                         |

- For local locations, the selected files or directories are additionally set as arguments for the script. However, only the filenames within the folder are passed, not the absolute paths! This means that the script is called as follows:  
    `~/.local/share/nautilus/scripts/ScriptName, <File1>, <File2>, ..., <FileN>`
- For network locations (e.g. via FTP, SSH, SMB), `NAUTILUS_SCRIPT_SELECTED_FILE_PATHS` and the argument list can also be empty.
