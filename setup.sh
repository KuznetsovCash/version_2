

mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $port
enableCORS = false

" > ~/.streamlit/config.toml

