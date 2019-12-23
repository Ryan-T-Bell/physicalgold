import dash
from dash_table import DataTable
from dash.dependencies import Output, Input, State 
from gold_physical import get_all

import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash(name=__name__)

app.layout = html.Div([
    html.H1('Gold Best Physical Price'),
    html.Button('Submit', id='btn_download'),
    DataTable(
        id='tbl_gold',
        style_table={'width':'30%'},
    ),
])

@app.callback(
    [
        Output('tbl_gold', 'data'),
        Output('tbl_gold', 'columns'),
    ],
    [
        Input('btn_download', 'n_clicks'),
    ],
)
def download_gold_data(btn_download):
    data, cols = [], []
    
    if btn_download!=None and btn_download>0:
        df = get_all()
        
        if not df.empty:
            cols = [{'id': i, 'name': i } for i in df.columns]
            data = df.to_dict('records')
        
    return data, cols

if __name__ == '__main__':
    app.run_server()