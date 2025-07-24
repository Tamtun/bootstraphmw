from flask import Flask, Response

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def return_contacts(path):
    try:
        with open('contacts.html', encoding='utf-8') as f:
            html_content = f.read()
        return Response(html_content, content_type='text/html')
    except FileNotFoundError:
        return Response('<h1>Файл contacts.html не найден</h1>', status=404, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)
