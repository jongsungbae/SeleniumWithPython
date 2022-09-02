class Locators:
    # global
    add_cart_cssSelector = 'button[id="button-cart"]'
    add_cart_success_text_cssSelector = (
        'div[class="alert alert-success alert-dismissible"]'
    )
    quantity_cssSelector = 'input[id="input-quantity"]'
    go_to_cart_id = "cart-total"
    checkout_button_xpath = '//p[@class="text-right"]/a[2]'

    # menu bar
    menu_phone_xpath = '//a[text()="Phones & PDAs"]'
    menu_laptop_xpath = '//a[text()="Laptops & Notebooks"]'
    menu_sub_all_xpath = '//a[text()="Show All Laptops & Notebooks"]'

    # phone page
    phone_title_xpath = "//div/h2"
    iphone_cssSelector = 'img[title="iPhone"]'
    first_picture_xpath = '//ul[@class="thumbnails"]/li[1]'
    right_arrow_button_cssSelector = 'button[title="Next (Right arrow key)"]'
    picture_close_cssSelector = 'button[class="mfp-close"]'

    # laptop page
    laptop_title_xpath = '//div[@id="content"]/h2'
    laptop_cssSelector = 'img[title="HP LP3065"]'
    calendar_xpath = '//i[@class="fa fa-calendar"]'
    select_month_xpath = '//th[@class="picker-switch"]'
    next_month_button_xpath = '//th[@class="next"]'
    select_day_xpath = '//td[text()="26"]'

    # New customer
    guest_checkout_cssSelector = 'input[value="guest"]'
    button_account_id = "button-account"
    step_2_xpath = '//a[text()="Step 2: Billing Details "]'
    first_name_id = "input-payment-firstname"
    last_name_id = "input-payment-lastname"
    email_id = "input-payment-email"
    telephone_id = "input-payment-telephone"
    company_id = "input-payment-company"
    address_1_id = "input-payment-address-1"
    address_2_id = "input-payment-address-2"
    city_id = "input-payment-city"
    postcode_id = "input-payment-postcode"
    country_id = "input-payment-country"
    zone_id = "input-payment-zone"
    shipping_check_box_name = "shipping_address"
    continue_button_01_id = "button-guest"
    continue_button_step_04_id = "button-shipping-method"
    continue_button_step_05_id = "button-payment-method"
    continue_button_step_06_id = "button-confirm"
    continue_button_last_xpath = '//div[@class="pull-right"]/a'
    terms_check_box_xpath = '//input[@name="agree"]'
    checkout_success_text_xpath = '//div[@class="col-sm-12"]/h1'
