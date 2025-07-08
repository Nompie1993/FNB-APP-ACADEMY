try:
    print(x)
    
    except NameError:
    print("Variable 'x' is not defined. Please define it before using.")    
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
    
    x= -1
    
    if x<0:
        raise Exception("Negative value error: x cannot be negative.")  