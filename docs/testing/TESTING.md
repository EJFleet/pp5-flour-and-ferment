# Testing

Return back to the [README.md](README.md) file.


## Code Validation


### HTML

### HTML Validation

For my HTML files, I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Due to the usage of Jinja syntax (e.g., `{% extends "base.html" %}` and `{{ form|crispy }}`) and authentication requirements, the following approach was used for validation:

1. Navigate to each individual page via the deployed Heroku app link.
2. Right-click the screen or use `CTRL+U` (`⌘+U` on Mac) to "View page source."
3. Copy the complete HTML code and paste it into the [validate by input](https://validator.w3.org/#validate_by_input) option.
4. Fix any errors or warnings, revalidate, and record results.

All pages passed validation.

<details>

<summary> Example screenshot of file that passed <summary

[Profile page](/docs/testing/testing-images/profile-w3c.png)

</details>

---

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

All files passed with no errors.

<details>

<summary> Example screenshot of file that passed <summary

[Profile css](/docs/testing/testing-images/css-profile-w3c.png)

</details>

---

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.  The JS files in my project were not written by me but taken from Boutique Ado, Stripe and CountryField.

All files passed with no errors.  The Stripe one has an extra semi-colon and two undefined variables, but as it did not come from me I am leaving it alone.

<details>

<summary> Stripe screenshot <summary

[Stripe JS](/docs/testing/testing-images/js-stripe-jshint-1.png)
[Stripe JS](/docs/testing/testing-images/js-stripe-jshint-2.png)

</details>

---

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

All files passed with no errors.

<details>

<summary> Example screenshot of file that passed <summary

[Profile pep8](/docs/testing/testing-images/profile-pep8.png)

</details>

---

## Dev Tools/Real World Device Testing
---

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. 
  
<br>

### Dev Tools Device Testing - all features tested, issues noted below

| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone SE | Product Detail page | Page looked cramped | Changed to col-11 rather than col-12, added mx-auto |
| Nest Hub Max | All features | No issues | None needed |
| iPad Mini | All features | No issues | None needed |
| Asus Zenbook Fold | Scroll down | Can't see footer | This is a browser issue and not a responsivity issue |
   
<br>

### Real World Device Testing

| Device      | Feature    | Issue  | Fix  | 
| ------------| ---------- | ------ |------|
| Samsung S9 | All features | No issues | None needed |
| iPad Pro (2020) | All features |  No issues  | None needed |
| HP 15S laptop  | All features | No issues | None needed |
| iPad Pro 2021 |    All features      |    No issues    |  None needed |
| Google Pixel 6 | All features | No issues | None needed |
| Samsung S22 | All features | No issues | None needed |


### Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Notes |
| --- | --- | --- |
| Chrome | Works as expected |
| Edge | Works as expected |
| Safari | Works as expected |
| Firefox | MailChimp box in footer looks cramped; arrows in quantity form that don't appear in other browswers |

<details>

<summary> Firefox Screenshots </summary>

MailChimp box in footer
[Firefox footer](/docs/testing/testing-images/browser/browser-firefox-footer.png)

Quantity form
[Firefox quantity form](/docs/testing/testing-images/browser/browser-firefox-quantity-form.png)

</details>

---

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.



## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing.

<details>

<summary> Manual Testing Results </summary>

| Page | User Action | Expected Result |  /Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page |  | |
| | Click on Shop link in navbar | Dropdown menu with links to All Items and different categories | | |
| | Click on Shop - All Items | Redirection to Products page | | |
| | Click on Shop - Sourdough Starters & Flours | Redirection to Products page with only Sourdough etc displayed | | |
| | Click on Shop - Baking Equipment | Redirection to Products page with only Baking Equipment displayed  | | |
| | Click on Shop - Cookbooks | Redirection to Products page with only Cookbooks displayed  | | |

| | Click on About link in navbar | Dropdown menu with links to Our Story, FAQ and Contact | | |
| | Click on About - Our Story | Redirect to Our Story page | | |
| | Click on About - FAQ | Redirect to FAQ page | | |
| | Click on About - Contact | Redirect to Contact page | | |

| | Enter text in Search box and click Search button | Redirect to Products page with results | | |

| | Click on Register link in navbar | Redirection to Register page | | |
| | Click on Login link in navbar | Redirection to Login page | | |
| | Click on Basket link in navbar | Redirection to Basket page | | |

| | Click on Account link in navbar | Dropdown menu with links to My Profile, My Wishlist and Logout displayed | | |
| | Click on Account - My Profile link in navbar | Redirection to user's Profile page |  | |
| | Click on Account - My Wishlist link in navbar | Redirection to user's Wishlist page |  | |
| | Click on Account - Logout link in navbar | Redirection to Logout page |  | |

| | Click on Admin link in navbar | Dropdown menu with links to Admin Panel, Add New Product and Edit/Delete A Product | | |
| | Click on Admin Panel link in navbar | Redirection to Admin Panel page |  | |
| | Click on Add New Product link in navbar | Redirection to Add Product page |  | |
| | Click on Edit/Delete A Product link in navbar | Redirection to Products page |  | |

| Footer | | | | |
| | Click on Home link | Redirection to Home page |  | |
| | Click on Shop link | Redirection to Products page |  | |
| | Click on Our Story link | Redirection to About page |  | |
| | Click on FAQ link | Redirection to FAQ page |  | |
| | Click on Contact link | Redirection to Contact page |  | |
| | Click on Register link | Redirection to Register page |  | |
| | Click on Login link | Redirection to Login page |  | |
| | Click on Profile link | Redirection to user's Profile page |  | |
| | Click on Wishlist link | Redirection to user's Wishlist page |  | |
| | Click on Logout link | Redirection to Logout page |  | |
| | Click on 'Subscribe' button in Newsletter sign-up box | 'Thank You for subscribing' message is displayed |  | |
| | Click on social media icons | Relevant social media page opens in new tab | | |

| Register | | | | |
| | Enter valid email address (twice) | Field will only accept email address format |  | |
| | Enter valid  word (twice) | Field will only accept  word format |  | |
| | Click on Sign Up button | Redirects user to notification to Verify Email Address |  |

| Log In | | | | |
| | Enter valid username/email | Field will accept username or email format |  | |
| | Enter valid  word | Field will only accept  word format |  | |
| | Click Sign In button | Log user in, redirects to home page |  | |

| Log Out | | | | |
| | Click Sign Out link in navbar Account dropdown menu | Logs out user, redirects user to home page |  |

| Profile | | | | |
| | Click on the Update Information button | Inputted information is saved |  | |
| | Click on Order History links | Redirects to user order confirmation, alert message displayed |  | |
| | Click on Back to Profile (in Order History) | Redirects to Profile page | | |

| Wishlist | | | | |
| | Click on the Add to Basket button | Item is added to basket |  | |
| | Click on Remove button | Item is removed from Wishlist |  | |
| | Click on Back to Store | Redirects to Products page | | |
| | Click product image | Redirect to the product details page |   | |
| | Click product name | Redirect to the product details page |   | |

| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Redirect to login page, redirect back after login |  | |

| Products | | | | |
| | Click on product image | Redirect to clicked product details page |  | |
| | Click on product title | Redirect to clicked product details page |  | |
| | Click on sorting dropdown options | Sort products by selected criteria |  | |

| Products - Admin Only| | | | |
| | Click on an edit button | Redirect to edit product page for that product |  | |
| | Click on a delete button | Trigger delete confirmation modal |  | |
| | Delete confirmation modal - 'Delete' button | Delete the product |   | |
| | Delete confirmation modal - 'Cancel' button | Close the modal |   | |

| Product Details | | | | |
| | Click on product image | Load full image |   | |
| | Click on 'Keep Shopping' button | Redirect to products page |   | |
| | Click on 'Add To Basket' button | Adds product to basket, basket message displayed |   | |
| | Click on Wishlist heart icon (logged in user) | Adds product to wishlist, succcess message displayed | | |
| | Click on Wishlist heart icon (logged out user) | Redirects to Sign Up page | | |

| Product Details - Admin Only | | | | |
| | Click on Edit button | Redirect to edit product page for that product |   | |
| | Click on Delete button | Trigger delete confirmation modal |   | |
| | Delete confirmation modal - 'Delete' button | Delete the product |   | |
| | Delete confirmation modal - 'Cancel' button | Close the modal |   | |

| FAQ | | | | |
| | Click on question | Dropdown with answer appears |   | |
| | Click on open question | Dropdown with answer disappears |   | |
| | Click on Back Home button | Redirection to Home page |  | |

| Contact | | | | |
| | Email input | Required, accepts only email format |   | |
| | Name input | Required |   | |
| | Subject input | Required |   | |
| | Message input | Require |   | |
| | Click on 'Send Message' button | Redirects to contact success page, success message displayed, message visible in Admin panel |   | |
| | Click on 'Back Home' button on contact success page | Redirection to Home page |  | |

| Add New Product - Admin Only | | | | |
| | Sku | Not required, select from options |   | |
| | Category Input | Not required, select from options |   | |
| | Name Input | Required |   | |
| | Description Input | Required |   | |
| | Price Input | Required, Numbers only |   | |
| | Image URL | Not required |   | |
| | Image | Not required |   | |

| Edit Product - Admin Only | | | | |
| | Click on 'Cancel' button | Redirect to Products page |   | |
| | Click on 'Update Product' button | Save changes, redirect to product details page |   | |

| Basket | | | | |
| | Adjust quantity by using + or - buttons | Quantity figure adjusts | |
| | Click on 'Update' link after adjusting quantity | Update quantity of product in basket, subtotal and total change |   | |
| | Click on 'Remove' link | Remove item from basket, total change |   | |
| | Click on 'Keep Shopping' button | Redirect to Products page |   | |
| | Click on 'Secure Checkout' button | Redirect to Checkout page |   | |
| | Click product image | Redirect to the product details page |   | |
| | Click product name | Redirect to the product details page |   | |

| Checkout | | | | |
| | Full Name Input | Required |   | |
| | Email Input | Required, autofill if saved |   | |
| | Phone Number Input | Required, autofill if saved |   | |
| | Street Address 1 Input | Required, autofill if saved |   | |
| | Street Address 2 Input | Not required, autofill if saved |   | |
| | Town Or City Input | Required, autofill if saved |   | |
| | County, State or Locality Input | Not required, autofill if saved |   | |
| | Postal Code Input | Not required, autofill if saved |   | |
| | Country Input | Required, autofill if saved, select from options |   | |
| | Stripe Card Details | Required, validates on input |   | |
| | Check 'save delivery info.' box | Saves information to user profile |   | |
| | Click product image in order summary | Redirect to the product details page |   | |
| | Click product name in order summary | Redirect to the product details page |   | |
| | Click on 'Adjust Basket' button | Redirect to Basket page |   | |
| | Click on 'Complete Order' button | Complete Checkout with given information, redirect to order confirmation page if valid |   | |


</details>



## Bug Fixes
---

|Bug|Solution|Fixed?|
|-----|-----|-----|
| Images not rendering in products.html | Fix filepaths in fixtures.json and add media context processor to settings.py | Yes |
| Order confirmation emails not sending | Added missing line in webhook_handler.py for sending the email when order is made | Yes |
| 'Complete Order' button is not working | I had copy and pasted JavaScript from the Boutique Ado project, but I had used code from too far ahead, which was causing the issues. I used code from the appropriate stage and was able to fix it. | Yes |
| Add to basket function not working in wishlist | The line `redirect_url = request.POST.get('redirect_url')` in basket/views.py was causing the issue, as the button to 'add to basket' on the wishlist was not associated with an item_id in the same way that the 'add to basket' button is on the product detail page.  Added `<input type="hidden" name="redirect_url" value="{% url 'wishlist' %}">` to the button in wishlist.html | Yes |
| 401 errors for Stripe webhooks | Stopped using the Stripe CLI for testing as it was causing confusion by giving a different signing secret | Yes |
| Hamburger icon disappeared from navbar | Added navbar-light back in, as the hamburger icon visibility is dependent on it. | Yes |
| Sorting selector not displaying sorting choice correctly | Updated view and added a default sorting order of 'Name(A-Z)' | Yes |


**There were no other known bugs at the time of submitting the project.**