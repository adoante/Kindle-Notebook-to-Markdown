# Kindle Highlight to Markdown

Program takes a `.csv` generated by a Kindle's Export Notes feature as input. Converts highlights to markdown quotes and any notes associated with the quote as a markdown bullet point underneath the quote. An output file name must be specificed.

No need to include `.md` in your output file name. Program will add `.md` to the end of output file name.


Use: `python .\kindle_notes_to_markdown.py ['input_file.csv'] ['output_file name']`

Ex: `python .\kindle_notes_to_markdown.py '.\The Creative Act_ A Way of Being-Notebook.csv' 'The Creative Act'`