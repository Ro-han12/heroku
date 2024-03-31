mkdir -p ~/.streamlit/

echo "/
[general]\n\
email=\"your-email@domain.com\"\n\
" > ~/.streamlit/config.tom

echo "/
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/st_app/config.toml