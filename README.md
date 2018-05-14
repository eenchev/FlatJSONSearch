FlatJSONSearch
=====


## What is FlatJSONSearch:

Iterates over a directory of (several levels nested) JSONs. Checks if the key, passed as an argument exists.

Say we have file called `hello.json` with the following content:
```json
{
   "glossary":{
      "title":"example glossary",
      "GlossDiv":{
         "title":"S",
         "GlossList":{
            "GlossEntry":{
               "ID":"SGML",
               "SortAs":"SGML",
               "GlossSee":"markup"
            }
         }
      }
   }
}
```
Executing the script with "SortAs" as key parameter:

```bash
evgeni@x:~$ python ./flat_json_search.py -k "SortAs"
```
will result in the following output:
```bash
Found in file hello.json:
Key: glossary_GlossDiv_GlossList_GlossEntry_SortAs, Value: SGML

```
Note how the nested key sequence is transformed to a snake_case variable name for the final key.

Additional features:
* Filter by value, corresponding to the key, using the `-v` flag
* Set directory path via the `-d` flag