<img alt="powershell.svg" src="assets/powershell.svg" width="96">

# PowerShell

## Configuration

### Profile
Type `code $PROFILE` in PowerShell to edit the profile script.

### Start without "logo" text
Use `-NoLogo` parameter to start PowerShell without the startup text.

## Modules

### Install latest PSReadline

See [PSReadLine#installation](https://github.com/PowerShell/PSReadLine#installation)

````powershell
Install-Module -Name PowerShellGet -Force
Install-Module PSReadLine -AllowPrerelease -Force
```