## hostnamer

Hostnamer is a simple docker image that serves up an http endpoint on port 8080. It will return `200 OK` and the hostname of the docker container.

### Usage

```bash
$ docker run -p 8080:8080 -h rabbit hostnamer
```


then, do a curl:

```bash
$ curl <docker IP>:8080
```

which will return the string `rabbit`
