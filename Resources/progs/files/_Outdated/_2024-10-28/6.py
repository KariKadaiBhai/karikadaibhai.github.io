def candidate_elimination(data):
    S, G = ['0'] * (len(data[0]) - 1), ['?'] * (len(data[0]) - 1)
    
    for instance in data:
        x, label = instance[:-1], instance[-1]
        
        if label == 'Yes':
            S = [xi if si == '0' else '?' if si != xi else si for si, xi in zip(S, x)]
        elif label == 'No':
            G = [gi if xi == gi else '?' for gi, xi in zip(G, x)]
    
    return S, G

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'No'],
    ['Sunny', 'Warm', 'High', 'Weak', 'Yes']
]

S, G = candidate_elimination(data)
print("S:", S)
print("G:", G)
