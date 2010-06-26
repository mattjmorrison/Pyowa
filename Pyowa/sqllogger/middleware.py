
from django.db import connections
from django import template
import itertools

TEMPLATE = template.Template("""
    <table>
    <tr>
        <th>Time</th>
        <th>SQL</th>
    </tr>
    {% for query in queries %}
       <tr>
        <td>{{ query.time }}</td>
        <td>{{ query.sql }}</td>
       </tr>
    {% endfor %}
    </table>""")

class SqlLoggerMiddleware(object):
    def process_response(self, request, response):
        queries = [[{'sql':q['sql'], 'time':q['time']} for q in c.queries] for c in connections.all()]
        response.write(TEMPLATE.render(template.Context({'queries':list(itertools.chain.from_iterable(queries))})))
        return response