# Notes on Singularity #

## Notes ##
- docker
- container
- ```*.sif``` is read-only

## Quick start ##

### Commands ###

```
singularity build -s mydir
singularity shell -c mydir
singularity shell -w mydir # writable; can remove files inside after
```

If need to use *package managers*, then you will need to use:
```
apt-get
sudo
```
