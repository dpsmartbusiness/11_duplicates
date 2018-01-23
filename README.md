# Anti-Duplicator

Programm searches duplicates in catalog by path to. Find all files in current directory and shows dupplicates (name, size, path) in console.

# Quickstart

Program takes one input argument is directory_path.

Example of script launch on Windows, Python 3.5:

```bash

$ python duplicates.py <path to directory>

```

The results of the programm (for example, took random directory from my computer):

```python

	File name: bars.py // Size: 2071 bytes // Number of duplicates: 2
        Paths:
        C:\devman\pythondocs\bars.py
        C:\devman\pythondocs\try\bars.py

        File name: test.txt // Size: 3 bytes // Number of duplicates: 2
        Paths:
        C:\devman\pythondocs\test.txt
        C:\devman\pythondocs\try\try again\test.txt

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
