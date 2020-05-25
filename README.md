# SpamD

SpamD is an Python 3 libray thats allow you to do spam in discord with multiples accounts.

## How To Use

1- Download the file (library), and put it in the same location of your python file.

2- Import SpamD library to your python file.

## Examples:

**Join Server:**

```py
import SpamD

SpamD.Join("Invite_Code","Authorization")
```

**Spam Messages:**

```py
import SpamD

while True:
    SpamD.Spam_M("Channel_Id","Authorization")

```

**Spam Reactions:**

```py
import SpamD

while True:
    SpamD.Spam_E("Channel_Id","Message_Id","Authorization")

```

**Ps: Authorization Means Account Token.**
