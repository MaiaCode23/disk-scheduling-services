from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#SSTF
def sstf(requests, start):
    total_head_movement = 0
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - start))
        total_head_movement += abs(closest_request - start)
        start = closest_request
        requests.remove(closest_request)
    return total_head_movement


#SCAN
def scan(requests, start, direction, max_track):
    total_head_movement = 0
    requests.sort()
    if direction == "left":
        requests = [x for x in requests if x <= start] + [x for x in requests if x > start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
    elif direction == "right":
        requests = [x for x in requests if x >= start] + [x for x in requests if x < start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
    return total_head_movement


#C-SCAN
def cscan(requests, start, direction, max_track):
    total_head_movement = 0
    requests.sort()
    if direction == "left":
        requests = [x for x in requests if x <= start] + [x for x in requests if x > start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
        total_head_movement += start  # volver al principio
        start = 0  # Regresa al principio del disco
    elif direction == "right":
        requests = [x for x in requests if x >= start] + [x for x in requests if x < start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
        total_head_movement += (max_track - start)  # Regresar al final
        start = max_track
    return total_head_movement


#LOOK
def look(requests, start, direction):
    total_head_movement = 0
    requests.sort()
    if direction == "left":
        requests = [x for x in requests if x <= start] + [x for x in requests if x > start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
    elif direction == "right":
        requests = [x for x in requests if x >= start] + [x for x in requests if x < start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
    return total_head_movement


#C-LOOK
def clook(requests, start, direction):
    total_head_movement = 0
    requests.sort()
    if direction == "left":
        requests = [x for x in requests if x <= start] + [x for x in requests if x > start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
        start = min(requests)  # Vuelve al inicio
    elif direction == "right":
        requests = [x for x in requests if x >= start] + [x for x in requests if x < start]
        for request in requests:
            total_head_movement += abs(request - start)
            start = request
        start = max(requests)  # Regresa al final
    return total_head_movement
    

#FUNCIÓN GENERAL
def disk_scheduling_algorithm(algorithm, requests, start, direction="right", max_track=200):
    if algorithm == "SSTF":
        return sstf(requests, start)
    elif algorithm == "SCAN":
        return scan(requests, start, direction, max_track)
    elif algorithm == "C-SCAN":
        return cscan(requests, start, direction, max_track)
    elif algorithm == "LOOK":
        return look(requests, start, direction)
    elif algorithm == "C-LOOK":
        return clook(requests, start, direction)
    elif algorithm == "FIFO":
        return fifo(requests, start)
    else:
        return {"error": "Unknown algorithm"} 
        

# Endpoint que manejará las solicitudes desde el frontend
@app.route('/api/disk-scheduling', methods=['POST'])
def handle_disk_scheduling():
    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON expected"}), 400
    
    data = request.get_json()

    # Verificación de los parámetros en el JSON
    if 'algorithm' not in data or 'requests' not in data:
        return jsonify({"error": "Missing required fields: 'algorithm' and 'requests'"}), 400
    
    algorithm = data['algorithm']
    requests = data['requests']
    start = data.get('start', 0)  # Valor por defecto para 'start' si no se especifica
    direction = data.get('direction', 'right')  # Dirección por defecto
    max_track = data.get('max_track', 200)  # Valor por defecto de 'max_track'

    # Ejecuta el algoritmo seleccionado
    result = disk_scheduling_algorithm(algorithm, requests, start, direction, max_track)
    
    # Devuelve la respuesta en formato JSON
    return jsonify({"total_head_movement": result})

# Si ejecutas el script directamente
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

