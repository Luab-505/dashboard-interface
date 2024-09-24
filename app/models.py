from . import db
from datetime import datetime

# Modelo de Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    historico_compras = db.Column(db.Text)

    def __repr__(self):
        return f'<Cliente {self.nome}>'

# Modelo de Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catalogo = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    metrica = db.Column(db.String(50), nullable=False)  # Ex: pç, metro linear, m2
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200))

    def __repr__(self):
        return f'<Produto {self.nome}>'

# Modelo de Orçamento
class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    taxa_entrega = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Ex: Pendente, Finalizado
    arquivo_pdf = db.Column(db.String(200))  # Link para o PDF gerado do orçamento
    cliente = db.relationship('Cliente', backref='orcamentos', lazy=True)

    def __repr__(self):
        return f'<Orcamento {self.id}>'

# Modelo de Venda
class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Ex: Pago, Pendente
    cliente = db.relationship('Cliente', backref='vendas', lazy=True)

    def __repr__(self):
        return f'<Venda {self.id}>'

# Modelo de FAQ
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(300), nullable=False)
    resposta = db.Column(db.Text, nullable=False)
    arquivo = db.Column(db.String(200))  # Arquivos como PDFs ou imagens

    def __repr__(self):
        return f'<FAQ {self.pergunta}>'
