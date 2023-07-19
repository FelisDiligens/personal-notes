# Common paths
Directories have a trailing `/`, files don't.

## User
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
- ESP mount point:
    - `/boot/efi`
- GRUB:
    - `/etc/default/grub`
    - `/boot/efi/EFI/[distro name]/grubx64.efi` (and `shimx64.efi` for Secure Boot)
- Kernels and modules:
    - `/usr/lib/kernel/` or `/lib/kernel/`
    - `/usr/lib/modules/` or `/lib/modules/`
    - `/boot/vmlinuz-*`

## systemd
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

## Fedora
- Copr repos: `/etc/yum.repos.d/_copr*`
- dnf config: `/etc/dnf/dnf.conf`
