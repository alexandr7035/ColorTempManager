import params
import json
import os

class ColorTempManager:

    def __init__(self):
        if not os.path.exists(params.CONFIG_FILE):

            self.config = open(params.CONFIG_FILE, 'w')

            settings = {}

            settings["day_value"] = params.TEMP_DAY_DEFAULT_VALUE
            settings["night_value"] = params.TEMP_NIGHT_DEFAULT_VALUE
            settings["is_enabled"] = False

            json.dump(settings, self.config)

            self.config.close()
            

        self.config = open(params.CONFIG_FILE, 'r+')
        self.settings = json.load(self.config)


    def update(self):
        pass


    def setDayTempValue(self):
        pass


    def setNightTempValue(self):
        pass


    def getDayTempValue(self):
        return self.settings["day_value"]

    def getNightTempValue(self):
        return self.settings["night_value"]

    
    def setEnabled(self, state):

        if state is True:
            pass
        else:
            pass

    
    def checkIfEnabled(self):
        return self.settings["is_enabled"]