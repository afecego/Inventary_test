<template>
    <div>
        <h3>Listado de Productos</h3>
        <table class="product-table">
            <thead>
                <tr>
                    <th>Producto</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in products" :key="product.nombre">
                    <td>{{ product.name }}</td>
                    <td colspan="4">
                        <table class="inner-table">
                            <thead>
                                <tr>
                                    <th>Cantidad Disponible</th>
                                    <th>Estado</th>
                                    <th>Fecha de Vencimiento</th>
                                    <th>Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="status in product.status" :key="status.status">
                                    <td>{{ status.cantidad_disponible }}</td>
                                    <td>{{ status.estado }}</td>
                                    <td>{{ status.fecha_vencimiento }}</td>
                                    <td>
                                        <button @click="addQuantity(status.product_id)">
                                            Ingreso inventario
                                        </button>
                                        <button @click="removeQuantity(status.id_entry, status.cantidad_disponible)">
                                            Salida inventario
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return { products: [] };
    },
    async mounted() {
        this.fetchProducts();
    },
    methods: {
        async fetchProducts() {
            try {
                const response = await axios.get('/api/products/list');
                this.products = response.data;
            } catch (error) {
                console.error("Error al cargar los productos:", error);
            }
        },
        async removeQuantity(entryId, availableQuantity) {
            const quantityToRemove = prompt(`Ingresa la cantidad a restar (máximo ${availableQuantity}):`);
            if (quantityToRemove === null) return;
            const quantity = parseInt(quantityToRemove);
            if (isNaN(quantity) || quantity <= 0) {
                alert("Por favor, ingresa un número válido mayor a 0.");
                return;
            }
            if (quantity > availableQuantity) {
                alert(`No puedes restar más que la cantidad disponible (${availableQuantity}).`);
                return;
            }
            try {
                await axios.post(`/api/inventory/exit`, {
                    data: { entry_id: entryId, quantity: quantity }
                });
                this.fetchProducts();
            } catch (error) {
                console.error("Error al eliminar la cantidad:", error);
            }
        },
        async addQuantity(product_id) {
            const quantity = prompt(`Ingresa la cantidad a ingresar:`);
            const expire_date = prompt(`Ingresa la fecha de vencimiento (formato: YYYY-MM-DD):`);
            if (quantity === null) return;

            if (expire_date === null) return;

            if (isNaN(quantity) || quantity <= 0) {
                alert("Por favor, ingresa un número válido mayor a 0.");
                return;
            }
            const datePattern = /^\d{4}-\d{2}-\d{2}$/; // Formato: YYYY-MM-DD
            if (!datePattern.test(expire_date)) {
                alert("La fecha ingresada no es válida. Debe estar en formato YYYY-MM-DD.");
                return;
            }

            // Convertir la cadena de fecha a un objeto Date
            const date = new Date(expire_date);
            if (isNaN(date.getTime())) {
                alert("La fecha ingresada no es válida. Por favor, intenta de nuevo.");
                return;
            }

            // Formatear la fecha al formato deseado
            const formattedExpireDate = date.toISOString().split('T')[0];

            try {
                console.log("hola")
                await axios.post(`/api/inventory/entry`, {
                    data: { product_id: product_id, quantity: quantity, expiration_date: expire_date}
                });
                this.fetchProducts();
            } catch (error) {
                console.error("Error al eliminar la cantidad:", error);
            }
        }
    }
};
</script>

<style scoped>
.product-table, .inner-table {
    width: 100%;
    border: 1px solid #ddd; /* Estilo de borde */
}

.product-table th, .inner-table td {
    text-align: left; /* Alineación a la izquierda para los encabezados y datos */
    padding: 8px; /* Espaciado interno */
    border: 1px solid #ddd; /* Estilo de borde */
}

/* Establecer un ancho específico a las celdas de la tabla interna */
.inner-table td {
    border: 1px solid #ddd; /* Estilo de borde */
    width: calc(100% / 4); /* Divide el ancho en partes iguales */
}

</style>