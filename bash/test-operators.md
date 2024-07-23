| File test operator    | Use                                           |
| ---                   | -----------                                   |
| -d                    | Test if a directory exists                    |
| -e                    | Test if a file exists                         |
| -r                    | Test if a file exists and is readable         |
| -w                    | Test if a file exists and is writable         |
| -x                    | Test if a file exists and is executable       |


| Numeric test operator | Use                                           |
| ---                   | -----------                                   |
| -eq                   | Test for equality between numbers             |
| -gt                   | Test if one number is greather than another   |
| -lt                   | Test if one number is less than another       |


**Warning**:
```
Be cautious of using the less-than symbol (<). 
`if [[ $VAL < $OTHR ]]`
In this context, the less-than operator uses lexical (alphabetical) ordering.
That means that 12 is less than 2
```
