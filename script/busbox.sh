#!/usr/bin/env bash
# /etc/init.d/busbox

### BEGIN INIT INFO
# Provides:          busbox
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts the busbox daemon
# Description:       Starts the busbox daemon
### END INIT INFO

# If you want a command to always run, put it here
# sudo update-rc.d busbox defaults
# sudo update-rc.d busbox remove

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting busbox"
    # run application you want to start
    docker run -it --name busbox --net host --rm busbox 11:75:58:DA:E6:E2 &
    ;;
  stop)
    echo "Stopping busbox"
    # kill application you want to stop
    docker kill busbox
    ;;
  *)
    echo "Usage: /etc/init.d/busbox {start|stop}"
    exit 1
    ;;
esac

exit 0