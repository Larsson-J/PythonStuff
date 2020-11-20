import os
import glob
import pandas as pd

# directory
os.chdir("C:\Users\Username\Projects\data.csv")

# choose csv as extension
extension = 'csv'

# format the csv
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combining the csv files
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# saving the new csv file
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')