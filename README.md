create env

```bash
conda create -n advertisement python=3.8 -y
```


activate env
```bash
conda activate advertisement
```


initialize git
```bash
git init
```

initialize dvc
```bash
init dvc
```

add data so that dvc can track the data file
```bash
dvc add data_given/Advertising.csv
```

