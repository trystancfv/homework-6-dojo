With how the Codesafe platform is designed, particularly with how each challenge and development environment is individually provisioned to you when you start a challenge, **the code that you modify and write does NOT automatically persist between challenges and when you restart a challenge.** In addition, there is currently no one-click option to "save" your code for a challenge in-progress and then come back to it the next day - challenge instances automatically are destroyed after a few hours. 

Even after you complete a challenge, the code will not persist; this does mean that you can always come back to a challenge and practice it again, try a different approach, or even simply play around with the scenario and challenge environment.

Fortunately, there is a mechanism to save your work if you are working on a particularly difficult challenge. If you would like to save your work, there are two options to do so:
- *Option #1*: You can copy-paste your work into a file that you own and control (e.g., text doc on your own machine, Google Drive, GitHub). *We ask that you not share your solutions publicly or with others.*
- *Option #2*: You can copy the file designated for modification of a challenge to the `/home/hacker` directory. The underlying infrastructure was designed to allow this directory to be persistent for your account.

**NOTE**: As of Jun. 2025, this platform could be reset at any time while it is under heavy testing and development, so you may still lose what you have  in the `/home/hacker` directory (as all accounts are also deleted if the platform is reset). We recommend that you go with the Option #1 at this time.

To complete this tutorial challenge, create a file in the `/home/hacker` directory, either through the VSCode interface or through the command line, and name it `i_have_persistence.txt`. The text you put in there does not matter, but you can write whatever you'd like and check that it is exactly the same in a future challenge (if this is not the case, please let us know ASAP!).

After completing the above, run the `checker` script in `/challenge` as you have been instructed to do so in the previous challenge.
