from dash import Dash, html, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Button(
        id='button', children='Press Me!', n_clicks=0
    ),
    html.Div(
        id = 'text',
        children=['...']
    )    
])


@callback(
    Output('text', 'children'),
    Input('button', 'n_clicks')
)
def f(b):
    return b

if __name__ == '__main__':
    app.run(debug=True)

