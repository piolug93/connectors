import sys
import time

from connector.base import Mandiant

try:
    mandiantConnector = Mandiant()
    mandiantConnector.run()
except Exception:
    time.sleep(10)
    sys.exit(0)
