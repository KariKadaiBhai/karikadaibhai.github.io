def find_s_algorithm(training_data):
    hypothesis = None
    for instance in training_data:
        features, label = instance[:-1], instance[-1]     
        if label == 'positive':   
            if hypothesis is None: 
                hypothesis = features.copy()   
            else: 
                for i in range(len(hypothesis)):
                    if hypothesis[i] != features[i]: 
                        hypothesis[i] = '?'  # Replace differing values with '?' 
    return hypothesis

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'positive'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'positive'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'negative'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'positive']
]

hypothesis = find_s_algorithm(training_data)
print("Most specific hypothesis:", hypothesis)
