# AAU Stads Checker
Simple Python/Python3 script, that will login to AAU Stads for students and parse the `Resultater` list and return it as a list.

Could be combined with a `crontab`, so that it checks STADS every 30 minutes or so, as it seems like STADS e-mail system is somewhat delayed.

To use it simply create a `.env` file, with the following, and source it (`source .env):

```
export AAU_STADS_USERNAME=username
export AAU_STADS_PASSWORD=password
```
