from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


# Inject 'enumerate' into Jinja environment.
@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


@app.route('/')
def index():
    # return "What up!?"
    return render_template('index.html', headers=dict(request.headers), dt=datetime.now())
    # req = dict(request.headers)
    # headerData = f"<h1>As of {datetime.now()}</h1><h2>Headers</h2><table>"

    # for i, (k, v) in enumerate(req.items()):
    #     i = i
    #     headerData += f"<tr><td>{k}</td><td>{v}</td></tr>"

    # return f"{headerData}</table><h2>Raw Data</h2>{str(req)}"


if __name__ == '__main__':
    app.run()