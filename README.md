
# Instagram Direct Message Automation Using Selenium

### This Python script automates the process of sending direct messages (DMs) on Instagram using the Selenium WebDriver. The script targets specific Instagram profiles and sends predefined messages to them.

## Features:

- <p>Automated Login: The script automates the login process to Instagram using provided credentials.</p>
- <p>Targeted DMs: It allows specifying a list of target Instagram profiles to send DMs to.</p>
- <p>Profile Filtering: The script filters out profiles based on a minimum followers limit, ensuring that DMs are sent only to profiles meeting certain criteria.</p>
- <p>Message Sending: It sends predefined messages to the targeted profiles.</p>
- <p>Error Handling: The script includes error handling to deal with exceptions that may occur during the automation process.</p>

## Usage:

```

#Path of your chrome web driver
chrome_webDriver_path = "path of your chrome webdriver"
#eg.- "C:\\Users\\danish\\Downloads\\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
min_followers_limit = 125
loginUsername = "yourUsername"
loginPassword = "yourPassword"
no_of_dm_to_send = 20
```

Set up the script by providing your <strong>Instagram username</strong>, <strong>password</strong>, and other parameters such as the <strong>number of DMs to send</strong>, <strong>path of your chrome webdriver</strong> and the <strong>minimum followers limit</strong>.

- Copy the message that you want to send. It'll paste the message you copied and send it.
  
Run the script, and it will automate the process of logging in, searching for target profiles, sending DMs, and handling errors.

## Dependencies:

- <strong>Selenium:</strong> A Python library used for automating web browser interaction.
- <strong>Chrome WebDriver:</strong> The script uses the Chrome WebDriver for browser automation.

<strong>Note:</strong> Before running the script, ensure you have installed the necessary dependencies and have the Chrome WebDriver installed and configured.

## Working
1. **Overview:**
   1.1 The provided script automates interactions with Instagram using the Selenium library. It performs tasks such as logging in, searching for profiles, following accounts, and sending direct messages.

2. **Setup and Configuration:**
   2.1 Importing Libraries: The script imports necessary libraries including `webdriver` from Selenium, and various modules and functions.
   2.2 Configuration Variables: Configuration variables like `chrome_webDriver_path`,  `min_followers_limit`, `loginUsername`, `loginPassword`, and `no_of_dm_to_send` are set to define parameters such as minimum follower count, login credentials, and the number of direct messages to send.

3. **WebDriver Initialization:**
   3.1 The script sets up a WebDriver for Chrome with custom options such as disabling images and plugins.

4. **Functions Definition:**
   4.1 Several functions are defined to encapsulate specific tasks like logging in, searching for profiles, following accounts, sending direct messages, etc.

5. **Main Flow:**
   5.1 The main logic is implemented in the `main_flow()` function. It iterates over a list of target Instagram accounts (`target_lst`). For each target account:
       5.1.1 It searches for the profile.
       5.1.2 Checks if the account has a sufficient number of followers (notHighProfile function).
       5.1.3 Attempts to follow the account if it hasn't been followed already.
       5.1.4 Navigates to the message section of the profile.
       5.1.5 Types and sends a predefined message to the account.
   
   5.2 The loop continues until the specified number of direct messages (`no_of_dm_to_send`) have been sent or until there are no more target accounts left.

6. **Execution:**
   6.1 The script executes the `main_flow()` function, triggering the automation process. Progress messages are printed indicating the number of direct messages sent, low-profile accounts skipped, and total targets hit.

7. **Conclusion:**
   7.1 Once the desired number of direct messages is sent or all target accounts are processed, the script terminates with an appropriate message.

### Made with ❤️ by <strong>MOHAMMAD DANISH</strong>

[Instagram](https://instagram.com/_itz_danish_ "Author's Instagram")

[Github](https://github.com/itz-danish "Author's Github")

[Linked in](https://www.linkedin.com/in/mohammad-danish-76570a24a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app "Author's Linkedin")