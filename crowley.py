import click

from engines import google
from libs import banner
from vull import sql_injection

@click.command()
@click.option('--dork', nargs=1)
def main(dork):

    search = google.SearchGoogle(dork)
    google_results = search.search_results()
    sqli = sql_injection.SqlInjection()

    for target in google_results:
        sqli.check_vull(target)
    
    sqli.report()

if __name__=='__main__':
    banner.banner()
    main()
