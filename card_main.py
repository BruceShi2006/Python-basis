
#  Author:Bruce
#  Version:1.0
#  Description: Business card management system
#  Last modified data: 2020.2.17

while True:
    # Display menu and option
    import card_info
    card_info.show_menu()
    action_str = input("please select the option:")
    print("your selection is [%s]" %action_str)
    # Call the specific function base on user's input
    if action_str in ["1","2","3"]:
        # Create new card
        if action_str == "1":
            card_info.create_card()
        # Display all card
        elif action_str == "2":
            card_info.show_allcards()
        # Search card
        else:
            card_info.search_card()

    # 0 (quit)
    elif action_str == "0":
        print("welcome to use the business card management system")
        break
    # Prompt message
    else:
        print("your input is wrong,please input the correct number")





