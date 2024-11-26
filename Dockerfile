# Stage 1: Build
FROM python:3.11-alpine AS build

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    freetype-dev \
    libpng-dev \
    openblas-dev

# Install Python dependencies
RUN pip install --no-cache-dir pypistats matplotlib pandas

# Copy the Python script into the build image
COPY chart.py /chart.py

# Stage 2: Final
FROM python:3.11-alpine

# Install runtime dependencies
RUN apk add --no-cache \
    libstdc++ \
    freetype \
    libpng \
    openblas

# Copy necessary files from the build stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /chart.py /chart.py

# Set the working directory
WORKDIR /

# Entry point to run the script with arguments
ENTRYPOINT ["python", "chart.py"]
