"""Flask application for payment processing."""

from flask import Flask, jsonify, request
from marshmallow import Schema, fields

app = Flask(__name__)


class PaymentSchema(Schema):
    amount = fields.Float(required=True)
    currency = fields.Str(required=True)
    merchant_id = fields.Str(required=True)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/payments", methods=["POST"])
def create_payment():
    schema = PaymentSchema()
    data = schema.load(request.get_json())
    return jsonify({"payment_id": "pay-001", **data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
