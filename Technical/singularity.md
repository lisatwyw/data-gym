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

## Quick start ##

### Commands ###

```
singularity build -s mydir
singularity shell -c mydir
singularity shell -w mydir # writable; can remove files inside after
```

