"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import email
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from sympy import im

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from recommenders.mymodules import genre_extractor


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","EDA","Solution Overview","Feedback",'About']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    st.sidebar.image('resources\imgs\Screen_lot_1.png',use_column_width=True)
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    if page_selection == "EDA":
        #load movie and rating 
        mov_df = pd.read_csv('resources\data\movies.csv')
        rate_df = pd.read_csv('resources\\data\\ratings.csv')
        
        #movie and rating dataframe 
        movie_rating_df = pd.merge(left=mov_df,right=rate_df,how='inner',left_on='movieId',right_on='movieId')
        movie_rating_df.drop(['movieId','timestamp'],axis=1,inplace=True)
        #delete dataframes to save memory
        del mov_df
        del rate_df

        #Showing dataframe
        if st.checkbox("Preview Dataframe"):
            
            if st.button('Dataframe'):
                st.write('Showing dataframe')
                st.write('df')
            
            if st.button('Head'):
                st.write('Showing first 5 rows')
                st.write(movie_rating_df.head())

            if st.button('Tail'):
                st.write('Showing last 5 rows')
                st.write(movie_rating_df.tail())

        #Searching movie GDetails
        st.write('Show for movies details')
        movie_title = movie_rating_df.title.unique()
        movie_genre = st.selectbox('Select a Movie',movie_title)
            
        if movie_genre == movie_title:
            selected_movie = movie_rating_df[movie_rating_df.title == movie_title]
            df_columns = ['Title','Genre','Highest Rating','Lowest Ratings','Average Rating','Total User Review']
            df_input = [movie_title,selected_movie.genres,round(selected_movie.rating.max(),3),round(selected_movie.rating.min(),3),round(selected_movie.rating.mean(),3),selected_movie.userId.count()]
            sel_mov = pd.DataFrame(data=df_input,columns=df_columns)
            sel_mov
            st.sucess('{} has been rated {} times with an IMDB average of {}'.format(movie_title,selected_movie.userId.count(),round(selected_movie.rating.mean(),3)))

        
        st.write('Show movies by Genre')
        genres = genre_extractor(movie_rating_df,'genres')
        





    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

        
    if page_selection == "About":    
        #st.subheader("Team NM 3")
        st.markdown("<h3 style='text-align: center; color: magenta; background: cyan; margin: 3px'>TEAM NM2</h1>", unsafe_allow_html=True)
		#st.markdown("<h3 style='text-align: center; color: green; background: #D3D3D3; margin: 3px'>TEAM NM2</h1>", unsafe_allow_html=True)
        

        from PIL import Image
        prince,izu = st.columns(2)
        dan,huzaifa,jerry =  st.columns(3)

        dan_img = Image.open('resources\imgs\daniel.jpg')
        jerry_img = Image.open('resources\imgs\jerry.jpg')
        huzaifa_img = Image.open('resources\imgs\huzaifa.jpg')
        prince_img = Image.open('resources\imgs\Prince_Okon.png')
        izu_img = Image.open('resources\imgs\izu.jpg')

        with prince:
            st.image(prince_img,caption='Prince Okon- Team lead')

        with huzaifa:
            st.image(huzaifa_img,caption='Huzaifa Abu - Technical Lead')

        with dan:
            st.image(dan_img,caption='Odukoya Daniel - Administrator')

        with jerry:
            st.image(jerry_img,caption='Jerry Iriri - Chief Designer')

        with izu:
            st.image(izu_img,caption='Izunna Eneude - Quality Control')
        

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.



    if page_selection == "Feedback":
        
        st.session_state;
        with st.form(key = 'Feedback'):
            
            name = st.text_input('Name')
            mail = st.text_input('Email')
            phone = st.text_input('Phone Number')
            
            #radio buttons
            feed_radio = st.radio('Select an option',('Feedback','Contact Us','Other'),key='radio_option')         
            
            subject = st.text_input('Subject') 
            message = st.text_area('Message')
            
            if st.form_submit_button('Submit'):
                if feed_radio != "Other":
                    st.success('Your {} form has been logged'.format(feed_radio))

                else:
                    st.success('Your comment has been logged'.format(feed_radio))

           

            
            

            
            

                


if __name__ == '__main__':
    main()
