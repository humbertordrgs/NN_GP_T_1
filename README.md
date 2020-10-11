# Neuronal Network and Genetic Programming Task 1  

## <div style="text-align: left"> 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() 
</div>
<br>
 

This is a quickstart project with neural networks the idea behind is to learn and understand the different processes that happen inside one of these models. It is important to notice that topics like backpropagation and activation functions are not part of this Task.

## Project structure

### Environment
```
- python 3.8.3
- jupyter
- numpy 
- sklearn
- plotly
```

### Runnable Command
- To run all the unit tests asociated to data transformation use: <br> ```python -m unittest src/test/test_*.py```


### Solution Approach
This solution is based on 2 sets of experiments each for a different dataset. The original datasets can be found on:
- [Handwritten Digits](https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits).
- [Poker Hand](https://archive.ics.uci.edu/ml/datasets/Poker+Hand).

The only change made to these datasets was the replace of the delimiter character (from `','` to `' '`), for this reason we include the modified dataset inside the folder `/resource/datasets/` of this project.

### Analysis and Results
These can be found on the live version of the jupyter notebook file [link](). The project can also be executed locally given you satisfy the requirements.