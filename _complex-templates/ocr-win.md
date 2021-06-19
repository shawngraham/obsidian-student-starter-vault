---
creation date: <% tp.file.creation_date() %>
tags: [OCR]
---
```
<%*
const supportedFileTypes = ["jpeg", "jpg", "png"];
const images = this.app.vault.getFiles().filter((item) => supportedFileTypes.indexOf(item.extension) >= 0)
const target = await tp.system.suggester((item) => item.path, images, true);
const out = await tp.user.ocr_win({ocr_input: target.path.replace('/', '\\')});
%><%* tR += out %>
```

