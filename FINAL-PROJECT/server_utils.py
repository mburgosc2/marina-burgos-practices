
from Seq2 import Seq
from pathlib import Path
from jinja2 import Template
import http.server
import http.client
import json

genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA":  "ENSG00000196839",
    "FXN":  "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


def read_template_html_file(filename):
    contents = Template(Path(filename).read_text())
    return contents

def get_data(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    print(SERVER + ENDPOINT + PARAMS)
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    print("Response received!:", response.status, response.reason)
    answer_decoded = response.read().decode("utf-8")
    dict_response = json.loads(answer_decoded)
    print(dict_response)
    return dict_response

def list_species(dict_response, limit):
    try:
        number_s = len(dict_response["species"])
        list_s = []
        if int(limit) == 0:
            contents = read_template_html_file("./html/ERROR.html").render()
        elif int(limit) < 0:
            contents = read_template_html_file("./html/ERROR.html").render()
        else:
            for n in range(0, int(limit)):

                try:
                    list_s.append(dict_response["species"][n]["display_name"])
                    context = {"limit": limit, "list_species": list_s, "number_s": number_s}
                    contents = read_template_html_file("./html/list_species.html").render(context=context)

                except KeyError:
                    pass
                except IndexError:
                    pass


    except ValueError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents

def karyotype(dict_response, specie_name):
    try:
        context = {"specie_name": specie_name, "karyotype": dict_response["karyotype"]}
        contents = read_template_html_file("./html/karyotype.html").render(context=context)
    except KeyError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents

def length_chromosome(dict_response, specie_name, chromo):
    try:
        length = dict_response["length"]
        context = {"specie": specie_name, "chromosome": chromo, "length": length}
        contents = read_template_html_file("./html/chromosome_length.html").render(context=context)
    except KeyError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents

def sequence(dict_response,gene):
    try:
        seq = dict_response["seq"]
        context = {"gene": gene, "seq": seq}
        contents = read_template_html_file("./html/geneSeq.html").render(context=context)
    except KeyError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents

def infoseq(dict_response, gene):
    try:
        desc = dict_response["desc"].split(":")
        desc_name = desc[1]
        desc_start = desc[3]
        desc_end = desc[4]
        id = dict_response["id"]
        len =  int(desc_end) - int(desc_start) + 1
        context = {"len": len,
                   "id": id,
                   "gene_name": gene,
                   "start": desc_start,
                   "end": desc_end,
                   "chrom_name": desc_name}
        contents = read_template_html_file("./html/geneInfo.html").render(context=context)
    except KeyError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents

def calcseq(dict_response, gene):
    try:
        seq = Seq(dict_response["seq"])
        percentage_bases = seq.percentage_base(seq.count_bases(), seq.len())
        context = {"percentage_bases": percentage_bases,
                   "gene_name": gene,
                   "total_length": seq.len()}
        contents = read_template_html_file("./html/geneCalc.html").render(context=context)
    except KeyError:
        contents = read_template_html_file("./html/ERROR.html").render()
    return contents












