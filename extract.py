import io
import re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def importantExtraction(rawStr):
    with open("output.txt", "w", encoding="utf-8") as text_file:
        print(rawStr, file=text_file)

    outputTxt = open('output.txt', 'r', encoding='utf-8')
    outputStr = outputTxt.read()
    chapter1 = re.findall(r'I. INTRODUCTION(.*?)II. RELATED WORK', outputStr, re.DOTALL)
    chapter3 = re.findall(r'III. PROPOSED METHOD(.*?)IV. EXPERIMENTAL RESULTS', outputStr, re.DOTALL)
    chapter4 = re.findall(r'IV. EXPERIMENTAL RESULTS AND DISCUSSION(.*?)V. CONCLUSION AND FUTURE WORK', outputStr, re.DOTALL)
    chapter5 = re.findall(r'V. CONCLUSION AND FUTURE WORK(.*?)ACKNOWLEDGMENT', outputStr, re.DOTALL)
    outputExtracted = chapter1 + chapter3 + chapter4 + chapter5
    outputExtractedStr = "".join(outputExtracted).replace('\\n', '\n')
    with open("outputextracted.txt", "w", encoding='utf-8') as text_file:
        print(outputExtractedStr, file=text_file)


output = convert_pdf_to_txt("research2.pdf")
importantExtraction(output)
