# Fonts

## Nerd fonts

![](https://www.nerdfonts.com/assets/img/nerd-fonts-logo.svg)

- https://www.nerdfonts.com/
- https://www.nerdfonts.com/cheat-sheet
- https://www.nerdfonts.com/font-downloads

```bash
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/FiraMono.zip
unzip FiraMono.zip -d ~/.fonts/FiraMono
rm -v FiraMono.zip
fc-cache
```

## MS Fonts

### Ubuntu
```bash
sudo apt install ttf-mscorefonts-installer -y  
sudo apt install fontforge cabextract -y  
wget https://gist.github.com/maxwelleite/10774746/raw/ttf-vista-fonts-installer.sh -q -O - | sudo bash
```

## Fix bad font rendering on Linux (e.g. MS Fonts like Calibri)
The solution is to disable embedded bitmaps in fonts.

Create `$HOME/.config/fontconfig/fonts.conf` and copy&paste this inside:
```xml
<!-- disable embedded bitmaps in fonts to fix Calibri, Cambria, etc. -->
<match target="font">
    <edit mode="assign" name="embeddedbitmap"><bool>false</bool></edit>
</match>
```