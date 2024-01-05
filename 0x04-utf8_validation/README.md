# 0x04. UTF-8 Validation

## Resources

**Read or watch:**

* <a href="https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ">UTF-8</a>
* <a href="https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw">Characters, Symbols, and the Unicode Miracle</a>

## Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7.x)
All your files must be executable

## Tasks

#### UTF-8 Validation
 
Write a method that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: `def validUTF8(data)`
* Return: `True` if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
