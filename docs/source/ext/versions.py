def setup(app):
    app.add_config_value('versions', False, 'html')
    app.add_config_value('downloads', False, 'html')

    app.connect('html-page-context', create_versions)

def create_versions(app, docname, templatename, ctx, doctree):
    ctx['versions']  = app.builder.env.config['versions']
    ctx['downloads'] = app.builder.env.config['downloads']

    ctx['display_github'] = True
    ctx['github_user']    = 'OpenNebula'
    ctx['github_repo']    = 'vOneCloud'
    ctx['github_version'] = 'master/'
    ctx['conf_py_path']   = 'docs/source/'
