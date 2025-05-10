import pandas as pd
import plotly.express as px

freq_path = "2A_aamna.tsv"
freq_df=pd.read_csv(freq_path, sep='\t')
freq_df['placename'] =freq_df['placename'].str.lower()

gaz_path = "../gazetteers/geonames_gaza_selection.tsv"
coord_df = pd.read_csv(gaz_path, sep="\t")
coord_df['asciiname'] = coord_df ['asciiname'].str.lower()


merged_df=pd.merge(freq_df, coord_df, left_on='placename', right_on='asciiname', how='left')
merged_df=merged_df.drop(columns=['asciiname', 'name','alternatenames', 'geonameid'])


fig_png=px.scatter_map(
        merged_df,
        lat='latitude',
        lon='longitude',
        color='placename',
        size='count',
        size_max=25,
        zoom=9.6,
        center={"lat":31.4, "lon": 34.4},
        map_style='carto-positron',
        title='Placename Frequency - Gaza Strip'
    )

fig_png.update_layout(
    width=1200,
    height=600
)

fig_png.update_traces(marker=dict(opacity=0.3))

fig_png.write_image('regex_png.png')
