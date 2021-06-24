## Configuring the 'Related' Notes template

#difficult 

The related notes template works in the same way that the ocr template does - it opens a file input prompt, and then passes that filename to an external program for processing, then puts the result at the cursor in whatever note happens to be open. (Indeed, I copied the code pretty much verbatim, since it works so well). The python code comes from [Obsidian user raudaschl](https://forum.obsidian.md/t/find-similar-notes-python-script/9450/15) .

It uses term frequency - inverse distribution frequency to determine a 'similarity' score. You might use this to discover conceptual links between notes that you hadn't expected or noticed. 

It depends on python. One can have many different installations of python on one's machine; python uses lots of different 'packages' of code for different purposes, and sometimes these can conflict. Mac users will already have python on their machine, but you don't necessarily want to be installing new packages into the same space (because: conflicts). 

This means that getting this template to work on your own machine is going to be a bit tricky.

Assumption: for Mac or Windows, I am assuming that you already have Python installed (for best results, go get the [Anaconda individual distribution and install it](https://www.anaconda.com/products/individual).)

## Preparing your machine

Open a command prompt or terminal **in the student-starter-vault folder**. On Windows, you can find the folder in your file explorer; type `cmd` in the address bar once you've got the folder displayed. On Mac, if you haven't done this before [here are some instructions with illustrations](https://www.stugon.com/open-terminal-in-current-folder-location-mac/); if you have, then you can right-click on the folder name in your Finder, and 'open terminal at folder.'

Once the terminal opens, **double-check where you are currently working** by typing ON MAC: `$ pwd` ON WINDOWS `dir`.  If you're not in the `student-starter-vault`, you're in the wrong place (remember, the `$` sign is a convention indicating that what follows is to be entered at the command prompt or terminal prompt). 

At the command prompt or the terminal:

`$ conda create -n obsidian python=3.8`

This creates an installation of python in an environment we are creating just for working with our vault; we've called the installation 'obsidian'.

`$ conda activate obsidian`

This turns that environment on; any python we run at this point will install things into the `obsidian` environment. On my machine, this means that the python command is located at `/Users/shawngraham/opt/anaconda3/envs/obsidian/bin/python` .  You can find this by typing

mac: `$ which python`

windows: `$ where python`

Another option, on both platforms, is: `$ conda info --envs`

Take note of that information. In obsidian, got to the plugin settings for templater, and add another **user function** called `sim` ; 

Place the following text in **with the location of your python as determined above**, as the value for the `sim` function:

`/Users/shawngraham/opt/anaconda3/envs/obsidian/bin/python similarity.py "$sim_input" `

![user-function](/other-images/user-function3.png)

That's mine. Yours will be at /your-name/ etc, right?

## Installing the Python bits we need

Now, at the command line where you created and then activated the `obsidian` environment, we're going to install the python packages that we need:

`$ pip install -r requirements.txt`

When that finishes, we need to get a language model file:

`$ python3 -m spacy download en`

When that finishes, we're going to get some stopwords and a few other things with the `prep-for-similarity.py` file I created and which is in this vault. At the command prompt/terminal enter:

`$ python prep-for-similarity.py`

## Final Step

Using a [text editor](https://atom.io), open the file `similarity.py`. Change **Line 30** to have the full path of the location of your vault:

```
rootdir = "/Users/shawngraham/Documents/student-starter-vault/" #PUT THE DIRECTORY TO YOUR VAULT ROOT HERE !!!
```

On a windows machine, it might look something like

```
rootdir = "C:\Users\Draykoth\Documents\student-starter-vault\" #PUT THE DIRECTORY TO YOUR VAULT ROOT HERE !!!
```

## Enjoy 

Now, with Obsidian open on a note of interest, put your cursor at the end of the note and select the `<%` button from the toolbar. Choose `related` and select whichever file in your vault you want to find similar notes for.

Caveat: I haven't tested this on a windows machine yet, June 19 2021.