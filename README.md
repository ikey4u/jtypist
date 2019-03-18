# Jtypist

JSON for typist

If you have ever tried to configure some software options,
you may think about JSON format which looking like the below

    {
        "a": {
            "b": {
                "c": {
                    "d": "good man!",
                    "e": "not so bad!\nnot so bad!\nnot so bad!\nnot so bad!\nnot so bad!"
                },
                "f": "awesome!\npigger!",
                "g": {
                    "h": {
                        "i": "oh really?"
                    },
                    "k": "haha",
                    "m": "look me"
                }
            },
            "t": "get up"
        },
        "e": {
            "g": "error"
        },
        "k": "10",
        "m": ""
    }

However, it is tedious to write countless double quote, colon ...

To make the life easy, it costs me for about one day to find a new way
to write JSON data manually efficiently. Finally, i make it.

Now, you may use only tab(consist of spaces) and dash(-) to write json format data quickly
and clear. Take the JSON data above, you can rewrite is as following

    - a
        - b
            - c
                - d
                    good man!
                - e
                    not so bad!
                    not so bad!
                    not so bad!
                    not so bad!
                    not so bad!
            - f
                awesome!
                pigger!
            - g
                - h
                    - i
                        oh really?
                - k
                    haha
                - m
                    look me
        - t
            get up
    - e
        - g
            error
    - k = 10
    - m


All of the key and values are string, a value may be composed of multiple lines,
Value of a key should indent for a specified length than the key.

In some cases, you just want the key and value in one line, its easy!
You just need to separate the key and value with an equal symbol(=).

# API

see the codes.
