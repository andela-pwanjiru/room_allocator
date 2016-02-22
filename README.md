# Room_allocator [![Build Status](https://travis-ci.org/andela-pwanjiru/Room_allocator.svg?branch=feature-review)](https://travis-ci.org/andela-pwanjiru/Room_allocator) 
[![Coverage Status](https://coveralls.io/repos/github/andela-pwanjiru/Room_allocator/badge.svg?branch=feature-review)](https://coveralls.io/github/andela-pwanjiru/Room_allocator?branch=feature-review)


### Description

This is a system used to allocate offices and living spaces at Amity to Andela employees.

### Setting up the program :


Clone the repo

  ```bash
  git clone https://github.com/andela-pwanjiru/Room_allocator.git
  ```

### How to run

* To view the allocated offices
  ```bash
  python app.py --offices 
  ```

* To view the allocated livingspaces
  ```bash
  python app.py --living
  ```

* To view members in an office
  ```bash
  python app.py --get office
  ```

* To view members in a living space
  ```bash
  python app.py --get living
  ```

* To view the people not allocated offices
  ```bash
  python app.py --show employees

* To view all fellows without a livingspace.
  ```bash
  python app.py --show fellows
  ```

### How to run tests:
```bash
nosetests
```
