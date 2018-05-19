# TF-Generator
Generator of multi-extremal test functions.

## Methods for constructing test functions:
1) The Bocharov and Feldbaum Method (the minimum operator is used) [(paper)](http://www.mathnet.ru/links/971da2f0ea009a71298d2c4fa1ccd381/at11985.pdf).
2) Hyperbolic potential functions.
3) Exponential potential functions.

These methods allow you to fully control the value of the function and the position of each extremum.
Functions constructed in this way are great for testing global optimization algorithms.

Software Features:
 - export parameters test function from a json file;
 - constructing a 3D representation of a function;
 - plotting isolines (lines of equal levels);
 - construction of linear sections of the function;
 - constructing function graphs with noise;
 - saving data in json format.
 
 ## Example
 
 1) `examples_tf_json/min/f5` - Bocharov-Feldbaum function
 ![alt text](https://github.com/redb0/tf-generator/blob/master/examples_tf_json/min/f5/f5.png)
 ![alt text](https://github.com/redb0/tf-generator/blob/master/examples_tf_json/min/f5/f5_k_sn%3D10.png)
 json file content
 ```json
{
    "index": 5,
    "dimension": 2,
    "type": "feldbaum_function",
    "number_extrema": 10,
    "coordinates": [
        [-2, 4], [0, 0], [4, 4], [4, 0], [-2, 0],
        [0, -2], [-4, 2], [2, -4], [2, 2], [-4, -2]
    ],
    "func_values": [0, 3, 5, 6, 7, 8, 9, 10, 11, 12],
    "degree_smoothness": [
        [0.6, 1.6], [1.6, 2], [0.6, 0.6], [1.1, 1.8], [0.5, 0.5],
        [1.3, 1.3], [0.8, 1.2], [0.9, 0.3], [1.1, 1.7], [1.2, 0.5]
    ],
    "coefficients_abruptness": [
        [6, 6], [6, 7], [6, 7], [5, 5], [5, 5],
        [5, 5], [4, 3], [2, 4], [6, 4], [3, 3]
    ],
    "constraints_high": [6, 6],
    "constraints_down": [-6, -6],
    "global_min": [-2, 4],
    "global_max": [-6, 6],
    "amp_noise": 13.69,
    "min_value": 0.0,
    "Max_value": 27.38
}
 ```
 The function has 10 minima. The global minimum is at the point (-2, 4).
 
 2) `examples_tf_json/hyperbolic_potential/f4` - hyperbolic potential function

 ![alt text](https://github.com/redb0/tf-generator/blob/master/examples_tf_json/hyperbolic_potential/f4/f4_with_ksn%3D10.png)

 3) `examples_tf_json/exponential_potential/f2` - exponential potential function

 ![alt text](https://github.com/redb0/tf-generator/blob/master/examples_tf_json/exponential_potential/f2/f2_with_ksn%3D10.png)
 
 
