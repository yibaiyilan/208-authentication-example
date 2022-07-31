import dash
import dash_auth
from dash import dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go


# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'Magic': 'Happens', 'Keep': 'Calm', 'Carry': 'On'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='auth example'
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1('Welcome to the Magic World'),
    html.H3('You are successfully authorized'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in [1, 2, 3, 4, 5]],
        value=1
    ),
    html.Div(id='graph-title'),
    dcc.Graph(id='graph'),
    html.A('Code on Github', href='https://github.com/yibaiyilan/208-authentication-example'),
    html.Br(),
    html.A("Data Source", href='https://dash.plotly.com/authentication'),
], className='container')

@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    dash.dependencies.Output('graph-title', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(dropdown_value):
    x = [x * 0.01 for x in range(-100, 100)]
    y = [(x**dropdown_value) for x in x]

    mu, sigma = 0, 0.1 # mean and standard deviation

    # Build figure
    fig = go.Figure()
    #graph_title='Graph of {}'.format(str(dropdown_value))
    # Add scatter trace with medium sized markers
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x,
            y=y,
            marker_symbol='star',
            marker=dict(
                color='yellow',
                size=20,
                opacity=0.5,
                line=dict(
                    color='orange',
                    width=2
                )
            ),
            showlegend=False
        )
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue"
    )
    fig.update_layout(width=400,height=400)

    return fig,graph_title, 

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
