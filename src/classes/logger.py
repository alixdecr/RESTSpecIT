import os, time
from colorama import init, Fore, Style


"""
Class which is used to log command prompt messages and data to external files.
"""
class Logger:


    """
    Constructor function.
    """
    def __init__(self, config):

        # initialize colorama colors on Windows machines
        init()

        # define colors
        self.colorDict = {"red": Fore.RED, "blue": Fore.BLUE, "green": Fore.GREEN, "white": Fore.WHITE, "purple": Fore.MAGENTA, "yellow": Fore.YELLOW, "cyan": Fore.CYAN}

        self.outPath = config["execution"]["out-path"]

        if not os.path.exists(f"{self.outPath}/logs/request_logs.txt"):
            # create request logs header
            with open(f"{self.outPath}/logs/request_logs.txt", "a") as outfile:
                outfile.write("TIME     | VALID | REASON      | COD | RESPONSE DATA                     | REQUEST\n==================================================================================\n")


    """
    Function which prints a command prompt message in a certain style and color.
    """
    def logMessage(self, message, type, color, newLine=False, extra=""):

        # if parameter color is valid, surround message with that color
        if color in self.colorDict:
            coloredMessage = self.colorDict[color] + message + Style.RESET_ALL
        else:
            coloredMessage = message

        # if need for a new line, add it
        if newLine:
            line = "\n"
        else:
            line = ""

        # if extra text is specified, add it after ':'
        if extra != "":
            coloredMessage += f": {extra}"

        if type == "title":
            print(f"{line}--- {coloredMessage} ---")

        elif type == "bullet":
            print(f"{line} - {coloredMessage}")

        elif type == "arrow":
            print(f"{line} -> {coloredMessage}")

        else:
            print(f"{line}{coloredMessage}")


    """
    Function which prints a command prompt text of a certain category.
    """
    def logText(self, text, category):

        # get current time
        t = time.localtime()
        timeString = time.strftime("%H:%M:%S", t)

        logCat = "[INFO]   "
        printCat = "[INFO]   "

        if category == "title":
            logCat = "[TITLE]  "
            printCat = self.colorDict["blue"] + "[TITLE]  " + Style.RESET_ALL
        elif category == "section":
            logCat = "[SECTION]"
            printCat = self.colorDict["purple"] + "[SECTION]" + Style.RESET_ALL
        elif category == "warning":
            logCat = "[WARNING]"
            printCat = self.colorDict["yellow"] + "[WARNING]" + Style.RESET_ALL
        elif category == "error":
            logCat = "[ERROR]  "
            printCat = self.colorDict["red"] + "[ERROR]  " + Style.RESET_ALL
        elif category == "success":
            logCat = "[SUCCESS]"
            printCat = self.colorDict["green"] + "[SUCCESS]" + Style.RESET_ALL
        elif category == "request":
            logCat = "[REQUEST]"
            printCat = self.colorDict["cyan"] + "[REQUEST]" + Style.RESET_ALL

        logText = timeString + " " + logCat + " " + text + "\n"
        printText = timeString + " " + printCat + " " + text

        print(printText)

        # add prompt data to log file
        with open(f"{self.outPath}/logs/execution_logs.txt", "a", encoding="utf-8") as outfile:
            outfile.write(logText)


    """
    Function which logs LLM prompt data to an external file.
    """
    def logPrompt(self, promptData):

        # get current time
        t = time.localtime()
        currentTime = time.strftime("%H:%M:%S", t)

        data = f"TIME: {currentTime}\nPROMPT: {promptData['prompt']}\nRESPONSE: {promptData['response']}\nOBJECT: {promptData['object']}\n\n"

        # add prompt data to log file
        with open(f"{self.outPath}/logs/prompt_logs.txt", "a", encoding="utf-8") as outfile:
            outfile.write(data)


    """
    Function which logs request data to an external file.
    """
    def logRequest(self, responseData):

        # get current time
        t = time.localtime()
        currentTime = time.strftime("%H:%M:%S", t)

        # shorten response text if it is too long
        text = responseData["text"].replace("\r", "").replace("\n", "")
        if len(text) > 30:
            text = text[:30] + "..."

        # find amount of spaces for good looking logs
        validText = str(responseData["valid"]) + (" " * (5 - len(str(responseData["valid"])))) # 5 is the length of the string "false"
        reasonText = responseData["reason"] + (" " * (11 - len(responseData["reason"]))) # 11 is the length of the string "status-code"
        dataText = text + (" " * (33 - len(text))) # 33 for max length of text

        # add request data to log file
        with open(f"{self.outPath}/logs/request_logs.txt", "a", encoding="utf-8") as outfile:
            outfile.write(f"{currentTime} | {validText} | {reasonText} | {responseData['code']} | {dataText} | {responseData['request']} \n")