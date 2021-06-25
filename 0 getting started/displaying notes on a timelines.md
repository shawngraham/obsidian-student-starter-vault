# This is what a default timeline looks like:

to see the timeline, hit the preview button. 

The timeline code block looks through notes that are tagged with 'timeline'; see [[displaying notes on a timelines#^b1043f]]

```timeline
test
```


# How to make a vertical timeline

This note uses the obsidian-timelines plugin, which is a bit idiosyncratic, but it works.

To _insert_ a timeline in a note, you need to put a codeblock with the word timeline after the three backticks, then you can filter which notes you want by putting the relevant tag:

\`\`\`timeline
test
\`\`\`

You can have more than one timeline in a note:

```timeline
anothertag
```

You _should_ be able to mix notes with differnent tags, eg `test;anothertag` but that doesn't seem to work. 

# How to make a horizontal timeline

Timelines can be rendered _horizontally_. You'll need to mouse over/scroll :

```timeline-vis
tags=
startDate=1935,01,01
endDate=2035,01,01
divHeight=200
anothertag
```

There's a video showing all this at https://www.youtube.com/watch?v=_gtpZDXWcrM

## An event note

^b1043f

Use the insert template command, and select 'event'. 

On a note that describes an event, you need to have a metadata block where the tags specify timeline, and then the other relevant descriptive terms `tags: [timeline, test]`. 

And then you can continue with the note, add links, etc in regular markdown.

BUT, you need to add a bit of html to style how the points on your timeline will look:

```
<span 
	  class='ob-timelines' 
	  data-date='144-43-49-00' 
	  data-title='Another Event' 
	  data-class='orange' 
	  data-img = 'folder/image.jpg' 
	  data-type='range' 
	  data-end="2000-10-20-00"> 
</span>
```


A special note on dates:
-   `YEAR-MONTH-DAY-HOUR`
-   Only integers (numbers) are allowed in the date other then the 4 seperators `-` used to distinguish the different groupsALL 4 GROUPS must be specified however if they don't exist / not want to be shown replace them with a zero. For example if an event only has the year and the month it can be written as follows `2300-02-00-00` this will be rendered on the timeline as `2300-02` (the trailing zeros will be removed). For only a year `2300-00-00-00` -> `2300`