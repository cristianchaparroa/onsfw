# ONSFW
The following is a simple example of how to use Open NSFW 2.

## Docker

We can create an docker image and then run it.
```
docker build --no-cache --progress=plain -t local/onsfw . 2>&1
docker run -p 8000:800 local/onsfw 
```

## Endpoints

The server expose the following endpoint

```
POST http://localhost:8000/images/moderations
```

### Usage

```curl
curl -X POST -F file=@output_grad_cam_3.jpg http://localhost:8000/images/moderations | jq .

{
  "output_grad_cam_3.jpg": 0.22624632716178894
}
```
