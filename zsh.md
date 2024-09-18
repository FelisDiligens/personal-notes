---
title: ZSH
category: Linux
---

![](./assets/zsh.png)

# zsh - the Z shell

## antidote

https://github.com/mattmc3/antidote  
https://getantidote.github.io/

**Installation:**
```bash
git clone --depth=1 https://github.com/mattmc3/antidote.git ${ZDOTDIR:-$HOME}/.antidote
```

**Add to `.zshrc`**
```bash
# Antidote
source ${ZDOTDIR:-$HOME}/.antidote/antidote.zsh
antidote load ${ZDOTDIR:-$HOME}/.zsh_plugins.txt
```

**Managing plugins:**
`.zsh_plugins.txt`

```bash
# Oh My Zsh plugins
getantidote/use-omz
ohmyzsh/ohmyzsh path:lib
ohmyzsh/ohmyzsh path:plugins/extract
ohmyzsh/ohmyzsh path:plugins/command-not-found

# add fish-like features
# zsh-users/zsh-syntax-highlighting
zdharma-continuum/fast-syntax-highlighting
zsh-users/zsh-autosuggestions
zsh-users/zsh-history-substring-search

# Powerlevel10k
romkatv/powerlevel10k
```

All oh-my-zsh plugins can be found here: https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins

## Powerlevel10k colors

### All available colors

Colors are specified using numbers from 0 to 255. Colors from 0 to 15 look differently in different terminals. Many terminals also support customization of these colors through color palettes (a.k.a. color schemes, or themes). Colors from 16 to 255 always look the same.

```bash
for i in {0..255}; do print -Pn "%K{$i} %k%F{$i}${(l:3::0:)i}%f " ${${(M)$((i%6)):#3}:+$'\n'}; done
```

![](./assets/zsh-colors.png)

### Change colors

Open `~/.p10k.zsh`, search for "color", "foreground" and "background" and change values of appropriate parameters.

Example:
```bash
# Ubuntu-like colors:
typeset -g POWERLEVEL9K_DIR_BACKGROUND=166
typeset -g POWERLEVEL9K_OS_ICON_FOREGROUND=202
# Manjaro-like colors:
typeset -g POWERLEVEL9K_DIR_BACKGROUND=030
typeset -g POWERLEVEL9K_OS_ICON_FOREGROUND=030
# Default
typeset -g POWERLEVEL9K_DIR_BACKGROUND=4
typeset -g POWERLEVEL9K_OS_ICON_FOREGROUND=232
```
