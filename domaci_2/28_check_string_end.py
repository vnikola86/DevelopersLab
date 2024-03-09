def ends_with_target(main_string, target_string):

    if main_string.endswith(target_string):
        return "Da"
    else:
        return "Ne"

main_string = input("Unesite glavni string: ")
target_string = input("Unesite target string: ")

result = ends_with_target(main_string, target_string)
print(result)
