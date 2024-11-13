import datetime

from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        context["repo_name"] = context["_copier_conf"]["dst_path"].name
        domain = context["domain"]
        cname = context["plugin_cname"]
        context["plugin_clap_id"] = ".".join(list(reversed(domain.split('.'))) + [cname]).lower()
        context["year"] = datetime.date.today().year
