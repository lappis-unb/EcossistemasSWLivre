Como gerar o pds:

Macos

``cpdf () { 
  gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile="$1" "${@:2}"
}``


	cpdf anexos.pdf os19-paper-A3-deLacerda.pdf 1909.05409.pdf ESEM\ 2018\ -\ PAPER\ 229\ -\ camera_ready\ -\ final.pdf  CAPA\ -\ SOFTWARE\ É\ CULTURA_Versão\ Final.pdf Software\ e\ Cultura\ no\ Brasil\ _\ UFABC_Versão\ Final0.pdf Software\ e\ Cultura\ no\ Brasil\ _\ UFABC_Versão\ Final1.pdf Framework\ de\ Assistente\ Virtual\ do\ Laboratório\ Lappis.pdf What\ I\ wish\ I\ knew\ before\ starting\ my\ first\ Chatbot\ project.pdf Encantando\ pessoas:\ poder\ da\ personalidade\ em\ Chatbots.pdf Algoritmos\ de\ aprendizagem\ de\ máquina\ com\ software\ em\ produção—\ análise\ de\ projetos\ da\ Lei\ Rouanet.pdf

