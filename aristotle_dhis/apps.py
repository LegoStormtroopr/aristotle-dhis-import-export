from aristotle_mdr.apps import AristotleExtensionBaseConfig

class AristotleDHISConfig(AristotleExtensionBaseConfig):
    name = 'aristotle_dhis'
    verbose_name = "Aristotle DHIS2 downloader"
    description = """Provides downloads for a number of different content types in
the <a href='http://www.ddialliance.org'>DHIS2 XML format</a>."""