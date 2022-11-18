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
