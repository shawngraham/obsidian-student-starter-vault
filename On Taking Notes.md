## Atomic Notes

The idea is that you keep one idea in one note. But by linking text as appropriate from one card to another, you build up a web of knowledge. As things connect, clusters of ideas emerge. I started down this way of notekeeping when I read this [post by Dan Sheffler](http://www.dansheffler.com/blog/2015-05-05-the-zettelkasten-method/), on the '[Zettelkasten Method](https://zettelkasten.de/introduction/)'. 

> A Zettelkasten is a personal tool for thinking and writing. It has hypertextual features to make a web of thought possible. The difference to other systems is that you create a web of thoughts instead of notes of arbitrary size and form, and emphasize connection, not a collection.

When you open the links panel, Obsidian will show you 'backlinks' or 'outgoing links', or notes that are linked to the present note in either direction; if there is a string of exact text in another note's filename, that will turn up in the 'unlinked mentions' panel, and you can then click on the link button; the `[[` and `]]` will appear automatically in your note in the right place. In this way, structure emerges as you take more notes.

Notes have metadata using the YAML format. Using the templates, you'll always have consistent metadata fields for your notes. YAML looks like this:

```
---
tags: #enchantment
date: 2021-06-16
project: hist5706-paper1
---
```



## Transclusion aka Embedding

**Because** each note is a single idea, you can create overview notes on larger ideas by integrating the smaller pieces as is useful. Sometimes people do this to create 'maps of content'; I like to do it when I'm trying to build up a piece of writing. 

You can embed a note by putting the ! in front of it, eg

![[finding connections]]

You won't see the text unless you hit the preview button.

## Starred Search 

Create a search you like; hit the star button to save it. You can also copy the search results and paste them into a note with wikilinks.

## Journey Plugin 

The journey plugin finds the shortest path through your vault (see the plugin's info for more on customizing this), and returns the pages to you so you can place them in a note; put the ! in front of them, write the connective tissue you need, and you might have a quite substantial piece of writing ready to go.

## Dataview 

The dataview plugin is installed; it allows you to create queries that you can embed in a note; these will update when you hit the preview button for that note. Two examples are in the project management folder; you can also find more (and more complex) query examples at the community pages at [obsidian.md](https://obsidian.md).

## A Possible Workflow 

Reading notes - that is, an overview on the source - should go in the reading notes folder.

Observations or atomic notes can go in the observations folder

Notes about your workflow, your projects, can go in your project management folder.

The flow is:

read -> take notes -> make a 'reading' note about the source as a whole -> refactor notes from other sources into atomic notes -> make new atomic notes -> look for connections -> make connections -> compile notes that speak to big ideas into overviews -> use the overviews as the nucleus for your formal writing

### Notes from Zotero into Obsidian
- When you encounter resources on the web, use Zotero to grab the bibliographic information, and the pdf if there is one around. 
- Use zotfile + zotero to push the pdf to a table if you have one; annotate the reading using whatever pdf reader you use. Zotfile can then retrieve your annotations and add them as notes attached to the resource in zotero.
- The mdnotes plugin for zotero can liberate those notes as markdown and save them into your obsidian vault 
- Export your bibliography in using the better bibtext plugin's 'better csl json' format to the `_bib` folder here; you'll do this periodically as your bibliography gets longer. (You can also force the citation plugin to renew its read of that file, see [[how to configure citation template]]. 
- use the refactor note settings (hit ctrl+p, then type 'refactor') to split the annotations up into separate atomic notes. 
- you can create new overview notes for your readings by using the command palette, and selecting 'citation: open literature note'. 
- see [[how to configure citation template]]

### Notes from Hypothes.is
- hypothes.is is a web plugin that enables you to annotate any web text or pdf in your browser
- you need to have an account at [https://hypothes.is](https://hypothes.is), then get your 'developer key' (available through your account page)
- make a new empty note
- use the `<%` button to select 'hypothesis'; the first time you run it it will want your developer key. Then, when you select it, it will ask you which page or what notes do you want to grab; follow the prompts.
- the result will be dumped into the empty note _or into whatever note is open at your cursor_
- use the refactor command to turn it into atomic notes.

### Notes as you read other sources 
- make a new note, insert template 'atomic-note' for your observations
- make a 'reading note' for an overview of the entire source; name it with the @ sign convention, follow the template

For all notes, you'd be well advised to insert the markdown citation (ctrl+p, citations, markdown citation) that's relevant so you don't lose track of things.

### Connection Phase 
- You can do this at any point, of course, but use the links pane (backlinks, outgoing links) to spot connections
- Put the cursor at the end of your note and then run the 'related notes' template by hitting the `<%` button and then selecting 'related' (see [[Configuring the related notes template]]); examine the results, and put `[[` and `]]` around the ones you want to link to.
- Use the 'journey' plugin to see if there are any paths between two separate ideas/atomic notes that are worth exploring. Such paths can become 'overview notes' if you copy the results into a new note, and then put the `!` in front of the wikilinks.
- Use note refactor to break atomic notes up if it seems like there's too much going on; delete or combine notes as seems appropriate. Think of all this as gardening.

### meta notes 
- use the daily notes as a kind of log of what you are up to on any given day; you never know when that might be useful
- I also use daily notes to remember _how_ I did things, or what kinds of searches or queries I used on different databases to find things. 
- These can also be linked into everything else when it seems appropriate
- There's a kanban board for turning your tasks into actionable things; I like having three columns, 'to do', 'doing', 'done' and I move (click and drag) items from one to the other as I get them done.
- There are also some demo queries in the project management folder; if you view them with editing turned on, you'll see how they work - basically, they examine every note's metadata and create tables from that. When preview is turned on, this runs the queries and you can see the results. The ''[[query - how much time is left]]'' query imagines you making a 'project note' to keep track of say an assignment, with a 'due date' in the metadata. The '[[query - what has been cited where]]' query keeps track of which resources you have used for what project, when you add a 'project: ' tag element to that resource's metadata
- you can also make notes from the search results. Do a search, then hit the copy results button. You can paste the results into a note. 