#!/usr/bin/python3

#arguments: iid_one iid_two in_folder out_folder
#MOT2S185FQM MOTS95W - chr3&chr16 one segment, chr19 two segments

import sys
import os

iid_one = sys.argv[1]

iid_two = sys.argv[2]

#

if(iid_one == iid_two):
    os._exit(0)

#

iid_pair = [iid_one, iid_two]

in_folder = sys.argv[3]
#"/mnt/18tbb/WGIAHS_AGI_CA_MERGED_HDF5_20250623/CH/ch"

out_folder = sys.argv[4]
#"/home/kjakab/HTCondor/wgiahs_htcondor/TEST_OUT_CLEANUP/"

prefix_out_iid_pair = '_'.join(iid_pair)

#

import pandas as pd

from ancIBD.run import hapBLOCK_chrom

#

ibd_segments_df = pd.DataFrame([], columns=["Start", "End", "StartM", "EndM", "length", "lengthM", "ch", "StartBP", "EndBP", "iid1", "iid2"])

chromosomes = range(1,23)

for chr in chromosomes:
    segments = hapBLOCK_chrom(folder_in=in_folder, iids=iid_pair,
                   ch=chr, folder_out='',
                   output=False, logfile=False, l_model="h5", e_model="haploid_gl2",
                   h_model="FiveStateScaled", t_model="standard", ibd_in=1, ibd_out=10, ibd_jump=400,
                   min_cm=6, cutoff_post=0.99, max_gap=0.0075)
    ibd_segments_df = pd.concat([ibd_segments_df, segments[0]])

#

if(len(ibd_segments_df) > 0):
    ibd_segments_df.iid1 = iid_one
    ibd_segments_df.iid2 = iid_two
    ibd_segments_df.drop("StartBP", axis=1, inplace=True)
    ibd_segments_df.drop("EndBP", axis=1, inplace=True)

else:
    os._exit(0)

#

import sqlite3

sqlite_connection = sqlite3.connect(out_folder+"/SEGMENTS_OUT.sqlite3", timeout=33.3)

cursor = sqlite_connection.cursor()


for row in range(len(ibd_segments_df)):
    data_to_insert = tuple(ibd_segments_df.iloc[row].to_list())
    data_query = f"INSERT INTO ibd_segment_output VALUES {data_to_insert}"
    cursor.execute(data_query)


sqlite_connection.commit()

cursor.close()
sqlite_connection.close()

