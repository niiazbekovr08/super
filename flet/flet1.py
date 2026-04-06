import flet as ft
import json
import datetime


class TodoApp:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "TODO Планировщик"
        self.page.window_width = 500
        self.page.window_height = 700

        self.tasks = []

        self.build_ui()
        self.load_tasks()

    # ---------------- UI ----------------
    def build_ui(self):

        self.task_input = ft.TextField(label="Задача", width=300)

        self.priority = ft.Dropdown(
            label="Приоритет",
            width=200,
            options=[
                ft.dropdown.Option("Высокий"),
                ft.dropdown.Option("Средний"),
                ft.dropdown.Option("Низкий"),
            ],
        )

        self.deadline = ft.TextField(label="Дедлайн (YYYY-MM-DD HH:MM)")

        self.search = ft.TextField(
            label="Поиск",
            on_change=self.search_task
        )

        add_btn = ft.ElevatedButton("Добавить", on_click=self.add_task)

        self.stats_text = ft.Text("")

        self.task_list = ft.Column()

        self.page.add(
            ft.Text("Планировщик задач", size=20, weight="bold"),
            self.task_input,
            self.priority,
            self.deadline,
            add_btn,
            self.search,
            self.stats_text,
            self.task_list
        )

    # ---------------- Добавление ----------------
    def add_task(self, e):

        if not self.task_input.value or not self.priority.value:
            return

        task = {
            "title": self.task_input.value,
            "priority": self.priority.value,
            "done": False,
            "deadline": self.deadline.value
        }

        self.tasks.append(task)

        self.task_input.value = ""
        self.priority.value = None
        self.deadline.value = ""

        self.save_tasks()
        self.update_tasks()
        self.page.update()

    # ---------------- Список ----------------
    def update_tasks(self, filtered_tasks=None):

        self.task_list.controls.clear()

        tasks_to_show = filtered_tasks if filtered_tasks is not None else self.tasks

        completed = 0

        for index, task in enumerate(tasks_to_show):

            color = "black"

            if task["priority"] == "Высокий":
                color = "red"
            elif task["priority"] == "Средний":
                color = "orange"
            elif task["priority"] == "Низкий":
                color = "green"

            if task["done"]:
                completed += 1

            checkbox = ft.Checkbox(
                value=task["done"],
                on_change=lambda e, i=index: self.toggle_done(i)
            )

            text = ft.Text(
                f"[{task['priority']}] {task['title']} ({task['deadline']})",
                color=color,
                italic=task["done"]
            )

            task_row = ft.Row(
                [
                    checkbox,
                    text,
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=lambda e, i=index: self.delete_task(i)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

            self.task_list.controls.append(task_row)

            # Проверка дедлайна
            if task["deadline"]:
                try:
                    dl = datetime.datetime.strptime(task["deadline"], "%Y-%m-%d %H:%M")
                    if datetime.datetime.now() > dl and not task["done"]:
                        self.show_deadline_alert(task["title"])
                except:
                    pass

        # статистика
        self.stats_text.value = f"Всего: {len(self.tasks)} | Выполнено: {completed}"

    # ---------------- Галочка ----------------
    def toggle_done(self, index):
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.save_tasks()
        self.update_tasks()
        self.page.update()

    # ---------------- Удаление ----------------
    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()
        self.update_tasks()
        self.page.update()

    # ---------------- Поиск ----------------
    def search_task(self, e):
        query = self.search.value.lower()

        filtered = [
            task for task in self.tasks
            if query in task["title"].lower()
        ]

        self.update_tasks(filtered)
        self.page.update()

    # ---------------- Сохранение ----------------
    def save_tasks(self):
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    # ---------------- Загрузка ----------------
    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except:
            self.tasks = []

        self.update_tasks()

    # ---------------- Уведомление ----------------
    def show_deadline_alert(self, title):
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Дедлайн прошёл!"),
            content=ft.Text(f"Задача '{title}' просрочена"),
            actions=[ft.TextButton("OK", on_click=lambda e: self.close_dialog())],
        )
        self.page.dialog.open = True
        self.page.update()

    def close_dialog(self):
        self.page.dialog.open = False
        self.page.update()


def main(page: ft.Page):
    TodoApp(page)


if __name__ == "__main__":
    ft.app(target=main)