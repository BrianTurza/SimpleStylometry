# SimpleStylometry

#### Simple implemantation of extracting stylometric features for the purpose of authorship identifcation.


### Setup
 Install requirements using pip. An virtual enviroment is adviced.

``` console
$ pip install -r requirements.txt
```
Probably code below needs to be run as well.

``` python3
import nltk
nltk.download('punkt')
```

### Run

``` console
$ cd src
$ python3 classifier.py --path ../data/phenomology_of_spirit.txt;../data/unabomber.txt 
