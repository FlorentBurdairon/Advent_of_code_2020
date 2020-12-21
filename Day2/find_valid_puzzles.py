
def read_puzzle_input( myfilename ):
    list_of_passwords = list()
    with open(myfilename) as fp:
        filecontent = fp.readlines()
        for element in filecontent:
            list_of_passwords.append(element[:-1])
    return list_of_passwords

def analyse_individual_entry( entry ):
    mystring = entry.split()
    bounds_str = mystring[0].split('-')
    bounds = [int(bounds_str[0]), int(bounds_str[1])]
    pattern = mystring[1]
    pattern = pattern[0]
    in_string = mystring[2]
    return bounds, pattern, in_string

def analyse_list_of_entries( input_list ):
    nb_valid_pwds = 0
    for element in input_list:
        bounds, pattern, in_string = analyse_individual_entry( element )
        validity = check_if_entry_is_valid( bounds, pattern, in_string )
        nb_valid_pwds += validity
    return nb_valid_pwds

def check_if_entry_is_valid( bounds, pattern, in_string ):
    nb = 0
    for character in in_string:
        if character == pattern:
            nb += 1
#    print(f"{pattern} is present {nb} times in {in_string} (bounds are {bounds})")
    if nb < bounds[0] or nb > bounds[1]:
#        print(f"{in_string} is NOT a valid password")
        validity = 0
    else:
#        print(f"{in_string} is a valid password")
        validity = 1
    return validity


filename = "puzzle.input"
dirname = "./"
input_list = read_puzzle_input( dirname+filename )
#input_list = input_list[:10]
#print(input_list)
nb_valid_pwds = analyse_list_of_entries( input_list )
print(f"There are a total of {nb_valid_pwds} valid passwords")
