"""Constants for JBL ProScan."""

from datetime import timedelta

DOMAIN = "jbl_proscan"
PLATFORMS = ["sensor"]

CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_AQUARIUM_ID = "aquarium_id"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_SCAN_INTERVAL = 360
MIN_SCAN_INTERVAL = 15
MAX_SCAN_INTERVAL = 1440

BASE_URL = "https://www.jbl.de"
LOGIN_PAGE = "/fr-fr/login"
LOGIN_VERIFY = "/fr-fr/login/verify?target_verify=0"
USER_INFO = "/?mod=userinformation&country=fr&lang=fr"
AQUARIUMS_URL = "/fr/useraquarium/mes-analyses?country=fr"
ANALYSES_URL = "/fr/useraquarium/detail/{aquarium_id}/mes-analyses?country=fr"

DEFAULT_TIMEOUT = 30
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=DEFAULT_SCAN_INTERVAL)

ATTR_RAW_VALUE = "raw_value"
ATTR_SOURCE = "source"
ATTR_MEASUREMENT_ID = "measurement_id"
ATTR_MEASUREMENT_DATE = "measurement_date"
ATTR_UNIT_HINT = "unit_hint"

ATTR_MEASUREMENTS = "measurements"
HISTORY_LIMIT = 100
