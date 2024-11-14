.. _api:

Library
=======

.. module:: sweetrpg_db

This part of the documentation covers all the public API for the SweetRPG
DB library. These are common functions and classes that other SweetRPG
packages make use of.


Exceptions
----------

Common exceptions.

.. autoclass:: sweetrpg_db.exceptions.ObjectNotFound

MongoDB Repository
------------------

These are some classes for interacting with MongoDB.

.. autoclass:: sweetrpg_db.mongodb.options.QueryOptions
   :members:
   :undoc-members:
   :private-members:

.. autoclass:: sweetrpg_db.mongodb.repo.MongoDataRepository
   :members:
   :undoc-members:
   :private-members:
