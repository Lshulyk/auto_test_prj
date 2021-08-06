

def test_amazon_card(amazon_page):
    assert amazon_page.search_input.is_displayed(), 'Amazon page Search input not displayed'
    # Search for books
    amazon_page.select_search_option('Books')
    amazon_page.search_button.click()
    # Once on the have_fun books page
    amazon_page.books_page_title.is_displayed(), 'Books at Amazon page not displayed'
    # Click the “Children&#39;s Books” option
    amazon_page.childrens_books.click()
    assert amazon_page.is_search_dd_option_selected('Children\'s Books'), '"Children\'s Books" option not selected'
    # Search by Tim Tebow books
    amazon_page.search_input.send_keys('Tim Tebow')
    amazon_page.search_button.click()
    # Select "A Party to Remember" book
    tim_tebow_book = amazon_page.get_book_by_name('A Party to Remember')
    assert tim_tebow_book.is_displayed(), '"A Party to Remember" book not displayed'
    tim_tebow_book.click()
    # Get book price
    tim_tebow_book_price = amazon_page.price.text
    # Add "A Party to Remember" book to the card
    amazon_page.add_to_card.click()
    # Assert 1 item in the cart
    assert int(amazon_page.items_in_the_card.text) == 1
    # Assert that the cart subtotal matches the book price
    assert amazon_page.card_subtotal.text == tim_tebow_book_price
    # Search by Chris Ferrie books
    amazon_page.search_input.send_keys('Chris Ferrie')
    amazon_page.search_button.click()
    # Select "Board Book Set" book
    chris_ferrie_book = amazon_page.get_book_by_name('Board Book Set')
    chris_ferrie_book.click()
    chris_ferrie_book_price = amazon_page.price.text
    amazon_page.add_to_card.click()
    assert int(amazon_page.items_in_the_card.text) == 2
    # Calculate total sum of books price
    total_price = float(chris_ferrie_book_price.replace('$', '')) + float(tim_tebow_book_price.replace('$', ''))
    # Assert that the cart subtotal matches both added books price
    assert amazon_page.card_subtotal.text == f'${total_price}'
    # Go to card
    amazon_page.items_in_the_card.click()
    # Assert card page opened
    assert amazon_page.card_page_title.is_displayed(), 'Card page not displayed'
    card_items = amazon_page.card_items
    # Assert that the desired items were added to the cart
    assert [s for s in card_items if 'Board Book Set' in s], 'Board Book Set is not in card'
    assert [s for s in card_items if 'A Party to Remember' in s], 'A Party to Remember is not in card'
    # Assert price for each item matches the seen price on item details page
    assert amazon_page.get_card_item_by_name('Board Book Set').price.text == chris_ferrie_book_price
    assert amazon_page.get_card_item_by_name('A Party to Remember').price.text == tim_tebow_book_price
    # Assert the subtotal of the 2 items is correct
    assert amazon_page.active_card_subtotal.text == f'${total_price}'
    amazon_page.get_card_item_by_name('Board Book Set').gift_mark.click()
    assert amazon_page.get_card_item_by_name('Board Book Set').gift_mark.is_selected(), \
        'This is a gift Learn more not selected'
    # Increase the qty (quantity) of the other item
    tim_tebow_books_qty = 4
    amazon_page.get_card_item_by_name('A Party to Remember').select_quantity(f'{tim_tebow_books_qty}')
    updated_tim_tebow_books_price = float(tim_tebow_book_price.replace('$', '')) * tim_tebow_books_qty
    # Assert that the item qty has increased
    assert int(amazon_page.get_card_item_by_name('A Party to Remember').current_qty.text) == tim_tebow_books_qty
    update_total_price = float(chris_ferrie_book_price.replace('$', '')) + updated_tim_tebow_books_price
    update_total_price = round(update_total_price, 2)
    # Assert that the price per quantity has increased for the item
    assert amazon_page.card_subtotal.text == '${:0.2f}'.format(update_total_price)
    # Assert that the subtotal has changed
    assert amazon_page.subtotal_label.text.strip() == f'Subtotal ({tim_tebow_books_qty + 1} items):'
    amazon_page.proceed_to_checkout.click()
    assert amazon_page.sign_in_page_title.is_displayed(), 'Sign-In page not opened'
    assert 'https://www.amazon.com/ap/signin?' in amazon_page.page_url, f'Current page url is: {amazon_page.page_url}'
