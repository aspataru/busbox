# BusBox
Transform the Divoom Timebox Mini into a bus timetable!

## Installation on Raspbian
Get docker and build the image
```bash
curl -sSL https://get.docker.com | sh
```
Set up the service busbox.service, simple guide here:
[Systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

Check service logs
```bash
journalctl -u busbox.service
```

#### Thanks to

* [ScR4tCh/timebox](https://github.com/ScR4tCh/timebox)
* [derHeinz/divoom-adapter](https://github.com/derHeinz/divoom-adapter)

![Busbox](https://raw.githubusercontent.com/aspataru/busbox/master/docs/busbox.jpg "Busbox!")
