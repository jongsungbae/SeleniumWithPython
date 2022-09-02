class Locators:
    # index page
    signin_button_value_xpath = '//a[@class="login"]'
    logo_image_value_xpath = '//img[@class="logo img-responsive"]'
    search_box_value_id = "search_query_top"
    search_submit_value_cssSelector = 'button[name="submit_search"]'

    # login page
    login_title_value_xpath = '//h1[text()="Authentication"]'
    login_email_box_id = "email"
    login_password_box_id = "passwd"
    login_submit_button_id = "SubmitLogin"
    login_create_account_id = "SubmitCreate"
    long_create_email_id = "email_create"

    # create account page
    create_account_title_xpath = '//h1[text()="Create an account"]'
    create_account_gender1_id = "id_gender1"
    create_account_gender2_id = "id_gender2"
    create_account_firstName_id = "customer_firstname"
    create_account_lastName_id = "customer_lastname"
    create_account_password_id = "passwd"
    create_account_address1_id = "address1"
    create_account_city_id = "city"
    create_account_postcode_id = "postcode"
    create_account_state_id = "id_state"
    create_account_phone_mobile_id = "phone_mobile"
    create_account_submit_button_id = "submitAccount"

    # my account Page
    myAccount_title_value_xpath = '//h1[text()="My account"]'
    wishlist_xpath = '//span[text()="My wishlists"]'
    orderhistory_xpath = '//span[text()="Order history and details"]'

    # search result page
    search_result_image_cssSelector = 'a[title = "Faded Short Sleeve T-shirts"]'
    search_result_more_cssSelector = 'a[title = "View"]'
    search_result_quantity_id = "quantity_wanted"
    search_result_size_xpath = '//select[@id="group_1"]'
    search_result_size_small_cssSelector = 'option[value = "1"]'
    search_result_size_medium_cssSelector = 'option[value = "2"]'
    search_result_size_large_cssSelector = 'option[value = "3"]'
    search_result_color_orange_cssSelector = 'a[title="Orange"]'
    search_result_color_blue_cssSelector = 'a[title="Blue"]'
    search_result_add_cart_button_cssSelector = 'button[name="Submit"]'
