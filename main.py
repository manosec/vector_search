#Controlling function parameters data types
from typing import Union

#For performing algebric calculation
import numpy as np

#For parsing the command line arguments
import argparse

#Cosine Similarity
def cosine_similarity(a_vector: list[Union[int, float]], b_vector: list[Union[int, float]]) -> Union[int,float]:
    try:
        dot_product = np.dot(a_vector, b_vector)
        norm_a = np.linalg.norm(a_vector)
        norm_b = np.linalg.norm(b_vector)
        cosine_score = dot_product / (norm_a*norm_b)
        return round(cosine_score, 2)
    except TypeError as e:
        return f"Error: Please ensure that both vectors are of the correct format."


#Helper Functions

def get_vector_input(prompt: str) -> list:
    vector_str = input(prompt)
    try:
        vector = [float(item) for item in vector_str[1:-1].split(',')]
        return vector
    except ValueError:
        print("Invalid input format. Please use the format [1, 2, 3, 4]")
        return get_vector_input(prompt)

def parse_vector_string(s: str):
    
    """_summary_
    
    Command line input is parsed as string type, for processing this into float we have this helper function

    Returns:
        list(float)
    """
    return [float(item) for item in s[1, -1].split(',')]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Take Two vectors of same dimension give similarity score between them")
    parser.add_argument('--a_vector', type=parse_vector_string, help="Enter your first vector")
    parser.add_argument('--b_vector', type=parse_vector_string, help="Enter your second vector")
    
    args = parser.parse_args() 
    
    if not args.a_vector:
        args.a_vector = get_vector_input("Enter the a_vector eg:[1,2,3,4]: ")
    
    if not args.b_vector:
        args.b_vector = get_vector_input("Enter the b_vector eg:[5,6,7,8]: ")
    
    similairty_score = cosine_similarity(args.a_vector, args.b_vector)
    print(f"Similairty Score for the given vectors: {similairty_score}")
