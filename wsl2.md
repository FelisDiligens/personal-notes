---
title: Windows Subsystem for Linux
category: Windows
---

<img src="assets/wsl.png" width="96">

# Windows Subsystem for Linux

## Installation

Enter in an unelevated PowerShell prompt:  
```powershell
wsl --install
```

This will install the following things:
- Virtual Machine Platform (German: "VM-Plattform")
- Windows Subsystem for Linux
- WSL Kernel
- Ubuntu

## Uninstallation

### Remove distro

```powershell
wsl --shutdown
wsl --unregister <distro>
```

### Remove WSL

Uninstall the following Windows Features:
- Virtual Machine Platform (German: "VM-Plattform")
- Windows Subsystem for Linux

## Usage

- Shutdown running distro(s): `wsl --shutdown`
- Update Linux kernel (not WSL itself): `wsl --update`
- List installed distros: `wsl --list --all --verbose`
- List installable distros: `wsl --list --online`
- Install distro (e.g. Debian): `wsl --install -d Debian`
- Uninstall distro (e.g. Debian): `wsl --unregister Debian`
- Export distro: `wsl --export Debian $env:USERPROFILE\WSL\DebianExport.tar`
- Import distro: `wsl --import Debian $env:USERPROFILE\WSL\Debian $env:USERPROFILE\WSL\DebianExport.tar`

## Troubleshooting

### Switch to version 2

Check which WSL version is used:
```powershell
wsl --list --verbose
```
```txt
  NAME          STATE            VERSION
* Ubuntu        Stopped          2
```

Switch to version 2:
```powershell
wsl --set-version Ubuntu 2
```

```txt
Conversion in progress, this may take a few minutes...
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
Conversion complete.
```

If the above command fails due to a missing update:
```powershell
wsl --update
```

### Use VMware/VirtualBox with WSL2

VMware 15.5.5+ and VirtualBox 6+ support Hyper-V, although the performance will be degraded:

> When Hyper-V is enabled on the Windows host, the hypervisor is running at ring 3 while without it, the hypervisor runs at ring 0. So it is expected to be slower as there are additional layers of software (the WHP API and so on) before it gets to the CPU virtualisation features.  
> [Source](https://communities.vmware.com/t5/VMware-Workstation-Player/Huge-performance-drop-of-VMWare-Player-guest-running-on-Windows/m-p/2808506/highlight/true#M35785)

You can check if Hyper-V is enabled with:
```powershell
bcdedit /enum | findstr -i hypervisorlaunchtype
```

To enable it:
```powershell
bcdedit /set hypervisorlaunchtype auto
```

And to disable it:
```powershell
bcdedit /set hypervisorlaunchtype off
```

Run the above commands in an elevated PowerShell prompt. You'll have to restart Windows to apply the change.

- With Hyper-V you can use WSL2, but VM performance will be significantly degraded.
- Without Hyper-V you cannot use WSL2, but VM performance will be normal.

You can switch between launch types depending on your need at any time.

### Portmaster

Add a firewall rule:

```powershell
New-NetFirewallRule -Name "WSL" -DisplayName "WSL" -Direction Inbound -InterfaceAlias "vEthernet (WSL)" -Action Allow
```

After a reboot, the rule won't work. Run to reactivate:

```powershell
Get-NetFirewallInterfaceFilter -AssociatedNetFirewallRule (Get-NetFirewallRule -DisplayName 'WSL') | Set-NetFirewallInterfaceFilter -InterfaceAlias 'vEthernet (WSL)'
```

You can automate the above command using a task.

[Source: reddit.com - r/safing u/csdvrx](https://www.reddit.com/r/safing/comments/ryioj7/portmaster_breaks_wsl2_in_windows_11_a_guide_to/)
[Source: github.com - microsoft/WSL Issue #4139](https://github.com/microsoft/WSL/issues/4139#issuecomment-778428577)

## Miscellaneous

### wslutilities

- [GitHub](https://github.com/wslutilities/wslu#readme)
- [Website](https://wslutiliti.es/wslu/)
- [Installation](https://wslutiliti.es/wslu/install.html)

#### Add desktop shortcuts

```bash
find /usr/share/icons -iname "*nautilus*"
wslusc -n "Files" -i /usr/share/icons/Yaru/256x256@2x/apps/org.gnome.Nautilus.png nautilus
```

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

#### Automatically

`wsl-startup.vbs`

Change `<Distro>` to the distro name you are using. Use `wsl -l` to find out the name.

```vbs
set ws=wscript.CreateObject("wscript.shell")
ws.run "wsl -d <Distro>", 0
```

> [Source](https://askubuntu.com/a/1452424)

### Mount ext4

List drives in PowerShell:
```powershell
Get-CimInstance -query "SELECT * from Win32_DiskDrive"
```

Mount a partition in WSL:
```powershell
wsl --mount \\.\PHYSICALDRIVE0 --type ext4 --partition 2 --name myDisk
```

This should mount it under: `/mnt/wsl/myDisk`

To unmount it:
```powershell
wsl --unmount \\.\PHYSICALDRIVE0
```

**However, there are some limitations.**

In general:
- Only entire disks can be attached to WSL 2, so the disk should be detached from Windows. (The boot device cannot be attached to WSL 2)

More specifically, when mounting a partition using `wsl --mount`:
- The disk needs to be either MBR (Master Boot Record) or GPT (GUID Partition Table).
- Only filesystems that are natively supported in the kernel can be mounted. Installed filesystem drivers (`ntfs-3g` for example) won't work.

If you need to attach LVM disks, or filesystems that aren't directly supported by the Kernel, you need to attach the disk via `--bare`.

> [Source: hanselman.com](https://www.hanselman.com/blog/wsl2-can-now-mount-linux-ext4-disks-directly)  
> [Source: learn.microsoft.com](https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk)