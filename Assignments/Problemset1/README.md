## ProblemSet → Conditionals

1. Problem statement 1 : In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes`if the user inputs `42`or (case-insensitively) `forty-two`or `forty two`. Otherwise output `NO` .
2. Problem statement 2 : In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
3. Problem statement 3 : Web browsers, by contrast, rely on [media types](https://en.wikipedia.org/wiki/Media_type), formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an [HTTP header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is `image/gif`, and the media type for a JPEG is `image/jpeg`. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.
    
    See [developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) for common types.
    
    In a file called `extensions.py`, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
    
    - `.gif`
    - `.jpg`
    - `.jpeg`
    - `.png`
    - `.pdf`
    - `.txt`
    - `.zip`
    
    If the file’s name ends with some other suffix or has no suffix at all, output `application/octet-stream` instead, which is a common default.
    
4. Problem statement 4 : In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:
    - `x` is an integer
    - `y` is `+`, ``, ``, or `/`
    - `z` is an integer
    
    For instance, if the user inputs `1 + 1`, your program should output `2.0`. Assume that, if `y` is `/`, then `z` will not be `0`.
    
    Note that, just as `python` itself is an interpreter for Python, so will your `interpreter.py` be an interpreter for math!
    
5. Problem statement 5 : Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
    
    In `meal.py`, implement a program that prompts the user for a time and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time`. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as `#:##` or `##:##`. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
    
    Structure your program per the below, wherein `convert` is a function (that can be called by `main`) that converts `time`, a `str` in 24-hour format, to the corresponding number of hours as a `float`. For instance, given a `time` like `"7:30"` (i.e., 7 hours and 30 minutes), `convert` should return `7.5` (i.e., 7.5 hours).
    
    ```python
    **def** main():
        ...
    
    **def** convert(time):
        ...
    
    **if** __name__ == "__main__":
        main()
    ```
    
    ### I have upgraded my program to sense the time for am , pm also.
