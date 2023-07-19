---
title: Git
category: Development tools
---

# Git

## Push newly created repo
1. First, create a new remote repo on GitHub: https://help.github.com/en/articles/creating-a-new-repository  
2. Then push to remote repo:

```
git init
git branch -m master main
git add -A
git commit -m "Initial commit"
git remote add origin https://github.com/<user>/<project>.git
git push -u origin main
```

## Drop commits

- Remove last commit and any changes: `git reset --hard HEAD^`
  - The last two commits: `git reset --hard HEAD~2`
- Remove last commit but keep changes staged: `git reset --soft HEAD^`

## Troubleshooting
### Repo already created?
Try: `git pull origin main --allow-unrelated-histories`

### "Push declined due to email privacy restrictions"
```bash
git config --global user.email "123456789+username@users.noreply.github.com"
git rebase -i
git commit --amend --reset-author
git rebase --continue
git push
```
> Source: https://web.archive.org/web/20200416175035/https://github.community/t5/How-to-use-Git-and-GitHub/push-declined-due-to-email-privacy-restrictions/td-p/7660

### Under Linux: How to store password?
```bash
git config --global credential.helper store
```

### "Detected dubious ownership in repository"

Here are a few possible solutions to this issue:

#### 1. Update ownership/permissions

Under Linux:
```
chown -R <username> .git
chmod -R 666 .git
```

Under Windows:
```
takeown /f <foldername> /r /d y
```
(Run as admin; might take a while; ==in German: type `j` instead of `y`==)


#### 2. Mount NTFS partition properly! (fstab)

Add `uid=1000,gid=1000,umask=0000` to the NTFS mount options in `/etc/fstab`.

Example:
```
/dev/disk/by-id/wwn-0x50014ee2118aa10d-part1 /mnt/Elements auto nosuid,nodev,nofail,exec,noauto,x-gvfs-show,x-gvfs-name=Elements,windows_names,uid=1000,gid=1000,umask=0000 0 0
```

See: https://askubuntu.com/a/208349

#### 3. Disable warning

This is not recommended!

```
git config --global --add safe.directory '*'
```

or add to `~/.gitconfig`:

```
[safe]
	directory = *
```

https://stackoverflow.com/a/73100228

### `LF` under Windows

`git config --global core.autocrlf false`

### See also

- [Move the most recent commit(s) to a new branch with Git - Stack Overflow](https://stackoverflow.com/questions/1628563/move-the-most-recent-commits-to-a-new-branch-with-git)
- [Git HowTo: revert a commit already pushed to a remote repository](https://gist.github.com/gunjanpatel/18f9e4d1eb609597c50c2118e416e6a6)