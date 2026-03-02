import datetime

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    # deprecated & ignored by newer versions of copier-template-extensions
    update = False

    def hook(self, context):
        context["repo_name"] = context["_copier_conf"]["dst_path"].name
        context["year"] = datetime.date.today().year
        # context does not yet contain prompted-for values during 'prompt' phase
        domain = context.get("domain")
        cname = context.get("plugin_cname")

        if domain and cname:
            context["plugin_clap_id"] = ".".join(list(reversed(domain.split('.'))) + [cname]).lower()
