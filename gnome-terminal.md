---
title: GNOME Terminal
category: Linux
---

<img src="https://upload.wikimedia.org/wikipedia/commons/d/da/GNOME_Terminal_icon_2019.svg" width="96">

# GNOME Terminal

## Customization

### Themes

- https://gogh-co.github.io/Gogh/
- `bash -c "$(wget -qO- https://git.io/vQgMr)"`
- I like `( 165 ) Panda` most

### Add padding
Add the following code to `~/.config/gtk-3.0/gtk.css`:
```css
VteTerminal,
TerminalScreen,
vte-terminal {
    padding: 10px 10px 10px 10px;
    -VteTerminal-inner-border: 10px 10px 10px 10px;
}
```
