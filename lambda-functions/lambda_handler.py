def lambda_handler(event, context):
    # This lambdda is just returning HTML that prints a simple hello world if rendered
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
        "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = """<html>
    <head>
    <title>Hello World!</title>
    <style>
    html, body {
    margin: 0; padding: 0;
    font-family: arial; font-weight: 700; font-size: 3em;
    text-align: center;
    }
    </style>
    </head>
    <body>
    <p>Hello World!</p>
    </body>
    </html>"""
    return response