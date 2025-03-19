# Classe base Produto
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def exibir_detalhes(self):
        return f"Nome: {self.nome}, Preço: {self.preco}, Estoque: {self.estoque} unidades"

# Classe Livro herdando de Produto
class Livro(Produto):
    def __init__(self, nome, preco, estoque, autor, isbn):
        super().__init__(nome, preco, estoque)
        self.autor = autor
        self.isbn = isbn
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Autor: {self.autor}, ISBN: {self.isbn}"

# Classe Eletronico herdando de Produto
class Eletronico(Produto):
    def __init__(self, nome, preco, estoque, marca, garantia):
        super().__init__(nome, preco, estoque)
        self.marca = marca
        self.garantia = garantia
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Marca: {self.marca}, Garantia: {self.garantia} meses"

# Classe Vestuario herdando de Produto
class Vestuario(Produto):
    def __init__(self, nome, preco, estoque, tamanho, material):
        super().__init__(nome, preco, estoque)
        self.tamanho = tamanho
        self.material = material
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Tamanho: {self.tamanho}, Material: {self.material}"

# Exemplo de uso
dados_livro = Livro("O Senhor dos Anéis", 39.90, 10, "J.R.R. Tolkien", "978-3-16-148410-0")
dados_eletronico = Eletronico("Smartphone X", 1999.99, 5, "TechBrand", 12)
dados_vestuario = Vestuario("Jaqueta de Couro", 299.99, 2, "M", "Couro legítimo")

print(dados_livro.exibir_detalhes())
print(dados_eletronico.exibir_detalhes())
print(dados_vestuario.exibir_detalhes())