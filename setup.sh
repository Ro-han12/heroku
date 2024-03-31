#!/bin/bash

# Create directory for Streamlit configuration if it doesn't exist
mkdir -p ~/.streamlit/

# Create Streamlit config file
echo "[general]" > ~/.streamlit/config.toml
echo "email = \"your-email@domain.com\"" >> ~/.streamlit/config.toml

# Create Streamlit server config file (if st_app directory exists)
if [ -d "~/st_app" ]; then
    echo "[server]" > ~/st_app/config.toml
    echo "headless = true" >> ~/st_app/config.toml
    echo "enableCORS = false" >> ~/st_app/config.toml
    echo "port = $PORT" >> ~/st_app/config.toml
fi
