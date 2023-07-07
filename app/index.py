from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  values = {"name":"Tamako"}
  return render_template('index.html', data=values)



@app.route("/test")
def test():
  values = {"message":"Hello! This is test page."}
  return render_template('test.html', data=values)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)