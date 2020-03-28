from app import create_app

app = create_app()

# This is only a test!

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
