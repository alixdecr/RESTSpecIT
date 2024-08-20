import json


"""
apiList = ["An API of Ice and Fire API",
           "Balldontlie API",
           "Bored API",
           "CheapShark API",
           "CoinCap API",
           "Datamuse API",
           "GBIF Species API",
           "Open Brewery DB API",
           "Random User Generator API",
           "ReqRes API"]
"""
apiList = ["Currency Exchange API",
           "Soccer API",
           "Weather API"]

resultDict = {"avg-route-percentage": 0, "avg-parameter-percentage": 0}

for api in apiList:
    resultDict[api] = {"name": api.replace(" ", "_"), "routes": {"min-found": 100, "max-found": 0, "found": 0, "total": 0, "percentage": 0}, "parameters": {"min-found": 100, "max-found": 0, "found": 0, "total": 0, "percentage": 0}}


for i in range(1, 11):
    
    for api in apiList:

        with open(f"./outputs-test-data-leakage/outputs_{i}/{resultDict[api]['name']}/found_doc.json", "r", encoding="utf-8") as openfile:
            data = json.load(openfile)
        
        resultDict[api]["routes"]["found"] += data["doc-routes"]["found"]
        resultDict[api]["routes"]["total"] += data["doc-routes"]["total"]
        resultDict[api]["parameters"]["found"] += data["doc-parameters"]["found"]
        resultDict[api]["parameters"]["total"] += data["doc-parameters"]["total"]

        resultDict[api]["routes"]["min-found"] = min(resultDict[api]["routes"]["min-found"], data["doc-routes"]["found"])
        resultDict[api]["parameters"]["min-found"] = min(resultDict[api]["parameters"]["min-found"], data["doc-parameters"]["found"])

        resultDict[api]["routes"]["max-found"] = max(resultDict[api]["routes"]["max-found"], data["doc-routes"]["found"])
        resultDict[api]["parameters"]["max-found"] = max(resultDict[api]["parameters"]["max-found"], data["doc-parameters"]["found"])

for api in apiList:
    resultDict[api]["routes"]["percentage"] = (resultDict[api]["routes"]["found"] / resultDict[api]["routes"]["total"]) * 100
    resultDict[api]["parameters"]["percentage"] = (resultDict[api]["parameters"]["found"] / resultDict[api]["parameters"]["total"]) * 100

    resultDict["avg-route-percentage"] += resultDict[api]["routes"]["percentage"]
    resultDict["avg-parameter-percentage"] += resultDict[api]["parameters"]["percentage"]

resultDict["avg-route-percentage"] = (resultDict["avg-route-percentage"] / 3)
resultDict["avg-parameter-percentage"] = (resultDict["avg-parameter-percentage"] / 3)

print(json.dumps(resultDict, indent=4))