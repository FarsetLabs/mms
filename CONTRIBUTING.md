# How to contribute
This project was developed for the needs of Farset Labs, but may be used by any group that takes subscriptions. To
that end we will most likely drive development to suit the needs and challenges we face, but we welcome any submissions 
that may enhance the project without breaking anything

## Getting Started
Both the Server and UI components have their own README's which should detail how to get started both in the running and
development of those components. Here we'll detail the organisational process. The first steps are really straightforward

* Have a Github account
* Submit a ticket for your issue or feature, assuming one does not already exist.
  * Clearly describe the issue including steps to reproduce when it is a issue. Make sure you fill in the earliest version that you know has the issue.
* Fork the repository on GitHub.

### Making Changes
We aim to follow the [Git Flow model](http://nvie.com/posts/a-successful-git-branching-model/) as closely as possible except 
in circumstances where it simply impedes progress. 

1. Create a topic branch from where you want to base your work.
     * This is usually the `dev` branch.
     * Only target release branches if you are certain your fix must be on that branch.
1. To quickly create a topic branch based on `dev`, run `git checkout -b fix/master/my_contribution dev`.
1. Make commits of logical units.
     * Check for unnecessary whitespace with `git diff --check` before committing.
     * We like tests. Sorry (not sorry).
1. Push your branch to Github

At this point you should create a PR, referencing the Github issue in the title of your PR. From there the project leads 
will review and either ask for some changes, or merge if it's ready
