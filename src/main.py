import json, os
from classes.api_inferer import ApiInferer
from classes.api_tester import ApiTester


"""
RESTSpecIT: RESTful API Specification Inference Tool, powered with a LLM
------------------------------------------------------------------------
"""

def main():

    # IMPORT THE API CONFIG FILE
    with open("./inputs/config.json", "r") as openfile:
        config = json.load(openfile)

    # check if model key is specified
    if config["llm"]["openai-key"] != "":
        # EXECUTION FOR TEST MODE
        if config["execution"]["mode"] == "test":
        
            # INSTANTIATE THE TESTER CLASS
            tester = ApiTester(config)

            # TEST EXECUTION FOR ONLINE APIS
            tester.execute(["Genome Nexus API"])
            """
            tester.execute(["An API of Ice and Fire API",
                            "Balldontlie API",
                            "Bored API",
                            "CheapShark API",
                            "CoinCap API",
                            "Datamuse API",
                            "GBIF Species API",
                            "Open Brewery DB API",
                            "Random User Generator API",
                            "ReqRes API"])
            """

            # TEST EXECUTION FOR LOCAL APIS
            """
            tester.execute(["Soccer API",
                            "Weather API",
                            "Currency Exchange API"])
            """

        # EXECUTION FOR INFERER MODE
        else:

            # CREATE OUTPUT FILES
            outPath = config["execution"]["out-path"]
            folderName = config["api"]["name"].replace(" ", "_") # replace API name spaces with underscores
            apiOutPath = f"{outPath}/{folderName}"
        
            # create output folders for the API
            folderList = [outPath, apiOutPath]
            for folder in folderList:
                if not os.path.exists(folder):
                    os.mkdir(folder)
                    
            config["execution"]["out-path"] = apiOutPath
            
            # INSTANTIATE INFERER AND EXECUTE
            inferer = ApiInferer(config)
            for i in range(3):
                inferer.execute(i)
    else:
        print("Specify an OpenAI key in config.json")


if __name__ == "__main__":
    main()