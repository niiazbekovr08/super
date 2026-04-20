import flet as ft
from ui import UI
import smtplib
from email.mime.text import MIMEText

class ProfileApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Анкеты'
        self.page.window_width = 500
        self.page.window_height = 650
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.ui = UI()

        self.build_event()
        self.page.overlay.append(self.ui.file_picker)
        self.page.add(*self.ui.build())

    def build_event(self):
        self.ui.button.on_click = self.create_profile
        self.ui.age.on_change = self.update_age
        self.ui.upload_btn.on_click = self.pick_file
        self.ui.file_picker.on_result = self.file_selected

    def update_age(self, e):
        self.ui.age_text.value = f'Возраст: {int(self.ui.age.value)}'
        self.page.update()

    def pick_file(self, e):
        self.ui.file_picker.pick_files(allow_multiple=False)

    def file_selected(self, e):
        if e.files:
            self.ui.image.src = e.files[0].path
            self.page.update()

    def send_email(self, text):
        sender = "your_email@gmail.com"
        password = "your_app_password"
        receiver = "your_email@gmail.com"

        msg = MIMEText(text)
        msg["Subject"] = "Новая анкета"
        msg["From"] = sender
        msg["To"] = receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.send_message(msg)
        except:
            pass

    def create_profile(self, e):
        errors = []

        if not self.ui.name.value:
            errors.append("Введите имя")
        if not self.ui.city.value:
            errors.append("Выберите город")
        if not self.ui.level.value:
            errors.append("Выберите уровень")

        if errors:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("\n".join(errors)),
                bgcolor="red"
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        skills = []

        if self.ui.skill1.value:
            skills.append("Python")
        if self.ui.skill2.value:
            skills.append("Django")
        if self.ui.skill3.value:
            skills.append("Flet")

        result_text = (
            f'Имя: {self.ui.name.value}\n'
            f'Город: {self.ui.city.value}\n'
            f'Возраст: {int(self.ui.age.value)}\n'
            f'Навыки: {", ".join(skills) if skills else "Нет"}\n'
            f'Уровень: {self.ui.level.value}\n'
            f'Готов к работе: {"Да" if self.ui.active.value else "Нет"}'
        )

        self.ui.result.value = result_text

        self.send_email(result_text)

        self.page.update()