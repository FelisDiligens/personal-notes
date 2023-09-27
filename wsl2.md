---
title: Windows Subsystem for Linux
category: Windows
---

<img src="assets/wsl.png" width="96">

# Windows Subsystem for Linux

## Usage

- Shutdown running distro(s): `wsl --shutdown`
- Update Linux kernel (not WSL itself): `wsl --update`
- List installed distros: `wsl --list --all --verbose`
- List installable distros: `wsl --list --online`
- Install distro (e.g. Debian): `wsl --install -d Debian`
- Uninstall distro (e.g. Debian): `wsl --unregister Debian`
- Export distro: `wsl --export Debian $env:USERPROFILE\WSL\DebianExport.tar`
- Import distro: `wsl --import Debian $env:USERPROFILE\WSL\Debian $env:USERPROFILE\WSL\DebianExport.tar`

## wslutilities

- [GitHub](https://github.com/wslutilities/wslu#readme)
- [Website](https://wslutiliti.es/wslu/)
- [Installation](https://wslutiliti.es/wslu/install.html)

### Add desktop shortcuts

```bash
find /usr/share/icons -iname "*nautilus*"
wslusc -n "Files" -i /usr/share/icons/Yaru/256x256@2x/apps/org.gnome.Nautilus.png nautilus
```


## Miscellaneous

### Change default shell

```bash
chsh --shell /usr/bin/fish
```

### systemd
Set the systemd flag set in your WSL distro settings.  
You will need to edit the [wsl.conf](https://docs.microsoft.com/windows/wsl/wsl-config#wslconf) file to ensure systemd starts up on boot.

`/etc/wsl.conf`
```ini
[boot]
systemd=true
```

### Run in background

#### Interactively

See https://gist.github.com/FelisDiligens/fedd413fc1192aa43150891a631e9c8c

#### Automatically

`wsl-startup.vbs`

Change `<Distro>` to the distro name you are using. Use `wsl -l` to find out the name.

```vbs
set ws=wscript.CreateObject("wscript.shell")
ws.run "wsl -d <Distro>", 0
```

> Source: https://askubuntu.com/a/1452424

### Mount ext4

https://www.hanselman.com/blog/wsl2-can-now-mount-linux-ext4-disks-directly

List drives in PowerShell:
```powershell
Get-CimInstance -query "SELECT * from Win32_DiskDrive"
wsl --mount \\.\PHYSICALDRIVE0 --type ext4 --partition 2
```

Mount a partition in WSL:
```powershell
wsl --mount \\.\PHYSICALDRIVE0 --type ext4 --partition 2
```

This should mount it under: `/mnt/wsl/PHYSICALDRIVE0p2`

To unmount it:
```powershell
wsl --unmount \\.\PHYSICALDRIVE0
```
