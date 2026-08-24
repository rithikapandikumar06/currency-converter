# Currency Converter

A simple Python-based currency converter that uses the Frankfurter API to fetch exchange rates and convert an amount from one currency to another.

## Features

- Convert currencies using exchange-rate data from the API
- Supports different currency codes such as USD, EUR, GBP, and INR
- Validates the entered amount
- Prevents conversion when the source and target currencies are the same
- Handles invalid currency codes
- Handles API and internet connection errors
- Displays the exchange rate and converted amount

## Technologies Used

- Python
- Requests
- Frankfurter API

## Project Structure

currency-converter/
│
├── currency_converter.py
├── requirements.txt
├── README.md
└── .gitignore

## How It Works

1. The user enters the amount to convert.
2. The user enters the source currency.
3. The user enters the target currency.
4. The program sends a request to the Frankfurter API.
5. The API returns the exchange rate.
6. The program calculates the converted amount.
7. The converted amount and exchange rate are displayed.

## API Used

Frankfurter API

API endpoint:

https://api.frankfurter.app/latest

Example:

https://api.frankfurter.app/latest?from=USD&to=INR
