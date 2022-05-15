import seaborn as sns 
import matplotlib.pyplot as plt
from data_cleaning import *

# after 1990
met_after_1990 = correct_lat_long_df[correct_lat_long_df['year'] > 1990]

def after_1990_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_after_1990)
    plt.show()

def horizontal_after_1990_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(y='year', data=met_after_1990)
    plt.show()

def after_1990_fall_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_after_1990, hue='fall')
    plt.show()

def after_1990_nametype_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_after_1990, hue='nametype')
    plt.show()

# 1961 to 1990
met_1961_to_1990 = correct_lat_long_df[(correct_lat_long_df['year'] > 1960) & (correct_lat_long_df['year'] < 1991)]
def between_1961_1990_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1961_to_1990)
    plt.show()

def between_1961_1990_fall_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1961_to_1990, hue='fall')
    plt.show()

def between_1961_1990_nametype_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1961_to_1990, hue='nametype')
    plt.show()

# 1921 to 1960

met_1921_to_1960 = correct_lat_long_df[(correct_lat_long_df['year'] > 1920) & (correct_lat_long_df['year'] < 1961)]

def between_1921_1960_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1921_to_1960)
    plt.show()

def between_1921_1960_fall_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1921_to_1960, hue='fall')
    plt.show()

def between_1921_1960_nametype_split_countplot():
    plt.figure(figsize=(20, 20))
    sns.countplot(x='year', data=met_1961_to_1990, hue='nametype')
    plt.show()

# before 1921
met_before_1921 = correct_lat_long_df[correct_lat_long_df['year'] < 1921]

def horizontal_before_1921_countplot():
    plt.figure(figsize=(20, 40))
    sns.countplot(y='year', data=met_before_1921)
    plt.show()