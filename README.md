[![Build Status](https://travis-ci.org/IvanBrasilico/bdicttalk.svg?branch=master)](https://travis-ci.org/IvanBrasilico/bdicttalk)

## Maps a dict configuration into conversations and actions

Classes to map a sequence of commands/words and parameters, like command line interfaces or chats, in a flow or through an action. Actual implementation allows a Restful API mapping

For use in text interfaces and in chatbots. Classes for bottery integration provided.

## Also a Bottery Extension - Context and flow management for your bots views - no code - simple JSON configuration
:battery: [Bottery](https://github.com/rougeth/bottery/)  - a framework for building bots

EXAMPLE
```python
# soon
```

The complete example is packaged within this repository. The extension could manage user context, any information desired. No need to code, just map your flow to a DICT/JSON. The tests and an example application demonstrates the usage.

* [Usage](#usage)
  * [Installing](#installing)
  * [Creating a project](#creating-a-project)


## Usage
Just import it on a project. Refer to examples and tests for more information.

Bottery project example:

```python
# On app main file
from botteryext.bdicttalk
import botteryext.bdicttalk.localizations

# On patterns.py
***
# On views
from app import ch
```

### Installing
```bash
$ git clone https://github.com/IvanBrasilico/bdicttalk.git
$ cd bdicttalk
$ pip install -e . # optional, you can just put botteryext folder inside your project
```

### Creating a project 

Refer to [bottery](https://github.com/rougeth/bottery/) documentation if you want to create a bottery project

