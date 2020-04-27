# Notebook Interface

Once the Notebook server is started we can create a new notebook by clicking on the **New** button on the up-right of the dashboard. The **New** pull down menu presents a list of choices that are available.

![New notebook](/images/new-notebook.png)

To create a notebook where the coding is in the Python language select the `Python 3` option. After the selection, the browser should open a new tab and we would see something like the following.

![New notebook interface](/images/new-notebook-interface.png)

We have created a new Jupyter Notebook and are in its display. The logo is there. At the top you see the title default name `Untitled`. Click on this to rename the notebook (so that renames our ipython notebook file). There is an `(autosaved)` marker that tells you Jupyter has automatically started your notebook to disk (and contitnue to do so regularly as you work on it). If you need any Help to walkthrough the interface I would recommend to click on the `help` section and select the `User interface tour` option.

Below the menu bar you will see a little box outlined in *green*. This is called a **cell**. Cells are where you write and run code. You can also change it to render Markdown, a popular formatting syntax for rendering web pages. I'll cover Markdown later. We also notice a *pencil* in the grey area below the python logo on the top-right of the screen. The *pencil* indicator tells you that the Notebook is in the **Edit** mode.

The Notebook has two modes **Edit** mode and **Command** mode. I'll cover the Command mode later but for now it is important to know that we can switch to the Command mode by pressing `esc` or clicking outside of the input text area. In this mode, no icon is displayed in the indicator area (i.e the *pencil* icon disappeared) and the border around the currently active cell is `blue`. The command mode allows us to perform **Actions** like adding and deleting cells. You can switch back to the Edit mode by hitting the enter key (`return`) or clicking in the input text area of the cell.

To run the code within an active cell you have a number of options available in the `Cell` menu. The `Cell` menu has the following choices:

![Cell choices](/images/choices.png)

For example, if you want to run the current cell and insert a new cell below the output then the `Run Cells and Inset below` option is selected. Another way to run this command is clicking the black arrow icon in the toolbar or the **keyboard shortcut** `option`+`return`. All the available keyboard shortcuts are listed in the `help` section menu by clicking on the option `keyboard shortcuts`. The example in the figure below shows the execution of the code `print ("Hello world")`.

![hello world](/images/first-example.png)

When you run a code cell, the output is displayed below the cell. The cell also gets numbered, you see `In [1]:` on the left. This lets you know the code was run and the order if you run multiple cells. Running the cell in Markdown mode renders the Markdown as text.

### The tool bar
Elsewhere on the tool bar, starting from the left:

- The anachronistic symbol for "save," the floppy disk. Saves the notebook!
- The + button creates a new cell
- Then, buttons to cut, copy, and paste cells.
- Run, stop, restart the kernel
- Cell type: code, Markdown, raw text, and header
- Command palette (see next)
- Cell toolbar, gives various options for cells such as using them as slides

### Command palette
The little keyboard is the command palette. This will bring up a panel with a search bar where you can search for various commands. This is really helpful for speeding up your workflow as you don't need to search around in the menus with your mouse. Just open the command palette and type in what you want to do.

### More things

Over on the right is the kernel type (Python 3 in my case) and next to it, a little circle. When the kernel is running a cell, it'll fill in. For most operations which run quickly, it won't fill in. It's a little indicator to let you know longer running code is actually running.

Along with the save button in the toolbar, notebooks are automatically saved periodically. The most recent save is noted to the right of the title. You can save manually with the save button, or by pressing `escape` then `s` on your keyboard. The `escape` key changes to command mode and `s` is the shortcut for "save." I'll cover command mode and keyboard shortcuts later.

In the "File" menu, you can download the notebook in multiple formats. You'll often want to download it as an HTML file to share with others who aren't using Jupyter. Also, you can download the notebook as a normal Python file where all the code will run like normal. The Markdown and reST formats are great for using notebooks in blogs or documentation.
