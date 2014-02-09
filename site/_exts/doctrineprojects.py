from docutils.parsers.rst import Directive, directives
from docutils import nodes, utils
from string import upper
import operator
import os
from yaml import load as yaml_load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class doctrineprojects(nodes.General, nodes.Element):
    pass

class DoctrineProjects(Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True
    option_spec = {
      'file': directives.path,
      'type': directives.unchanged # 'top' -> all toplevel projects, 'all' -> all projects
    }

    def run(self):
        """
        Implements the directive
        """
        # Get content and options
        file_path = self.options.get('file', None)
        type = self.options.get('type', 'all')

        if not file_path:
            return [self._report('file_path -option missing')]

        projects = yaml_load(open(self._get_directive_path(file_path)).read())

        ret = []
        for project in projects:
            project = projects[project]

            if type == 'top' and project['is_primary'] == False:
                continue

            node = doctrineprojects()
            node['project'] = project
            node['type']    = type
            node['sort']    = project['sort']
            ret.append(node)

        ret.sort(key=operator.itemgetter('sort'))

        return ret

    def _get_directive_path(self, path):
        """
        Returns transformed path from the directive
        option/content
        """
        source = self.state_machine.input_lines.source(
          self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))
        path = os.path.normpath(os.path.join(source_dir, path))

        return utils.relative_path(None, path)

def visit_doctrineprojects_html(self, node):
    self.body.append('<li class="project" id="%s"><h3><a href="/projects/%s.html">%s</a></h3>\n' % (node['project']['slug'], node['project']['slug'], node['project']['title']) )
    self.body.append('<p>%s</p>' % (node['project']['description']) )

    if node['type'] != 'short':
        self.body.append('<p class="centered">')
        self.body.append('<a href="%s">Issues</a> |\n' % (node['project']['issues_link']) )
        self.body.append('<a href="http://docs.doctrine-project.org/projects/doctrine-%s/en/latest/">Documentation</a> |\n' % (node['project']['slug']) )
        self.body.append('<a href="/api/%s/%s/index.html">API</a> |\n' % (node['project']['slug'], node['project']['latest_version']) )
        self.body.append('<a href="/projects/%s.html">Download</a> |\n' % (node['project']['slug']) )
        self.body.append('<a href="%s">Browse Source</a>\n' % (node['project']['browse_source_link']) )
        self.body.append('</p>')

    self.body.append('</li>')
    raise nodes.SkipNode

def depart_doctrineprojects_html(self, node):
    self.body.append('</div>\n')

def visit_doctrineprojects_latex(self, node):
    pass

def depart_doctrineprojects_latex(self, node):
    pass

def setup(app):
    app.add_node(doctrineprojects,
                 html=(visit_doctrineprojects_html, depart_doctrineprojects_html),
                 latex=(visit_doctrineprojects_latex, depart_doctrineprojects_latex))
    app.add_directive('doctrine-projects', DoctrineProjects)
