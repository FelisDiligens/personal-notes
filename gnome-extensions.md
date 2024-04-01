---
title: GNOME Extensions
category: Linux
---

<img src="assets/Gnomelogo-white.svg" width="160">

# Extensions

## Installation

GNOME extensions are installed into
- system-wide: `/usr/share/gnome-shell/extensions/`
- for the user only: `~/.local/share/gnome-shell/extensions/`

### Commands
- `gnome-extensions install <archive.[zip|tar|...]>`
- `gnome-extensions enable <extension-id>`
- `gnome-extensions help [<command>]`

### Enable/Disable version validation
```bash
gsettings set org.gnome.shell disable-extension-version-validation "true"
```

```bash
gsettings set org.gnome.shell disable-extension-version-validation "false"
```

### GUI

Installation on Ubuntu:
```bash
sudo apt install gnome-tweaks gnome-shell-extensions
flatpak install org.gnome.Extensions com.mattjakeman.ExtensionManager
```

## Favorites

|   | Extension                                                                                                                                                | Links                                                                                                                       | GNOME 46 | Description                                                                                                                                                |
|---|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⭐ | [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/)                                                                                 | [GitHub](https://github.com/micheleg/dash-to-dock/)                                                                         | 🚧 (Git) |                                                                                                                                                            |
|   | [Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/)                                                                              | [GitHub](https://github.com/home-sweet-gnome/dash-to-panel#readme)                                                          |          |                                                                                                                                                            |
|   | [ArcMenu](https://extensions.gnome.org/extension/3628/arcmenu/)                                                                                          | [Gitlab](https://gitlab.com/arcmenu/ArcMenu)                                                                                |          |                                                                                                                                                            |
|   | [Desktop Icons NG (DING)](https://extensions.gnome.org/extension/2087/desktop-icons-ng-ding/)                                                            | [Gitlab](https://gitlab.com/rastersoft/desktop-icons-ng)                                                                    | ✅        |                                                                                                                                                            |
| ⭐ | [AppIndicator and KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/)<br>(also known as Ubuntu AppIndicators) | [GitHub](https://github.com/ubuntu/gnome-shell-extension-appindicator)                                                      | 🚧 (Git) |                                                                                                                                                            |
| ⭐ | [Coverflow Alt-Tab by dsheeler](https://extensions.gnome.org/extension/97/coverflow-alt-tab/)                                                            | [GitHub](https://github.com/dmo60/CoverflowAltTab)                                                                          | ✅        |                                                                                                                                                            |
|   | [Bing Wallpaper](https://extensions.gnome.org/extension/1262/bing-wallpaper-changer/)                                                                    | [GitHub](https://github.com/neffo/bing-wallpaper-gnome-extension)                                                           |          | Syncs your desktop & lock screen wallpaper to Microsoft Bing's Image of the Day                                                                            |
| ⭐ | [Clipboard Indicator](https://extensions.gnome.org/extension/779/clipboard-indicator/)                                                                   | [GitHub](https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator)                                              | ✅        | Adds a clipboard indicator to the top panel, and caches clipboard history.                                                                                 |
|   | [Pano - Next-gen Clipboard Manager](https://extensions.gnome.org/extension/5278/pano/)                                                                   | [GitHub](https://github.com/oae/gnome-shell-pano)                                                                           | 🚧 (Git) | Next-gen Clipboard Manager for Gnome Shell                                                                                                                 |
| ⭐ | [OpenWeather Refined](https://extensions.gnome.org/extension/6655/openweather/)                                                                          | [GitHub](https://github.com/penguin-teal/gnome-openweather)                                                                 | ✅        | A GNOME Shell extension to show the weather of any location on Earth. This is a fork of Kenneth Topp's fork of the OpenWeather extension.                  |
| ⭐ | [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)                                                                                         | [GitHub](https://github.com/eonpatapon/gnome-shell-extension-caffeine)                                                      | ✅        | Disable the screensaver and auto suspend                                                                                                                   |
| ⭐ | [Grand Theft Focus](https://extensions.gnome.org/extension/5410/grand-theft-focus/)                                                                      | [GitHub](https://github.com/zalckos/GrandTheftFocus)                                                                        | ✅        | Removes the 'Window is ready' notification and puts the window into focus.                                                                                 |
| ⭐ | [GSConnect](https://extensions.gnome.org/extension/1319/gsconnect/)                                                                                      | [GitHub](https://github.com/GSConnect/gnome-shell-extension-gsconnect/wiki)                                                 | 🚧       | Complete implementation of KDE Connect                                                                                                                     |
| ⭐ | [Alphabetical App Grid](https://extensions.gnome.org/extension/4269/alphabetical-app-grid/)                                                              | [GitHub](https://github.com/stuarthayhurst/alphabetical-grid-extension)                                                     | ✅        |                                                                                                                                                            |
| ⭐ | [Favourites in AppGrid](https://extensions.gnome.org/extension/4485/favourites-in-appgrid/)                                                              | [Gitlab](https://gitlab.gnome.org/harshadgavali/favourites-in-appgrid/)                                                     | ☠️       |                                                                                                                                                            |
| ⭐ | [Overview Background](https://extensions.gnome.org/extension/5856/overview-background/)                                                                  | [GitHub](https://github.com/orbitcorrecton/overview-background)                                                             | ☠️       |                                                                                                                                                            |
| ⭐ | [Gnome 4x UI Improvements](https://extensions.gnome.org/extension/4158/gnome-40-ui-improvements/)                                                        | [GitHub](https://github.com/axxapy/gnome-ui-tune)                                                                           | ✅        |                                                                                                                                                            |
|   | [Search Light](https://extensions.gnome.org/extension/5489/search-light/)                                                                                | [GitHub](https://github.com/icedman/search-light)                                                                           |          | Take the apps search out of overview                                                                                                                       |
| ⭐ | [Tiling Assistant](https://extensions.gnome.org/extension/3733/tiling-assistant/)                                                                        | [GitHub](https://github.com/Leleat/Tiling-Assistant)                                                                        | ✅        |                                                                                                                                                            |
|   | [Custom Accent Colors](https://extensions.gnome.org/extension/5547/custom-accent-colors/)                                                                | [GitHub](https://github.com/dimitriskp22/custom-accent-colors)                                                              | ✅        |                                                                                                                                                            |
| ⭐ | [Rounded Window Corners](https://extensions.gnome.org/extension/5237/rounded-window-corners/)                                                            | [GitHub](https://github.com/yilozt/rounded-window-corners)                                                                  | ?        |                                                                                                                                                            |
| ⭐ | [App Hider](https://extensions.gnome.org/extension/5895/app-hider/)                                                                                      | [GitHub](https://github.com/LynithDev/gnome-app-hider)                                                                      | ✅        |                                                                                                                                                            |
