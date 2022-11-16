import requests
import toml

secrets = toml.load("config\secrets.toml")


def GetToken():
    url = "https://login.microsoftonline.com/2790fa5d-0b60-4226-86d5-663a2d76ff28/oauth2/v2.0/token"

    payload = f"""client_id={secrets['client_id']}
                &grant_type=client_credentials
                &client_secret={secrets['client_secret']}
                &scope=https%3A%2F%2Forg35bbcdc7.api.crm.dynamics.com%2F.default"""

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload).json()

    return response


def GetValues(flow):
    url = f"https://org35bbcdc7.crm.dynamics.com/api/data/v9.2/crea7_orquestradors?$top=10&$filter=crea7_name eq '{flow}'&$orderby=crea7_datadeinicio desc"

    payload = 'top=5'
    headers = {
        'Authorization': f"Bearer {GetToken()['access_token']}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload).json()

    return response


def GetFlows():
    url = "https://org35bbcdc7.crm.dynamics.com/api/data/v9.2/crea7_orquestradors?$apply=groupby((crea7_name))"

    headers = {
        'Authorization': f"Bearer {GetToken()['access_token']}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request(
        "GET", url, headers=headers).json()

    return response
