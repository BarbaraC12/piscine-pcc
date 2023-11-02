# Training Piscine Python for datascience - 0 Starting

## New rules from the exercice 05

- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script:
```python
def main():
    # your tests and your error handling
if __name__ == "__main__":
    main()
```
- Any exception not caught will invalidate the exercices, even in the event of an error that you were asked to test.
```python
try:
    try:
        if cond is False:   #Si condition fausse
            raise AssertionError("Que c'est il passé?")
        n = int(args[1])    # cas ou args[1] n'est pas un digit = erreur
    except ValueError:      # Si une erreur survient
        raise AssertionError("Message d'erreur")
    suite()                 # Si il n'y a pas d'erreur continue

except AssertionError as err:
    print(AssertionError.__name__ + ":", err)
```
- All your functions must have a documentation (__doc__)
```python
def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """
   
    return argument1

print(some_function.__doc__)
```
- Your code must be at the norm flake8:
  -  Installation: `pip install flake8`
  -  In zshrc/bashrc: `alias norminette=<path to flake8>`

