def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)

#kwargs automatically is a dictionary.