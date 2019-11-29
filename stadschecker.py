from bs4 import BeautifulSoup
import requests
import os

class stads(object):
    def __init__(self, username, password):
        # variables that is set by our program
        # to determine various things
        self.initialized = False
        self.logged_in = False
        self.results = False

        # store username/password
        self.username = username
        self.password = password

        # init a requests session
        self.s = requests.session()

        # our base URL for stads
        self.url_base = "https://sb.aau.dk/sb-ad/sb/"

        self.init()

    # makes a initial request to STADS
    def init(self):
        req = self.s.get(self.url_base+"index.jsp")
        self.initialized = True
        return True

    def login(self):
        if not self.initialized:
            print("Need to be initialized first")
            return False

        url = self.url_base+"index.jsp"

        data = {
            "lang": None,
            "submit_action": "login",
            "brugernavn": self.username,
            "adgangskode": self.password,
        }

        req = self.s.post(url, data=data)

        if "Velkommen til STADS-Selvbetjening" in req.text:
            self.logged_in = True
            return True
        else:
            return False

    def getResults(self):
        if not self.logged_in:
            print("Not logged in, so cannot fetch results")
            return False

        url = self.url_base+"resultater/studresultater.jsp"
        req = self.s.get(url)

        bs = BeautifulSoup(req.text, "html.parser")
        tbody = bs.find("table", {"id": "resultTable"}).find("tbody")

        if not tbody:
            print("Could not find table body")
            return False

        results = []
        for row in tbody.findAll("tr"):
            columns = row.findAll("td")

            result = {
                    "name": columns[0].getText().strip(),
                    "date": columns[1].getText().strip(),
                    "grade": columns[2].getText().strip(),
                    "ects-grade": columns[3].getText().strip(),
                    "ects": columns[4].getText().strip(),
            }

            results.append(result)

        self.results = results
        return results

    def printResults(self):
        if not self.results:
            print("No results to print")
            return False
        for result in self.results:
            print(result["name"])
            print("- Grade: \t"+result["grade"])
            print("- ECTS-Grade: \t"+result["ects-grade"])
            print("- ECTS: \t"+result["ects"])
            print("- date: \t"+result["date"])
            print("----------")

    def checkResultAvailable(self, keywords = []):
        if not self.results:
            print("No results available to check against")
            return False

        for result in self.results:
            for keyword in keywords:
                if keyword.lower() in result["name"].lower():
                    return result
        return False




if __name__ == "__main__":
    x = stads(os.environ['AAU_STADS_USERNAME'], os.environ['AAU_STADS_PASSWORD'])
    x.login()
    x.getResults()
    x.printResults()
    print(x.checkResultAvailable(["fdsfsd"]))
    print(x.checkResultAvailable(["lineære"]))
    print(x.checkResultAvailable(["beregnings"]))

