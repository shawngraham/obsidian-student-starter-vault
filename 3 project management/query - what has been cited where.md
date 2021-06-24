
# What has been cited where?

This note uses the dataview plugin to look at the reading notes folder and retrieve any note there that has been tagged with the abbreviation for the project that it might be used with.

This depends on keeping projects and readings properly tagged.

```dataview
table authors, title, project
from "1 reading notes"
where project
```