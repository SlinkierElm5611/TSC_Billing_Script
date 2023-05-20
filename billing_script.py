import os

def genertate_output(input_data: list[str]) -> str:
    output_string :str = ""
    for point in input_data:
        output_string += point + "\n"
    return output_string

def extract_balance_from_line(line: str):
        final_balance :str = line.split(":")[1].strip()
        while("," in final_balance):
            index_of_comma :int = final_balance.find(",")
            final_balance = final_balance[:index_of_comma] + final_balance[index_of_comma + 1:]
        return final_balance

def main():
    list_of_files_in_directory : list[str]= os.listdir()

    list_of_text_files : list[str]= []

    for file in list_of_files_in_directory:
        if(".txt" in file):
            list_of_text_files.append(file)

    billing_data :list[str] = []
    for file_name in list_of_text_files:
        with open(file_name) as file:
            user_name :str = file_name.split(".")[0]
            lines_of_text :list[str] = file.readlines()
            line_with_user_balance = lines_of_text[16]
            final_balance = extract_balance_from_line(line_with_user_balance)
            billing_data.append(user_name+","+final_balance)

    output_string :str = genertate_output(billing_data)
    with open("output.csv", "w") as f:
        print(output_string, file=f)

if __name__ == "__main__":
    main()
