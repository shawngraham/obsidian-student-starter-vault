---
creation date: <% tp.file.creation_date() %>
tags: [similarity]
---

A 'score' of 1 or text_similarity of 1 is the result of comparing the note against itself. The closer a score is to 1, the more similar the text. Add `[[` and `]]`  to link to the most similar notes.

<%*
const supportedFileTypes = ["md"];
const images = this.app.vault.getFiles().filter((item) => supportedFileTypes.indexOf(item.extension) >= 0)
const target = await tp.system.suggester((item) => item.path, images, true);
const out = await tp.user.sim({sim_input: target.path});
%><%* tR += out %>
