from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
babel = Babel(app)

stories = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_language/<language>')
def set_language(language):
    app.config['BABEL_DEFAULT_LOCALE'] = language
    return redirect(url_for('home'))

@app.route('/avoir_18_ans', methods=['POST'])
def avoir_18_ans():
    data = request.form
    if 'story' in data:
        story = data['story']
        stories.append(story)
        return render_template('thanks.html', message=_("Your story has been successfully submitted!"))
    else:
        return render_template('error.html', message=_("Error: Please provide your story.")), 400

@babel.localeselector
def get_locale():
    return app.config['BABEL_DEFAULT_LOCALE']

if __name__ == '__main__':
    app.run(debug=True)
