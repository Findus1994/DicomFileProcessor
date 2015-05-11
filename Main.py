__author__ = 'UNKNOWN'

import sys
import os

from Parser import Parser
from TagSearcher import TagSearcher
from ConfigFileReader import ConfigFileReader
from TagExporter import TagExporter


# Wird als Programmeinstiegspunkt genutzt. Liest Verzeizeichispfad von Dicomdateien  ein, der mitgegeben wurde.
# Optional kann auch der Pfad zur Configdatei eingelesen werden.

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 Main.py <Attributefile> <Directory of dicom files> <Outputfile>")
        exit()

    attributefile = sys.argv[1]
    dicomDirectory = sys.argv[2]
    outputfile = sys.argv[3]
    datas = []
    exporter = TagExporter()
    configFileReader = ConfigFileReader()
    tagSearcher = TagSearcher(configFileReader.read_config(sys.argv[1]))

    for x in os.listdir(dicomDirectory):
        if os.path.isfile(dicomDirectory + x):
            datas.append(dicomDirectory + x)

    for x in datas:
        print(x + ":")
        parsed = {}
        parsed = Parser().parse_dicom_file(tagSearcher, x)
        for key in parsed:
            exporter.saveTag(key, parsed[key], str(x).split("/")[-1])
            print(key + ": " + parsed[key])
        print("\n\n")

    exporter.writeToFile(outputfile, configFileReader.read_config(attributefile))


