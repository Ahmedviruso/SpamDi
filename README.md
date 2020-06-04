# SpamDi

SpamDi is an Python 3 library that's allow you to do spam in discord using multiples accounts.

## How To Use

1- Download the file , and put it in the same location of your python file.

2- Import library to your python file.

## Examples:

**Join Server:**

```py
import SpamDi

SpamDi.Join("Invite_Code","Authorization")
```

**Spam Messages:**

```py
import SpamDi

while True:
    SpamDi.Spam_M("Channel_Id","Authorization")

```

**Spam Reactions:**

```py
import SpamDi

while True:
    SpamDi.Spam_E("Channel_Id","Message_Id","Authorization")

```

**Ps: Authorization Means Account Token.**
