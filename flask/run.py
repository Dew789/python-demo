import json
import traceback

from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/test', methods=['POST'])
def compare_v3():
    try:
        score = "100"
    except Exception as e:
        traceback.print_exc()
        return str(e), 500

    result = {"data": score}

    return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
