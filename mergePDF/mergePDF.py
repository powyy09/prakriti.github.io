import pypdf

hello = "C:\\Users\\katte\\Documents\\Assets\\Python\\mergePDF\\hello.pdf"
hiee = "C:\\Users\\katte\\Documents\\Assets\\Python\\mergePDF\\hiee.pdf"

pdfs = [hello, hiee]
merger =  PdfMerger ()

for pdf in pdfs :
    merger.append(pdf)
    
mergedpdf = "C:\\Users\\katte\\Documents\\Assets\\Python\\mergePDF\\mergedpdf.pdf"

merger.write(mergedpdf)