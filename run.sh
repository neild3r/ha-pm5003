#!/usr/bin/env bash
set -e

CONFIG_PATH=/data/options.json

# Read configuration options
DEVICE=$(jq -r '.device' $CONFIG_PATH)
BAUDRATE=$(jq -r '.baudrate' $CONFIG_PATH)
POLL_INTERVAL=$(jq -r '.poll_interval' $CONFIG_PATH)

echo "Starting PM5003 sensor add-on..."
echo "Device: ${DEVICE}"
echo "Baudrate: ${BAUDRATE}"
echo "Poll interval: ${POLL_INTERVAL} seconds"

# Activate virtual environment and run Python script
source /opt/venv/bin/activate
python3 /pm5003_reader.py --device "${DEVICE}" --baudrate "${BAUDRATE}" --poll-interval "${POLL_INTERVAL}"
