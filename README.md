# `act` demo

A ~10min intro to [act](https://github.com/nektos/act) for linux or macos

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Demo](#getting-started-demo)
- [Links](#links)
- [Thank you](#thank-you)

---

## [Installation](https://nektosact.com/installation/)
e.g. via homebrew
```bash
brew install act
```

### Recommended: Install **GitHub Local Actions** 
[GitHub Local Actions](https://sanjulaganepola.github.io/github-local-actions-docs/) is an extension for act on VS code and it is awesome. This is an optional but highly recommended step. 

---

## Requirements
**A running container!**

Below is a quick example of installing and starting a docker engine with colima (see [colima-demo](https://github.com/angelphanth/colima-demo/blob/main/README.md) for more info ☺️)

### Install colima 
```bash
brew install colima
```

### Install docker
```bash
brew install docker
```

### Start up docker
```bash
colima start
```


> [!TIP]
> For act+colima, you may need to set up `$DOCKER_HOST` via your shell profile (e.g., in `~/.zshrc` add `export DOCKER_HOST="$HOME/.colima/default/docker.sock"`) or set up a symlink
> e.g. `sudo ln -s ~/.colima/default/docker.sock /var/run/docker.sock`
> Check out the [colima FAQ](https://colima.run/docs/faq/#cannot-connect-to-docker-daemon-error)

---

## Getting started demo
1. Run a job 
```bash
act -j test
```

2. Trigger an event
```bash
act pull_request
```

3. Now try running jobs from the GitHub Local Actions

---

## Links
- [act docs](https://nektosact.com/)
- [act GitHub repo](https://github.com/nektos/act)
- [GitHub Local Actions extension](https://sanjulaganepola.github.io/github-local-actions-docs/)
- [intro to ci/cd](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- [intro to GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)


## Thank you 
Thank you to the above resources and for your attention :) 
