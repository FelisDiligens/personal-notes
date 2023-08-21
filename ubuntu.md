---
title: Ubuntu
category: Linux
---

<img src="assets/ubuntu.png" style="height: 96px;">

## Settings

### Ubuntu dock settings

Ubuntu's dock is a fork of Dash to Dock, but it does not expose all the settings like the original. However, you can still set them using `gsettings`:

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize-or-previews'
gsettings set org.gnome.shell.extensions.dash-to-dock scroll-action 'cycle-windows'
```

## Package management
Some interesting projects:

- [apt-select](https://github.com/jblakeman/apt-select) - Find a fast, up-to-date Ubuntu Archive Mirror.
- [Nala](https://gitlab.com/volian/nala) is a front-end for libapt-pkg.
- [Pacstall](https://pacstall.dev/) - The AUR Ubuntu never had

## Troubleshooting

### Install Microsoft Fonts

> **warning**  
> These are non-free fonts. The license might prevent you from installing it in your organization.

The easiest way to install Microsoft Fonts is to simply copy them from a Windows installation. This of course only works if you dual boot with Windows or have a Windows machine available.

```bash
sudo apt install fontforge
windows_mount_point="/media/${USER}/Windows" # Corresponds to C:\ drive, replace with your path! Make sure to mount it beforehand
msfonts_install_folder="$HOME/.fonts/msfonts"
# msfonts_install_folder="/usr/share/fonts/truetype/msfonts"
mkdir -p $msfonts_install_folder
# Copy all ttf fonts:
cp $windows_mount_point/Windows/Fonts/*.ttf $msfonts_install_folder
# Extract ttf fonts from font collections (ttc):
ttc_temp_folder="$(xdg-user-dir DOWNLOAD)/ttc" # I use the Downloads folder as a temp folder, feel free to change.
mkdir -p "$ttc_temp_folder"
cp $windows_mount_point/Windows/Fonts/*.ttc "$ttc_temp_folder"
cd "$ttc_temp_folder"
fontforge -lang=ff -c 'Open("cambria.ttc(Cambria)"); Generate("cambria.ttf"); Close(); Open("cambria.ttc(Cambria Math)"); Generate("cambriamath.ttf"); Close();'
# add more fontforge commands here, if you need the other fonts...
# Copy extracted fonts:
cp *.ttf $msfonts_install_folder
# Regenerate cache:
fc-cache $msfonts_install_folder
```

An alternative to fontforge would be to use a service such as https://transfonter.org/

If you don't have a Windows installation available, read this: https://needforbits.wordpress.com/2017/07/19/install-microsoft-windows-fonts-on-ubuntu-the-ultimate-guide/

### Remove "Ubuntu Pro" messages

```bash
sudo pro config set apt_news=false
```