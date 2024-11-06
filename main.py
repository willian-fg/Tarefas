import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_heigth = 450
        self.page.window_resizable = True
        self.page.window_always_on_top = True
        self.page.title = 'ToDo '
        self.task = ''
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name, status)')
        self.results = self.db_execute('SELECT *FROM tasks')
        self.main_page()

    #Banco de Dados
    def db_execute(self, query, params = []):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()

    #Container das tarefas 
    def task_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content = ft.Column(
                controls = [
                    ft.Checkbox(label=res[0], value = True if res[1] == 'complete' else False)
                    for res in self.results if res
                ]
            )

        )
    
    def set_value(self, e):
        self.task = e.control.value
        print(self.task)

    #Função para adicionar tarefas
    def add(self, e, input_tasks ):
       name = self.task
       status = 'incompleto'

       if name:
           self.db_execute(
               query="INSERT INTO tasks VALUES (?, ?)",
               params=[name, status])
           
           input_tasks.value = ''
           self.results = self.db_execute('SELECT *FROM tasks')
           self.update_task_list()

    def update_task_list(self):
        tasks = self.task_container()
        self.page.controls.pop()
        self.page.add(tasks)
        self.page.update()

    def main_page(self):

        # Adicionar tarefas -------
        input_task = ft.TextField(
            hint_text = 'Digite sua tarefa aqui',
              expand=True,
              on_change=self.set_value 
              ) #Local de escrever

        input_bar = ft.Row( #Botão de adcionar
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=lambda e:self.add(e, input_task))
            ]
        )
        
        #Abas de status de tarefas
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
            ft.Tab(text='Todos'),
            ft.Tab(text='Em andamento'),
            ft.Tab(text='Finalizados'),
            ]

        )

        #Tarefas
        tasks = self.task_container()

        self.page.add(input_bar, tabs, tasks)

ft.app(target = ToDo)