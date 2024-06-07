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
    "security.allowedUNCHosts": ["wsl.localhost"],
    "window.titleBarStyle": "custom",
    "window.menuBarVisibility": "compact",
    "window.commandCenter": true,
    "editor.rulers": [80],
    "editor.fontLigatures": true,
    "editor.fontFamily": "Hack, Hack Nerd Font, Hack NF, Source Code Pro, Fira Code, Consolas, monospace",
    "terminal.integrated.fontFamily": "Hack Nerd Font, Hack NF, FiraCode Nerd Font, FiraCode NF, Hack, FiraCode, Consolas, monospace",
    "terminal.integrated.cursorBlinking": true,
    "terminal.integrated.fontSize": 16,
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "terminal.integrated.profiles.windows": {
        "Cygwin Bash": {
            "path": "C:\\cygwin64\\bin\\bash.exe",
            "args": ["/bin/xhere", "/bin/bash"],
            "icon": "terminal-bash"
        }
    },
    "terminal.integrated.defaultProfile.windows": "Cygwin Bash",
    "terminal.integrated.defaultProfile.linux": "zsh",
    "terminal.integrated.shellIntegration.enabled": false,
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "javascript.preferences.importModuleSpecifier": "relative",
    "typescript.preferences.importModuleSpecifier": "relative",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": "always",
    },
    "[markdown]": {
        "editor.wordWrap": "off"
    },
    "markdown.styles": [
        ".obsidian/snippets/vscode.css"
    ],
    "markdownExtended.pdfDisplayHeaderFooter": false,
    "files.associations": {
        "*.pacscript": "shellscript"
    },
    "explorer.confirmDelete": false,
    "git.autofetch": true,
    "git.openRepositoryInParentFolders": "never",
    "rust-analyzer.server.path": "~/.cargo/bin/rust-analyzer",
    "files.eol": "\n",
}

```

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

| Extension                                                                                                                     | Categories                                        | Unique Identifier                            |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------- |
| [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)                              | Other                                             | `jebbs.markdown-extended`                    |
| [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) | Other                                             | `bierner.markdown-preview-github-styles`     |
| [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer)                                  | Programming Languages, Formatters                 | `rust-lang.rust-analyzer`                    |
| [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)                              | Programming Languages, Linters, Formatters, Other | `tamasfe.even-better-toml`                   |
| [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)                                        | Formatter                                         | `esbenp.prettier-vscode`                     |
| [vscode-styled-components](https://marketplace.visualstudio.com/items?itemName=styled-components.vscode-styled-components)    | Programming Languages                             | `styled-components.vscode-styled-components` |
| [css2react](https://marketplace.visualstudio.com/items?itemName=gottfired.css2react)                                          | Other                                             | `gottfired.css2react`                        |
| [ES7+ React/Redux/React-Native snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) | Snippets                                          | `dsznajder.es7-react-js-snippets`            |
| [AutoHotkey Plus Plus](https://marketplace.visualstudio.com/items?itemName=mark-wiemer.vscode-autohotkey-plus-plus)           | Programming Languages, Snippets                   | `mark-wiemer.vscode-autohotkey-plus-plus`    |
