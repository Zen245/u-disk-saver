import daemon
from MAIN import MAIN
with daemon.DaemonContext():
    MAIN()
