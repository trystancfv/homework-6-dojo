Welcome to Codesafe! Codesafe is a computer science education platform with a focus on teaching concepts and skills relevant to software engineering and software security, with the intent to also drive upskilling/reskilling for anyone looking to break into the tech industry or at least learn how to develop software and scripts for their respective professions. **Codesafe is currently under active research & development, so any feedback and participation in its research activities would be greatly appreciated!**

This platform is heavily inspired by [pwn.college](https://pwn.college/), and its behind-the-scenes is a fork off of their [DOJO](https://github.com/pwncollege/dojo) infrastructure, which in turn is heavily inspired by "capture-the-flag" (CTF) challenges in the field of cybersecurity. We aim to take the CTF concept to create challenges that are grounded in the software engineering experience, creating a scenario-driven, gamified learning experience that can be delivered at scale. For more information, please check out the main page of this site or reach out to `skngo1@uci.edu`.

**You will be interacting with Codesafe's challenges through a provided workspace that can be accessed directly in your browser. The workspace is a Visual Studio Code (VSCode) development environment to mimic the main experience of developing code.** "Start" this challenge, and then you can interact with it by clicking on "Workspace" in the site's navigation bar or "VSCode Workspace" in the pop-up after the challenge has successfully started. 

If you are unfamiliar with VSCode, here are the quick basics to get going:
- *To open a terminal*: Click on the three-lines icon at the top-left, hover over "Terminal", and click "New Terminal".
- *To open up a specific folder in the left-hand sidebar*: Click on the three-lines icon at the top-left, hover over "File", click on "Open Folder...". In the pop-up, you can then specify the folder you want to open up.
    - When opening up the VSCode workspace for the first time, you should be able to simply click on "Open Folder" to get to the pop-up.
- *If you'd like to change it to dark-mode*: Click on the gear icon at the bottom-left, hover over "Themes", click "Color Theme", and click on one of the themes listed under "dark themes".

**For each challenge, make sure to read these descriptions! They will often have instructions to help you get started and also teach you something new.**

To complete this challenge, open up a terminal in the VSCode workspace and then run the following commands:
```
$ cd /challenge
$ ./start_here
```

'start_here' is a Python script you can directly execute, and it will give you the flag to complete this tutorial challenge. The flag can then be copy-pasted into the "Flag" input box in the challenge's drop-down (right below the "Start" button) to complete the challenge. Your goal in each challenge is to follow the instructions and complete what is asked to get the flag.

You should be able to copy-paste the flag from the VSCode workspace terminal to the main site.

**NOTE**: You are also able to run `start_here` by doing `$ python3 start_here` in the `/challenge` folder. This is usually fine, but for this environment and platform, due to how permissions are handled so that you cannot simply read the flag, you MUST run `start_here` by doing `$ ./start_here` so that it can successfully read the flag and print it in the terminal. If you use `$ python3 start_here`, it will execute but will be unable to read the flag.

In addition, you won't always be able to read everything in the `/challenge` folder. We will explain more in the next  tutorial.
