def modify_content(content):
    return content.upper()


if __name__ == "__main__":
    try:
        input_file = input("Enter name of the file to read: ")
        with open(input_file, "r") as f:
            content = f.read()

        modified_content = modify_content(content)

        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified content saved to '{output_file}'")
    except FileNotFoundError:
        print("Error: File does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
