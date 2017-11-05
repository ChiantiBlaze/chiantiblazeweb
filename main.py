from flask import Flask, render_template, request

app = Flask(__name__, static_folder='./static', template_folder='./static')

@app.route('/')
def main():
	return render_template('main.html')



if __name__ == "__main__":
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=80, threaded=True)