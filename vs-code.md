---
title: Visual Studio Code
category: Development tools
---

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" width="96">

# Visual Studio Code

## settings.json

```json
{
	"security.workspace.trust.untrustedFiles": "open",
	"security.workspace.trust.banner": "never",
    "security.workspace.trust.enabled": false,
    "window.titleBarStyle": "custom",
    "window.menuBarVisibility": "compact",
    "window.commandCenter": true,
	"editor.fontLigatures": true,
    "editor.fontFamily": "Fira Code, Consolas, 'Courier New', monospace",
    "terminal.integrated.fontFamily": "FiraCode NF",
    "terminal.integrated.cursorBlinking": true,
    "terminal.integrated.fontSize": 16,
	"terminal.integrated.enableMultiLinePasteWarning": false,
    "terminal.integrated.profiles.windows": {
        "Cygwin Bash": {
            "path": "C:\\cygwin64\\bin\\bash.exe",
            "args": ["/bin/xhere", "/bin/bash"],
            "icon": "terminal-bash"
        },
        "Cygwin Fish": {
            "path": "C:\\cygwin64\\bin\\bash.exe",
            "args": ["/bin/xhere", "/bin/fish"],
            "icon": "star"
        }
    },
    "terminal.integrated.defaultProfile.windows": "Cygwin Fish",
    "javascript.preferences.importModuleSpecifier": "relative",
    "typescript.preferences.importModuleSpecifier": "relative",
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
	"[markdown]": {
        "editor.wordWrap": "on"
    },
    "markdown.styles": [
        ".obsidian/snippets/vscode.css"
    ],
    "prettier.tabWidth": 4,
}
```

### Nerd font

- `"terminal.integrated.fontFamily": "FiraCode NF"`
- Windows: `FiraCode NF`
- Linux: `FiraCode Nerd Font`


## Extensions

Extensions can be installed by entering `ext install <uid>` into the Command Palette.  
Or you can use the command line:  
> To make it easier to automate and configure VS Code, it is possible to list, install, and uninstall extensions from the command line. When identifying an extension, provide the full name of the form publisher.extension, for example donjayamanne.python.
> ```bash
> code --list-extensions
> code --install-extension jebbs.markdown-extended
> code --uninstall-extension jebbs.markdown-extended
> ```
> Source: [Documentation](https://code.visualstudio.com/docs/editor/extension-marketplace#_command-line-extension-management)

| Extension                                                                                                                     | Categories                       | Unique Identifier                            |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------|
| [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)                              | Other                            | `jebbs.markdown-extended`                    |
| [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)                         | Programming Languages, Formatter | `yzhang.markdown-all-in-one`                 |
| [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)                                        | Formatter                        | `esbenp.prettier-vscode`                     |
| [vscode-styled-components](https://marketplace.visualstudio.com/items?itemName=styled-components.vscode-styled-components)    | Programming Languages            | `styled-components.vscode-styled-components` |
| [css2react](https://marketplace.visualstudio.com/items?itemName=gottfired.css2react)                                          | Other                            | `gottfired.css2react`                        |
| [ES7+ React/Redux/React-Native snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) | Snippets                         | `dsznajder.es7-react-js-snippets`            |
| [AutoHotkey Plus Plus](https://marketplace.visualstudio.com/items?itemName=mark-wiemer.vscode-autohotkey-plus-plus)           | Programming Languages, Snippets  | `mark-wiemer.vscode-autohotkey-plus-plus`    |
