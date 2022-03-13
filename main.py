import webbrowser
from app import app

if __name__ == "__main__":
    webbrowser.open("http://localhost:3000/")
    app.run(port = 3000, debug = True, use_reloader=False)
