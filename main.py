import pandas as pd
import os
import sys

def main():
    # Part 1
    file_path = construct_file_path("people.csv")
    df = pd.read_csv(file_path)
    print(df.head(5))
    df.to_csv("people_ismail.csv", index=False)

    # Part 2
    file_path = construct_file_path("people_no_header.csv")
    header = ['name', 'age', 'sex', 'height', 'weight', 'bmi', 'sibling_count', 'birth_order', 'years_played_sports']
    df = pd.read_csv(file_path, header=None, names=header)
    print(df.head(5))
    df.to_csv("people_header_added_ismail.csv", index=False)

    # Part 3
    # Read in the file as is, then replace the header with correct column names
    clean_header = ['name', 'age', 'sex', 'height', 'weight', 'bmi', 'sibling_count', 'birth_order', 'years_played_sports']
    file_path = construct_file_path("people_dirty_header.csv")
    df = pd.read_csv(file_path)
    df.columns = clean_header
    df.to_csv("people_clean_header_ismail.csv", index=False)


# Use os.path.join to construct the file path that is compatible with all operating systems
def construct_file_path(filename):
    file_path = os.path.join('data', filename)
    return file_path

if __name__ == "__main__":
    main()

# Gotchas
# 1. The file path is relative to the script's location, not the current working directory. The student
# may not know to use os.path.dirname(os.path.abspath(__file__)) to get the script's directory.
# 2. The student may not know how to use os.path.join to create a file path that works on all operating systems.
# 3. The student may not realize to convert to NAN and then set na_rep to NULL when writing the CSV file.
# 4. The student may not know how to use a dictionary to do replacements for NAN values.
