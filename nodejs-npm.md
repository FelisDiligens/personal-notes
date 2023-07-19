---
title: Node.js / NPM
category: Development tools
---

![](assets/nodejs-npm.png)

# Node.js / NPM

## Troubleshooting

### `Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules'`

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo "export PATH=~/.npm-global/bin:\$PATH" >> ~/.bashrc
```
> Source: https://stackoverflow.com/a/55274930

### Stuck on "sill idealTree buildDeps"

Sometimes, there are issues due to IPv6. One can force the use of IPv4:

```bash
alias npm="node --dns-result-order=ipv4first $(which npm)"
```

> https://stackoverflow.com/a/74493718
> https://github.com/npm/cli/issues/4163
