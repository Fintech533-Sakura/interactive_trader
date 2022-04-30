from dash import dash_table
import datetime
import pandas as pd

blotter = pd.DataFrame(
    columns=['date', 'trip', 'action', 'ticker', 'size',
             'price', 'status']
)

order_page = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in blotter.columns],
    data=blotter.to_dict('records'),
    id='pair-blotter-link'
)




