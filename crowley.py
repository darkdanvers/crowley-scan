import click

from engines import google
from libs import banner
from vull import sql_injection
from vull import reporting

@click.command()
@click.option('--dork', nargs=1)
@click.option('--max_results', default=100, nargs=1, type=click.INT)
@click.option('--timeout', default=3, nargs=1, type=click.INT)
def main(dork, max_results, timeout):

    search = google.SearchGoogle(dork, max_results, timeout)
    google_results = search.search_results()
    sqli = sql_injection.SqlInjection()
    report = reporting.ReportVulnerabilities()

    for target in google_results:
        sqli.check_vull(target)
    
    report.create_report()

if __name__=='__main__':
    banner.banner()
    main()
