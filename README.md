# Splinter and Dust Web Store

## Overview

### What is the site for?

This site allows both users wishing to purchase products and also trade users who wish to upload there own products to the site, trade users sign up and pay a subscription fee using [Stripe](https://stripe.com/gb). This allows them to upload products, images, prices, company information, banners and logos.

### How does it work?

There are two parts to the site. A trade part and a customer part. Trade users pay a subscription and can upload products, edit prodcuts, add account information from their profile. Standard customers can only see products they have purchased.


## Features

### Exisisting Features
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
1. Clone this repositry using ```git clone https://github.com/jamessan85/splinter_and_dust```
2. Create a virtual enviroment and use the requirements.txt file to install ```pip install -r requirements.txt```
3. Run the program and connect to localhost:8000 to view the site
4. Create test logins for both trade and customer to see the differences and upload products on the trade logins to see how the accounts work.

## Testing