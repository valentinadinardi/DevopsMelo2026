from flask import Flask, jsonify, render_template
import routeros_api

app = Flask(__name__)

ROUTER = {
    "host": "192.168.88.1",
    "username": "admin",
    "password": "admin",
    "port": 8728,
}


def get_router_data():
    connection = None
    try:
        connection = routeros_api.RouterOsApiPool(
            ROUTER["host"],
            username=ROUTER["username"],
            password=ROUTER["password"],
            port=ROUTER["port"],
            plaintext_login=True,
        )
        api = connection.get_api()

        interfaces = api.get_resource('/interface').get()
        system_info = api.get_resource('/system/resource').get()
        info = system_info[0] if system_info else {}

        return {
            "ok": True,
            "interfaces": [
                {
                    "name": interface.get("name", "Sin nombre"),
                    "running": interface.get("running", "false") in (True, "true", "yes"),
                    "disabled": interface.get("disabled", "false") in (True, "true", "yes"),
                    "type": interface.get("type", "-"),
                    "mtu": interface.get("actual-mtu", interface.get("mtu", "-")),
                }
                for interface in interfaces
            ],
            "system": {
                "cpu_load": info.get("cpu-load", 0),
                "free_hdd_space": info.get("free-hdd-space", 0),
                "total_hdd_space": info.get("total-hdd-space", 0),
                "total_memory": info.get("total-memory", 0),
                "free_memory": info.get("free-memory", 0),
                "version": info.get("version", "-"),
                "uptime": info.get("uptime", "-"),
                "board_name": info.get("board-name", "-"),
                "cpu": info.get("cpu", "-"),
            },
        }
    except Exception as exc:
        return {"ok": False, "error": str(exc)}
    finally:
        if connection:
            connection.disconnect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/status')
def status():
    data = get_router_data()
    return jsonify(data), 200 if data.get("ok") else 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)