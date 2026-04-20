import flet as ft

class UI:
    def __init__(self):
        self.title = ft.Text('Создание пользователей', size=20)

        self.name = ft.TextField(label='Имя', width=300)

        self.city = ft.Dropdown(
            label='Город',
            width=300,
            options=[
                ft.dropdown.Option('Бишкек'),
                ft.dropdown.Option('Ош'),
                ft.dropdown.Option('Токмок'),
            ],
        )

        self.age_text = ft.Text('Возраст: 10')

        self.age = ft.Slider(
            min=10,
            max=60,
            divisions=50,
            value=10,
            label="{value}"
        )

        self.skill1 = ft.Checkbox(label='Python')
        self.skill2 = ft.Checkbox(label='Django')
        self.skill3 = ft.Checkbox(label='Flet')

        self.level = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Junior', label='Junior'),
                ft.Radio(value='Middle', label='Middle'),
                ft.Radio(value='Senior', label='Senior'),
            ])
        )

        self.active = ft.Switch(label='Готов к работе')

        self.file_picker = ft.FilePicker()

        self.image = ft.Image(src="", width=150, height=150)

        self.upload_btn = ft.ElevatedButton("Загрузить фото")

        self.button = ft.ElevatedButton('Отправить резюме')

        self.result = ft.Text()

    def build(self):
        return [
            self.title,
            self.name,
            self.city,
            self.age_text,
            self.age,
            ft.Text('Навыки:'),
            self.skill1,
            self.skill2,
            self.skill3,
            ft.Text('Уровень:'),
            self.level,
            self.active,
            self.upload_btn,
            self.image,
            self.button,
            self.result
        ]