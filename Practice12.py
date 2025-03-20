#Practice debugging

#Practice try/except
def custom_ciel(user_float):

    #Test that it's a number
    try:
        new_val = user_float // 1
    except ValueError:
        print("Error: Could not round value up as is not number")
    except Exception as e:
        print(")