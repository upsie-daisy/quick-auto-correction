<h1><i><code>Quick-Auto-Correction</code></i>  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">
</h1>

<p>A Stupid Script to Correct Words in your Python Code</p>

<h2><i>Installation :</i></h2>

```bash
git clone https://github.com/upsie-daisy/quick-auto-correction
```

<h2><i>Example :</i></h2>

```python
from auto_correction import auto_correction

print("Input : ", end="")
user_input = input()

correct_words = ["Hello", "Hi", "Good Morning", "Good Evening", "Upsie", "Hey", "Bye", "Good Bye"]
auto_corrected = auto_correction(user_input, correct_words)

print(f"Did you mean \"{auto_corrected}\" ?")
```

<p>Result : </p>

<img src="https://media.giphy.com/media/QBz5zLTrWsWmCyqjLo/giphy.gif">

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/IlIIlIIllIlI) 
