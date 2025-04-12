import pandas as pd
# a = pd.read_csv("data/malls_summary.csv")
# b = pd.read_csv("data/coord.csv")

# merged_df = pd.merge(a, b, on='Mall', how='left')
# merged_df.to_csv("data/merged_output.csv", index=False)


a = pd.read_csv("data/merged_output.csv")
a['Review'] = a['Review'] + ',' +a['MRT_Review']
a.drop(axis=1, columns='MRT_Review', inplace=True)
a.to_csv("data/merged_output.csv", index=False)
