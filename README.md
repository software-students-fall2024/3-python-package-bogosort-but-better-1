# BohanCompliment

A fun Python package that generates random compliments to brighten your day.

## Table of Contents

- [Description](#description)
- [PyPI Page](#pypi-page)
- [Installation](#installation)
- [Virtual Environment & Dependencies](#virtual-environment--dependencies)
- [Running BohanCompliment](#running-bohancompliment)
- [Examples](#examples)
- [Contributing](#contributing)
- [Author](#author)

## Description

**BohanCompliment** is a delightful Python package designed to generate random compliments. Whether you need a quick boost or want to share kind words with friends and colleagues, BohanCompliment provides a variety of functions to suit your needs. With support for multiple languages and personalized messages, it's a versatile tool for spreading positivity.

## PyPI Page

You can find **BohanCompliment** on PyPI [HERE](https://pypi.org/project/BohanCompliment/).

## Installation

Install **BohanCompliment** with pip:

```bash
pip install BohanCompliment
```

## Virtual Environment & Dependencies

Setting up the virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running BohanCompliment

After installation, BohanCompliment can be directly ran in Python scripts or interactivelty via the Python shell:

```

```

## Examples

### Function Parameters
1. name(str): The name of the person to compliment. 
2. trait(str): A specific trait to complimnet on.
3. count(int): The number of compliments to generate. 
4. language(str): the langauge code for the compliment ('en', 'es', 'fr').

### Available Functions: 
compliment(name): Retunrs a random compliment for the given name:
```
from BohanCompliment import compliment
print(compliment("Alice"))
# Output: You're an awesome person, Alice!
```

personalized_compliment(name, trait): Returns a compliment focusing on a specific trait: 
```
from BohanCompliment import personalized_compliment
print(personalized_compliment("Bob", "sense of humor"))
# Output: Bob, your sense of humor is truly remarkable!
```

multi_compliment(name, count): returns multiple compliments
```
from BohanCompliment import multi_compliment
compliments = multi_compliment("Charlie", 3)
for c in compliments:
    print(c)
# Output:
# You're a fantastic problem solver, Charlie!
# You have a great sense of humor, Charlie!
# Charlie, your code is so elegant!
```

compliment_in_language(name, language): Returns a compliment in a specific language ('en', 'es', 'fr')
```
from BohanCompliment import compliment_in_language
print(compliment_in_language("Dana", "es"))
# Output: ¡Eres increíble, Dana!

print(compliment_in_language("Eve", "de"))
# Output: Language 'de' not supported.
```

## Contributing
To contribute to this project, here are the folliwng steps:

Clone the GitHub repository
```
git clone https://github.com/software-students-fall2024/3-python-package-bowohan.git
cd BohanCompliment
```

Set up and activate the virtual environment
```
python -m venv venv
source venve/bin/activate
```

Install the required dependencies

```
pip install -r requirements.txt
```

Build and test the python package
```
python -m build
pytest
```

## Author
Bohan Hou