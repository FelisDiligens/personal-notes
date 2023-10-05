---
title: Cygwin
category: Windows
---

<img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Cygwin_logo.svg" width="96">

# Cygwin

## Install packages

### Using the setup.exe

Cygwin's setup accepts [command-line arguments](https://cygwin.com/faq/faq.html#faq.setup.cli) to install packages from the command-line.

`setup-x86.exe -q -P packagename1,packagename2` to install packages without any GUI interaction ("unattended setup mode").

Use `setup-x86.exe --no-admin` if you don't have admin rights or want to install it for the current user only.

> **note**  
> Note that you need to use `setup-x86.exe` or `setup-x86_64.exe` as appropriate.

See https://cygwin.com/packages/ for the package list.

> Source: https://stackoverflow.com/a/14986916

### apt-cyg

> **warning**  
> Requires `wget`

For a more convenient installer, you may want to use `apt-cyg` as your package manager. It's syntax is similar to `apt-get`. To install, type in the terminal:

```bash
wget https://raw.githubusercontent.com/transcode-open/apt-cyg/master/apt-cyg
chmod +x apt-cyg
mv apt-cyg /usr/local/bin
```

> Source: https://stackoverflow.com/a/16869816

## Windows Terminal Profil

> **warning**  
> Requires `chere`  
> `apt-cyg install chere`

<details>
<summary>Default path (bash)</summary>

```json
{
	"commandline": "C:\\cygwin64\\bin\\bash.exe /bin/xhere /bin/bash",
	"guid": "{56f5c0d8-8dfa-48ae-a9a3-5287ab830a1a}",
	"hidden": false,
	"icon": "C:\\cygwin64\\Bash.ico",
	"name": "Cygwin Bash",
	"startingDirectory": "C:\\cygwin64\\home\\user"
},
```

</details>

<details>
<summary>Default path (fish)</summary>

```json
{
	"commandline": "C:\\cygwin64\\bin\\bash.exe /bin/xhere /bin/fish",
	"guid": "{89499317-6013-453b-8b44-7799a5d76f77}",
	"hidden": false,
	"icon": "C:\\cygwin64\\oh-my-fish.ico",
	"name": "Cygwin Fish",
	"startingDirectory": "C:\\Users\\user"
},
```

</details>

## Troubleshooting

### Change Cygwin home directory

Edit `/etc/nsswitch.conf` and add `db_home: <unix_path>`

For the Windows `%USERPROFILE%`, set `db_home: windows`

> Source: https://stackoverflow.com/a/1494721

### Change DOS-style line endings (CRLF) to Unix-style line endings (LF)
```bash
apt-cyg install dos2unix
dos2unix /path/to/file
```

### `fish` is missing cygpcre2-16-0.dll
```
apt-cyg install libpcre2_16_0
```

### Suppress "Starting /bin/xyz"
Edit the script `/bin/xhere` and comment the echo line at the end.

> Source: https://superuser.com/a/740274