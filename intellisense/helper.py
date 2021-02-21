import io
import os
import zipfile


def get_zipped_vocabulary(zip_path: str) -> set:
    exists = os.path.isfile(zip_path)
    if not exists:
        raise FileNotFoundError('Zipped vocabulary don\'t exist')
    words = set()
    with zipfile.ZipFile(zip_path) as compressed_file:
        files = compressed_file.namelist()
        for file_name in files:
            with io.TextIOWrapper(compressed_file.open(file_name),
                                  encoding="utf-8") as uncompressed_file:
                words = words.union(set(uncompressed_file.read().split()))
    return set(map(lambda x: x.lower(), words))


def get_vocabulary(language_iso_code: str) -> set:
    if language_iso_code not in ["en", "de"]:
        raise ValueError
    source_dir = os.path.dirname(os.path.abspath(__file__)) + '/data/'
    filename = "vocabulary-{}.zip".format(language_iso_code)
    return get_zipped_vocabulary(source_dir + filename)

