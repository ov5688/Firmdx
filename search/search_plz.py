from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
from django.db.models import Q
from googleMapsAPI.geocoords import GeoCoords

class Search:

    def filter_plz(self, firm_list, search_input):

        self.firm_list = firm_list
        self.search_input = search_input

        distance = GeoCoords()
        distance = distance.distance_matrix(search_input, firm_list)
        ord_list = []
        dist = []
        for key in distance:
            for f in firm_list:
                if key[0] == f.id:
                    ord_list.append(f)
                    dist.append(key[1])

        print("ORD_LIST EXTENDS DISTANCE -------> ", ord_list)
        # vector = SearchVector('plz')
        # query = SearchQuery(self.search_input)
        #
        # # branch_firms = firm_list.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        # branch_firms = firm_list.annotate(similarity=TrigramSimilarity('plz', search_input)).filter(similarity__gt=0.2).order_by('-similarity')
        # branch_firms = list(branch_firms)
        # firm_list = list(firm_list)
        #
        # for firm in firm_list:
        #     if firm not in branch_firms:
        #         branch_firms.append(firm)

        # branch_firms = firm_list.annotate(distance=TrigramDistance('plz', search_input)).filter(distance__lte=0.7).order_by('distance')
        # https://docs.djangoproject.com/en/1.11/topics/db/queries/
        # branch_firms = firm_list.filter(Q(plz__lte=int(self.search_input)+1000),
        #                                 Q(plz__gte=int(self.search_input)-1000)
        #                                 ).annotate(rank=SearchRank(vector, query)).order_by('-rank')
        # branch_firms = firm_list.annotate(similarity=TrigramSimilarity('plz', search_input),).filter(similarity__gt=0.3).order_by('-similarity')

        return (ord_list, dist)
