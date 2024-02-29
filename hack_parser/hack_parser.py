class HackParser:
    def __init__(self, file_path):
        self.file_text = ...

    def get_name(self):
        return self.file_text

    def parse(self):
        return {
            "first_name": self.get_name(),
            "last_name": "",
            "middle_name": "",
            "birth_date": "",
            "birth_date_year_only": False,
            "country": "",
            "city": "",
            "about": "",
            "key_skills": "",
            "salary_expectations_amount": "",
            "salary_expectations_currency": "",
            "photo_path": "",
            "gender": "",
            "resume_name": "",
            "source_link": "",
            "contactItems": [],
            "educationItems": [],
            "experienceItems": [],
            "languageItems": []
        }
