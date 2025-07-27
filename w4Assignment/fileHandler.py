#File Read & Write Challenge 🖋️:
#1.Create a program that reads a file and writes a modified version to a new file.
#2.Error Handling Lab 🧪: Ask the user for a filename and 
#3.handle errors if it doesn’t exist or can’t be read.

# Ask the user for the input filename
input_filename = input("Enter the name of the input file (e.g., 'input.txt'): ")

try:
    # Try to open and read the input file
    with open(input_filename, "r") as file:
        data = file.read()

    # Process the data
    upper_cased_data = data.upper()
    word_length = len(upper_cased_data.split())

    # Ask the user for the output filename
    output_filename = input("Enter the name of the output file (e.g., 'output.txt'): ")

    # Write the processed data to the output file
    with open(output_filename, "w") as file:
        file.write(upper_cased_data)
        file.write(f"\n\nWord count is {word_length}")

    print(f"Processing complete! Results saved in '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")