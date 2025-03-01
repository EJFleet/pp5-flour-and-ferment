## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

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
