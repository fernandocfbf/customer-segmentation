from contextlib import AsyncExitStack


def is_cancelled(text):
    return str(text[0]) == 'C'

def remove_cancelled_transactions(df):
    df_non_cancelled = df.copy()
    df_non_cancelled["cancelled"] = 0
    df_non_cancelled["cancelled"] = df_non_cancelled.apply(lambda x: is_cancelled(x["InvoiceNo"]), axis=1)
    return df_non_cancelled.loc[df_non_cancelled["cancelled"] == 0].drop(["cancelled"], axis=1)

def products_per_customer_per_country(df):
    temp_table = df.groupby(by=["Country", "CustomerID"], as_index=False)['InvoiceDate'].count()
    dict_countries = list_to_dict(temp_table["Country"].unique().tolist())
    for country in dict_countries:
        temp_table_unique_country = temp_table.loc[temp_table["Country"] == country]
        dict_countries[country] = temp_table_unique_country["InvoiceDate"].tolist()
    return dict_countries

def list_to_dict(list):
    resp = dict()
    for item in list:
        resp[item] = []
    return resp
