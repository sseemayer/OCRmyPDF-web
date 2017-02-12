# OCRmyPDF-web

A simple web service for running [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF). Builds on top of the official OCRmyPDF docker container and adds a simple REST API and lightweight web frontend. Simply drag a PDF file into the browser window and get a file download with the OCRed file back!

## Running

### Using Dokku
OCRmyPDF-web has been designed with [Dokku](http://dokku.viewdocs.io/dokku/) in mind. Just follow the standard Dockerfile deploy steps!

### Using Docker
Expose on port 8888:

```bash
docker run -p 8888:8000 --name ocrmypdf-web sseemayer/ocrmypdf-web
```
