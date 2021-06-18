- this uses zotero
- in zotero, export your library as `better csl-json`. You'll need the better bibtex plugin for zotero installed in zotero.
- save that .bib file in a new folder in the folder you're using as your vault (say for instance, ./bib)
- go to obsidian settings, turn off safe mode, enable community plugins, find, install, and enable the citations plugin
- go to the citations settings.  Give it the path to your bib file, eg `bib/demo.json`. If it finds your jsn file, it'll tell you how many items are in the library right away
- if you update your zotero library, export it anew and drop it in again. then go into the plugin settings, erase a few characters of the path then type them back; this will force the plugin to reload your new bib.
- by default, it'll make all new notes have the citation key for the reference as the name of the note.
- after you modify the template for a 'literature note' (see below), 
	- you can create new overview notes for your readings by using the command palette, and selecting 'citation: open literature note'. 
	- you can insert citation links by using the command palette, and selecting 'citations: insert literature note link' or by typing `[[@` which will bring up the quick selector and you'll be able to select the reference you want to link to.
- go to the citations settings, and modify the template for a 'literature note' with all of the following:


---
title: {{title}}
authors: {{authorString}}
year: {{year}}

tags: 
date: {{date}}
---

{{title}}

[Open in Zotero]({{zoteroSelectURI}})


### Summary

### Own thoughts

### Related topics / notes