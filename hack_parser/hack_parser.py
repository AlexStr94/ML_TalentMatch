class HackParser:
    def __init__(self, file_path=None):
        if not file_path:
            self.text = ...
        else:
            self.text = ...
        self.model = ...

    def set_file(self, file_path):
        self.text = ...

    def get_name(self):
        return self.model()

    def parse(self):
        return {
            "first_name": self.get_name(file_text),
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
    def extract_contact_info(self, resume_lines):
        
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\+?[0-9\s\-\(\)]{7,}"
        linkedin_pattern = r"\b(?:https?:\/\/)?(?:www\.)?(linkedin\.com\/[^\s,]*)"
        github_pattern = r"\b(?:https?:\/\/)?(?:www\.)?(github\.com\/[^\s,]*|[a-zA-Z0-9-]+\.github\.io\/?[^\s,]*)"
    
        email, phone, linkedin, github = None, None, None, None
    
        for line in resume_lines:
            if not email:
                email_match = re.search(email_pattern, line)
                if email_match:
                    email = email_match.group(0)
    
            if not phone:
                phone_match = re.search(phone_pattern, line)
                if phone_match:
                    phone = phone_match.group(0)
    
            if not linkedin:
                linkedin_match = re.search(linkedin_pattern, line)
                if linkedin_match:
                    linkedin = linkedin_match.group(0)
    
            if not github:
                github_match = re.search(github_pattern, line)
                if github_match:
                    github = github_match.group(0)
    
            if email and phone and linkedin and github:
                break
    
        return email, phone, linkedin, github
