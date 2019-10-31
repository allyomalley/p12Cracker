# p12Cracker
A simple tool to brute force a password for a password-protected PKCS#12 (PFX/P12) file
  
**Usage**

* You must supply your own wordlist for the brute forcing in text format, using whatever tool you prefer
* Supply the path to the PKCS12 file, and your wordlist of guesses to the script
    

```sudo pip install -r requirements.txt```

```python p12Cracker.py --p12-path crackme.p12 --wordlist guesses.txt```

![ScreenShot](https://raw.githubusercontent.com/allyomalley/p12Cracker/master/image_output.png)
