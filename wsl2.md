---
title: Windows Subsystem for Linux
category: Windows
---

<img src="assets/wsl.png" width="96">

# Windows Subsystem for Linux

## wslutilities

Contains `wslview`

- https://github.com/wslutilities/wslu#readme
- https://wslutiliti.es/wslu/
- `sudo apt install wslu`


## Run in background

### Interactively

See https://gist.github.com/FelisDiligens/fedd413fc1192aa43150891a631e9c8c

### Automatically

`wsl-startup.vbs`

Change `<Distro>` to the distro name you are using. Use `wsl -l` to find out the name.

```vbs
set ws=wscript.CreateObject("wscript.shell")
ws.run "wsl -d <Distro>", 0
```

> Source: https://askubuntu.com/a/1452424


## systemd

### Set the systemd flag set in your WSL distro settings

You will need to edit the [wsl.conf](https://docs.microsoft.com/windows/wsl/wsl-config#wslconf) file to ensure systemd starts up on boot.

`/etc/wsl.conf`
```ini
[boot]
systemd=true
```

## Debian

First, install Debian in WSL2:
```bash
wsl --install -d Debian
```

Then for the packages:
```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install git wget curl vim python-is-python3 fish bat exa zoxide fzf pipx gnupg2 apt-transport-https
# Starship
curl -sS https://starship.rs/install.sh | sh
# WSL Utilities: https://wslutiliti.es/wslu/install.html
wget -O - https://pkg.wslutiliti.es/public.key | sudo tee -a /etc/apt/trusted.gpg.d/wslu.asc
echo "deb https://pkg.wslutiliti.es/debian bookworm main" | sudo tee -a /etc/apt/sources.list
sudo apt update
sudo apt install wslu
```

## Miscellaneous

### Change default shell

```bash
chsh --shell /usr/bin/fish
```
