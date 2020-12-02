# Notes on Singularity #

## Notes ##
- docker
- container
- ```*.sif``` is read-only if built without w option
- If need to use *package managers*, then you will need to use:
  ```
  apt-get
  sudo
  ```
  
  
- If build from docker file, then build on your own machine first and upload
  ```
  local$ docker save -o myfile.tar myfile
  # upload tar onto Compute Canada
  cedar$ singularity build -s mydir docker-archive://myfile.tar
  ```


## Quick start ##

### Commands ###

```
singularity build -s mydir docker://centos:7
singularity shell -c mydir
singularity shell -w mydir # writable; can remove files inside after
```
