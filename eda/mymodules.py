import base64
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

def load_datasets():
    train_df = pd.read_csv('resources/data/train.csv')
    test_df = pd.read_csv('resources/data/test.csv')

    movies_df =  pd.read_csv('resources/data/movies.csv', index_col='movieId')
    imdb_df =  pd.read_csv('resources/data/imdb_data.csv', index_col='movieId')
    links_df =  pd.read_csv('resources/data/links.csv', index_col='movieId')
    genome_scores =  pd.read_csv('resources/data/genome_scores.csv', index_col='movieId')
    genome_tags =  pd.read_csv('resources/data/genome_tags.csv', index_col='tagId')
    tags =  pd.read_csv('resources/data/tags.csv')

def genre_extractor(df, col):
    """
    Returns a list of all unique features in a DataFrame columns separated by "|"
    """
    df.fillna("", inplace=True)
    feat_set = set()
    for i in range(len(df[f'{col}'])):
        for feat in df[f'{col}'].iloc[i].split('|'):
            feat_set.add(feat)
    return sorted([feat for feat in feat_set if feat != ""])


def user_ratings_count(df, n):
    """
    Counts the number of user ratings.
    Parameters
    ----------
        df (DataFrame): input DataFrame
        n (int): number of users to show
    Returns
    -------
        barplot (NoneType): barplot of top n users by number of observations
    Example
    -------
        >>> df = pd.DataFrame({'userId':[1,2,3,1,2,4,5,4]})
        >>> user_ratings_count(df, 3)
            NoneType (barplot)
    """
    fig = plt.figure(figsize=(8,6))
    data = df['userId'].value_counts().head(n)
    ax = sns.barplot(x = data.index, y = data, order= data.index, palette='brg', edgecolor="black")
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), fontsize=11, ha='center', va='bottom')
    plt.title(f'Top {n} Users by Number of Ratings', fontsize=14)
    plt.xlabel('User ID')
    plt.ylabel('Number of Ratings')
    st.pyplot(fig)





def mean_ratings_scatter(df, color='#4DA017', column='userId'):
    """
    Make scatterplots of mean ratings.
    Parameters
    ----------
        df (DataFrame): input DataFrame
        color (str): plot colour
        column (str): column to plot
    Returns
    -------
        scatterplot (NoneType): scatterplot of mean number of ratings
    """
    fig = plt.figure(figsize=(6,4))
    mean_ratings = df.groupby(f'{column}')['rating'].mean()
    user_counts = df.groupby(f'{column}')['movieId'].count().values
    sns.scatterplot(x=mean_ratings, y = user_counts, color=color)
    plt.title(f'Mean Ratings by Number of Ratings', fontsize=14)
    plt.xlabel('Rating')
    plt.ylabel('Number of Ratings')
    st.pyplot(fig)





def loading_data():
    #\genome_scores.csv
    movies_df =  pd.read_csv('resources/data/movies.csv', index_col='movieId')
    imdb_df =  pd.read_csv('resources/data/imdb_data.csv', index_col='movieId')
    links_df =  pd.read_csv('resources/data/links.csv', index_col='movieId')
    genome_scores =  pd.read_csv('resources/data/genome_scores.csv', index_col='movieId')
    genome_tags =  pd.read_csv('resources/data/genome_tags.csv', index_col='tagId')
    #tags =  pd.read_csv('/kaggle/input/edsa-movie-recommendation-2022/tags.csv')
    




def download_csv(name,df):
    
    csv = df.to_csv(index=False)
    base = base64.b64encode(csv.encode()).decode()
    file = (f'<a href="data:file/csv;base64,{base}" download="%s.csv">Download file</a>' % (name))
    
    return file