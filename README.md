Complete project setup
----------------------

- [ ] Initialise a git repository in this directory
- [ ] Create a repository on [GitHub](https://github.com/OpenUpSA) and add as a remote to this repository
  - e.g. `git remote add origin git@github.com:OpenUpSA/end_to_end_test.git`
- [ ] Enable Continuous Integration checks for the GitHub Repository at [travis-ci.org](https://travis-ci.org)
- [ ] Enable code coverage reporting for the project at [codecov.io](https://codecov.io)
  - [ ] Enable GitHub integration - it automatically configures Travis-CI and shows coverage diffs in pull requests
  - [ ] Verify that you see coverage % on the Commits tab for the project. If it's just zero, check for errors by clicking a commit item.


Running tests
-------------

    docker-compose run --rm web python manage.py test

Tests might fail to connect to the databse if the docker-compose `db` service wasn't running and configured yet. Just check the logs for the `db` service and run the tests again.

## Coverage

Ensure the host directory where docker-compose is run from is writable by the UID inside the container. The easiest way to do that is to make it globally-writable, e.g. `chmod 777 .` but be aware of the security implications of this.

Adding dependencies using Pipenv
--------------------------------

Run the container as root to have permission to change files

    docker-compose run -u root web bash

and in that shell install what you need
