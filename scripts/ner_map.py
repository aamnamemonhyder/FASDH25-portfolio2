import pandas as pd
import plotly.express as px

freq_path = 'ner_counts_aamna.tsv'
freq_df = pd.read_csv(freq_path, sep='\t')

coord_path = 'ner_gazetteer_aamna.tsv'
coord_df = pd.read_csv(coord_path, sep='\t')

merged_df=pd.merge(freq_df, coord_df, on='placenames', how='left')

fig=px.scatter_map(
    merged_df,
    lat='latitude',
    lon='longitude',
    size='frequency',
    size_max=40,
    hover_name='placenames',
    zoom=1,
    title='Placename Frequency - Global'
    )

fig.update_traces(marker=dict(color='yellow',
                              opacity=0.7,
                              sizemode='area'
                              ))
fig.show()


