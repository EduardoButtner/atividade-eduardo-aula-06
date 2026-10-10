from models.tarefa import Tarefa

class TarefaController:
    def __init__(self):
        self.tarefas = []
        self._proximo_id = 1

    def adicionar_tarefa(self, descricao: str):
        if descricao and descricao.strip():
            tarefa = Tarefa(self._proximo_id, descricao.strip())
            self.tarefas.append(tarefa)
            self._proximo_id += 1

    def listar_tarefas(self):
        return self.tarefas

    def remover_tarefa(self, id_tarefa: int):
        self.tarefas = [t for t in self.tarefas if t.id != id_tarefa]

    def concluir_tarefa(self, id_tarefa: int):
        for t in self.tarefas:
            if t.id == id_tarefa:
                t.marcar_como_concluida()
                break
