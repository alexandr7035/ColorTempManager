import params
import json
import os

class ColorTempManager:

    def __init__(self):
        if not os.path.exists(params.CONFIG_FILE):

            self.config = open(params.CONFIG_FILE, 'w')

            default_settings = {}

            default_settings["day_value"] = params.TEMP_DAY_DEFAULT_VALUE
            default_settings["night_value"] = params.TEMP_NIGHT_DEFAULT_VALUE
            default_settings["is_enabled"] = False

            json.dump(default_settings, self.config)

            self.config.close()
            

        self.config = open(params.CONFIG_FILE, 'r+')
        self.settings = json.load(self.config)


    def update(self):
        os.system("redshift -P -O " + str(self.settings["day_value"]))
        self.settings['is_enabled'] = True
        self.config.seek(0)
        json.dump(self.settings, self.config)
        self.config.truncate()

    def stop(self):
        os.system("redshift -x ")
        self.settings['is_enabled'] = False
        self.config.seek(0)
        json.dump(self.settings, self.config)
        self.config.truncate()


    def setDayTempValue(self, value):

        self.settings['day_value'] = value
        self.config.seek(0)
        json.dump(self.settings, self.config)
        self.config.truncate()


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

    