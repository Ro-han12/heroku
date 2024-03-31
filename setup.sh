# Create directory for Streamlit configuration if it doesn't exist
mkdir -p ~/.streamlit/

# Create Streamlit config file
cat <<EOT > ~/.streamlit/config.toml
[general]
EOT

# Create Streamlit server config file (if st_app directory exists)
if [ -d "~/st_app" ]; then
    cat <<EOT > ~/st_app/config.toml
[server]
headless = true
enableCORS = false
port = $PORT
EOT
fi
