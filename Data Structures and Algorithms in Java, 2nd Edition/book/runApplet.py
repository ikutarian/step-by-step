#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__=="__main__":
    html_file = ''
    for filename in os.listdir(os.getcwd()):
        if (len(filename) >= 4) and (filename[-4:] == 'html'):
            html_file = filename            
            break
            
    if html_file != '':
        os.system('appletviewer ' + html_file)