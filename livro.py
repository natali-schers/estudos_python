class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

livro = Livro("1984", "George Orwell")

print(livro.titulo)
print(livro.autor) 

livro.titulo = "Animal Farm";
livro.autor = "Orwell";

print(livro.titulo)
print(livro.autor)