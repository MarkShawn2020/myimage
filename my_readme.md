### Upload to Pypi
```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

> Token
```bash
__token__
<PASTE HERE>
```

### Upload to Github
```bash
git add -A
git commit -m "update"
git push
```
