from src.modules.upload.models import FileModel


def filter_files(search_query) -> list:
    """
    Filter files by search query.

    :param search_query: search query
    :return: filtered query
    """
    files = FileModel.query.filter(
            FileModel.keywords.like('%' + search_query + '%') | FileModel.collocations.like('%' + search_query + '%')
        )
    return files
