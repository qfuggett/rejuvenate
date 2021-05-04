## Rejuvenate
A Python-Flask application that allows users to create and record smoothies consumed.

## Installation
Since this application uses an API, you will have to request an API key from https://developer.edamam.com/food-database-api-docs.
After receiving your key, create a `secrets.sh` file for it to be stored there. Remember to include `secrets.sh` in your `.gitignore` file.
Create a database by running `createdb rejuvenate`, in order to store user data.

## Usage
Run `python3 server.py` to run the server. Click on the link generated to open the application in your browser.

## Contributing
Bug reports and pull requests are welcome on Github at https://github.com/qfuggett/rejuvenate.git. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.

## License
Copyright 2021 QueenTesa Fuggett

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.