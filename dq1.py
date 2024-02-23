#books as resource

class Book(models.Model):
    @app.route('/')
    def index():
        #SQL SELECT * FROM Books
        pass
    
    @app.route('/books')
    def get(self):
        #SELECT * FROM Books WHERE id = :id
        pass

    @app.route('/books')
    def post(self):
        #INSERT INTO books (column) VALUES (values)
        pass
    
    @app.route('/books/<int:id>')
    def patch(self):
        #UPDATE Books SET column_name = value WHERE id = :id
        pass
    
    @app.route('/books/<int:id>')
    def delete(self):
        #DELETE FROM table_name WHERE some_column=some_value
        pass