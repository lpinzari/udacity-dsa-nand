# What are Jupyter Notebooks ?

The [jupyter](!https://jupyter.org/) notebook is a **web application** that allows you to combine *explanatory text, math equations, code, and visualizations* all in one easily sharable document. It's a way for us to **run code interactively within a web browser alongside some visualizations and some markdown text to explain the process of what's going on**. A lot of scientific institutions are using these notebooks in order to clearly explain exactly how they got the results and we can reproduce the results from within the notebooks themselves. For example, a notebook to share is the analysis of [gravitational waves from two colliding blackholes](!https://www.gw-openscience.org/s/events/GW150914/GW150914_tutorial.html) detected by the LIGO experiment. You could download the data, run the code in the notebook, and repeat the analysis, in effect detecting the gravitational waves yourself!

Notebooks have quickly become an essential tool when working with data. You'll find them being used for [data cleaning and exploration](!https://nbviewer.jupyter.org/github/jmsteinw/Notebooks/blob/master/IndeedJobs.ipynb), visualization, [machine learning](!https://nbviewer.jupyter.org/github/masinoa/machine_learning/blob/master/04_Neural_Networks.ipynb), and [big data analysis](!https://nbviewer.jupyter.org/github/tdhopper/rta-pyspark-presentation/blob/master/slides.ipynb). Here's an [example notebook](!https://github.com/mcleonard/blog_posts/blob/master/body_fat_percentage.ipynb) for a blog that shows off many of the features of notebooks. Typically you'd be doing this work in a terminal, either the normal Python shell or with IPython. Your visualizations would be in separate windows, any documentation would be in separate documents, along with various scripts for functions and classes. However, with notebooks, all of these are in one place and easily read together.

Notebooks are also **rendered automatically on GitHub**. It’s a great feature that lets you easily share your work. There is also [nbviewer](!http://nbviewer.jupyter.org/) that renders the notebooks from your GitHub repo or from notebooks stored elsewhere. This service loads the notebook document from the URL and renders it as a static web page. The results may thus be shared with a colleague, or as a public blog post, without other users needing to install IPython themselves.

## Literate Programming

Notebooks are a form of [literate programming](!http://www.literateprogramming.com/) proposed by Donald Knuth in 1984. With literate programming, the documentation is written as a narrative alongside the code instead of sitting off by its own. In Donald Knuth's words,

> Instead of imaging that our main task is to instruct a compiler what to do, let us concentrate rather on explaining to human beings what we want a computer to do

After all, code is written for humans, not for computers. Notebooks provide exactly this capability. You are able to write documentation as narrative text, along with code. This is not only useful for the people reading your notebooks, but for your future self coming back to the analysis.

## How notebooks work

Jupyter notebooks grew out of the [IPython](!https://ipython.org/) project started by Fernando Perez. IPython is an interactive shell, similar to the normal Python shell but with great features like syntax highlighting and code completion. Originally, notebooks worked by sending messages from the web app (the notebook you see in the browser) to an IPython kernel (an IPython application running in the background). The kernel executed the code, then sent it back to the notebook. The current architecture is similar, drawn out below. Image from [documentation](!https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html)

![jupyter components](./images/notebook-components.png)

The central point is the **notebook server**. You connect to the server through your browser and the notebook is rendered as a web app. Code you write in the web app is sent through the server to the kernel. The kernel runs the code and sends it back to the server, then any output is rendered back in the browser. When you save the notebook, it is written to the server as a JSON file with a `.ipynb` file extension.

Notebooks may be exported to a range of static formats, including HTML (for example, for blog posts), reStructuredText, LaTeX, PDF, and slide shows.

The notebook server, not the kernel, is responsible for saving and loading notebooks, so you can edit notebooks even if you don’t have the kernel for that language—you just won’t be able to run code. The kernel doesn’t know anything about the notebook document: it just gets sent cells of code to execute when the user runs them.

The great part of this architecture is that the kernel doesn't need to run Python. Since the notebook and the kernel are separate, code in any language can be sent between them. For example, two of the earlier non-Python kernels were for the [R](!https://www.r-project.org/) and [Julia](!https://julialang.org/) languages. With an R kernel, code written in R will be sent to the R kernel where it is executed, exactly the same as Python code running on a Python kernel. IPython notebooks were renamed because notebooks became language agnostic. The new name **Jupyter** comes from the combination of Julia (**Ju**), Python (**pyt**), and R (**r**). If you're interested, here's a list of available [kernels](1https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). A list of kernels widely used in data science is here: [data science kernels](!https://jupyter.readthedocs.io/en/latest/use-cases/data_science.html)



Another benefit is that the server can be run anywhere and accessed via the internet. Typically you'll be running the server on your own machine where all your data and notebook files are stored. But, you could also [set up a server](!https://jupyter-notebook.readthedocs.io/en/latest/public_server.html) on a remote machine or cloud instance like Amazon's EC2. Then, you can access the notebooks in your browser from anywhere in the world.

## Summary

[Doc summary](!https://jupyter-notebook.readthedocs.io/en/latest/notebook.html).

The Jupyter notebook combines two components:

- **A web application**
- **Notebook documents (files)**

### Main features of the web application

- In-browser editing for code, with automatic syntax highlighting, indentation, and tab completion/introspection.

- The ability to execute code from the browser, with the results of computations attached to the code which generated them.

- Displaying the result of computation using rich media representations, such as HTML, LaTeX, PNG, SVG, etc. For example, publication-quality figures rendered by the [matplotlib](!https://matplotlib.org/) library, can be included inline.

- In-browser editing for rich text using the [Markdown](!https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images) markup language, which can provide commentary for the code, is not limited to plain text.

- The ability to easily include mathematical notation within markdown cells using LaTeX, and rendered natively by [MathJax](!https://www.mathjax.org/)

### Notebook documents

Notebook documents contains the inputs and outputs of a interactive session as well as additional text that accompanies the code but is not meant for execution. In this way, notebook files can serve as a complete computational record of a session, interleaving executable code with explanatory text, mathematics, and rich representations of resulting objects. These documents are internally JSON files and are saved with the `.ipynb` extension. Since JSON is a plain text format, they can be version-controlled and shared with colleagues. [Details on Notebook JSON format](!https://nbformat.readthedocs.io/en/latest/format_description.html#notebook-file-format).


Notebooks may be exported to a range of static formats, including HTML (for example, for blog posts), reStructuredText, LaTeX, PDF, and slide shows, via the nbconvert command.

Furthermore, any `.ipynb` notebook document available from a public URL can be shared via the Jupyter Notebook Viewer ([nbviewer](!http://nbviewer.jupyter.org/)). This service loads the notebook document from the URL and renders it as a static web page. The results may thus be shared with a colleague, or as a public blog post, without other users needing to install the Jupyter notebook themselves.
