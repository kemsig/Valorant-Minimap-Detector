import json

def replace_word_in_json(input_file, output_file, word_to_replace, replacement_word):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Function to recursively search and replace words in nested dictionaries
    def recursive_replace(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str):
                    obj[key] = value.replace(word_to_replace, replacement_word)
                elif isinstance(value, (dict, list)):
                    recursive_replace(value)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                if isinstance(value, str):
                    obj[index] = value.replace(word_to_replace, replacement_word)
                elif isinstance(value, (dict, list)):
                    recursive_replace(value)

    # Call the function to replace words
    recursive_replace(data)

    # Write the modified content to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage:
input_file = 'TrainingSet\input.json'
output_file = 'TrainingSet\output.json'

blue_classes = [
    'bomb',
    'dead blue',
    'dead red',
    'fade blue',
    'fade red',
    'kj blue',
    'kj red',
    'omen blue',
    'omen red',
    'raze blue',
    'raze red',
    'viper blue',
    'viper red'
]
for b_class in blue_classes:
    replace_word_in_json(input_file, output_file, b_class, 'blue')


print("Word replacement completed. New JSON file generated.")
