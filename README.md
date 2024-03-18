# Building The Transmitter Circuit

**Materials:**

2.2k resistor (4x)

Tacticle Switch (4x)

Jumper Cables (8+)

Assuming you already have Cyber:Bot and breadboard.

**Schematic:**

![Schematic Picture](https://github.com/Cocoiscool-531/CyberBotRadioCommunications/assets/119710842/4c10454a-b78e-42f8-880e-071b292fb477)

**Instructions (pictures coming soon):**

***Step 1:***

Connect the 4 resistors to different rows in the breadboard, and 

***Step 2:***

In the center of the breadboard, place 4 buttons in a plus configuration

***Step 3:***

Place jumper wires from the resistors to the right side of the buttons, looking from the back of the bot

***Step 4:***

Place jumper wires connecting the left side of the buttons to each pin they are designated, as shown below:
Left Button: Pin 0
Top Button: Pin 6
Bottom Button: Pin 10
Right Button: Pin 15

***Step 5:***

Now run the code to test!

# Uploading

To add this module to your project, you can either get the example project, or merge this into your own.

**Downloading example project:**

Find the most recent release on the right side of the home page, download the HEX file and upload it into the [micro:bit Micro Python Editor](https://python.microbit.org/v/3/project)

**Installing into your own project:**

Locate the most recent release on the right side of the homepage, download the radioComms.py file. Upload this file into the [micro:bit Micro Python Editor](https://python.microbit.org/v/3/project)
For this to work, you must also download the [Cyber:Bot python library](https://www.parallax.com/package/cyberbot-library-python/) and upload it in the same way.

# Older releases, Contributing, & Beta Code

**Downloading older releases:**

To download an older release, click the releases button on the right side of the screen and find the release you want, then use the instructions above to add to your project

**Want to contribute or beta test?**

If you would like to contribute, click "Fork" at the top of the page, and make the changes you would like to see in the official repo, once your done and its tested, create a pull request on your
fork and describe your changes. We will review it and either deny or accept the changes. To beta test, find if there are any current branches other than main open, and download the radioComms file. Note that these may be unstable or not work; hence why they are beta, and not part of offical releases yet.
