# Testing

Return back to the [README.md](README.md) file.


## Code Validation


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
| --- | --- |
| Chrome | Works as expected |
| Edge | Works as expected |
| Safari | Works as expected |
| Firefox | MailChimp box in footer looks cramped; arrows in quantity form that don't appear in other browswers |

<details>

<summary> Firefox Screenshots </summary>

MailChimp box in footer
![Firefox footer](/docs/testing/testing-images/browser/browser-firefox-footer.png)

Quantity form
![Firefox quantity form](/docs/testing/testing-images/browser/browser-firefox-quantity-form.png)

</details>

---

## Lighthouse Audit

I tested my deployed project using the Lighthouse Audit tool in Chrome Dev Tools on each page, in incognito mode.

I initially used the Lighthouse extension to test and was getting much better results for performance.  When I changed to the tool in dev tools, my pages scored much lower. I subsequently went back and tested every page with the dev tools method and these are the scores you see below.

Performance is much lower than I would like it to be, and I would fix this in future development.

I was more concerned that my accessibility scores would be adequate, which they appear to be.

### Test Results Table

| Page | Screenshot | Comments |
|------|------------|----------|
| **Home** | ![Home Screenshot](/docs/testing/testing-images/lighthouse/home-new-again.png) |  |
| **Products** | ![Products Screenshot](/docs/testing/testing-images/lighthouse/products.png) |  |
| **Product Detail** | ![Product Detail Screenshot](/docs/testing/testing-images/lighthouse/product-detail.png) |  |
| **Our Story** | ![Our Story Screenshot](/docs/testing/testing-images/lighthouse/our-story.png) |  |
| **FAQ** | ![FAQ Screenshot](/docs/testing/testing-images/lighthouse/faq.png) |  |
| **Contact** | ![Contact Screenshot](/docs/testing/testing-images/lighthouse/contact.png) |  |
| **Contact Success** | ![Contact Success Screenshot](/docs/testing/testing-images/lighthouse/contact-success.png) |  |
| **My Profile** | ![My Profile Screenshot](/docs/testing/testing-images/lighthouse/my-profile.png) |  |
| **Order Summary** | ![Order Summary Screenshot](/docs/testing/testing-images/lighthouse/order-summary.png) |  |
| **My Wishlist** | ![My Wishlist Screenshot](/docs/testing/testing-images/lighthouse/my-wishlist.png) |  |
| **Register** | ![Register Screenshot](/docs/testing/testing-images/lighthouse/register.png) |  |
| **Login** | ![Login Screenshot](/docs/testing/testing-images/lighthouse/login.png) |  |
| **Logout** | ![Logout Screenshot](/docs/testing/testing-images/lighthouse/logout.png) |  |
| **Add Product** | ![Add Product Screenshot](/docs/testing/testing-images/lighthouse/add-product.png) |  |
| **Edit Product** | ![Edit Product Screenshot](/docs/testing/testing-images/lighthouse/edit-product.png) |  |
| **Basket** | ![Basket Screenshot](/docs/testing/testing-images/lighthouse/basket.png) |  |
| **Checkout** | ![Checkout Screenshot](/docs/testing/testing-images/lighthouse/checkout.png) |  |
| **Order Confirmation** | ![Order Confirmation Screenshot](/docs/testing/testing-images/lighthouse/order-confirmation.png) |  |

---


## Stripe and Webhooks

### Stripe Payment Flow

| Test Step | Description | Expected Result | Status |
|-----------|------------|----------------|--------|
| **1. Load Checkout Page** | Navigate to the checkout page with a test product in the cart. | Page loads correctly with the expected order details. | Pass |
| **2. Initiate Payment** | Fill in delivery details and enter a valid test card (e.g., `4242 4242 4242 4242`) and use a valid CVC, expiration, and zip code. Click **Complete Order** button | Transaction is processed successfully, and the user is redirected to the confirmation page. | Pass |
| **3. Validate Webhook Trigger** | Check if the Stripe webhook is received and that there are green 200 messages on each (`payment-intent.created`, `charge.succeeded`, `payment_intent.succeeded`, `charge.updated`). | Webhook event is logged and processed correctly. | Pass |
| **4. Verify Order Database Entry** | Check if the order appears in the database. | Order data is correctly stored and matches the Stripe transaction ID. | Pass |
| **5. Test Payment Failure** | Use a failing test card (e.g., `4000 0000 0000 9995` for insufficient funds). | Payment is declined, and an error message appears. | Pass |
| **6. Check Email Notifications** | Confirm if an order confirmation email is sent to the customer. | Email is received with the correct order details. | Pass |
| **7. Test Authentication (3D Secure)** | Use a test card that **requires authentication** (`4000 0025 0000 3155`). | Stripe presents an authentication challenge (e.g., 3D Secure prompt). | Pass |
| **8. Confirm Authentication Success** | Approve the authentication challenge in Stripe's test modal. | Payment succeeds, user is redirected, and webhook fires. | Pass |
| **9. Test Authentication Failure** | Choose to fail the authentication challenge in Stripe's test modal. | Payment fails with an authentication error message. | Pass  |

---


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing.

<details>

<summary> Manual Testing Results </summary>

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page |  | |
| | Click on Shop link in navbar | Dropdown menu with links to All Items and different categories | | |
| | Click on Shop - All Items | Redirection to Products page | | |
| | Click on Shop - Sourdough Starters & Flours | Redirection to Products page with only Sourdough etc displayed | | |
| | Click on Shop - Baking Equipment | Redirection to Products page with only Baking Equipment displayed  | | |
| | Click on Shop - Cookbooks | Redirection to Products page with only Cookbooks displayed  | | |

| | Click on About link in navbar | Dropdown menu with links to Our Story, FAQ and Contact | Pass | |
| | Click on About - Our Story | Redirect to Our Story page | Pass | |
| | Click on About - FAQ | Redirect to FAQ page | Pass | |
| | Click on About - Contact | Redirect to Contact page | Pass | |

| | Enter text in Search box and click Search button | Redirect to Products page with results | Pass | |

| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Basket link in navbar | Redirection to Basket page | Pass | |

| | Click on Account link in navbar | Dropdown menu with links to My Profile, My Wishlist and Logout displayed | Pass | |
| | Click on Account - My Profile link in navbar | Redirection to user's Profile page | Pass | |
| | Click on Account - My Wishlist link in navbar | Redirection to user's Wishlist page | Pass  | |
| | Click on Account - Logout link in navbar | Redirection to Logout page | Pass | |

| | Click on Admin link in navbar | Dropdown menu with links to Admin Panel, Add New Product and Edit/Delete A Product | Pass | |
| | Click on Admin Panel link in navbar | Redirection to Admin Panel page | Pass | |
| | Click on Add New Product link in navbar | Redirection to Add Product page | Pass | |
| | Click on Edit/Delete A Product link in navbar | Redirection to Products page | Pass | |

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