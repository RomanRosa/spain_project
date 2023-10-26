import pandas as pd
import numpy as np
import streamlit.components.v1 as t
from PIL import Image
import warnings


# define the main function
import streamlit as st
import pandas as pd
from textblob import TextBlob
import re

# Load the logo image
logo = Image.open("Logo Principal_blanco_fondotrnsp.png")
logo_porter = Image.open("pn_sld_rgb_pos_wht.jpg")

# Display the logo on the sidebar
st.sidebar.image(logo, width=300, use_column_width=False)

    # Create a column to display the logo_porter image on the right side of the page
col1, col2 = st.columns([1, 1])
with col2:
    st.image(logo_porter, width=300, use_column_width=False)


def main():
    warnings.filterwarnings("ignore")
    st.title("Pulse Track - Spain Project")
    
    
    def sentiment_analysis(texto):
        analysis = TextBlob(texto)
        return analysis.sentiment.polarity
    
    def crear_dicc_keywords(df_keywords):
        df_keywords=df_keywords.fillna('exxxtract')
        #df_keywords
        area_dict = df_keywords.to_dict('list')
        #print(area_dict)
        for k,v in area_dict.items():
            #print(v)
            nv=list(set(v))
            nv=[x for x in v if x != 'exxxtract']
            nv=list(set(nv))
            area_dict[k]=nv
        return area_dict
    
    def contar_palabras(comentario, palabras):
        contador = 0
        for palabra in palabras:
            contador += len(re.findall(fr"\b{palabra}\b", comentario, re.IGNORECASE))
        return contador

    def palabras_presentes(comentario, palabras):
        return [palabra for palabra in palabras if re.search(fr"\b{palabra}\b", comentario, re.IGNORECASE)]

    # Add a selectbox to the sidebar to allow upload of the dataset in excel format, the title for the button is "Upload Hashtags File"
    st.sidebar.title("Upload Input Data File")
    
    # Add a file uploader to the sidebar and capture the uploaded file in a variable
    
    input_data = st.sidebar.file_uploader("Input Data File", type=["xlsx"])
    
    # View the uploaded file
    if input_data is not None:
        input_data = pd.read_excel(input_data)
        # Convert the headers to lowercase
        input_data.columns = [col.lower() for col in input_data.columns]
        input_data['mention content'] = input_data['mention content'].astype(str)
        input_data['title'] = input_data['title'].astype(str)
        input_data['sentiment_mention_content'] = input_data['mention content'].apply(sentiment_analysis)
        input_data['sentiment_mention_title'] = input_data['title'].apply(sentiment_analysis)
        st.write("Input data file shape:", input_data.shape)
        st.write("Input data file head:", input_data.head())
        
        input_data_splited = input_data[['id', 'date', 'time', 'media type', 'site name', 'title', 'mention content']]
        # Convert the following columns to lowercase: media type, site name, title, mention content
        input_data_splited['media type'] = input_data_splited['media type'].str.lower()
        input_data_splited['site name'] = input_data_splited['site name'].str.lower()
        input_data_splited['title'] = input_data_splited['title'].str.lower()
        input_data_splited['mention content'] = input_data_splited['mention content'].str.lower()
        
        st.write("Input data file splited shape:", input_data_splited.shape)
        st.write("Input data file splited head:", input_data_splited.head())
    
    st.sidebar.title("Upload Hashtags File")

    # Add a file uploader to the sidebar and capture the uploaded file in a variable
    uploaded_hashtags_file = st.sidebar.file_uploader("Upload Hashtags File", type=["xlsx"])

    # View the uploaded file
    if uploaded_hashtags_file is not None:
        uploaded_hashtags_file = pd.read_excel(uploaded_hashtags_file)
        # Convert the headers to lowercase
        uploaded_hashtags_file.columns = [col.lower() for col in uploaded_hashtags_file.columns]
        st.write("Hashtags file shape:", uploaded_hashtags_file.shape)
        st.write("Hashtags file head:", uploaded_hashtags_file.head())
        
        uploaded_hashtags_file_splited = uploaded_hashtags_file[['tweetdate', 'content', 'twitterprofile']]
        uploaded_hashtags_file_splited['content'] = uploaded_hashtags_file_splited['content'].astype(str)
        uploaded_hashtags_file_splited['content'] = uploaded_hashtags_file_splited['content'].str.lower()
        
        st.write("Hashtags file splited shape:", uploaded_hashtags_file_splited.shape)
        st.write("Hashtags file splited head:", uploaded_hashtags_file_splited.head())

    # Add a selectbox to the sidebar to allow upload of the dataset in excel format, the title for the button is "Upload Instagram Posts File"
    st.sidebar.title("Upload Instagram Posts File")
    uploaded_instagram_posts_file = st.sidebar.file_uploader("Upload Instagram Posts File", type=["xlsx"])

    # View the uploaded file
    if uploaded_instagram_posts_file is not None:
        uploaded_instagram_posts_file = pd.read_excel(uploaded_instagram_posts_file)
        # Convert the headers to lowercase
        uploaded_instagram_posts_file.columns = [col.lower() for col in uploaded_instagram_posts_file.columns]
        st.write("Instagram posts file shape:", uploaded_instagram_posts_file.shape)
        st.write("Instagram posts file head:", uploaded_instagram_posts_file.head())

    # Add a selectbox to the sidebar to allow upload of the dataset in excel format, the title for the button is "Upload LinkedIn Profiles File"
    st.sidebar.title("Upload LinkedIn Profiles File")
    uploaded_linkedin_profiles_file = st.sidebar.file_uploader("Upload LinkedIn Profiles File", type=["xlsx"])

    # View the uploaded file
    if uploaded_linkedin_profiles_file is not None:
        uploaded_linkedin_profiles_file = pd.read_excel(uploaded_linkedin_profiles_file)
        # Convert the headers to lowercase
        uploaded_linkedin_profiles_file.columns = [col.lower() for col in uploaded_linkedin_profiles_file.columns]
        st.write("LinkedIn profiles file shape:", uploaded_linkedin_profiles_file.shape)
        st.write("LinkedIn profiles file head:", uploaded_linkedin_profiles_file.head())


    # Add a selectbox to the sidebar to allow upload of the dataset in excel format, the title for the button is "Upload Keywords File"
    st.sidebar.title("Upload Keywords File")
    uploaded_keywords_file = st.sidebar.file_uploader("Upload Keywords File", type=["xlsx"])
    
    # View the uploaded file
    if uploaded_keywords_file is not None:
        uploaded_keywords_file = pd.read_excel(uploaded_keywords_file)
        # Convert the headers to lowercase
        uploaded_keywords_file.columns = [col.lower() for col in uploaded_keywords_file.columns]
        st.write("Keywords file shape:", uploaded_keywords_file.shape)
        st.write("Keywords file head:", uploaded_keywords_file.head())
        
        # Apply the function crear_dicc_keywords to the uploaded_keywords_file
        dic_keywords = crear_dicc_keywords(uploaded_keywords_file)
        st.write("Keywords file dic:", dic_keywords)

    # Add a selectbox to the sidebar to allow upload of the dataset in excel format, the title for the button is "Upload Taxonomy File"
    st.sidebar.title("Upload Taxonomy File")
    uploaded_taxonomy_file = st.sidebar.file_uploader("Upload Taxonomy File", type=["xlsx"])
    
    # Apply the function crear_dicc_keywords to the uploaded_keywords_file
    # Macrodiccionario
    #dic_keywords = crear_dicc_keywords(df_keywords)
    #dic_keywords

    # View the uploaded file
    if uploaded_taxonomy_file is not None:
        uploaded_taxonomy_file = pd.read_excel(uploaded_taxonomy_file)
        # Convert the headers to lowercase
        uploaded_taxonomy_file.columns = [col.lower() for col in uploaded_taxonomy_file.columns]
        st.write("Taxonomy file shape:", uploaded_taxonomy_file.shape)
        st.write("Taxonomy file head:", uploaded_taxonomy_file.head())
        
        
    # Concat the columns with text:
    input_data['title'] = input_data['title'].astype(str)
    input_data['title'] = input_data['title'].str.lower()
    
    input_data['mention content'] = input_data['mention content'].astype(str)
    input_data['mention content'] = input_data['mention content'].str.lower()
    
    uploaded_hashtags_file['content'] = uploaded_hashtags_file['content'].astype(str)
    uploaded_hashtags_file['content'] = uploaded_hashtags_file['content'].str.lower()
    
    uploaded_instagram_posts_file['description'] = uploaded_instagram_posts_file['description'].astype(str)
    uploaded_instagram_posts_file['description'] = uploaded_instagram_posts_file['description'].str.lower()
    
    # Concat the columns input_data, uploaded_hashtags_file, uploaded_instagram_posts_file in a new dataframe.
    #text_data = pd.concat([
    #    input_data[['title', 'mention content']],
    #    uploaded_hashtags_file[['content']],
    #    uploaded_instagram_posts_file[['description']],
    #], axis=0)
    
    #st.write("Text data shape:", text_data.shape)
    #st.write("Text data head:", text_data.head(20))
    
    # apply the function palabras_presentes to the column: mention content of the input_data dataframe using the dic_keywords to look for all the keywords in the text.
    # for each key of the key-value pair in the dic_keywords, create a new column in a new dataframe with the name of the key and the value of the column is the result of the function palabras_presentes. add to each columns at the beginning the prefix: "fdw_" ans show the result in the cell as a dictionary.
    for k,v in dic_keywords.items():
        input_data[f'Fdw_{k}']=input_data['mention content'].apply(lambda x: palabras_presentes(x, v))
        # in orher column count the finded words
        input_data[f'Count_{k}'] = input_data['mention content'].apply(lambda x: contar_palabras(x, v))
    #for k,v in dic_keywords.items():
    #    input_data[f'fdw_{k}']=input_data['mention content'].apply(lambda x: palabras_presentes(x, v))
    
    st.write("Input data shape:", input_data.shape)
    st.write("Input data head:", input_data.head())
    
    #for k,v in dic_keywords.items():
    #    input_data[k]=input_data['mention content'].apply(lambda x: palabras_presentes(x, v))
    
    st.write("Input data shape:", input_data.shape)
    st.write("Input data head:", input_data.head())
                                                                              
    #for categoria, palabras in categorias.items():
    #df[f'Conteo_{categoria}'] = df['Mention Content'].apply(lambda x: contar_palabras(x, palabras))
    #df[f'Palabras_{categoria}'] = df['Mention Content'].apply(lambda x: palabras_presentes(x, palabras))
    
    # Insert a text area above the button with the message "Ask me anything" in bold letters
    
    # add a button to download the input_data dataframe as an excel file
    if st.button("Download Processed Input Data File"):
        st.write("Download Input Data File")
        st.write(input_data)
        input_data.to_excel('C:\github_repos\spain_bank\output_input_data.xlsx', index=False, engine='xlsxwriter')
        
    chat_input = st.text_area("Ask me anything about your data:")
    analysis = st.button("Analyze")

 
    # Check if all the required files have been uploaded
    if uploaded_hashtags_file is None or uploaded_instagram_posts_file is None or uploaded_linkedin_profiles_file is None or uploaded_keywords_file is None or uploaded_taxonomy_file is None:
        st.error("Please upload all the required files.")
        
if __name__ == "__main__":
    main()