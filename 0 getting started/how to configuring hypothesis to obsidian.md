You need to have a [hypothes.is](https://hypothes.is) account; go to your user page there, look for 'developer' to grab your api key.

1.  Install Templater plugin in Obsidian
2.  Configure your templates folder in the **templater settings** (not 'templates') plugin page in “settings”
3.  Copy the text in the [gist at](https://gist.github.com/roamhacker/c48bca69f1520deed0ecbc8840f6241a) to a file in your templates folder for templater (however, I've already done this for you)
4.  Now you can run that script (look for the <% icon in the tool bar) and select the script you copied in.
5.  The first time it runs, it creates the Hypothesis config.md file for you with all the settings you need.

When you run this template, you will then get options on whether to extract all user annotations, annotations from a specific page, and so on.

You should probably then use the 'note refactor' plugin to split that note into smaller pieces, as appropriate. Assuming you've already used zotero to grab its bibliographic info, you might want to copy some parts into a reading note, and some parts into observation notes. 