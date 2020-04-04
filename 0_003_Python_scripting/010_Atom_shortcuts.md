# Atom Keyboard Shortcuts

**Windows Management**

| Command        | MacOS          | Description  |
| ------------- |:-------------:| -----:|
| New File   | `cmd`+`n` | Open an empty file in a new tab |
| New Window   | `shift`+`cmd`+`n` | Open a new editor window |
| Open   | `cmd`+`o` | Shows the Open File dialog, which lets you select a file to open in the editor |
| Open fuzzy file finder  | `cmd`+`t` or `cmd`+ `p` | Opens the Fuzzy Finder palette in which you can search and open files |
| Open Folder  | `cmd`+`shift`+`o` | Shows the Open Folder dialog, which lets you select a folder to add to the editor's Tree View |
| Save  | `cmd`+`s` | Saves the currently active file |
| Save As | `shift`+`cmd`+`s` | Saves the currently active file under a different name |
| Save All | `option`+`cmd`+`s` | Saves all changed files |
| Close Tab | `cmd`+`w` | Closes the currently active tab |
| Reopen Tab | `shift`+`cmd`+`t` | Reopen a recently closed tab |
| Switch Tab left | `shift`+`cmd`+`[` | Switch to the tab on the left of the current tab |
| Switch Tab right | `shift`+`cmd`+`]` | Switch to the tab on the right of the current tab |
| Close Window | `shift`+`cmd`+`w` | Closes the currently active editor window |

**Note**

- `left` is the left-arrow keyboard `<-`
- `right` is the left-arrow keyboard `->`
- `up` is the up-arrow keyboard
- `down` is the down-arrow keyboard


**Editing**

| Command        | MacOS          | Description  |
| ------------- |:-------------:| -----:|
| Cut   | `cmd`+`x` | cut the highlighted text and copy to the clipboard |
| Copy   | `cmd`+`c` | copy the highlighted text to the clipboard |
| Paste   | `cmd`+`v` | paste the text copied in the clipboard |
| Undo   | `cmd`+`z` | undo the previous command |
| Redo   | `shift`+`cmd`+`z` | reversing the undo command |
| Duplicate Line   | `shift`+`cmd`+`d` | Duplicates the line of the current cursor position and creates a new line under it with the same contents |
| Delete Line   | `control`+`shift`+`k` | Deletes the current line |
| Move Line up   | `control`+`cmd`+`up` | Moves the contents of the current cursor position up one line. If there is a line above with content, the current lines content will swap with the one above it. |
| Move Line down   | `control`+`cmd`+`down` | Moves the contents of the current cursor position down one line. If there is a line below with content, the line's content will swap with the one below it.|
| Select Line  | `cmd`+`l` | Selects the entire line the cursor's current position is in. If you want to select more lines keep pressing the same command.|
| Toggle Comment  | `cmd`+`/` | Toggles the selected text into a comment of the current grammar |
| Select All File  | `cmd`+`a` | Selects the entire file's content |
| Select Same Words  | `cmd`+`d` | If you select a word or string (instance of highlighted characters), and then hit the key combo for this command, Atom will select the next same word for you. Then you can either type directly (which will replace the old words) or use left or right arrow to append things.|
| Select All the Same Words at Once  | `cmd`+`control`+`g` | this short-cut is similar to `cmd`+`d` but it selects all the matching words or strings at once.|
| Undo selection  | `cmd`+`u` | This undoes the previous selection, like from Select Same Words.|
| Find/Replace in current document  | `cmd`+`f` | Opens up the Find/Replace panel|
| Find/Replace in project  | `control`+`cmd`+`f` | Opens up the Find/Replace in project panel|
| Find Next  | `cmd`+`g` | Toggles forward through the results of the current buffer in the file while the Find/Replace panel is active|
| Find Previous  | `control`+`cmd`+`g` | Toggles backward through the results of the current buffer in the file while the Find/Replace panel is active|
| Indent  | `tab` or `cmd`+`]` | move the highlighted text to the right |
| Unindent  | `control`+`tab` or `cmd`+`[` | move the highlighted text to the left |


**Move Cursor**

| Command        | MacOS          | Description  |
| ------------- |:-------------:| -----:|
| Go to previous word   | `option`+`left` | move cursor to previous word |
| Go to next word   | `option`+`right` | move cursor to next word |
| Go to line start  | `cmd`+`left` | move cursor to start of current line |
| Go to line end  | `cmd`+`right` | move cursor to end of current line |
| Go to start file  | `cmd`+`up` | move cursor to start of Document |
| Go to end file  | `cmd`+`down` | move cursor to end of Document |
| Go to matching Parentheses/Brackets/Braces  | `cmd`+`m` | The cursor goes to the matching top bracket that the cursor is ecapsulated in |
| Go to line  | `control`+`g` | Opens the Go To Line panel|
| Go to definition  | `cmd`+`r` | This shortcuts opens a palette that lists all the symbols (or functions) in your current file allowing you to fuzzy search and jump lines.|
