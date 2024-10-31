from app import create_app

#Inicializo Flask corriendo en el puerto 5000 por default
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)