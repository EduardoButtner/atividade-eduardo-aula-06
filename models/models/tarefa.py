class Tarefa:
    def __init__(self, id_tarefa: int, descricao: str, concluida: bool = False):
        self.id = id_tarefa
        self.descricao = descricao
        self.concluida = concluida

    def marcar_como_concluida(self):
        self.concluida = True

    def atualizar_descricao(self, nova_descricao: str):
        self.descricao = nova_descricao
