from requests import get

apiKey = "d76957244bec878c76cd0a09a0c404ad"
res = get(f"http://api.aviationstack.com/v1/flights?access_key={apiKey}").json()["data"]
for x in res:
    print(x)