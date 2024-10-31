<template>
    <div id="app">
        <header>
            <h1>Aplicación de Inventario</h1>
        </header>
        <main>
            <router-view></router-view>
        </main>
    </div>
</template>

<script>
export default {
    name: 'App',
};
</script>

<style>
header {
    background-color: #f8f9fa;
    padding: 20px;
    text-align: center;
}

main {
    padding: 20px;
}
</style>