def sort_contacts(contacts):

    keys = contacts.keys()
    keys = sorted(keys)
    # value = list(contacts.values())
    new_tuple = ""
    new_list = []
    for i in keys:
        new_tuple = (i, contacts[i][0], contacts[i][1])

        new_list.append(new_tuple)

    return new_list


    # new_tuple = (i, value[i][0], value[i][0])
    #     value = list(contacts.values())
    #     new_tuple = i, value[i][0], value[i][1]
    # print(new_tuple)
    # new_list = list(contacts.items())
    # new_list.sort()
    # print(new_list)
    # contacts.get([0])
    # it = list(contacts.items())
    # it.sort()
    # tup = ""
    # for i in it:
    #     i = (i[0], i[1][0], i[1][1])
    # new_list = list(contacts.items())
    # updated_list = ""
    # for i in new_list:
    #     updated_list = (i[0], i[1][0], i[1][1])
    #     print(updated_list)
    # sort_contacts(
    #     {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com")})
sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
               "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
               "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")})
