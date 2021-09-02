from parse import load_dataframes
import pandas as pd
import shutil
import numpy as np
import scipy
from scipy import sparse

def users_reviews_csr_matrix(dataframes):
    users = dataframes['users']
    reviews = dataframes['reviews']
    merge = pd.merge(
        users, reviews, left_on='id', right_on='user'
    )[:1000]

    pivot_table = merge.pivot_table(index='user', columns='store', values='score', aggfunc=np.mean, fill_value=0)
    csr_matrix = scipy.sparse.csr_matrix(pivot_table)
    return csr_matrix

def main():
    df = load_dataframes()
    # users_reviews_csr_matrix(df)

if __name__ == "__main__":
    main()
