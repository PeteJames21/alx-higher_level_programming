# 0x10. Python - Network #0
A series of exercises on how to work with the `curl` Linux command.
NOTE: all Bash scripts are constrained to be a max of 3 lines long:
- First line containing the shebang
- Second line containing a comment describing the purpose of the script
- Third line containing the bash command(s)

## 0-body_size.sh
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- The size must be displayed in bytes
- `curl` must be used

## 1-body.sh
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

## 2-delete.sh
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

## 3-methods.sh
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept

## 4-header.sh
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
- A header variable `X-School-User-Id` must be sent with the value `98`

## 5-post_params.sh
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`

## 100-status_code.sh
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
Restrictions:
- You use any pipe, redirection, etc.
- You are not allowed to use ; and &&

## 101-post_json.sh
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
- The script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
