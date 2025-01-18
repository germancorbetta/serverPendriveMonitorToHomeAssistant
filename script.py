from flask import Flask, jsonify
import os
import shutil

app = Flask(__name__)

# Listen to /pendrive
# Listen to GET operation
@app.route('/pendrive', methods=['GET'])
def get_pendrive_usage():
    mount_path = '/mnt/pendrive'

    # Check if the pendrive is mounted
    if not os.path.ismount(mount_path):
        return jsonify({"error": "Pendrive is not mounted at /mnt/pendrive"}), 400

    # Get disk usage statistics
    try:
        total, used, free = shutil.disk_usage(mount_path)
        usage_percent = (used / total) * 100

        return jsonify({
            "total": total,
            "used": used,
            "free": free,
            "usage_percent": round(usage_percent, 2)
        }), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run and listen to localhost:5590
# Port 5590
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5590)