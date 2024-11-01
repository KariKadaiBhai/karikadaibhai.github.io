def diagnose_fever(symptoms):
    if 'high temperature' in symptoms:
        if 'headache' in symptoms and 'chills' in symptoms:
            return "Diagnosis: You likely have a fever."
        elif 'sweating' in symptoms:
            return "Diagnosis: You might have a mild fever."
        else:
            return "Diagnosis: Check for other symptoms, but fever is possible."
    else:
        return "Diagnosis: You do not appear to have a fever."
    
if __name__ == "__main__":
    print("Enter your symptoms separated by commas (e.g., 'high temperature, headache, sweating'):")
    user_input = input().split(', ')
    result = diagnose_fever(user_input)
    print(result)
                                 
