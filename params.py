from os.path import expanduser

APP_NAME = "ColorTempManager"
APP_VERSION = "1.0"

WINDOW_TITLE = APP_NAME + " v" + APP_VERSION

WORK_DIR = expanduser("~") + "/.ctm.d"

CONFIG_FILE = WORK_DIR + "/ctm.json"

TEMP_MAX_VALUE = 6500
TEMP_MIN_VALUE = 1000

TEMP_DAY_DEFAULT_VALUE = 5000
TEMP_NIGHT_DEFAULT_VALUE = 4000
