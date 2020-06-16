## Source of the *Satoshi Village* blog

[_Satoshi Village_](https://blog.dhimmel.com) is [Daniel Himmelstein](http://dhimmel.com)'s personal blog.

The blog is created using [Pelican](http://docs.getpelican.com/) -- a static site generator, written in Python.
This program allows posts to be written in markdown and easily converted into html pages.

The theme is a slightly modified version of [Pelicanyan](https://github.com/thomaswilley/pelicanyan),
which is a port of Jekyll's [Lanyon Theme](https://github.com/poole/lanyon/).

The blog is hosted using [GitHub Pages](https://pages.github.com/),
which serves the `gh-pages` branch of the repository.
The custom subdomain of `blog.dhimmel.com` is specified in top-level `CNAME` file of `gh-pages`.

## Usage

Install the conda environment for generating the blog with:

```sh
conda env create --file environment.yml

# or if already exists and should be updated
conda env update --file environment.yml
```

Activate the environment using `conda activate blog`.

Run `pelican content/` to process the posts and export the HTML pages to `output`.

To view the blog locally use:

```sh
cd output
python -m http.server
```

Deploy to GitHub pages using:

```sh
ghp-import --push output
```
