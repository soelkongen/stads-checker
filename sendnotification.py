import requests

class SendNotification():
    def __init__(self, AppletName, key):
        self.WebHooksKey = key
        self.AppletName = AppletName
    
    def Send(self, ModuleName, Grade, ECTS):
        PostURL = "https://maker.ifttt.com/trigger/" + self.AppletName + "/with/key/" + str(self.WebHooksKey)
        print(PostURL)
        PostData = {'value1':ModuleName,'value2':Grade,'value3':ECTS}
        r = requests.post(url = PostURL, data = PostData)
        if r.text != "Congratulations! You've fired the "+ self.AppletName + " event":
            print("ERROR : No response. Maybe wrong key")
        
        print(r.text)


        