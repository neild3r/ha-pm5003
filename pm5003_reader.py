#!/usr/bin/env python3
"""PM5003 Sensor Reader for Home Assistant.

This script reads particulate matter data from a Pimoroni PM5003 sensor
and outputs it in a format that Home Assistant can consume.
"""

import argparse
import json
import sys
import time

from pms5003 import PMS5003


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Read PM5003 particulate matter sensor data"
    )
    parser.add_argument(
        "--device",
        default="/dev/ttyAMA0",
        help="Serial device path (default: /dev/ttyAMA0)",
    )
    parser.add_argument(
        "--baudrate",
        type=int,
        default=9600,
        help="Serial baudrate (default: 9600)",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=10,
        help="Polling interval in seconds (default: 10)",
    )
    parser.add_argument(
        "--pin-enable",
        default="GPIO22",
        help="Enable pin",
    )
    parser.add_argument(
        "--pin-reset",
        default="GPIO27",
        help="Reset pin",
    )

    return parser.parse_args()


def read_sensor(pms5003):
    """Read data from the PM5003 sensor.

    Args:
        pms5003: PMS5003 sensor instance.

    Returns:
        dict: Sensor readings or None if read failed.
    """
    try:
        data = pms5003.read()
        return {
            "pm1_0": data.pm_ug_per_m3(1.0),
            "pm2_5": data.pm_ug_per_m3(2.5),
            "pm10": data.pm_ug_per_m3(10),
            "pm1_0_atm": data.pm_ug_per_m3(1.0, atmospheric_environment=True),
            "pm2_5_atm": data.pm_ug_per_m3(2.5, atmospheric_environment=True),
            "pm10_atm": data.pm_ug_per_m3(10, atmospheric_environment=True),
        }
    except Exception as e:
        print(f"Error reading sensor: {e}", file=sys.stderr)
        return None


def main():
    """Main entry point."""
    args = parse_args()

    print(f"Initializing PM5003 sensor on {args.device} at {args.baudrate} baud...")

    try:
        pms5003 = PMS5003(device=args.device, baudrate=args.baudrate, pin_enable=args.pin_enable, pin_reset=args.pin_reset)
    except Exception as e:
        print(f"Failed to initialize sensor: {e}", file=sys.stderr)
        sys.exit(1)

    print("Sensor initialized. Starting continuous readings...")

    while True:
        readings = read_sensor(pms5003)
        if readings:
            print(json.dumps(readings))
        time.sleep(args.poll_interval)


if __name__ == "__main__":
    main()
