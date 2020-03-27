def setup(app):
    app.add_config_value('versions', [], 'html')

    app.connect('html-page-context', create_versions)


def create_versions(app, docname, templatename, ctx, doctree):
    ctx['versions']  = app.builder.env.config['versions']

    ctx['display_github'] = True
    ctx['github_user']    = 'OpenNebula'
    ctx['github_repo']    = 'vOneCloud-docs'
    ctx['github_version'] = 'newvone/'
    ctx['conf_py_path']   = 'source/'
