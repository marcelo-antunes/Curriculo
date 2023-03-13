import plotly.express as px
import pandas as pd

df = pd.read_excel('./data/experiencia.xlsx')

df['start_date'] = pd.to_datetime(df['start_date'],format='%Y')
df['end_date'] = pd.to_datetime(df['end_date'],format='%Y')

fig = px.timeline(df, 
                  x_start="start_date", 
                  x_end="end_date", 
                  y="job", 
                  color="city", 
                  color_discrete_sequence=['darkgreen','chocolate','firebrick','darkturquoise'], 
                  title="Experiências",
                  width=700, 
                  height=180
)

fig.update_layout(font_family='Calibri',
                  font_color='rgb(0,0,0)',
                  title_font_family='Calibri Black',
                  title_font_size=18, 
                  title_x=0.5, 
                  title_xanchor='center',
                  legend_title="    Cidade",
                  legend_title_font_family='Calibri Black',
                  legend_title_font_size=14,
                  legend_font_size=10, 
                  plot_bgcolor='rgba(0,0,0,0)', 
                  paper_bgcolor='rgba(0,0,0,0)',
                  margin_t=40,
                  margin_b=20,
                  margin_l=80,
                  margin_r=10
)

fig.update_xaxes(tickfont_size=10,
                 tickmode="auto",
                 nticks=20,
                 showgrid=False)

fig.update_yaxes(title_text="",
                 tickfont_size=10,
                 showgrid=False,
                 automargin=False,
                 autorange="reversed"
)

fig.write_image('./img/experiencias3.png', scale=10)