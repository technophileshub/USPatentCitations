import numpy as np
import pandas as pd
from download import download_patent_file
from patent_parser import read_patent

def main():
    df_filelist = pd.read_csv("patent_weekly_list.csv", header=0)
    download_patent_file(df_filelist.iloc[[40]])
    read_patent(df_filelist.iloc[[40]])


if __name__ == '__main__':
    exit(main())
