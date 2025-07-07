# AI-Powered Code Completion Example


# Copilot-Suggested Function to Sort List of Dictionaries by Key
def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Sample usage:
sample_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
print("Copilot Result:", sort_by_key(sample_data, 'age'))



# Manually Written Function to Sort List of Dictionaries by Key
def sort_by_key(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

# Sample usage:
sample_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
print("Manual Result:", sort_by_key(sample_data, 'age'))




