# FIVB VIS Python Client Documentation

The documentation is based on FIVB VIS web service requests. It is simple and includes only requests documented by the FIVB developer team.

[This list contains all available requests via the VIS web service](https://www.fivb.org/VisSDK/VisWebService/#RequestList.html); those with links are documented. Currently, this Python client is read-only.

## Article

`class` Article()

- ### `getArticle(no, fields, content_type)`

    Get an article

    #### Parameters

    > | name           | type     | data type | description                | note                    | default                                                                                                |
    > |----------------|----------|-----------|----------------------------|-------------------------|--------------------------------------------------------------------------------------------------------|
    > | `no`           | required | int       | Number of the article      |                         |                                                                                                        |
    > | `fields`       | optional | str       | Fields in the article data | Must be space-separated | `No Category Source SourceCategory TeamCode TournamentCode NoMatch PublishOnHome VideoUri IsVideoLive` |
    > | `content_type` | optional | str       | Response content-type      | `xml` or `json`         | `xml`                                                                                                  |

    #### Resource

    [List of Article Fields](https://www.fivb.org/VisSDK/VisWebService/Article.html)

    #### Example

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticle(no=69213, fields="no source isVideoLive", content_type="json"))
    ```

- ### `getArticleList(fields, filter, tags, content_type)`

    Get a list of article

    #### Parameters

    > | name           | type     | data type | description                       | note                    | default                                                                                                |
    > |----------------|----------|-----------|-----------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------|
    > | `fields`       | required | str       | Fields in the article data        | Must be space-separated | `No Category Source SourceCategory TeamCode TournamentCode NoMatch PublishOnHome VideoUri IsVideoLive` |
    > | `filter`       | optional | str       | Where the articles were published | Must be space-separated |                                                                                                        |
    > | `tags`         | optional | str       | Tags in the article data          | Must be space-separated |                                                                                                        |
    > | `content_type` | optional | str       | Response content-type             | `xml` or `json`         | `xml`                                                                                                  |

    #### Resources

    [List of Article Fields](https://www.fivb.org/VisSDK/VisWebService/Article.html)

    [Filters for an article](https://www.fivb.org/VisSDK/VisWebService/PressReleasePublishOn.html)

    [Tags Filtering examples](https://www.fivb.org/VisSDK/VisWebService/TagFiltering.html)

    #### Example

    ```python
    from fivbvis import Article

    a = Article()
    print(a.getArticleList(filter="Home", tags="volley-tournament:979"))
    ```

## Beach `WIP`

`class` Beach()

- ### `getBeachMatch(no, fields, content_type)`

    Get a beach volleyball match

    #### Parameters

    > | name           | type     | data type | description                               | note                    | default                                                                                                      |
    > |----------------|----------|-----------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
    > | `no`           | required | int       | Number of the match                       |                         |                                                                                                              |
    > | `fields`       | optional | str       | Fields in the beach volleyball match data | Must be space-separated | `NoInTournament LocalDate LocalTime TeamAType TeamAName TeamBType TeamBName Court MatchPointsA MatchPointsB` |
    > | `content_type` | optional | str       | Response content-type                     | `xml` or `json`         | `xml`                                                                                                        |

    #### Resource

    [List of Beach Match Fields](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

    #### Example

    ```python
    from fivbvis import Beach

    b = Beach()
    print(b.getBeachMatch(15592))
    ```

- ### `getBeachMatchList(fields, filter, content_type)`

    Get a list of beach volleyball matches

    #### Parameters

    > | name            | type     | data type | description                                | note                    | default                                                                                                      |
    > |-----------------|----------|-----------|--------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
    > | `filter`        | required | str       | Filters in the beach volleyball match data | Must be space-separated |                                                                                                              |
    > | `fields`        | optional | str       | Fields in the beach volleyball match data  | Must be space-separated | `NoInTournament LocalDate LocalTime TeamAType TeamAName TeamBType TeamBName Court MatchPointsA MatchPointsB` |
    > | `content_type`  | optional | str       | Response content-type                      | `xml` or `json`         | `xml`                                                                                                        |

    #### Resources

    [List of Beach Match Filter](https://www.fivb.org/VisSDK/VisWebService/BeachMatchFilter.html)

    [List of Beach Match Fields](https://www.fivb.org/VisSDK/VisWebService/BeachMatch.html)

    #### Example

    ```python
    from fivbvis import Beach

    b = Beach()
    print(b.getBeachMatchList(filter='NoTournament="502"'))
    ```

- ### `getBeachOlympicSelectionRanking()`

    Get the beach volleyball selection ranking for the Olympic Games

    Only XML response

- ### `getBeachRound()`

    Get a beach volleyball round

    Only XML response

- ### `getBeachRoundList()`

    Get a list of beach volleyball rounds

    Only XML response

- ### `getBeachRoundRanking()`

    Get the ranking of a beach volleyball round

    Only XML response

- ### `getBeachTeam()`

    Get a beach volleyball team

- ### `getBeachTeamList()`

    Get a list of beach volleyball teams

- ### `getBeachTournament()`

    Get a beach volleyball tournament

- ### `getBeachTournamentRanking()`

    Get the ranking of a beach volleyball tournament

    Only XML response

- ### `getBeachWorldTourRanking()`

    Get a beach volleyball World Tour ranking

    Only XML response

## Event `WIP`

`class` Event()

- ### `getEvent()`

    Get an event

    Only XML response

- ### `getEventList()`

    Get a list of events

    Only XML response

## Image `WIP`

`class` Image()

- ### `getImage()`

    Get the content of an image

## Player `WIP`

`class` Player()

- ### `getPlayer()`

    Get a player

## Volleyball `WIP`

`class` Volleyball()

- ### `getVolleyMatch(no, fields, content_type)`

    Get a volleyball match

    #### Parameters

    > | name           | type     | data type | description                         | note                    | default                                                                                                      |
    > |----------------|----------|-----------|-------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
    > | `no`           | required | int       | Number of the match                 |                         |                                                                                                              |
    > | `fields`       | optional | str       | Fields in the volleyball match data | Must be space-separated | `City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName` |                                                                                                             |
    > | `content_type` | optional | str       | Response content-type               | `xml` or `json`         | `xml`                                                                                                        |

    #### Resource

    [List of Volley Match Fields](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

    #### Example

    ```python
    from fivbvis import Volleyball

    v = Volleyball()
    print(v.GetVolleyMatch(9211))
    ```

- ### `getVolleyMatchList(no_tournament, fields, filter, content_type)`

    Get a list of volleyball matches

    #### Parameters

    > | name            | type     | data type | description                          | note                    | default                                                                                                      |
    > |-----------------|----------|-----------|--------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
    > | `no_tournament` | required | int       | Number of the tournament             |                         |                                                                                                              |
    > | `fields`        | optional | str       | Fields in the volleyball match data  | Must be space-separated | `City CountryName DateTimeLocal DurationTotal Hall MatchPointsA MatchPointsB MatchResultText No NoTournament Season TeamAName TeamBName` |
    > | `filter`        | optional | str       | Filters in the volleyball match data | Must be space-separated |                                                                                                              |
    > | `content_type`  | optional | str       | Response content-type                | `xml` or `json`         | `xml`                                                                                                        |

    #### Resources

    [List of Volley Match Fields](https://www.fivb.org/VisSDK/VisWebService/#VolleyMatch.html)

    [List of Volley Match Filter](https://www.fivb.org/VisSDK/VisWebService/VolleyMatchFilter.html)

    #### Example

    ```python
    from fivbvis import Volleyball

    v = Volleyball()
    print(v.getVolleyMatchList(no_tournament=979, filter='FirstDate="2017-7-5" LastDate="2017-7-5"'))
    ```

    #### Note

    Requesting all parameters may result in a 404 error

- ### `getVolleyPlayer()`

    Get a registration of a player in a volleyball tournament

- ### `getVolleyPlayerList()`

    Get a list of registrations of players in volleyball tournaments

- ### `getVolleyPlayersRankingList()`

    Get the list of rankings of players in a volleyball tournament

    Only XML response

- ### `getVolleyPool()`

    Get a volleyball pool

- ### `getVolleyPoolList()`

    Get a list of volleyball pools

- ### `getVolleyPoolRanking()`

    Get the ranking for a volleyball pool

- ### `getVolleyTeam()`

    Get a registration of a team in a volleyball tournament

- ### `getVolleyTeamList()`

    Get a list of registrations of teams in volleyball tournaments

- ### `getVolleyTournament()`

    Get a volleyball tournament

- ### `getVolleyTournamentList()`

    Get a list of volleyball tournaments

- ### `getVolleyTournamentRanking()`

    Get the ranking of a volleyball tournament

    Note: the `teamType` property is not available in JSON