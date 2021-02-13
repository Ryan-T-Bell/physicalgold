import flask
import dash
from dash_table import DataTable
from dash.dependencies import Output, Input, State 
from gold_physical import get_all

import dash_html_components as html
import dash_core_components as dcc

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
server = app.server
app.layout = html.Div([
    html.H1('Gold Best Physical Price'),
    
    html.Div([
        
        html.Div([
            html.H3('Cash Back Percentage'),
            dcc.Input(id='input_cashback', value=1.0),
        ]),
        html.Button('Submit', id='btn_download'),
    ]),
    
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
    [
        State('input_cashback', 'value'),
    ]
)
def download_gold_data(btn_download, input_cashback):
    data, cols = [], []
    
    if btn_download!=None and btn_download>0:
        input_cashback = input_cashback*1.0/100.0
        
        df = get_all(cash_back=input_cashback)
        
        if not df.empty:
            cols = [{'id': i, 'name': i } for i in df.columns]
            data = df.to_dict('records')
        
    return data, cols

if __name__ == '__main__':
    app.run_server()