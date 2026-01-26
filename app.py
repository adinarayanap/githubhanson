cat > app.py <<'EOF'
def start():
    print("App started")

def config():
    print("Loading config")

def run():
    start()
    config()
    print("Running app")

run()
EOF

