import data_fetcher
import json
import os

def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML."""
    output = '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'  # Start of card text
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>\n'  # End of card text
    output += '</li>\n'
    return output

def generate_animal_html(data):
    """Generates HTML for all animal information."""
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output

def create_animals_html(template_file, output_file, api_animal_data, animal_name):  # animal_name parameter
    """Creates the final HTML file, handling the 'animal not found' message."""
    try:
        with open(template_file, "r") as file:
            template_content = file.read()

        if api_animal_data and len(api_animal_data) > 0:  # Check if API returned results AND list is not empty
            animal_html = generate_animal_html(api_animal_data)
            updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html)
            with open(output_file, "w") as file:
                file.write(updated_content)
            print(f"Website was successfully generated to the file {output_file}.")

        else:  # No animals found, create "not found" message
            not_found_message = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
            updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", not_found_message)
            with open(output_file, "w") as file:
                file.write(updated_content)
            print(f"Website generated to {output_file} (but no animals were found).")

    except FileNotFoundError:
        print(f"Error: File '{template_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# File paths
template_file = "animals_template.html"
output_file = "animals.html"

# Get animal name from the user
animal_name = input("Enter a name of an animal: ")
animal_data = data_fetcher.fetch_data(animal_name)


if animal_data is not None:
    create_animals_html(template_file, output_file, animal_data, animal_name)  # Pass animal_name
else:
    print("An error occurred while fetching data from the API.")

...
