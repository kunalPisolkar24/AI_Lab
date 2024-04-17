class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = {
            "fever": False,
            "cough": False,
            "shortness of breath": False,
            "fatigue": False,
            "body aches": False,
            "loss of taste or smell": False,
            "headache": False,
            "sore throat": False,
            "chest pain": False,
            "nausea": False,
            "vomiting": False,
            "abdominal pain": False,
        }
        self.hospitals = {
            "COVID-19": {"Hospital A": "123-456-7890", "Hospital B": "234-567-8901"},
            "Flu": {"Hospital C": "345-678-9012", "Hospital D": "456-789-0123"},
            "Food Poisoning": {"Hospital E": "567-890-1234", "Hospital F": "678-901-2345"},
        }

    def diagnose(self):
        if self.symptoms["fever"] and self.symptoms["cough"] and self.symptoms["shortness of breath"]:
            return "You may have COVID-19. Please get tested immediately. Here are some hospitals you can contact: " + str(self.hospitals["COVID-19"])
        elif self.symptoms["fatigue"] and self.symptoms["body aches"]:
            return "You may have the flu. Please rest and drink plenty of fluids. Here are some hospitals you can contact: " + str(self.hospitals["Flu"])
        elif self.symptoms["nausea"] and self.symptoms["vomiting"] and self.symptoms["abdominal pain"]:
            return "You may have food poisoning. Please seek medical attention. Here are some hospitals you can contact: " + str(self.hospitals["Food Poisoning"])
        else:
            return "Your symptoms don't match a specific disease. Please consult with a healthcare professional."

    def update_symptoms(self, symptom, value):
        if symptom in self.symptoms:
            self.symptoms[symptom] = value
        else:
            print("Invalid symptom")

# Usage
expert_system = MedicalExpertSystem()
expert_system.update_symptoms("nausea", True)
expert_system.update_symptoms("vomiting", True)
expert_system.update_symptoms("abdominal pain", True)
print(expert_system.diagnose())

'''
------------------------------------------------------------------
Output
-----------------------------------------------------------------
You may have food poisoning. Please seek medical attention.
Here are some hospitals you can contact: {'Hospital E': '567-890-1234', 'Hospital F': '678-901-2345'}
'''
