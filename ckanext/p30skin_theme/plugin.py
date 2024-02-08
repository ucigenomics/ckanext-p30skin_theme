import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
pconfig = toolkit.config
from ckan.common import config
from ckan.lib.app_globals import set_app_global
import ckan.logic as logic
import ckan.lib.helpers as h
from datetime import datetime


class P30SKINThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        set_app_global('ckan.p30skin_portal_url',
                   pconfig.get('%s.p30skin_portal_url' % __name__))

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'p30skin_theme')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'p30skin_theme_get_last_datasets': lambda: logic.get_action('package_search')({}, {"rows": 8})['results'],
            'p30skin_theme_get_resource_number': p30skin_theme_get_resource_number,
            'p30skin_theme_get_showcase_number': p30skin_theme_get_showcase_number,
            'p30skin_theme_get_popular_datasets': lambda: logic.get_action('package_search')({}, {"rows": 4, 'sort': 'views_total desc'})['results'],
            'p30skin_theme_display_date': p30skin_theme_display_date,
            'p30skin_theme_get_groups': lambda: logic.get_action('group_list')({}, {"all_fields": True}),
            'p30skin_theme_osmnames_key': lambda: config.get('ckanext.p30skin_theme.osmnames_key', '')
        }


def p30skin_theme_display_date(strDate):
    return datetime.strptime(strDate, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d/%m/%Y')


def p30skin_theme_get_resource_number():
    return logic.get_action('resource_search')({}, {'query': {'name:': ''}})['count']


def p30skin_theme_get_showcase_number():
    return len(logic.get_action('ckanext_showcase_list')({}, {}))
