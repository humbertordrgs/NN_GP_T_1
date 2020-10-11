# Neuronal Network and Genetic Programming Task 1  
This is a quickstart project with neural networks the idea behind is to learn and understand the different processes that happen inside one of these models. It is important to notice that topics like backpropagation and activation functions are not part of this Task.

## Project structure

### Environment
```
- conda
- python 3.8.3
- jupyter
- numpy 
- sklearn
- plotly
- plotly-orca (for static rendering of charts)
```

### Runnable Command
- To run all the unit tests asociated to data transformation use: <br> ```python -m unittest src/test/test_*.py```


### Solution Approach
This solution is based on 2 sets of experiments each for a different dataset. The original datasets can be found on:
- [Handwritten Digits](https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits).
- [Poker Hand](https://archive.ics.uci.edu/ml/datasets/Poker+Hand).

The only change made to these datasets was the replace of the delimiter character (from `','` to `' '`), for this reason we include the modified dataset inside the folder `/resource/datasets/` of this project.

### Analysis and Results
These can be found on jupyter notebook file inside this project.