import abc

class Ireport(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def generate(self):
        pass

    
class ReportExcel(Ireport):
    def generate(self):
        return "Generando Excel...."
    
class ReportPDF(Ireport):
    def generate(self):
        return "Generando PDF...."
    
class ReportHTML(Ireport):
    def generate(self):
        return "Generando HTML...."
        
class ReportGenerator: 
    def generate(self,data):
        return data.generate()
        

report = ReportGenerator()
reportresult = report.generate(ReportExcel())
print(reportresult)
        