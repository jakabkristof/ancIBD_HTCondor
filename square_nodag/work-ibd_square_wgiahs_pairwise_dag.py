#!/usr/bin/python3

#arguments: iid_one iid_two in_folder out_folder
#MOT2S185FQM MOTS95W - chr3&chr16 one segment, chr19 two segments



import sys
import os

import pandas as pd

from ancIBD.run import hapBLOCK_chrom


iid_one = sys.argv[1]

iid_two_file = sys.argv[2]
#/home/kjakab/HTCondor/wgiahs_htcondor/square/MOT_square_iids.txt
iid_two_list = open(iid_two_file, 'r').read().split()

in_folder = sys.argv[3]
#"/mnt/18tbb/WGIAHS_AGI_CA_MERGED_HDF5_20250623/CH/ch"

out_folder = sys.argv[4]
#"/home/kjakab/HTCondor/wgiahs_htcondor/TEST_OUT_CLEANUP/"

chromosomes = range(1,23)


#


for iid_two in iid_two_list:

    if(iid_one == iid_two):
        os._exit(0)

    iid_pair = [iid_one, iid_two]

    prefix_out_iid_pair = '_'.join(iid_pair)

    for chr in chromosomes:
        hapBLOCK_chrom(folder_in=in_folder, iids=iid_pair,
                       ch=chr, folder_out=out_folder,
                       output=False, prefix_out=prefix_out_iid_pair, logfile=False, l_model='h5', e_model='haploid_gl2',
                       h_model='FiveStateScaled', t_model='standard', ibd_in=1, ibd_out=10, ibd_jump=400,
                       min_cm=6, cutoff_post=0.99, max_gap=0.0075)

    #os.mkdir(out_folder + '/SEGMENTS_OUT/') 

    for chr in chromosomes:
        input_file_path = out_folder + '/' + prefix_out_iid_pair + '/ch' + str(chr) + ".tsv"
        line_count = open(input_file_path, 'r').read().count('\n')
        if(line_count > 1):
            ibd_df = pd.read_csv(input_file_path, sep='\t')
            ibd_df.iid1 = iid_one
            ibd_df.iid2 = iid_two
            ibd_df.drop("StartBP", axis=1, inplace=True)
            ibd_df.drop("EndBP", axis=1, inplace=True)
            ibd_df.to_csv(out_folder+"/SEGMENTS_OUT.tsv", mode='a', index=False, header=False, sep='\t')
            #ibd_df.to_csv(out_folder+'/SEGMENTS_OUT/'+prefix_out_iid_pair+'_chr' + str(chr) + ".tsv", index=False, sep='\t')
        os.remove(input_file_path) 

    os.rmdir(out_folder + '/' + prefix_out_iid_pair)

