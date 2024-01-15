import requests

FIELDS = 'DateTime DeletedDT ENewsLocation HasPhoto IsVideoLive LastChangeDT LastChangeUser LastChangeUsername No PhotoUrl PublishOnBeach PublishOnDevelopment PublishOnFivb PublishOnHeadlines PublishOnHome PublishOnMedical PublishOnMsdp PublishOnPresident PublishOnRefereeingRules PublishOnSnow PublishOnTechnicalCoach PublishOnTournament PublishOnTwitter PublishOnVolley PublishOnVolleyballWorld PublishOnWorldVolleyNews ShareUrl Source Url ValidFrom ValidTo	DateTime Version VideoUri'

class Article():
    def __init__(self):
        self.headers = {'Accept': 'application/json'}
        self.base_url = "https://www.fivb.org/Vis2009/XmlRequest.asmx?Request="

    def get(self, no, fields=FIELDS):
        url = self.base_url + "<Request Type='GetArticle' No='{}' Fields='{}'/>".format(no, fields)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def list(self, fields=FIELDS, filters='', tags=''):
        url = self.base_url + "<Request Type='GetArticleList' Fields='{}'><Filter>'{}'<Tags>{}</Tags></Filter></Request>".format(fields, filters, tags)

        response = requests.get(url, headers=self.headers)

        return response.json()