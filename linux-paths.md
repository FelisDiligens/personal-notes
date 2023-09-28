---
title: Common paths
category: Linux
---

# Common paths under Linux
Directories have a trailing `/`, files don't.

## Basics
Here's an overview over the linux file system structure:

- ⚙️ `/etc/` - editable-text-configurations: contains system configuration files, such as the password file (`passwd`), network configuration files, and startup scripts
- 📦 `/bin/` - contains binaries (essential ones such as `ls`, `cp`, and `mv`)
- 🧰 `/sbin/` - contains system binaries that only root can/should execute
- 🛠️ `/opt/` - contains optional binaries and libraries
- 🧑‍💻 `/usr/` - contains various files (including binaries) that users share
	- 📦 `/usr/bin/` - often symlinked to `/bin/`, but can also be used separately for non-essential binaries (such as text editors, web browsers, and office suites) installed through the package manager depending on the Linux distro
	- 📦 `/usr/local/bin/` - contains binaries a user compiled/installed manually (i.e. not through the package manager)
- 📜 `/var/` - variable data files: contains logs, cache, memory dumps, mail spools, and **var**ious other files that may change over time
- 👢 `/boot/` - contains the kernel, initrd (initial ram disk), and the boot loader
- 🖱️ `/dev/` - contains device files, which represent physical devices such as hard drives, CD-ROM drives, and network interfaces
- 💻 `/proc/` - contains information about running processes (folders by PID)
- 📚 `/lib/` - contains libraries shared by applications (`*.so` files)
- 💽 `/media/` - contains mount points for removable media devices, such as CDs and USB drives (mounted automatically by the operating system)
- 💾 `/mnt/` - used for mounting file systems manually (by the user)
- 🗑️ `/tmp/` - contains temporary files
- 👑 `/root/` - home folder of the root user (UID: 0)
- 🏡 `/home/` - contains home folders of all regular users

## User
- Default home files (including `.bashrc`): `/etc/skel/`
- \*.desktop files:
	-  `/usr/share/applications/`
	-  `/usr/local/share/applications/` (system-wide)
	-  `~/.local/share/applications/` (user-specific)
	-  `/var/lib/snapd/desktop/applications/` (snap)
- Icons / Cursors:
	- `/usr/share/icons/`
	- `~/.icons/`
- Fonts:
	- `/usr/share/fonts/`
	- `~/.fonts/`
- Themes:
	- `/usr/share/themes/`
	- `~/.themes/`
	- `~/.local/share/themes/`

## System
- Environment variables:
	- `/etc/environment`
- ESP mount point:
    - `/boot/efi`
- GRUB:
    - `/etc/default/grub`
    - `/boot/efi/EFI/[distro name]/grubx64.efi` (and `shimx64.efi` for Secure Boot)
- Kernels, modules, and DKMS:
    - `/usr/lib/kernel/` or `/lib/kernel/`
    - `/usr/lib/modules/` or `/lib/modules/`
		- `/lib/modules/**/updates/dkms/`
    - `/var/lib/dkms`
    - `/boot/vmlinuz-*`
- TLS Certificates (`*.crt`, `*.pem`):
	- `/etc/ssl/certs/*.pem`
	- `/usr/local/share/ca-certificates/*.crt`

## systemd
- Environment variables (per user):
	- `~/.config/environment.d/*.conf`
- Daemons:
    - `/etc/systemd/system/`
    - `/usr/lib/systemd/system/` or `/lib/systemd/system/`
- `~/.config/systemd/user/`

## VMs
- libvirt \*.qcow2 images:
    - `/var/lib/libvirt/images/`
 
## Docker
- Volumes: `/var/lib/docker/volumes/`

## Debian / Ubuntu
- Apt stuff:
	- `/usr/share/keyrings/`
	- `/etc/apt/sources.list.d/`
	- `/etc/apt/sources.list`
	- `/var/lib/dpkg/info/`

## Fedora
- Copr repos: `/etc/yum.repos.d/_copr*`
- dnf config: `/etc/dnf/dnf.conf`
