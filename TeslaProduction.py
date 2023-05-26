from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
# import dash_html_components as html
from navbar import create_navbar

df = pd.read_csv("tesla_vehicles.csv")
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar
navbar = create_navbar()

# Create Layout for App
app.layout = dbc.Container([
    navbar,
    dcc.Location(id='url', refresh=False),
    dbc.Container(id='page-content', className="mt-4"),
    # dbc.Row(dcc.Graph(id='vehicle-graph'), justify='center'),
    # dbc.Row([
    #     dbc.Col(dcc.RangeSlider(
    #         id='year-range-slider',
    #         min=df['Year'].min(),
    #         max=df['Year'].max(),
    #         marks={str(year): str(year) for year in df['Year'].unique()},
    #         value=[df['Year'].min(), df['Year'].max()],
    #         step=None
    #     ), width=6)], justify='center'),
    # dbc.Row([dbc.Col(dcc.Graph(id='vehicle-table'), width=6)], justify='center')
], fluid=True)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return dbc.Container([html.H1('Home Page')])
    elif pathname == '/about':
        return dbc.Container([html.H1('About Page')])
    elif pathname == '/contact':
        return dbc.Container([html.H1('Contact Page')])
    else:
        return dbc.Container([html.H1('404 Page Not Found')])
# @app.callback(
#     Output('page-content', 'children'),
#     Output('vehicle-graph', 'figure'),
#     Output('vehicle-table', 'figure'),
#     Input('url', 'pathname'),
#     Input('year-range-slider', 'value')
# )
# def update_graph(pathname, selected_years):
#     start_year, end_year = selected_years
#     filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
#     traces = []
#     colors = ['rgba(0, 0, 255, 0.5)', 'rgba(255, 0, 0, 0.5)', 'rgba(0, 255, 0, 0.5)', 'rgba(0, 255, 255, 0.5)']
#     quarters = ['Q1', 'Q2', 'Q3', 'Q4']
#
#     for quarter in range(1, 5):
#         quarter_data = filtered_df[filtered_df['Quarter'] == quarter]
#         trace = go.Bar(
#             x=quarter_data['Year'],
#             y=quarter_data['New Vehicles'],
#             name=quarters[quarter-1],
#             marker_color=colors[quarter-1],
#             showlegend=(quarter == 1 or quarter == 2 or quarter == 3 or quarter == 4)  # Set showlegend to True only for the first trace of each quarter
#         )
#         traces.append(trace)
#
#     fig = go.Figure(data=traces)
#     fig.update_layout(
#         title='Tesla New Vehicle Production by Year and Quarter',
#         xaxis_title='Year',
#         yaxis_title='New Vehicles',
#         legend_title_text='Quarter',
#         barmode='group'
#     )
#
#     table_trace = go.Table(
#         header=dict(values=filtered_df.columns,
#                     line_color='darkslategray',
#                     fill_color='lightskyblue',
#                     align='left'),
#         cells=dict(values=[filtered_df.Year, filtered_df.Quarter, filtered_df['New Vehicles']],
#                    line_color='darkslategray',
#                    fill_color='lightcyan',
#                    align='left')
#     )
#     table = go.Figure(data=[table_trace])
#
#     if pathname == '/':
#         return fig, table, dbc.Jumbotron([('Home Page')])
#     elif pathname == '/about':
#         return fig, table, dbc.Jumbotron([('About Page')])
#     elif pathname == '/contact':
#         return fig, table, dbc.Jumbotron([('Contact Page')])
#     else:
#         return fig, table, dbc.Jumbotron([('404 Page Not Found')])

if __name__ == '__main__':
    app.run_server(debug=True)
