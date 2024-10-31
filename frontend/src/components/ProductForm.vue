<template>
    <div class="form-container">
        <h3>Crear Producto</h3>
        <form @submit.prevent="createProduct">
            <fieldset>
                <div class="form-group">
                    <label for="nombre">Nombre</label>
                    <input
                        v-model="nombre"
                        id="nombre"
                        placeholder="Nombre"
                        class="form-input"
                        required
                    />
                </div>
                <div class="form-group">
                    <label for="descripcion">Descripción</label>
                    <textarea
                        v-model="descripcion"
                        id="descripcion"
                        placeholder="Descripción"
                        class="form-input"
                        required
                    ></textarea>
                </div>
                <div class="form-group">
                    <button type="submit" class="form-button">Agregar Producto</button>
                </div>
            </fieldset>
        </form>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return { nombre: '', descripcion: '' };
    },
    methods: {
        async createProduct() {
            await axios.post('/api/products', { name: this.nombre, description: this.descripcion });
            this.nombre = '';
            this.descripcion = '';
        }
    }
};
</script>
<style>
.form-container {
    max-width: 400px; /* Ancho máximo del formulario */
    margin: 20px auto; /* Centrando el formulario */
    padding: 20px;
    border: 1px solid #ccc; /* Borde para el formulario */
    border-radius: 8px; /* Bordes redondeados */
    background-color: #f9f9f9; /* Color de fondo más claro */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Sombra para resaltar */
}

h3 {
    text-align: center; /* Centrar el título */
    margin-bottom: 20px; /* Espacio debajo del título */
}

.form-group {
    margin-bottom: 15px; /* Espacio entre los campos del formulario */
}

label {
    display: block; /* Mostrar la etiqueta como bloque */
    margin-bottom: 5px; /* Espacio debajo de la etiqueta */
    font-weight: bold; /* Hacer la etiqueta más visible */
}

.form-input {
    width: 100%; /* Ancho completo para los campos de entrada */
    padding: 10px; /* Espaciado interno */
    border: 1px solid #ccc; /* Borde para los campos */
    border-radius: 4px; /* Bordes redondeados */
    box-sizing: border-box; /* Para incluir el padding y borde en el ancho total */
}

.form-button {
    width: 100%; /* Ancho completo para el botón */
    padding: 10px; /* Espaciado interno */
    background-color: #007bff; /* Color de fondo del botón */
    color: white; /* Color del texto del botón */
    border: none; /* Sin borde */
    border-radius: 4px; /* Bordes redondeados */
    cursor: pointer; /* Cambiar cursor al pasar sobre el botón */
    font-size: 16px; /* Tamaño de fuente del botón */
}

.form-button:hover {
    background-color: #0056b3; /* Color más oscuro al pasar el ratón */
}

</style>
