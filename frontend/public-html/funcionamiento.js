// Datos de ejemplo para la solicitud POST
const data = {
  algorithm: 'FIFO',  // O 'SSTF', 'SCAN', 'C-SCAN', 'LOOK', 'C-LOOK'
  requests: [30, 60, 10, 70],
  start: 50,
  direction: 'right',  // 'left' o 'right'
  max_track: 200
};

// Realizar la solicitud POST
fetch('http://localhost:8000/api/disk-scheduling', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())  // Convierte la respuesta a JSON
  .then(responseData => {
    console.log('Total head movement:', responseData.total_head_movement);
    // Aquí puedes actualizar el frontend con el resultado
  })
  .catch(error => console.error('Error:', error));



document.getElementById("myForm").addEventListener("submit", function(e) {
    e.preventDefault();  // Evita el envío tradicional del formulario

    const data = {
        algorithm: 'FIFO',
        requests: [30, 60, 10, 70],
        start: 50,
        direction: 'right',
        max_track: 200
    };

    fetch('http://localhost:8000/api/disk-scheduling', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Resultado:', data);
        // Mostrar los resultados en el frontend
    })
    .catch(error => console.error('Error:', error));
});
