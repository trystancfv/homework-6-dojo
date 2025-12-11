If you have played in cybersecurity capture-the-flag (CTF) events before or have self-studied cybersecurity on [pwn.college](https://pwn.college/), you may already be familiar with how CTF challenges work: you start the challenge or access the challenge environment however it's hosted, and then you do what is hinted at in the challenge to get a string of pre-set or random text, or the "flag", to submit to get points. There are a variety of CTF challenge categories out there, such as reverse engineering, binary/server exploitation, web security, cryptography, etc. But most CTF challenges do not really cover programming/software development apart from any scripts you may write to help solve a specific challenge. This is to be expected since CTF events are grounded in testing advanced cybersecurity skills. 

We aim to take the CTF concept to create challenges that are grounded in the software engineering experience, creating a scenario-driven, gamified learning experience that can be delivered at scale. And so, **a majority of challenges on Codesafe will involve writing and modifying provided code in the VSCode workspace to complete the given tasks of a challenge, running the provided test cases through a 'checker' Python executable (often named `checker`), and getting the flag in the terminal if you have successfully completed the challenge**. 

**You will always be working in the `/challenge` folder of the environment (these descriptions will specify otherwise if needed), so you can set your VSCode workspace to only have the `/challenge` folder loaded in the left side-bar.** Revisit the first tutorial challenge if needed!

If your left side-bar in VSCode is set to only have the `/challenge` folder, you will see the following files/folder relevant to the challenge:
- `backup` - This folder will contain a non-writable copy of the original provided code that you can copy over into the file you are supposed to modify in `/challenge` if you need to start over.
- `checker` - You will run this Python executable when you want to check your current solution to the challenge. Make sure to always run it as `$ ./checker` in the terminal. The name of this file may vary per challenge. You will not always be able to read this file in VSCode, which is intentional! In some challenges, being able to read the checker script will give away the intended solution. The file permissions can be configured so that you can execute the script, but not read it.
- `DESCRIPTION.md` - This is the same description you read in the original challenge's description back on the main site.
- `modify_me.py` - You will modify this file as specified in the task of this tutorial. The name of this file will vary per challenge.

To complete this challenge, simply modify `hello_world()` in `modify_me.py` to return `"Hello World"`. After doing that, open up a terminal in the VSCode workspace and run the following commands:
```
$ cd /challenge
$ ./checker
```

**NOTE**: The VSCode workspace will not automatically refresh for you when switching to a new challenge. You will need to close out of the tab with your workspace and then open a new one after starting a new challenge.
