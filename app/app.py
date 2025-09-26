from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Let's make the page a bit more fancy!
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Workshop App</title>
        <style>
            body {
                background: linear-gradient(to right, #2c3e50, #4ca1af);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                flex-direction: column;
            }
            h1 {
                font-size: 4rem;
                margin-bottom: 0;
            }
            p {
                font-size: 1.5rem;
                margin-top: 10px;
            }
            .version {
                position: absolute;
                bottom: 10px;
                right: 10px;
                font-size: 1rem;
                color: #f0f0f0;
                background-color: rgba(0,0,0,0.3);
                padding: 5px 10px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Success!</h1>
            <p>Hello From DevOps Workshop.</p>
        </div>
        <div class="version">
            Version 1.0
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # The port is mapped by ECS, so we just run on the container's port 5000
    app.run(host='0.0.0.0', port=5000) 