import flet as ft

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_heigth = 450
        self.page.window_resizable = True
        self.page.window_always_on_top = True
        self.page.title = 'ToDo '
        self.main_page()

    #Container das tarefas 
    def task_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content = ft.Column(
                controls = [
                    ft.Checkbox(label='Tarefa1', value = True)
                ]
            )

        )

    def main_page(self):

        # Adicionar tarefas -------
        input_task = ft.TextField(hint_text = 'Digite sua tarefa aqui', expand=True ) #Local de escrever

        input_bar = ft.Row( #Botão de adcionar
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
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