from flask import Flask, jsonify, request

app = Flask(__name__)

shipment = {
"12345": {"status": "Sedang dikirim", "kurir": "JNE", "tujuan": "Jakarta"},
"67890": {"status": "Diterima", "kurir": "SiCepat", "tujuan": "Bandung"},
}

@app.route('/status/<tracking_id>', methods=['GET'])
def get_status(tracking_id):
    if tracking_id in shipment:
        return jsonify({"tracking_id":tracking_id, **shipment[tracking_id]})
    else:
        return jsonify({"error": "Tracking ID tidak ditemukan"}), 404

# endpoint untuk menambahkan pengiriman baru
@app.route('/add_shipment', methods=['POST'])
def add_shipment():
    data = request.json
    tracking_id = data.get('tracking_id')
    if not tracking_id or tracking_id in shipment:
        return jsonify({"error": "Tracking ID sudah ada atau tidak valid"}), 400

    shipment[tracking_id] = {
        "status": data.get('status', "dalam proses"),
        "kurir": data.get('kurir', "Tidak diketahui"),
        "tujuan": data.get('tujuan', "Tidak diketahui")
    }

    return jsonify({"message": "Pengiriman berhasil ditambahkan", "data": shipment[tracking_id]}), 201

# Endpoint untuk memperbarui status pengiriman
@app.route('/update_status/<tracking_id>', methods=['PUT'])
def update_status(tracking_id):
    if tracking_id not in shipment:
        return jsonify({"error": "Tracking ID tidak ditemukan"}), 404

    data = request.json
    shipment[tracking_id]["status"] = data.get("status", shipment[tracking_id]["status"])
    return jsonify({"message": "Status diperbarui", "data": shipment[tracking_id]})

# Endpoint untuk menghapus pengiriman berdasarkan tracking_id
@app.route('/delete_shipment/<tracking_id>', methods=['DELETE'])
def delete_shipment(tracking_id):
    if tracking_id in shipment:
        del shipment[tracking_id]
        return jsonify({"message": "Pengiriman berhasil dihapus"}), 200
    else:
        return jsonify({"error": "Tracking ID tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)