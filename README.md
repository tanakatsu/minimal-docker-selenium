## minimal docker selenium


```
# Build container image
$ docker build -t docker-selenium .

# Run bash in container
$ docker run -it -v ${PWD}:/usr/src docker-selenium /bin/bash

# Run test script
root@f79d1011e1a3:/# cd /usr/src
root@f79d1011e1a3:/usr/src# python test.py
https://qiita.com/
OK
```

Check `test.png` out

