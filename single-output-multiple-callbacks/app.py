from dash import Dash, html, callback, Input, Output, ctx


app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Button('Context Input 1', id='ctx-input-1', n_clicks=0),
        html.Button('Context Input 2', id='ctx-input-2', n_clicks=0),
        html.Div('Context Placeholder', id='ctx-output')
    ]),
    html.Div([
        html.Button('Allow Duplicates Input 1', id='dup-input-1', n_clicks=0),
        html.Button('Allow Duplicates Input 2', id='dup-input-2', n_clicks=0),
        html.Div('Allow Duplicates Placeholder', id='dup-output')
    ])
])


@callback(
    Output('ctx-output', 'children'),
    Input('ctx-input-1', 'n_clicks'),
    Input('ctx-input-2', 'n_clicks'),
    prevent_initial_call=True
)
def ctx_update(input1, input2):
    match ctx.triggered_id:
        case 'ctx-input-1':
            return 'Ctx from Input 1'
        case 'ctx-input-2':
            return 'Ctx from Input 2'

@callback(
    Output('dup-output', 'children'),
    Input('dup-input-1', 'n_clicks')
)
def dup_update_1(input1):
    return 'Dup from input 1'


@callback(
    Output('dup-output', 'children', allow_duplicate=True),
    Input('dup-input-2', 'n_clicks'),
    prevent_initial_call=True
)
def dup_update_2(input2):
    return 'Dup from input 2'


if __name__ == '__main__':
    app.run(debug=True)








