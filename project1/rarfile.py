#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rarfile

rf = rarfile.RarFile('myarchive.rar')
for f in rf.infolist():
    print f.filename, f.file_size
    if f.filename == 'README':
        print(rf.read(f))

with rarfile.RarFile('archive.rar') as rf:
    with rf.open('README') as f:
        for ln in f:
            print(ln.strip())


# Set to full path of unrar.exe if it is not in PATH
rarfile.UNRAR_TOOL = "unrar"

# Set to '\\' to be more compatible with old rarfile
rarfile.PATH_SEP = '/'