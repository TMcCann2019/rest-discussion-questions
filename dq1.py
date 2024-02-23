#books as resource

class Book(models.Model):
    @app.route('/')
    def index():
        #SQL SELECT * FROM Books
        pass
    
    @app.route('/books')
    def get(self):
        #SELECT * FROM Books
        pass

    @app.route('/books')
    def post(self):
        #CREATE INDEX index_name ON table_name (column_name)
        pass
    
    @app.route('/books/<int:id>')
    def patch(self):
        #UPDATE Books SET column_name
        pass
    
    @app.route('/books/<int:id>')
    def delete(self):
        #DELETE FROM table_name WHERE some_column=some_value
        pass