from flask import Blueprint, render_template, request, redirect, url_for
from controllers.tarefa_controller import TarefaController

tarefa_bp = Blueprint('tarefa', __name__)
controller = TarefaController()

@tarefa_bp.route('/')
def index():
    status_filtro = request.args.get('status', 'todas')
    tarefas = controller.listar_tarefas()

    if status_filtro == 'pendentes':
        tarefas_filtradas = [t for t in tarefas if not t.concluida]
    elif status_filtro == 'concluidas':
        tarefas_filtradas = [t for t in tarefas if t.concluida]
    else:
        tarefas_filtradas = tarefas

    return render_template('index.html', tarefas=tarefas_filtradas, status_filtro=status_filtro)

@tarefa_bp.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao')
    if descricao:
        controller.adicionar_tarefa(descricao)
    return redirect(url_for('tarefa.index'))

@tarefa_bp.route('/remover/<int:id_tarefa>', methods=['POST', 'GET'])
def remover(id_tarefa):
    controller.remover_tarefa(id_tarefa)
    return redirect(url_for('tarefa.index'))

@tarefa_bp.route('/concluir/<int:id_tarefa>', methods=['POST', 'GET'])
def concluir(id_tarefa):
    controller.concluir_tarefa(id_tarefa)
    return redirect(url_for('tarefa.index'))
