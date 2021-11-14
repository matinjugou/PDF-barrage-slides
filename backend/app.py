from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

barrage_pools = {}

@app.route("/")
def helloWorld():
  return "Hello!"

@app.route("/send", methods=['POST'])
def send_barrage():
    channel = request.form.get('channel', '')
    message = request.form.get('message', '')
    color = request.form.get('color', '')
    if barrage_pools.get(channel, None) is None:
        barrage_pools[channel] = []
    barrage_pools[channel].append({
        'message': message,
        'color': color,
    })
    return make_response(jsonify({'message': f"Add message to channel: {channel}"}))


@app.route("/clean", methods=['POST'])
def clean_barrage():
    channel = request.form.get('channel', '')
    if barrage_pools.get(channel, None) is not None:
        del barrage_pools[channel]
    return make_response(jsonify({'message': f'Clean out messages in channel: {channel}'}))

@app.route("/get", methods=['GET'])
def get_barrage():
    channel = request.args.get('channel', '')
    index = int(request.args.get('index', 0))
    res = barrage_pools.get(channel, [])
    return make_response(jsonify(res[index:]))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)