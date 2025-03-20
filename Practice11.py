def world_clock_decorator(func):
    def wrapper(this_time):
        func(this_time)
        print("Times around the world:")
        print(f"Paris: {this_time + 8}:00")
        print(f"Tokyo: {this_time + 16}:00")
        print(f"Canberra: {this_time + 18}:00")  # Call the original function

    return wrapper  # Return the wrapper function


@world_clock_decorator
def clock_app(current_time):
    print(f"It is currently {current_time}:00!")


users_time = int(input("What time is it? "))
clock_app(users_time)
