bouncer-filters
===============

A filter list generator for the
[Bouncer](https://github.com/afterxleep/Bouncer) SMS filtering app.

Usage
-----

1. Add words to the input list `input_list.txt`.
2. Run the program:

    ```shell
    python filter.py
    ```
3. Import the output file `output/filter_list_*.json` into Bouncer.

Configuration
-------------

### Word lists

The word lists (`word_lists/`) are used to exclude common words from
the block lists so that they aren't too sensitive. You can modify the
existing word lists or add a new one.

`word_lists/word_list_soft.txt` is based on
[this word frequency list](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction)
from Wikipedia and contains the top 2000 words from contemporary
fiction.

`word_lists/word_list_strict.txt` is based on
[this word frequency list](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt)
from `first20hours/google-10000-english` and contains a list of the
10,000 most common English words from Google's Trillion Word Corpus.

### Output

Two files are output, one for each word list described above. Choose
whichever strictness you prefer.

License
-------
This repository is licensed under the MIT license. See `LICENSE` file.

The strict word list (`word_lists/word_list_strict.txt`) is licensed as
follows:

```
Data files are derived from the Google Web Trillion Word Corpus, as 
described by Thorsten Brants and Alex Franz, and distributed by the 
Linguistic Data Consortium. Subsets of this corpus distributed by Peter 
Novig. Corpus editing and cleanup by Josh Kaufman.

Educational and personal/research use of this data is permitted under 
the LDC license, Norvig's MIT license for his contributions, and US 
fair use doctrine. I do not recommend using this data for commercial 
purposes without licensing it from the Linguistic Data Consortium.
```