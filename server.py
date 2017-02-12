#!/usr/bin/env python
import hug
from hug_middleware_cors import CORSMiddleware

import subprocess
from tempfile import NamedTemporaryFile

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.get('/')
def index():
    return "hello"


@hug.post('/ocr', output=hug.output_format.file)
def ocr(body, response, language: "The language(s) to use for OCR"="eng"):
    if not len(body) == 1:
        raise Exception("Need exactly one file!")

    fn, content = list(body.items()).pop()

    f_out = NamedTemporaryFile(suffix='.pdf')

    with NamedTemporaryFile(suffix='.pdf', mode="wb") as f_in:
        f_in.write(content)
        f_in.flush()

        proc = subprocess.Popen(['ocrmypdf', '--force-ocr', '-l', language, f_in.name, f_out.name])

        code = proc.wait()

        response.set_header('X-OCR-Exit-Code', str(code))

        print(f_out.name)

        return f_out
