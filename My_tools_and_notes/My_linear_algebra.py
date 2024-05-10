"""
This is the python code containing the usage of some Linear Algebra properties.
Aims to show the concepts of Linear algebra and also how to implement on code
"""

#Vector
import math
from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    '''Adds corresponding elements'''
    assert len(v) == len(w), "Vectors mus be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    '''Subtracts corresponding elements'''
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    '''Sums all corresponding elements'''
    # Check that vectors is not empty
    assert vectors, "No vectors provided"

    #Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different sizes!"

    #the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    '''Multiplies every elemnet by c'''
    return [c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    '''Computes the element-wise average'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    '''Computes v_i * w_i + ... = v_n * w_n'''
    assert len(v) == len(w), "vector must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    '''Returns v_1 * v_1 + ... + v_n * v_n'''
    return dot(v,v)

def magnitude(v: Vector) -> float:
    '''Returns the magnitude (or length) of v'''
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    '''Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2'''
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    '''Comutes the distance between v and w'''
    return math.sqrt(squared_distance(v, w))
    #Or else:
    return magnitude(subtract(v, w))