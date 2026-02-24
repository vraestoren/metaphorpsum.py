# metaphorpsum.py
Web-API for [metaphorpsum.com](https://metaphorpsum.com) website that generates metaphor

## Example
```python
from metaphorpsum import MetaphorpSum

metapsum = MetaphorpSum()
sentences = metapsum.get_sentences(count="")
print(sentences)
```
