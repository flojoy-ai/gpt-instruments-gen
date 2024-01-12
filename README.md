
# Device Code Geneartion with GPT

See notebook for more details on development

## Run

```
export OPENAI_API_KEY=""  # set your key
export AIRTABLE_API_KEY=""  # set your key
pip install -r requirements.txt
python generate_md_files.py -d <Path to instruments database directory>
```

### Notes on re-running

In this repo, the data and results are all cached. If you want to re-run this from scratch (ie a change was made to airtable), run
```
rm -rf .cache
python generate_md_files.py -d <Path to instruments database directory>
```

## Details

This does the following:
1. Load the CSV from airtable (if it doesnt exist)
2. Gets each library
3. Loads the raw python code for each particular device
4. Queries chatgpt for the code snippet based on the docstring python code
5. Generates Markdown pages for Starlette app in given directory path.
