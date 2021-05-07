# get all related files
files = list.files(dirname(rstudioapi::getActiveDocumentContext()$path), 
                   recursive = TRUE, full.names = TRUE)
repo = strsplit(strsplit(files[[1]],"courses/moer")[[1]][2],"/")[[1]][2]
md_files = xfun::sans_ext(basename(files[grep("/units/", files)]))
outpath = paste0(getwd(),"/docs/assets/pdf/")
url = paste0("https://geomoer.github.io/",repo,"/")
localURL = paste0("http://127.0.0.1:4000/",repo,"/")
pan_arguments=' -f markdown-raw_tex -V colorlinks -V urlcolor=NavyBlue -V toccolor=Reds -f html-native_divs '
wkhtml_arguments=" --footer-left [webpage]  --footer-font-size 8 --footer-line --header-left [title] --header-line --margin-top 30 --margin-left 25 --margin-right 25 --margin-bottom 15 "
# res= lapply(md_files, function(x){
#   system(paste0("pandoc ",localURL,strsplit(strsplit(strsplit(x = x,split = "_")[[1]][1],"/")[[1]][1],"-")[[1]][1],"/",xfun::sans_ext(basename(x)),".html ",pan_arguments, "-o ",outpath, xfun::sans_ext(basename(x)),".pdf ","--pdf-engine=pdflatex"),wait = TRUE)
#   })
# system(paste0("pandoc ",url,"index.html ",pan_arguments, "-o ",outpath, "index.pdf ","--pdf-engine=pdflatex"),wait = TRUE)

res= lapply(md_files, function(x){
  cmd=paste0(wkhtml_arguments, " ",url,strsplit(strsplit(strsplit(x = x,split = "_")[[1]][1],"/")[[1]][1],"-")[[1]][1],"/",xfun::sans_ext(basename(x)),".html ",outpath, xfun::sans_ext(basename(x)),".pdf")
  system2("wkhtmltopdf",cmd,wait = TRUE)
})
system(paste0("wkhtmltopdf ",wkhtml_arguments, " ",url,"index.html ",outpath, "index.pdf "),wait = TRUE)



files2zip <- dir(outpath, full.names = TRUE)
zipfile = paste0(outpath,repo,".zip")
pdfpath= strsplit(outpath,"pdf")[[1]][1]
zip::zip(zipfile, "pdf" , root = pdfpath,include_directories = FALSE,compression_level = 9)
#pandoc https://geomoer.github.io/moer-bsc-systemdynamik/assignments/unit00-02_assignments.html -f markdown-raw_tex -V colorlinks -V urlcolor=NavyBlue -V toccolor=Reds -f html-native_divs -o /home/creu/edu/courses/moer/moer-bsc-systemdynamik/docs/assets/pdf/unit00-02_assignments.pdf --pdf-engine=pdflatex
#pandoc /home/creu/edu/courses/moer/moer-bsc-systemdynamik/docs/_site/unit05/unit05-01_sitzung.html -f markdown-raw_tex -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm" -V colorlinks -V urlcolor=NavyBlue -V toccolor=Reds -f html-native_divs -o /home/creu/edu/courses/moer/moer-bsc-systemdynamik/docs/assets/pdf/unit05-01_sitzung.pdf --pdf-engine=pdflatex
#wkhtmltopdf --page-size Letter --footer-left [webpage]  --footer-font-size 8 --footer-line --header-left [title] --header-line --margin-top 30 --margin-left 25 --margin-right 25 --margin-bottom 15  http://127.0.0.1:4000/moer-bsc-systemdynamik/unit00/unit00-02_assignments.html     layout.pdf

