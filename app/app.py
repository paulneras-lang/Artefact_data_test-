import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Data Visualization web application")


if st.button("Click me"):
    st.balloons()


df = pd.read_csv('data/CO2_per_capita.csv', sep = ';') 

st.dataframe(df.head(10))

country = st.selectbox("Select Country", df['Country Name'].unique())
start_year, end_year = st.slider("Select Year", min_value=1950, max_value=2010, value=(1950,2010))

def show_life_expectancy(start_year, end_year, country='Canada'):
    
    filtered_df = df[(df['Year']>=start_year) & (df['Year']<=end_year) & (df['Country Name']==country)]
    figure = px.line(filtered_df, x="Year", y="CO2 Per Capita (metric tons)", title=f'CO2 per capita in {country} ({start_year}-{end_year})')
    return figure

fig = show_life_expectancy(start_year, end_year, country)

st.plotly_chart(fig)

st.dataframe(df)


options = [5, 10, 15, 20]
nb_displayed_str = st.segmented_control("select display", options, selection_mode="single", default=5)

def top_n_emitters(df, start_year, end_year, nb_displayed=5):

    co2_df_filtered = df[(df["Year"]>=start_year)&(df["Year"]<=end_year)] 
    co2_df_by_country = co2_df_filtered[["Country Name", "CO2 Per Capita (metric tons)"]].groupby("Country Name", as_index=False).mean()
    co2_df_top = co2_df_by_country.sort_values("CO2 Per Capita (metric tons)", ascending=False)[:nb_displayed]  
    figure2 = px.bar(co2_df_top, x="Country Name", y="CO2 Per Capita (metric tons)")     
    return figure2


fig2 = top_n_emitters(df, start_year, end_year,nb_displayed_str)

st.plotly_chart(fig2)



co2_df_to_plot = df.dropna().sort_values(by="Year")
fig3 = px.scatter_geo(co2_df_to_plot.dropna(), locations="Country Code",
                    hover_name="Country Name",
                    size="CO2 Per Capita (metric tons)",
                    animation_frame = "Year",
                    projection="natural earth")

st.plotly_chart(fig3)


from streamlit_extras.image_compare_slider import *

st.write("Pokemon Comparison")
st.write("Drag the slider to compare the two images.")

image_compare_slider(
    "https://www.gamecash.fr/thumbnail-600/pokemon-bleu-gb-e106882.jpg",
    "https://www.gamecash.fr/thumbnail-600/pokemon-rouge-e57519.jpg",
    label1="Color",
    label2="Grayscale",
    key="basic_compare",
)
st.write("By default, the slider doesn't trigger reruns.")


st.write("Pokemon Comparison2")
st.write("Drag the slider to compare the two images.")

image_compare_slider(
    "https://m.media-amazon.com/images/I/81E5GaIww-S.jpg",
    "https://static.fnac-static.com/multimedia/images_produits/ZoomPE/3/4/9/0045496464943/tsp20250116214635/Pokemon-Version-Perle.jpg",
    label1="Color",
    label2="Grayscale",
    key="basic_compare",
)
st.write("By default, the slider doesn't trigger reruns.")