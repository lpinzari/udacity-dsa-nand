# Markdown cells

As mentioned before, cells can also be used for text written in Markdown. Markdown is a formatting syntax that allows you to include links, style text as bold or italicized, and format code. As with code cells, you press `Shift` + `Enter` or `Control` + `Enter` to run the Markdown cell, where it will render the Markdown to formatted text. Including text allows you to write a narrative alongside your code, as well as documenting your code and the thoughts that went into it.

You can find a nice markdown cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#videos).

### Math expressions

You can create math expressions in Markdown cells using [LaTeX](https://www.latex-project.org/) symbols. Notebooks use MathJax to render the LaTeX symbols as math symbols. To start math mode, wrap the LaTeX in dollar signs `$y = mx + b$` for inline math. For a math block, use double dollar signs,

```
$$
y = \frac{a}{b+c}
$$
```
Here is a simple [tutorial](https://www.latex-tutorial.com/) on how to use it.

![latex example](/images/math_latex.png)

After pressing `Shift` + `Enter`, or run cells in the menu.

![latex rendering](/images/math_latex_2.png)
