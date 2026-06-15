import json
import os
from pathlib import Path

class Child:
    def __init__(self, name, age, correct_sounds=None, incorrect_sounds=None, mixed_sounds=None):
        self.name = name
        self.age = age
        self.correct_sounds = correct_sounds if correct_sounds is not None else []
        self.incorrect_sounds = incorrect_sounds if incorrect_sounds is not None else []
        self.mixed_sounds = mixed_sounds if mixed_sounds is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "correct_sounds": self.correct_sounds,
            "incorrect_sounds": self.incorrect_sounds,
            "mixed_sounds": self.mixed_sounds}
    @classmethod
    def from_dict(cls, data):
        return cls( name=data.get("name"),
                      age=data.get("age"),
                      correct_sounds=data.get("correct_sounds"),
                      incorrect_sounds=data.get("incorrect_sounds"),
                    mixed_sounds=data.get("mixed_sounds"))

class LogopedApp:
    def __init__(self, filename="children_database.json"):
        documents_dir = Path.home() / "Documents" / "LogopedApp"
        documents_dir.mkdir(parents=True, exist_ok=True)
        self.filename = filename
        self.children = []
        self.load_data()
        print(f" База даних завантажена з: {self.filename}")
    def add_child(self, name, age):
        new_child = Child(name, age)
        self.children.append(new_child)
        self.save_data()
        print(f" Дитину {name} ({age} р.) успішно додано!")

    def run_diagnostics(self, name):
        child = self.find_child(name)
        if not child:
            print(" Дитину з таким ім'ям не знайдено.")
            return

        print(f"\n--- Діагностика звуків для: {child.name} ({child.age} років) ---")
        print("Вводьте звуки через кому (наприклад: р, л, с)")

        correct = input("1. Які звуки вимовляє ПРАВИЛЬНО?: ").strip()
        incorrect = input("2. Які звуки вимовляє НЕПРАВИЛЬНО (відсутні/спотворені)?: ").strip()
        mixed = input("3. Які звуки ЗМІШУЄ (замінює один на інший)?: ").strip()

        child.correct_sounds = [s.strip() for s in correct.split(",") if s.strip()]
        child.incorrect_sounds = [s.strip() for s in incorrect.split(",") if s.strip()]
        child.mixed_sounds = [s.strip() for s in mixed.split(",") if s.strip()]

        self.save_data()
        print(f"✅ Діагностику для {child.name} збережено!")

    def show_children_by_age(self):
        if not self.children:
            print(" Список дітей порожній.")
            return
        sorted_children = sorted(self.children, key=lambda c: c.age)
        print("\n--- СПИСОК ДІТЕЙ (за віком) ---")
        for child in sorted_children:
            print(f"• {child.name} — Вік: {child.age} р.")
            print(f"  [+] Правильні: {', '.join(child.correct_sounds) if child.correct_sounds else '-'}")
            print(f"  [-] Неправильні: {', '.join(child.incorrect_sounds) if child.incorrect_sounds else '-'}")
            print(f"  [/] Змішує: {', '.join(child.mixed_sounds) if child.mixed_sounds else '-'}")
        print("-------------------------------")

    def export_report_txt(self):
        if not self.children:
            print(" Немає даних для експорту.")
            return

        export_path = Path.home() / "Documents" / "LogopedApp" / "Звіт_Логопеда.txt"

        try:
            with open(export_path, mode="w", encoding="utf-8") as f:
                f.write("=== ЗАГАЛЬНИЙ ЗВІТ ДІАГНОСТИКИ ===\n\n")
                for child in self.children:
                    f.write(f"Дитина: {child.name}\n")
                    f.write(f"Вік: {child.age} р.\n")
                    f.write(f"Правильні звуки: {', '.join(child.correct_sounds) if child.correct_sounds else '-'}\n")
                    f.write(
                        f"Проблемні звуки: {', '.join(child.incorrect_sounds) if child.incorrect_sounds else '-'}\n")
                    f.write(f"Змішує звуки: {', '.join(child.mixed_sounds) if child.mixed_sounds else '-'}\n")
                    f.write("-" * 30 + "\n")
            print(f" Звіт успішно збережено у файл:\n   {export_path}")
        except Exception as e:
            print(f" Не вдалося зберегти текстовий звіт: {e}")

    def find_child(self, name):
        for child in self.children:
            if child.name.lower() == name.lower():
                return child
        return None

    def save_data(self):
        try:
          with open(self.filename, mode="w", encoding="utf-8") as f:
            json_data = [child.to_dict() for child in self.children]
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
             print(f"❌ Помилка запису у файл: {e}")
    def load_data(self):
        """Завантажує дані з файлу JSON, якщо він існує."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    json_data = json.load(f)
                    self.children = [Child.from_dict(data) for data in json_data]
            except Exception:
                print(" Не вдалося прочитати базу даних, створено нову.")
                self.children = []

def main():
    app = LogopedApp()

    while True:
        print("\n=== МЕНЮ ЛОГОПЕДА ===")
        print("1. Додати дитину")
        print("2. Провести/оновити діагностику звуків")
        print("3. Переглянути список дітей (за віком)")
        print("4. Вийти")

        choice = input("Оберіть дію (1-4): ").strip()

        if choice == "1":
            name = input("Введіть ім'я та прізвище дитини: ").strip()
            try:
                age = int(input("Введіть вік (повних років): ").strip())
                app.add_child(name, age)
            except ValueError:
                print(" Вік має бути числом!")

        elif choice == "2":
            name = input("Введіть ім'я дитини для діагностики: ").strip()
            app.run_diagnostics(name)

        elif choice == "3":
            app.show_children_by_age()

        elif choice == "4":
            print("👋 Роботу завершено. Дані надійно збережені в базі!")
            break
        else:
            print(" Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()