# Problem Statements -
1. Problem Statement 1 : In a file called `emojize.py`, implement a program that prompts the user for a `str`in English and then outputs the “emojized” version of that `str`, converting any codes (or aliases) therein to their corresponding emoji.
2. Problem Statement 2 : Among the fonts supported by FIGlet are those at [figlet.org/examples.html](http://www.figlet.org/examples.html). FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).
    
    In a file called `figlet.py`, implement a program that:
    
    - Expects zero or two command-line arguments:
        - Zero if the user would like to output text in a random font.
        - Two if the user would like to output text in a specific font, in which case the first of the two should be `f` or `-font`, and the second of the two should be the name of the font.
    - Prompts the user for a `str` of text.
    - Outputs that text in the desired font.
        
        If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.
        
3. Problem Statement 3 : In a file called `adieu.py`, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one `and`, three names with two commas and one `and`, and � names with �−1 commas and one `and`, as in the below:
    
    ```python
    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
    ```
    
4. Problem Statement 4 : In a file called `game.py`, implement a program that:
    - Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
    - Randomly generates an integer between 1 and , inclusive, using the `random` module.
    - Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        - If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
        - If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
        - If the guess is the same as that integer, the program should output `Just right!` and exit.
5. Problem Statement 5 : In a file called `professor.py`, implement a program that:
    - Prompts the user for a level, . If the user does not input `1`, `2`, or `3`, the program should prompt again.
    - Randomly generates ten (10) math problems formatted as `X + Y =` , wherein each of `X` and `Y` is a non-negative integer with  digits. No need to support operations other than addition (`+`).
    - Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
    - The program should ultimately output the user’s score: the number of correct answers out of 10.
        
        Structure your program as follows, wherein `get_level` prompts (and, if need be, re-prompts) the user for a level and returns `1`, `2`, or `3`, and `generate_integer` returns a randomly generated non-negative integer with `level` digits or raises a `ValueError` if `level` is not `1`, `2`, or `3`:
        
        ```python
        import random
        
        def main():
            ...
        
        def get_level():
            ...
        
        def generate_integer(level):
            ...
        
        if __name__ == "__main__":
            main()
        ```
        
6. Problem Statement 6 : In a file called `bitcoin.py`, implement a program that:
    - Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.
    - Queries the API for the CoinDesk Bitcoin Price Index at [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json), which returns a [JSON](https://en.wikipedia.org/wiki/JSON) object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any [exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions), as with code like:
        
        ```python
        **import** requests
        
        **try**:
            ...
        **except** requests.RequestException:
            ...
        ```
        
    - Outputs the current cost of  Bitcoins in USD to four decimal places, using `,` as a thousands separator.
