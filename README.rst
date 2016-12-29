Checkers
========

`Draughts <https://en.wikipedia.org/wiki/Draughts>`_ or checkers is a group of strategy board games for two players which involve diagonal moves of uniform game pieces and mandatory captures by jumping over opponent pieces.

Game features
-------------

* Fully responsive design
* Custom size of the board

Demo
----

You can see it in action right here: `6x6 <https://checkers-game.herokuapp.com/board/6>`_, `8x8 <https://checkers-game.herokuapp.com/>`_, `10x10 <https://checkers-game.herokuapp.com/board/10>`_.

Development
-----------

Clone repository, set up python virtual environment and install dependencies:

.. code:: sh

  $ cd checkers
  $ virtualenv -p python3 venv
  $ . venv/bin/activate
  $ pip install -r requirements.txt
  $ python run.py

To create a new requirements file from a known working environment, use:

.. code:: sh

  $ pip freeze > requirements.txt

Tests
-----

.. image:: https://circleci.com/gh/rafaltrzop/checkers.svg?style=svg
    :target: https://circleci.com/gh/rafaltrzop/checkers

To run tests on your local machine type:

.. code:: sh

  $ python setup.py test
