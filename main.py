def main():
    my_list = ["foo"]
    my_list = append_bar(my_list)
    print(my_list)

    my_list = append_bar()
    print(my_list)

    my_list = append_bar([])
    print(my_list)

    my_list = append_bar()
    print(my_list)

def append_bar(my_list=[]):
    my_list.append("bar")
    return my_list


if __name__ == '__main__':
    main()
