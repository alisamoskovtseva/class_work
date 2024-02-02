from io import BytesIO
import requests

api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
api_server = "https://search-maps.yandex.ru/v1/"

addres_ll = "37.588392,55.734036"
params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": addres_ll,
    "type": "biz"
}
response = requests.get(api_server, params=params)
if not response:
    print(1)
else:
    json_respons = response.json()
    organization = json_respons["features"][0]
    name = organization["properties"]["CompanyMetaData"]["name"]
    address = organization["properties"]["CompanyMetaData"]["address"]
    point = organization["geometry"]["coordinates"]
    org_point = f"{point[0]},{point[1]}"
    delta = "0.005"
    map_params = {
        "ll": addres_ll,
        "spn": ",".join([delta, delta]),
        "l": "map",
        "pt": f"{org_point},pm2dgl"
    }
    api_server = 'https://static-maps.yandex.ru/1.x/'
    response = requests.get(api_server, params=map_params)
    #Image.open(BytesIO(response.content)).show()
