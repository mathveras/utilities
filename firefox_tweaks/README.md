# 「BROKEN」🔥 Firefox Tweaks 🦊

This Python script is used to automatically set up a selection of Firefox's `about:config` settings and extensions in order to run faster,smoothly, secure more privacy and help with productivity. I took some settings from [MakeUseOf](https://www.makeuseof.com/tag/speed-up-firefox-immediately-with-these-6-simple-tweaks/) if you wanna check it out.

## 「📝」Context & Objective

There are some `about:config` settings and extensions that I commonly use in my Firefox installations, so it can be run smoothly, secure some more privacy and even help with my productivity. As I have multiple laptops and switch/reinstall my OS very often, I wanted to automate the configuration process using a script that I could run once and everything would be set up, without the need of logging in an account.

## 「🔩」Broken

While the `about:config` settings works as intended - using the `setup_user_js` function to set up the [custom user.js](resources/user.js) - it isn't selecting the right profile. It should be **Profile: default-release** instead of **Profile: default** from `about:profiles`.

Also, no extensions are being installed at all for any of the profiles, even though the script accuses them of already being installed.

I need to understand how exactly these work. Don't know when though as by the time I'm writing that I have MANY things I have to do, so remind me if I don't come back to this project in like 6 months, alright? 🤣
