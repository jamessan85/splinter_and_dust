# Splinter and Dust Web Store

## Overview

### What is the site for?

This site allows both users wishing to purchase products and also trade users who wish to upload their own products to the site, trade users sign up and pay a subscription fee using [Stripe](https://stripe.com/gb). This allows them to upload products, images, prices, company information, banners and logos.

### How does it work?

There are two parts to the site. A trade part and a customer part. Trade users pay a subscription and can upload products, edit prodcuts, add account information from their profile. Standard customers can only see products they have purchased.


## Features

### Existing Features
- Stripe subscriptions
- Stripe payments for individual products
- Upload/Edit products
- Add/Edit account information
- View purchased products

### Features to implement
- Online basket before checking out to allow muliple items to be added
- Save customer credit card details

## Tech Used
- [django](https://www.djangoproject.com/)
	- django is used as the base framework for the site

- [bootstrap](http://getbootstrap.com/)
	- for the responsive layout of the site


## Contributing


### Getting it all up and running
1. Clone this repository using ```git clone https://github.com/jamessan85/splinter_and_dust```
2. Create a virtual environment and use the requirements.txt file to install ```pip install -r requirements.txt```
3. Run the program and connect to localhost:8000 to view the site
4. Create test logins for both trade and customer to see the differences and upload products on the trade logins to see how the accounts work.

## Testing
Testing was done was with the help of friends and colleagues using multiple devices and then reported back to myself any issues that were found.

 
### Issues found

- Issue with hamburger icon in the mobile view not dropping down the navbar when the page was loading stripe.js, in pages Trade Register and Purchasing. 
- This was resolved with adding ```<script type="text/javascript" src="{% static "js/main.js" %}"></script>``` to `{block head_js}` on the traderegister and purchasing pages. 
<br><br>
- Issue was found with stripe payments not like the decimal place in the price, so a price of £8008 would become £80.08 on stripe.
- To resolve this issue a small calculation was added to the amount when the form was submitted so stripe would process the correct amount. 
```
customer = stripe.Charge.create(
    amount=int(product.price * 100),
    currency="GBP",
    description=product.title,
    card=form.cleaned_data['stripe_id'],
 )
 ```

- Issue with the customer user model not migrating.
- This issue was caused when I decided to use the customer user model after making my first migration - after search on various forums it seemed to be the best method was to create a new project and copy and paste everything into the new project and then run the migrations again. 
