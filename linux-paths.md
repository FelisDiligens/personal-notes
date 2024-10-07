---
title: Common paths
category: Linux
---

# Common paths under Linux

Most Linux distributions use the [Filesystem Hierarchy Standard (FHS)](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) (although exceptions like NixOS exist).

!!! note Note
Directories have a trailing `/`, files don't.
!!!

## Basics
Here's an overview over the linux file system structure:

- ⚙️ `/etc/` - "Editable Text Configurations": contains host-specific system-wide configuration files, such as the password file (`passwd`), network configuration files, and startup scripts
- 📦 `/bin/` - contains binaries (essential ones such as `cat`, `ls`, `cp`, and `mv`)
- 🧰 `/sbin/` - contains system binaries that only root can/should execute
- 🛠️ `/opt/` - contains optional binaries and libraries
- 🧑‍💻 `/usr/` - contains various files (including binaries) that users share (secondary hierarchy for user data)
	- 📦 `/usr/bin/` - often symlinked to `/bin/`, but can also be used separately for non-essential binaries (such as text editors, web browsers, and office suites) installed through the package manager depending on the Linux distro
	- 📚 `/usr/lib/` - often symlinked to `/lib/`, but can also be used separately for libraries used for non-essential binaries (`/usr/bin`)
	- 📄 `/usr/src/` - source code (e.g., the kernel source code with its header files)
	- 🎨 `/usr/share/` - architecture-independent (shared) data (themes, icons, desktop files, app and desktop settings, etc.)
	- 🧭 `/usr/local/` - tertiary hierarchy for local data
		- 📦 `/usr/local/bin/` - contains binaries a user compiled/installed manually (i.e. not through the package manager)
- 📜 `/var/` - variable data files: contains logs, cache, memory dumps, mail spools, and **var**ious other files that may change over time
	- 👟 `/var/run/` - symlinked to `/run/`
- 👢 `/boot/` - contains the kernel, initrd (initramfs cpio archive), and the boot loader (often under `/boot/efi`)
- 🖱️ `/dev/` - contains device files, which represent physical devices such as hard drives, CD-ROM drives, and network interfaces. But also virtual devices (e.g. `/dev/null`, `/dev/random`)
- 💻 `/proc/` - contains information about running processes (folders by PID) and other system information ([procfs](https://en.wikipedia.org/wiki/Procfs) mount)
- 💻 `/sys/` - exports and allows modification of various kernel subsystems, hardware devices, and associated device drivers ([sysfs](https://en.wikipedia.org/wiki/Sysfs) mount)
- 📚 `/lib/` - contains libraries shared by applications (`*.o` and `*.so` files), especially for binaries from `/bin` and `/sbin`
- 💽 `/media/` - contains mount points for removable media devices, such as CDs and USB drives (mounted automatically by the operating system)
- 💾 `/mnt/` - used for mounting file systems manually (by the user)
- 👟 `/run/` - temporary file system mounted early during the boot process to store volatile runtime data for various services, e.g. systemd, udev ([tmpfs](https://en.wikipedia.org/wiki/Tmpfs) mount)
- 🗑️ `/tmp/` - contains temporary files
- 👑 `/root/` - home folder of the root user (UID: 0)
- 🏡 `/home/` - contains home folders of all regular users (including saved files, personal settings, etc.)

## Customizations
- Default home files (including `.bashrc`): `/etc/skel/`
- \*.desktop files:
	-  `/usr/share/applications/`
	-  `/usr/local/share/applications/` (system-wide)
	-  `~/.local/share/applications/` (user-specific)
	-  `/var/lib/snapd/desktop/applications/` (snap)
- Autostart:
	- `/etc/xdg/autostart/*.desktop`
	- `~/.config/autostart/*.desktop`
- Icons / Cursors:
	- `/usr/share/icons/`
	- `~/.icons/`
- Fonts:
	- `/usr/share/fonts/`
	- `/usr/local/share/fonts/`
	- `~/.fonts/`
- Themes:
	- `/usr/share/themes/`
	- `~/.themes/`
	- `~/.local/share/themes/`
- Wallpapers:
	- `/usr/share/wallpapers/`
	- `/usr/share/backgrounds/`
	- `/usr/share/themes/**/backgrounds/`
	- `~/.local/share/backgrounds`

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
	- `/usr/src/`
    - `/var/lib/dkms`
    - `/boot/vmlinuz-*`
- TLS Certificates (`*.crt`, `*.pem`):
	- `/etc/ssl/certs/*.pem`
	- `/usr/local/share/ca-certificates/*.crt`
- Sessions:
    - Wayland: `/usr/share/wayland-sessions/*.desktop`
	- X11: `/usr/share/xsessions/*.desktop`

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
