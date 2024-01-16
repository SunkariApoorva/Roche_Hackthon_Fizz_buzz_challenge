from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)

request_counter = Counter()

def fizz_buzz(int1, int2, limit, str1, str2):
    result = []
    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            result.append(str1 + str2)
        elif i % int1 == 0:
            result.append(str1)
        elif i % int2 == 0:
            result.append(str2)
        else:
            result.append(str(i))
    return result

@app.route('/fizzbuzz', methods=['GET'])
def fizz_buzz_endpoint():
    int1 = int(request.args.get('int1', 3))
    int2 = int(request.args.get('int2', 5))
    limit = int(request.args.get('limit', 100))
    str1 = request.args.get('str1', 'fizz')
    str2 = request.args.get('str2', 'buzz')

    result = fizz_buzz(int1, int2, limit, str1, str2)

    # Increment request counter
    request_counter[(int1, int2, limit, str1, str2)] += 1

    return jsonify(result)

@app.route('/statistics', methods=['GET'])
def statistics_endpoint():
    most_used_request = request_counter.most_common(1)
    if most_used_request:
        params, hits = most_used_request[0]
        return jsonify({
            'parameters': {
                'int1': params[0],
                'int2': params[1],
                'limit': params[2],
                'str1': params[3],
                'str2': params[4]
            },
            'hits': hits
        })
    else:
        return jsonify({'message': 'No requests yet'})

if __name__ == '__main__':
    app.run(debug=True)
