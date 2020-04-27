# Installing Jupyter Notebook

While Jupyter runs code in many programming languages, Python is a requirement (Python 3.3 or greater, or Python 2.7) for installing the Jupyter Notebook.

We recommend using the Anaconda distribution to install Python and Jupyter. We’ll go through its installation in the next section.

## Installing Jupyter using Anaconda

For new users, we highly recommend installing [Anaconda](!https://www.anaconda.com/distribution/). Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.

Use the following installation steps:

1. Download [Anaconda](!https://www.anaconda.com/distribution/). We recommend downloading Anaconda’s latest Python 3 version (currently Python 3.7).

2. Install the version of Anaconda which you downloaded, following the instructions on the download page.

Congratulations, you have installed Jupyter Notebook.

## Installing Jupyter using pip

As an existing Python user, you may wish to install Jupyter using Python’s package manager, pip, instead of Anaconda.

First, ensure that you have the latest pip; older versions may have trouble with some dependencies:

```console
$ pip3 install --upgrade pip
```

Then install the Jupyter Notebook using:

```console
$ pip3 install jupyter
```
