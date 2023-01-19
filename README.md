# Fetch Rewards Coding Assessment - Machine Learning Engineer

## Requirements
Docker

## Setup Instructions
1. Clone this repository 
```bash
$ git clone https://github.com/ShivaSankeerth/assignment_fetch_rewards_mle.git
$ cd assignment_fetch_rewards_mle
```
2. Build Image
```bash
$ docker build -t fr_mle_assignment .
```
3. Start flask app
```bash
$ docker run -it -p 4500:4500 fr_mle_assignment
```
## Running
1. Open [http://localhost:4500/](http://localhost:4500/). 

2. Submit the form after specifying Image dimensions and Corner points as shown below

### 1. Image dimensions
```python
    (3, 3)
```

### 2. Corner Points
```python
    [
        (1.5, 1.5),
        (4.0, 1.5),
        (1.5, 8.0),
        (4.0, 8.0)
    ]  
```

## Output
'''
Result for input: image_dimensions = (3, 3) , corner_points = [(1.5, 1.5), (4.0, 1.5), (1.5, 8.0), (4.0, 8.0)] is : [[1.5, 1.5], [2.75, 1.5], [4.0, 1.5], [1.5, 4.75], [2.75, 4.75], [4.0, 4.75], [1.5, 8.0], [2.75, 8.0], [4.0, 8.0]]
'''
<!-- 
Fetch Rewards MLE Assessment

1. Converted the Corner points into an numpy array allowing me to get min and max co-ordinates for each axis faster
2. Used np.linspace to get evenly spaced points between x_min and x_max . Here I used the y-axis part of the image dimension to get the number of samples
3. Similarly used np.linspace to get evenly spaced points between y_min and y_max using the x-axis part of the image dimension to get the number of samples
4. Now, using np.meshgrid we create a rectangular grid out of two given one-dimensional arrays and get the x,y coordinates of the grid.
5. Now both the x and y co-ordinates are stacked along the y-axis using np.stack and then reshaped such that each element as only 2 values representing a co-ordinate point -->