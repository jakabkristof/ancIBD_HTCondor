#!/usr/bin/python3

#arguments: iid_one iid_two in_folder out_folder
#MOT2S185FQM MOTS95W - chr3&chr16 one segment, chr19 two segments



import sys
import os
import pandas as pd

from ancIBD.run import hapBLOCK_chrom


for a in range(len(sys.argv)):
    print(a, sys.argv[a])

