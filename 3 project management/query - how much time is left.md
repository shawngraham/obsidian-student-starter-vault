# Time Left Query

This note uses the dataview plugin to look at all of the notes for metadata in the fields 'status', 'due-date', and 'date', to work out how much time remains in a task. It gives you a sense of how you might generate other kinds of queries that are useful for you.

```dataview
table status, due-date, date, (due-date - date) as Time-Left
from ""
where status
sort status desc
```