---
title: "`tar` command line utility"
category: Development tools
---

<img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Tar_gz_archive_icon.svg" width="96">

# `tar` command line utility

This is a quick reference, for more information:
```bash
man tar
```

## Usage

### Explanation of parameters

- `-c`: Compress/Create
- `-x`: Extract
- `-u`: Update (add files to existing archive)
- `-v`: Verbose output
- `-f`: Read/write file instead of stdin/stdout (archive)

#### Compression

| Parameter       | Format                   |
|-----------------|--------------------------|
| `-z`, `--gzip`  | Use `.gzip` compression  |
| `-j`, `--bzip2` | Use `.bzip2` compression |
| `-J`, `--xz`    | Use `.xz` compression    |
| `--lzip`        | Use lzip compression     |
| `--lzma`        | Use lzma compression     |
| `--zstd`        | Use zstd compression     |

### Examples

- Extract (auto-detect): `tar -xavf {archive}.tar.gz`

#### gzip (`.tar.gz` or `.tgz`):

- Compress: `tar -czvf {archive}.tar.gz {files...}`
- Extract: `tar -xzvf {archive}.tar.gz`

#### bzip2 (`.tar.bz2`)

- Compress: `tar -cjvf {archive}.tar.bz2 {files...}`
- Extract: `tar -xjvf {archive}.tar.bz2`