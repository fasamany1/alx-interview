# 0x06. Star Wars API

## Requirements

#### General

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be intrepreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/node`
* Mandatory `README.md` file
* Code should be `semistandard` compliant. [Rules of Standard](https://www.standardjs.com/rules.html) + [semicolons on top](https://www.github.com/standard/semistandard). Also as reference: [AirBnB style](https://www.github.com/airbnb/javascript)
* All files must be executable
* The length of the file will be tested using `wc`
* You are not allowed to use `var`.

## More Info

#### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

<a href="https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw">Documentation</a>

```$ sudo npm install semistandard --global```

#### Install `request` module and use it

<a href="https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw">Documentation</a>

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
## Tasks

**0. Star Wars Characters**
mandatory

Write a script that prints all characters of a Star Wars movie:

* The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name per line **in the same order as the “characters” list in the** `/films/` **endpoint**
* You must use the <a href="https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg">Star wars API</a>
* You must use the `request` module
