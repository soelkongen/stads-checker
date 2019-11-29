# -*- coding: utf-8 -*-

import yaml
from stadschecker import stads
from sendnotification import SendNotification
from time import sleep


class Configuration():
    def readYAMLfile(self, fileName):
        with open(fileName, 'r') as stream:
            try:
                yamlDic = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
            self.configuration = yamlDic
            return self.configuration
            
    def setConfig(self):
        self.AppletName = self.configuration[0]["config"]["AppletName"]
        self.WebHooksKey = self.configuration[0]["config"]["WebHooksKey"]
        self.UpdateInterval = self.configuration[0]["config"]["UpdateInterval"]
        self.Username = self.configuration[0]["config"]["Username"]
        self.Password = self.configuration[0]["config"]["Password"]
        self.WordList = self.configuration[1]["searchwords"]
    
    
if __name__ == "__main__":
    PositiveResults = False

    Configuration = Configuration()
    Configuration.readYAMLfile("C:/Users/gusta/Desktop/config.yaml")
    Configuration.setConfig()
    
    SendNotification = SendNotification(Configuration.AppletName, Configuration.WebHooksKey)
    
    StadsInteraction = stads(Configuration.Username, Configuration.Password)
    StadsInteraction.login()
    
    while PositiveResults == False:
        StadsInteraction.getResults()
        Result = StadsInteraction.checkResultAvailable(Configuration.WordList)
        if Result != False: 
            SendNotification.Send(Result["name"],Result["grade"],Result["ects"])
            PositiveResults = True
        sleep(Configuration.UpdateInterval)
        
        
        
        
    