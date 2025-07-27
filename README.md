## Source of the *Satoshi Village* blog

[_Satoshi Village_](https://blog.dhimmel.com) is [Daniel Himmelstein](https://dhimmel.com)'s personal blog.

The blog is created using [Pelican](http://docs.getpelican.com/) -- a static site generator, written in Python.
This program allows posts to be written in markdown and easily converted into html pages.

The theme is a slightly modified version of [Pelicanyan](https://github.com/thomaswilley/pelicanyan),
which is a port of Jekyll's [Lanyon Theme](https://github.com/poole/lanyon/).

The blog is hosted using [GitHub Pages](https://pages.github.com/),
which serves the `gh-pages` branch of the repository.
The custom subdomain of `blog.dhimmel.com` is specified in top-level `CNAME` file of `gh-pages`.

## Usage

```sh
# Install the environment
uv sync

# enable pre-commit checks (once per local repo)
pre-commit install

# Build the blog to output
uv run pelican

# view the blog locally at http://localhost:8000/
uv run pelican --autoreload --listen
```

Deployment is done via CI.
