ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python and required system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    python3-dev \
    gcc \
    musl-dev \
    linux-headers \
    jq

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies in virtual environment
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

# Copy application files
COPY pm5003_reader.py /pm5003_reader.py
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
