from flask import jsonify


def success(data, status=200):
    return jsonify({"data": data}), status


def error(message, status=400):
    return jsonify({"error": message}), status
