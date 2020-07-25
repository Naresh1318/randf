# randf

<p align=center>
    <img src="https://files.naresh1318.com/public/randf/randf.gif" alt="randf"/>
    <p align="center"> <b>Having a hard time picking a restraunt to order food from? So did I.</b> </p>
</p>

# Example
<p align=center>
    <img src="https://files.naresh1318.com/public/randf/randf_screenshot.png" alt="randf"/>
    <p align="center"> <b>Website</b> </p>
</p>

# Install
1. Build image
```bash
docker build -t randf:latest .
```

2. Run container
```bash
docker run -v <path to randf/data>:/randf/data -p <PORT>:5000 -d randf:latest
```

Example:
```bash
docker run -v /Users/naresh/Projects/randf/data:/randf/data -p 4000:5000 -d randf:latest
```

