<template>
    <div class="home">
        <h1>Bienvenido a la Gestión de Inventario</h1>
        <nav>
            <router-link to="/add-product">Insertar Producto Nuevo</router-link>
        </nav>
        <nav>
            <router-link to="/product-list">Lista de productos y transacciones (Ingresar o retirar inventario)</router-link>
        </nav>
        <p>Utiliza los enlaces de arriba para navegar.</p>
    </div>
</template>

<script>
export default {
    name: 'Home',
};
</script>

<style scoped>
.home {
    text-align: center;
    margin: 20px;
}

nav {
    margin: 20px 0;
}

nav a {
    margin: 0 10px;
    text-decoration: none;
    color: blue;
}
</style>