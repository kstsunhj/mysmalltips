
def extract_number_from_str():
    temp_string = "Hi my age is 32 years and 250 days12"
    print(temp_string)

    numbers = [int(temp)for temp in temp_string.split() if temp.isdigit()]

    print(numbers)
if __name__ == "__main__":
    extract_number_from_str()
