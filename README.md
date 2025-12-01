# ha-pm5003

Home Assistant add-on for the Pimoroni PM5003 particulate matter sensor.

## About

This add-on reads particulate matter data from a [Pimoroni PM5003 sensor](https://shop.pimoroni.com/products/pms5003-particulate-matter-sensor-with-cable) using the [pms5003-python](https://github.com/pimoroni/pms5003-python) library and makes it available to Home Assistant.

## Installation

1. Add this repository to your Home Assistant add-on store
2. Install the "PM5003 Sensor" add-on
3. Configure the add-on with your serial device settings
4. Start the add-on

## Configuration

| Option | Description | Default |
|--------|-------------|---------|
| `device` | Serial device path | `/dev/ttyAMA0` |
| `baudrate` | Serial baudrate | `9600` |
| `poll_interval` | Polling interval in seconds | `10` |

### Example configuration

```yaml
device: "/dev/ttyAMA0"
baudrate: 9600
poll_interval: 10
```

## Hardware Setup

For Raspberry Pi, you may need to enable the serial port:

### Raspberry Pi OS Bookworm

```bash
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_serial_cons 1
```

Add `dtoverlay=pi3-miniuart-bt` to your `/boot/config.txt`

### Raspberry Pi OS Bullseye

```bash
sudo raspi-config nonint set_config_var enable_uart 1 /boot/config.txt
sudo raspi-config nonint do_serial 1
```

Add `dtoverlay=pi3-miniuart-bt` to your `/boot/config.txt`

## Sensor Data

The add-on reads the following measurements from the PM5003 sensor:

- **PM1.0** - Particulate matter ≤1.0μm (μg/m³)
- **PM2.5** - Particulate matter ≤2.5μm (μg/m³)
- **PM10** - Particulate matter ≤10μm (μg/m³)
- **PM1.0 ATM** - PM1.0 atmospheric environment reading
- **PM2.5 ATM** - PM2.5 atmospheric environment reading
- **PM10 ATM** - PM10 atmospheric environment reading

## License

MIT License
