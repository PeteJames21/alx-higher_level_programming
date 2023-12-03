# 0x11. Python - Network #1
Networking with Python

## 0-hbtn_status.py
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the urllib package

## 1-hbtn_header.py
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response using urllib. The URL is passed as the sole argument to the script

## 2-post_email.py
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8). The email must be sent in the `email` variable

## 3-error_code.py
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
- Manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code

## 4-hbtn_status.py
Write a Python script that fetches https://alx-intranet.hbtn.io/status using the requests package

## 5-hbtn_header.py
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header. Use the requests package

## 6-post_email.py
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response

## 7-error_code.py
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- Use the requests package
