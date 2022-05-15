import seaborn as sns
from data_cleaning import *
import matplotlib.pyplot as plt

def between_1970_2000_annotated_sns_histogram():
    plt.figure(figsize=(10,20))
    my_hist = sns.distplot(correct_lat_long_df.loc[(correct_lat_long_df['year'] >= 1970) & (correct_lat_long_df['year'] < 2001), 'year'], bins=6, kde=False)
    for i in my_hist.patches:
        my_hist.annotate(str(int(i.get_height())), xy=(i.get_x() + i.get_width() / 2, i.get_height()), ha='center', va='bottom')


def between_1970_2000_annotated_plt_histogram():
    plt.figure(figsize=(20, 20))
    my_new = plt.hist(correct_lat_long_df.loc[(correct_lat_long_df['year'] >= 1970) & (correct_lat_long_df['year'] < 2001), 'year'], bins=6)
    for i in my_new[2]:
        plt.annotate(str(int(i.get_height())), xy=(i.get_x() + i.get_width() / 2, i.get_height()), ha='center', va='bottom')
    plt.grid()

# count of each type of meterorite in decreasing order
met_class_counts = correct_lat_long_df['recclass'].value_counts()

# histograms for top 10 most frequent meteroite types
def top_10_met_type_histograms():
    for c in met_class_counts[:10].index:
        plt.figure(figsize=(20, 5))
        plt.title(c) # The 'title()' function adds a title to the graph. Here, we are providing the meteorite class as a title.
        plt.hist(correct_lat_long_df.loc[(correct_lat_long_df['recclass'] == c) & (correct_lat_long_df['year'] > 1900), 'year'], bins=50)
        plt.grid()
        plt.show()

top_10_met_type_histograms()