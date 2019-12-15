import dash
from dash_table import DataTable
from dash.dependencies import Output, Input, State 
from gold_physical import get_all

import dash_html_components as html
import dash_core_components as dcc

df = get_all()

app = dash.Dash(name=__name__)#, assets_url_path='gold')

app.layout = html.Div([
    html.H1('Gold Best Physical Price'),
    DataTable(
        id='tbl_gold',
        columns=[{'id': i, 'name': i } for i in df.columns],
        data = df.to_dict('records'),
        style_table={'width':'30%'},
    ),
])

if __name__ == '__main__':
    app.run_server()