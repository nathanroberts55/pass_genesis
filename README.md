<i>Created By: Nate Roberts</i> <br>
<i>September 5, 2020</i>

<h1>Password Genesis</h1>

<h2>Generator.py</h2>
<p>Password generator to help create strong random passwords. User can determine the length and complexity of their passwords based on use of letters, numbers, and special characters</p>

<h2>Common_Pass.py</h2>
<p>Takes user input and checks password against list of commonly used passwords. User password is passed to the pwnedpassword API for comparison. For more details about the pwnedpassword API click <a href="https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/">here</a></p>

<h2>Strength_Check.py</h2>
<p>Users can pass in a password and/or password policy. This script can test the strenth/complexity of a password, and if given a password policy, can test the password against the password policy requirements. When compared against the password policy the script can say which parts of the policy the password fails.</p>

<h2>Test_Generator.py</h2>
<p>Test cases written to check the basic functionality of password generator methods.</p>

<h2>Test_Common_Pass.py</h2>
<p>Test cases written to check the basic functionality of common password checker methods.</p>