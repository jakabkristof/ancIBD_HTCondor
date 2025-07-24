#!/usr/bin/python3


#arguments: iid_pair in_foloder out_folder

print("helloka")


import sys as sys
#import os
#import pandas as pd

from ancIBD.run import hapBLOCK_chrom


#for i in range(len(sys.argv)):
#    print(i, sys.argv[i])

#print(list(sys.argv))

iid_one = sys.argv[1]
print("id1:", iid_one)

iid_two = sys.argv[2]
print("id2:", iid_two)

#iid_pair = sys.argv[1].split(' ')
iid_pair = [iid_one, iid_two]
print("pair:", iid_pair)
#MOT2S185FQM MOT2S185FQM

in_folder = sys.argv[3]
print("ind:", in_folder)
#/home/kjakab/HTCondor/wgiahs_htcondor/ch
#in_folder = "/home/agi/WGIAHS_AGI_CA_MERGED_HDF5_20250623/ch"
#"/home/agi/WGIAHS_AGI_CA_MERGED_HDF5_20250623/ch"

out_folder = sys.argv[4]
print("outd:", out_folder)
#/home/kjakab/HTCondor/wgiahs_htcondor/TEST_OUT/
#out_folder = "/home/agi/WGIAHS_AGI_CA_MERGED_HDF5_20250623/CLI_OUT/"
#"/home/agi/WGIAHS_AGI_CA_MERGED_HDF5_20250623/CLI_OUT/"

#print(in_folder, out_folder)

for chrom in range(1,23):
    hapBLOCK_chrom(folder_in=in_folder, iids=iid_pair,
                   ch=chrom, folder_out=out_folder,
                   output=False, prefix_out='_'.join(iid_pair), logfile=False, l_model='h5', e_model='haploid_gl2',
                   h_model='FiveStateScaled', t_model='standard', ibd_in=1, ibd_out=10, ibd_jump=400,
                   min_cm=6, cutoff_post=0.99, max_gap=0.0075)

