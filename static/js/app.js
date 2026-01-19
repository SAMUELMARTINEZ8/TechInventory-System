// Esperar a que la página cargue
document.addEventListener('DOMContentLoaded', () => {
    cargarProductos();
});

// 1. FUNCIÓN: Cargar productos desde Python
async function cargarProductos() {
    try {
        const respuesta = await fetch('/api/productos');
        const productos = await respuesta.json();
        
        const tabla = document.getElementById('tablaProductos');
        tabla.innerHTML = ''; // Limpiar tabla

        productos.forEach(prod => {
            const fila = `
                <tr>
                    <td>#${prod.id}</td>
                    <td><strong>${prod.nombre}</strong></td>
                    <td><span style="color: #00f3ff">${prod.categoria}</span></td>
                    <td>$${prod.precio}</td>
                    <td>${prod.stock} unid.</td>
                </tr>
            `;
            tabla.innerHTML += fila;
        });
    } catch (error) {
        console.error('Error cargando inventario:', error);
    }
}

// 2. FUNCIÓN: Guardar nuevo producto
document.getElementById('techForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que la página se recargue

    // Capturamos los datos del formulario
    const nuevoProducto = {
        nombre: document.getElementById('nombre').value,
        categoria: document.getElementById('categoria').value,
        precio: parseFloat(document.getElementById('precio').value),
        stock: parseInt(document.getElementById('stock').value)
    };

    // Enviamos a Python (Backend)
    const respuesta = await fetch('/api/productos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevoProducto)
    });

    if (respuesta.ok) {
        alert('✅ Equipo registrado en el sistema');
        document.getElementById('techForm').reset(); // Limpiar formulario
        cargarProductos(); // Recargar la tabla automáticamente
    } else {
        alert('❌ Hubo un error al guardar');
    }
});
