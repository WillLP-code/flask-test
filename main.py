from website import create_app # Website has an init file so is a package

app = create_app()

# Starts the app, makes a webserver
if __name__ == '__main__': 
    # Debug reruns when we make changes
    app.run(debug=True)