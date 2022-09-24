import justpy as jp
import definition
import json


class Api:
    """http://127.0.0.1:8000/api?w=word"""

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        jp.Div(a=wp, text=word.title())
        defined = definition.Definition(word).get()
        response = {
            'w': word,
            'definition': defined
        }
        wp.html = json.dumps(response)
        return wp


