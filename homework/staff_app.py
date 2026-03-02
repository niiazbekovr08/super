import flet
from flet import (
    Page,
    Text,
    TextField,
    Dropdown,
    dropdown,
    ElevatedButton,
    OutlinedButton,
    IconButton,
    icons,
    Column,
    Row,
)


class StaffApp:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Сотрудники"
        self.staff = []

        self.name_input = TextField(label="Имя", width=300)
        self.surname_input = TextField(label="Фамилия", width=300)
        self.age_input = TextField(
            label="Возраст", width=300, keyboard_type=flet.KeyboardType.NUMBER
        )
        self.salary_input = TextField(
            label="Зарплата", width=300, keyboard_type=flet.KeyboardType.NUMBER
        )

        self.position_input = Dropdown(
            label="Должность",
            width=300,
            options=[
                dropdown.Option("Разработчик"),
                dropdown.Option("Дизайнер"),
                dropdown.Option("Менеджер"),
                dropdown.Option("Тестировщик"),
            ],
        )

        self.msg = Text()
        self.list_box = Column()

        add_btn = ElevatedButton("Добавить", on_click=self.add_staff)
        sort_btn = OutlinedButton(
            "Сортировать по зарплате", on_click=self.sort_staff
        )

        self.page.add(
            self.name_input,
            self.surname_input,
            self.age_input,
            self.salary_input,
            self.position_input,
            add_btn,
            sort_btn,
            self.msg,
            self.list_box,
        )

    def add_staff(self, e):
        if not (
            self.name_input.value
            and self.surname_input.value
            and self.age_input.value
            and self.salary_input.value
            and self.position_input.value
        ):
            self.msg.value = "Заполните все поля!"
            self.msg.color = "red"
        else:
            try:
                age = int(self.age_input.value)
                salary = int(self.salary_input.value)
            except ValueError:
                self.msg.value = "Возраст и зарплата должны быть числами!"
                self.msg.color = "red"
                self.page.update()
                return

            if age < 18:
                self.msg.value = "Сотрудник должен быть старше 18"
                self.msg.color = "red"
            else:
                emp = {
                    "name": self.name_input.value,
                    "surname": self.surname_input.value,
                    "age": age,
                    "position": self.position_input.value,
                    "salary": salary,
                }

                self.staff.append(emp)

                self.msg.value = "Сотрудник добавлен!"
                self.msg.color = "green"

                # очистка полей
                self.name_input.value = ""
                self.surname_input.value = ""
                self.age_input.value = ""
                self.salary_input.value = ""
                self.position_input.value = None

                self.update_list()

        self.page.update()

    def update_list(self):
        self.list_box.controls.clear()

        for i, emp in enumerate(self.staff):
            color = "green" if emp["salary"] > 100000 else "black"

            row = Row(
                [
                    Text(
                        f'{emp["name"]} {emp["surname"]} | '
                        f'{emp["position"]} | '
                        f'{emp["age"]} | '
                        f'{emp["salary"]}',
                        color=color,
                    ),
                    IconButton(
                        icons.delete,
                        on_click=lambda e, idx=i: self.delete_staff(idx),
                        icon_color="red",
                    ),
                ]
            )

            self.list_box.controls.append(row)

        self.page.update()

    def delete_staff(self, idx):
        self.staff.pop(idx)
        self.update_list()

    def sort_staff(self, e):
        self.staff.sort(key=lambda x: x["salary"])
        self.update_list()


def main(page: Page):
    StaffApp(page)


if __name__ == "__main__":
    flet.app(target=main)