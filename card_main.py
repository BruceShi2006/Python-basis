card_list = []


def show_menu():
    print("*" * 50)
    print("Welcome use business card management system V1.0")
    print("")
    print("1.Create new card")
    print("2.Display all card's information")
    print("3.Inquiry specific card")
    print("")
    print("0.Leave")
    print("*" * 50)


def create_card():
    # Define a empty list to record the input card information

    print("*" * 50)
    print("Create new card:")
    # Define 4 strings to store the input
    name_str = input("Please input your name:")
    phone_str = input("Please input your phone number:")
    wechat_str = input("Please input your Wechat number:")
    email_str = input("Please input your E-mail address:")
    card_dict = {"Name": name_str,
                 "Phone": phone_str,
                 "Wechat": wechat_str,
                 "E-mail": email_str}
    # Add the input dictionary to the list (it's empty at first time)
    card_list.append(card_dict)
    # Show cards info and prompt message
    print(card_list)
    print("added %s's card success" % name_str)


def show_allcards():
    print("*" * 50)
    print("All cards' information:")
    if len(card_list) == 0:
        print("There is no record,please create new record")
        return
    # Print key list
    for name in ["Name","Phone","Wechat","E-mail"]:
        print(name, end="\t\t")
    print("")
    # Print split line
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["Name"],card_dict["Phone"],card_dict["Wechat"],card_dict["E-mail"]))


def search_card():
    print("*" * 50)
    find_dict = input("Please input user's name:")
    for card_dict in card_list:
        if card_dict["Name"] == find_dict:
            for name in ["Name", "Phone", "Wechat", "E-mail"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["Name"], card_dict["Phone"], card_dict["Wechat"], card_dict["E-mail"]))
            deal_card(card_dict)
            break
    else:
        print("The name you are searching does not exist")


def deal_card(find_dict):
    """

    :param find_dict: 查找到的信息卡
    """
    print(find_dict)
    action_str = input("Please select the option "
                       "[1] Modify [2] Delete [0] Return")
    if action_str == "1":
        find_dict["Name"] = input_card_info(find_dict["Name"],"Name:")
        find_dict["Phone"] = input_card_info(find_dict["Phone"],"Phone:")
        find_dict["Wechat"] = input_card_info(find_dict["Wechat"],"Wechat:")
        find_dict["E-mail"] = input_card_info(find_dict["E-mail"],"E-mail:")
        print("Modify card successful")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("Delete card successful")
def input_card_info(dict_value,tip_message):
    """
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容 则返回内容 如果用户没有输入内容 则返回原有值   """

    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.对输入进行判断,如果用户输入了内容,直接修改
    if len(result_str) > 0:
        return  result_str

    # 3.如果用户没有输入内容直接回车,则不改变原来字典内的键值
    else:
        return dict_value


